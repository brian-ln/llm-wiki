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
    make_event("Diffusion models, under the Software 2.0 paradigm, act as specialized neural processors that learn a 'diffusion process' to gradually denoise continuous probability distributions (like images).", "raw/diffusion_model.md"),
    make_event("Unlike autoregressive Transformers which generate discrete tokens sequentially, Diffusion models use a continuous random walk with drift (often leveraging U-Nets or DiTs as the backbone) to undo Gaussian noise.", "raw/diffusion_model.md"),
    make_event("Mixture of Experts (MoE) represents a routing architecture for neural processors, essentially acting as conditional computation where multiple expert networks handle different problem space regions dynamically.", "raw/mixture_of_experts.md"),
    make_event("MoE introduces a 'gating function' acting as a load-balancer/router, making the overall model sparsely activated—increasing parameter count and specialization without proportionately increasing inference compute costs.", "raw/mixture_of_experts.md")
]

with open("events/processor_events.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

diffusion_node = {
  "id": "node:concept_diffusion_model",
  "type": "concept",
  "title": "Diffusion Models as Continuous Neural Processors",
  "description": "Within the Software 2.0 paradigm, Diffusion models are a class of generative processor optimized for continuous probability distributions (e.g., images, video, audio). Instead of autoregressive token prediction, their 'instruction set' involves iteratively denoising a state space. They perform a reverse random walk with drift, typically using a U-Net or Transformer backbone, to map Gaussian noise back to structured data.",
  "status": "active",
  "tags": ["software2.0", "processor", "diffusion", "continuous", "generative"],
  "edges": [
    { "target": events[0]["id"], "relation": "supported_by" },
    { "target": events[1]["id"], "relation": "supported_by" },
    { "target": "node:software_2_0_architectures", "relation": "instance_of" }
  ]
}

moe_node = {
  "id": "node:concept_mixture_of_experts",
  "type": "concept",
  "title": "Mixture of Experts (MoE) Routing Architecture",
  "description": "Mixture of Experts (MoE) is a neural architectural pattern enabling 'conditional computation'. It uses a learned gating function to dynamically route inputs to specialized sub-networks (experts). Under the Software 2.0 lens, this functions like a sparsely-activated multi-core processor or dynamic dispatch system: it scales the total parameter count (knowledge capacity) while holding active compute roughly constant.",
  "status": "active",
  "tags": ["software2.0", "architecture", "moe", "routing", "sparse"],
  "edges": [
    { "target": events[2]["id"], "relation": "supported_by" },
    { "target": events[3]["id"], "relation": "supported_by" },
    { "target": "node:software_2_0_architectures", "relation": "instance_of" }
  ]
}

with open("nodes/node_concept_diffusion_model.json", "w") as f:
    json.dump(diffusion_node, f, indent=2)

with open("nodes/node_concept_mixture_of_experts.json", "w") as f:
    json.dump(moe_node, f, indent=2)

print("Nodes created and events appended.")
