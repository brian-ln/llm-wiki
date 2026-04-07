import json
import datetime
import uuid

def make_claim_event(claim, source="user_inquiry:metaphorical_pluralism"):
    return {
        "id": f"evt:logic:{uuid.uuid4().hex[:8]}",
        "timestamp": datetime.datetime.now().isoformat() + "Z",
        "actor": "algo",
        "action": "ASSERT_CLAIM",
        "payload": {
            "claim": claim,
            "source": source
        }
    }

events = [
    make_claim_event("[AGENT-RESEARCH] Yes, to a layman, a stored prompt like `research-process.md` is absolutely a 'program'. If a file contains instructions that make a computer perform a task, it fulfills the functional definition of a program from the user's perspective."),
    make_claim_event("[AGENT-RESEARCH] The defining feature of computing abstractions is that intermediate layers (ASTs, IRs, tokenizers, KV caches, binary logic) 'fall out' or disappear from the user's view. When you double-click an executable, you don't see the compiler; when you invoke a prompt, you don't see the LLM's forward pass."),
    make_claim_event("[AGENT-RESEARCH] The Epistemic Engine must support 'Metaphorical Pluralism'. The ontology of a 'Prompt' changes depending on the observer's abstraction layer: To the ML Engineer, it is `stdin`; to the Compiler Engineer, it is High-Level Source Code; to the Layman/End-User, it is simply The Program.")
]

with open("events/paradigm_events.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

# Materialize new node for Metaphorical Pluralism
node = {
  "id": "node:concept_polymorphic_prompt_metaphors",
  "type": "concept",
  "title": "Polymorphic Metaphors of the Prompt",
  "description": "[USER-INSIGHT] [AGENT-RESEARCH] To build a robust cognitive topology, the system must support multiple co-existing metaphorical frameworks based on the user's abstraction layer. 1. **The ML Engineer Lens (Bare Metal)**: The prompt is `stdin`, the weights are the compiled program. 2. **The Compiler Lens (Virtual Machine)**: The prompt is high-level Source Code, the KV cache is the AST/IR, the LLM is the Interpreter. 3. **The Layman Lens (HCI/End-User)**: A saved prompt like `research-process.md` *is* the 'Program' or 'App'. All intermediate complexity (tokenization, attention mechanisms, embeddings) 'falls out' of view, just as assembly code falls out of view when a user launches a web browser.",
  "status": "active",
  "tags": ["software2.0", "prompt", "metaphor", "abstraction", "hci", "epistemology"],
  "edges": [
      {"target": events[0]["id"], "relation": "supported_by"},
      {"target": events[1]["id"], "relation": "supported_by"},
      {"target": events[2]["id"], "relation": "supported_by"},
      {"target": "node:concept_prompt_as_source", "relation": "contextualizes"}
  ]
}

with open("nodes/node_concept_polymorphic_prompt_metaphors.json", "w") as f:
    json.dump(node, f, indent=2)

print("Polymorphic Metaphors synthesized and logged.")
