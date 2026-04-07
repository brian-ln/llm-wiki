import json
import datetime
import uuid

def make_ingest_event():
    return {
        "id": f"evt:raw:{uuid.uuid4().hex[:8]}",
        "timestamp": datetime.datetime.now().isoformat() + "Z",
        "actor": "algo",
        "action": "INGEST_RAW",
        "payload": {
            "source_uri": "https://karpathy.medium.com/software-2-0-a64152b37c35",
            "local_path": "raw/karpathy_software_2_0.md",
            "title": "Software 2.0 by Andrej Karpathy"
        }
    }

def make_claim_event(claim, source):
    return {
        "id": f"evt:research:{uuid.uuid4().hex[:8]}",
        "timestamp": datetime.datetime.now().isoformat() + "Z",
        "actor": "algo",
        "action": "ASSERT_CLAIM",
        "payload": {
            "claim": claim,
            "source": source
        }
    }

ingest_evt = make_ingest_event()
raw_id = ingest_evt["id"]

claims = [
    make_claim_event("Software 1.0 is composed of explicit instructions written by a programmer (a complex, heterogeneous instruction set).", raw_id),
    make_claim_event("Software 2.0 (neural networks) is computationally homogeneous, relying on a drastically simpler instruction set (e.g., matrix multiplication and ReLU thresholding).", raw_id),
    make_claim_event("Because the instruction set of Software 2.0 is so small and homogeneous, it is much easier to bake directly into silicon (ASICs, neuromorphic chips).", raw_id),
    make_claim_event("Software 2.0 modules can meld into an optimal whole. Unlike 1.0 modules connected via rigid APIs, 2.0 modules interact via differentiable boundaries, allowing backpropagation to auto-tune the entire stack end-to-end.", raw_id)
]

with open("events/paradigm_events.jsonl", "a") as f:
    f.write(json.dumps(ingest_evt) + "\n")
    for c in claims:
        f.write(json.dumps(c) + "\n")

# Update sys_raw_index
with open("nodes/sys_raw_index.json", "r") as f:
    idx = json.load(f)

idx["edges"].append({
    "target": raw_id,
    "relation": "tracks_provenance_of",
    "metadata": {
        "uri": ingest_evt["payload"]["source_uri"],
        "local_path": ingest_evt["payload"]["local_path"]
    }
})

with open("nodes/sys_raw_index.json", "w") as f:
    json.dump(idx, f, indent=2)

print("Karpathy's Software 2.0 essay ingested.")
