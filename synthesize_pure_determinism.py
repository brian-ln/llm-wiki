import json
import datetime
import uuid

def make_claim_event(claim, source="user_inquiry:pure_determinism_examples"):
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
    make_claim_event("[AGENT-RESEARCH] Pure determinism exists almost exclusively in the realm of mathematics, theoretical computer science, and closed formal logic systems. It requires a domain free from thermodynamics, quantum uncertainty, and physical degradation."),
    make_claim_event("[AGENT-RESEARCH] Examples of purely deterministic systems include: 1. Mathematical Functions (e.g., the Fibonacci sequence, 2+2=4). 2. Cryptographic Hash Functions (e.g., SHA-256 mathematically guarantees the exact same output hash for the exact same input bit-string). 3. Cellular Automata (e.g., Conway's Game of Life, where the next grid state is perfectly calculable from the current state). 4. Theoretical Turing Machines and Deterministic Finite Automata (DFAs). 5. The rule-state graphs of perfect-information games like Chess or Tic-Tac-Toe."),
    make_claim_event("[AGENT-RESEARCH] The crucial distinction is between the *algorithm* (which is purely deterministic) and its *physical execution*. SHA-256 is mathematically pure, but when executed on a physical silicon CPU, a cosmic ray could flip a bit (a soft error), altering the output. We invent Error Correcting Codes (ECC) to force physical hardware to perfectly simulate theoretical determinism.")
]

with open("events/paradigm_events.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

node = {
  "id": "node:concept_pure_determinism",
  "type": "concept",
  "title": "Pure Determinism (Formal Systems vs Physical Reality)",
  "description": "[AGENT-RESEARCH] Pure determinism is a property of formal, theoretical systems completely isolated from physical entropy. Examples include mathematical operations (Fibonacci), cryptographic algorithms (SHA-256), Cellular Automata (Conway's Game of Life), and rulesets of perfect-information games (Chess). In these systems, State A + Input B will yield State C with 100% mathematical certainty until the end of time. However, the moment a purely deterministic algorithm is instantiated on physical hardware, it becomes subject to thermodynamics and quantum mechanics (e.g., bit flips from cosmic rays). Software 1.0 uses heavy abstraction (logic gates, ECC memory, checksums) to force chaotic physical matter to perfectly simulate these purely deterministic theoretical constructs.",
  "status": "active",
  "tags": ["determinism", "mathematics", "physics", "cellular_automata", "cryptography"],
  "edges": [
      {"target": events[0]["id"], "relation": "supported_by"},
      {"target": events[1]["id"], "relation": "supported_by"},
      {"target": events[2]["id"], "relation": "supported_by"},
      {"target": "node:concept_determinism", "relation": "clarifies"}
  ]
}

with open("nodes/node_concept_pure_determinism.json", "w") as f:
    json.dump(node, f, indent=2)

print("Pure determinism examples synthesized and logged.")
