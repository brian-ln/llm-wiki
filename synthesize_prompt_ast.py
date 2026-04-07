import json
import datetime
import uuid

def make_claim_event(claim, source="user_inquiry:ast_ir_metaphor"):
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
    make_claim_event("[AGENT-RESEARCH] If we view the LLM not as a raw CPU, but as an Interpreter or Virtual Machine (like the JVM), then the Prompt is not the AST/IR; the Prompt is the High-Level Source Code (written in natural language)."),
    make_claim_event("[AGENT-RESEARCH] In this 'Prompting-as-Programming' metaphor, the LLM parses the Prompt and projects it into high-dimensional continuous embeddings. This embedding space (and the resulting KV Cache) is the true analog to the AST (Abstract Syntax Tree) or IR (Intermediate Representation)—it is the machine-readable structural representation of the user's intent."),
    make_claim_event("[AGENT-RESEARCH] Storing a prompt as `research-process.md` is exactly analogous to storing a `.sh` shell script or `.py` python file. It is a 'Software 2.0 Script' or 'Cognitive Routine'. When the Agent OS reads this file and pipes it to the LLM, it is invoking a stored program.")
]

with open("events/paradigm_events.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

# Materialize new node for the Prompt-as-Source metaphor
node = {
  "id": "node:concept_prompt_as_source",
  "type": "concept",
  "title": "Prompts as Software 2.0 Source Code",
  "description": "[HYPOTHESIS] [AGENT-RESEARCH] Depending on the abstraction level, a prompt's ontology shifts. At the hardware/training level (Karpathy's strict Software 2.0), weights are the compiled binary and the prompt is `stdin`. However, at the Agent OS level (In-Context Learning), the LLM acts as an Interpreter/VM. Here, the Prompt is the High-Level Source Code (Natural Language). The LLM compiles this prompt into continuous latent embeddings and a KV Cache, which serve as the AST (Abstract Syntax Tree) or IR (Intermediate Representation). Therefore, a file like `research-process.md` is functionally a Software 2.0 executable script.",
  "status": "active",
  "tags": ["software2.0", "prompt", "ast", "ir", "metaphor", "script"],
  "edges": [
      {"target": events[0]["id"], "relation": "supported_by"},
      {"target": events[1]["id"], "relation": "supported_by"},
      {"target": events[2]["id"], "relation": "supported_by"},
      {"target": "node:concept_prompt", "relation": "extends"}
  ]
}

with open("nodes/node_concept_prompt_as_source.json", "w") as f:
    json.dump(node, f, indent=2)

print("AST/IR metaphor synthesized and logged.")
