import json
import datetime
import uuid
import glob

def make_ingest_event(uri, local_path, title, timestamp=None):
    return {
        "id": f"evt:raw:{uuid.uuid4().hex[:8]}",
        "timestamp": timestamp or (datetime.datetime.now().isoformat() + "Z"),
        "actor": "algo",
        "action": "INGEST_RAW",
        "payload": {
            "source_uri": uri,
            "local_path": local_path,
            "title": title
        }
    }

events = [
    make_ingest_event("https://en.wikipedia.org/wiki/Diffusion_model", "raw/diffusion_model.md", "Wikipedia: Diffusion Model"),
    make_ingest_event("https://en.wikipedia.org/wiki/Mixture_of_experts", "raw/mixture_of_experts.md", "Wikipedia: Mixture of experts"),
    make_ingest_event("https://arxiv.org/abs/2312.00752", "raw/arxiv_2312_00752_abstract.txt", "ArXiv: Mamba: Linear-Time Sequence Modeling with Selective State Spaces")
]

with open("events/processor_events.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

# Also let's save the abstract to raw/
mamba_abstract = "Foundation models, now powering most of the exciting applications in deep learning, are almost universally based on the Transformer architecture and its core attention module. Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers' computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language. We identify that a key weakness of such models is their inability to perform content-based reasoning, and make several improvements. First, simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities, allowing the model to selectively propagate or forget information along the sequence length dimension depending on the current token. Second, even though this change prevents the use of efficient convolutions, we design a hardware-aware parallel algorithm in recurrent mode. We integrate these selective SSMs into a simplified end-to-end neural network architecture without attention or even MLP blocks (Mamba). Mamba enjoys fast inference (5x higher throughput than Transformers) and linear scaling in sequence length, and its performance improves on real data up to million-length sequences. As a general sequence model backbone, Mamba achieves state-of-the-art performance across several modalities such as language, audio, and genomics. On language modeling, our Mamba-3B model outperforms Transformers of the same size and matches Transformers twice its size, both in pretraining and downstream evaluation."
with open("raw/arxiv_2312_00752_abstract.txt", "w") as f:
    f.write(mamba_abstract)

# Now, let's build a materialized view of the index
index_node = {
    "id": "sys:raw_index",
    "type": "protocol",
    "title": "System Raw Materials Index",
    "description": "A materialized view of all Layer 0 immutable raw sources ingested into the Epistemic Engine. The single source of truth for provenance is the INGEST_RAW events in the ledger. We do not use frontmatter in /raw/ to preserve the byte-for-byte integrity of external documents.",
    "status": "active",
    "tags": ["system", "provenance", "index"],
    "edges": []
}

# Scan all events for INGEST_RAW
for file in glob.glob("events/*.jsonl"):
    with open(file, "r") as f:
        for line in f:
            if not line.strip(): continue
            evt = json.loads(line)
            if evt.get("action") == "INGEST_RAW":
                index_node["edges"].append({
                    "target": evt["id"],
                    "relation": "tracks_provenance_of",
                    "metadata": {
                        "uri": evt["payload"]["source_uri"],
                        "local_path": evt["payload"]["local_path"]
                    }
                })

with open("nodes/sys_raw_index.json", "w") as f:
    json.dump(index_node, f, indent=2)

print("Provenance ledger updated and sys_raw_index materialized.")
