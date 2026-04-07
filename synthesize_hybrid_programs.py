import json
import datetime
import uuid

def make_claim_event(claim, source="agent_research:local_skill_inspection"):
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
    make_claim_event("[MEASURED] Markdown files defining agents or skills (like `SKILL.md`) are Hybrid Programs. The Agent OS parses parts of the file (e.g., YAML frontmatter defining routes, allowed tools, and metadata) using strict, deterministic Software 1.0 logic. Only the body of the file is evaluated probabilistically by the Software 2.0 LLM."),
    make_claim_event("[AGENT-RESEARCH] Because Markdown is a DAG (a DOM), it does not strictly require SW 2.0 interpretation. A deterministic parser can extract specific nodes—such as a `<bash>` code block or an `<example>` tag—and execute them directly on the host machine without ever invoking the probabilistic neural network."),
    make_claim_event("[AGENT-RESEARCH] In Software 1.0, we tame real-world non-determinism (network drops, hardware faults, human error) using architectural patterns: Idempotency (safe retries), State Machines (enforced valid transitions), Strict Typing/Schemas, and Exponential Backoff loops."),
    make_claim_event("[AGENT-RESEARCH] To make Software 2.0 Markdown programs 'more deterministic' or predictable, we map these SW 1.0 patterns into the Agent OS. The OS enforces JSON Schema validation on LLM outputs (Typing), runs `try/catch` re-prompt loops if the LLM hallucinates (Retries), and restricts the LLM's available toolset to safe, idempotent operations (State Constraints).")
]

with open("events/paradigm_events.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

# Node 1: Hybrid Markdown Programs
node_hybrid = {
  "id": "node:concept_hybrid_markdown_programs",
  "type": "concept",
  "title": "Markdown Skills as Hybrid Programs",
  "description": "[MEASURED] [AGENT-RESEARCH] Agents and skills defined in Markdown (e.g., Claude Code `SKILL.md` files) are structurally 'Hybrid Programs'. They are not exclusively Software 2.0 prompts. Because Markdown is a parsable DAG, the Agent OS reads the file and routes different sub-trees to different processors. The YAML frontmatter (defining routes, allowed tools, UI descriptions) is routed to a deterministic Software 1.0 parser. The natural language body is routed to the probabilistic Software 2.0 LLM. Furthermore, embedded artifacts (like code blocks) can be executed directly by the OS, bypassing the LLM entirely. Therefore, a Markdown skill is a unified source file compiling down to both deterministic machine code and probabilistic neural conditioning.",
  "status": "active",
  "tags": ["software1.0", "software2.0", "markdown", "hybrid", "skills", "agents"],
  "edges": [
      {"target": events[0]["id"], "relation": "supported_by"},
      {"target": events[1]["id"], "relation": "supported_by"},
      {"target": "node:concept_markdown_dag", "relation": "extends"},
      {"target": "node:concept_agent_os", "relation": "executed_by"}
  ]
}

with open("nodes/node_concept_hybrid_markdown_programs.json", "w") as f:
    json.dump(node_hybrid, f, indent=2)

# Node 2: Taming Non-Determinism
node_taming = {
  "id": "node:concept_taming_nondeterminism",
  "type": "concept",
  "title": "Taming Non-Determinism (SW 1.0 vs SW 2.0)",
  "description": "[AGENT-RESEARCH] In the non-deterministic physical world, Software 1.0 relies on architectural guardrails: Idempotency, State Machines, Type-Checking/Schemas, and Retry Loops (try/catch). To make Software 2.0 'Markdown programs' more predictable, these exact same patterns must be ported to the Agent OS level. The OS must enforce Schema Validation (Type-Checking) on the LLM's output. If the LLM hallucinates or outputs malformed data, the OS catches the error and automatically injects the stack trace back into the context window (the SW 2.0 equivalent of a Retry Loop). By wrapping the probabilistic LLM in a rigid, deterministic Software 1.0 scaffolding, we tame the entropy of the neural processor.",
  "status": "active",
  "tags": ["determinism", "error_handling", "software1.0", "software2.0", "architecture", "reliability"],
  "edges": [
      {"target": events[2]["id"], "relation": "supported_by"},
      {"target": events[3]["id"], "relation": "supported_by"},
      {"target": "node:concept_probabilistic_predictability", "relation": "implements"}
  ]
}

with open("nodes/node_concept_taming_nondeterminism.json", "w") as f:
    json.dump(node_taming, f, indent=2)

print("Hybrid programming and non-determinism concepts synthesized and logged.")
