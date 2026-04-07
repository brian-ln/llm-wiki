import json
import datetime
import uuid

def make_event(claim, source):
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

events = [
    make_event("State Space Models (SSMs), such as Mamba, are subquadratic-time architectures designed to address the computational inefficiency of Transformers on long sequences by replacing the core attention module.", "arxiv:2312.00752"),
    make_event("Mamba introduces 'selective SSMs' where parameters are functions of the input, enabling the model to selectively propagate or forget information along the sequence length dimension (content-based reasoning).", "arxiv:2312.00752"),
    make_event("Mamba enjoys fast inference (5x higher throughput than Transformers) and linear scaling in sequence length, making it highly efficient for continuous or million-length sequence modalities like audio and genomics.", "arxiv:2312.00752"),
    make_event("[HYPOTHESIS] [AGENT-RESEARCH] Under the Software 2.0 paradigm, SSMs like Mamba function as a continuous-state sequence processor. Unlike Transformers (which compute all-to-all attention), Mamba's 'instruction set' compresses context into a fixed-size hidden state that conditionally updates per-token, acting more like a dynamic recurrent processor.", "arxiv:2312.00752")
]

with open("events/processor_events.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

mamba_node = {
  "id": "node:concept_state_space_model",
  "type": "concept",
  "title": "State Space Models (Mamba) as Recurrent Neural Processors",
  "description": "[HYPOTHESIS] [AGENT-RESEARCH] In the Software 2.0 paradigm, State Space Models (SSMs) like Mamba represent a different 'ISA' from Transformers. Instead of executing an O(N^2) all-to-all attention memory fetch, an SSM processor maintains a fixed-size recurrent state buffer. It executes a selective gating instruction per input token, deciding what to propagate or forget. This allows linear-time execution over massive sequences (audio, genomics, long text) at the cost of exact historical recall.",
  "status": "active",
  "tags": ["software2.0", "architecture", "ssm", "mamba", "sequence_model", "recurrent"],
  "edges": [
    { "target": events[0]["id"], "relation": "supported_by" },
    { "target": events[1]["id"], "relation": "supported_by" },
    { "target": events[2]["id"], "relation": "supported_by" },
    { "target": events[3]["id"], "relation": "supported_by" },
    { "target": "node:software_2_0_architectures", "relation": "instance_of" }
  ]
}

with open("nodes/node_concept_state_space_model.json", "w") as f:
    json.dump(mamba_node, f, indent=2)

# Update node_software_2_0_architectures.json to depend on Mamba
with open("nodes/node_software_2_0_architectures.json", "r") as f:
    arch_node = json.load(f)

arch_node["edges"].append({"target": mamba_node["id"], "relation": "includes"})

with open("nodes/node_software_2_0_architectures.json", "w") as f:
    json.dump(arch_node, f, indent=2)

print("Mamba SSM events and node ingested.")
