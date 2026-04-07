import json
import datetime
import uuid

def make_claim_event(claim, source="user_insight:determinism_myth"):
    return {
        "id": f"evt:logic:{uuid.uuid4().hex[:8]}",
        "timestamp": datetime.datetime.now().isoformat() + "Z",
        "actor": "human",
        "action": "ASSERT_CLAIM",
        "payload": {
            "claim": claim,
            "source": source
        }
    }

events = [
    make_claim_event("[USER-INSIGHT] Determinism is an illusion, a myth, and a mathematical crutch. In physical reality, computing systems are at best 'probabilistically predictable' due to thermodynamics, quantum uncertainty, and hardware degradation."),
    make_claim_event("[USER-INSIGHT] Because pure determinism does not exist outside of formal logic, everything in the real world fundamentally requires a 'try/catch' clause somewhere in its architecture to handle the probabilistic nature of reality.")
]

with open("events/paradigm_events.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

node = {
  "id": "node:concept_probabilistic_predictability",
  "type": "concept",
  "title": "The Myth of Determinism (Probabilistic Predictability)",
  "description": "[USER-INSIGHT] Determinism is an engineered illusion and a mathematical crutch. While pure determinism exists in formal logic and cryptography (e.g., node:concept_pure_determinism), physical reality is governed by thermodynamics, quantum uncertainty, and degradation. Therefore, classical computing is not truly deterministic; it is 'probabilistically predictable' with a very high confidence interval. Recognizing this breaks the false binary between 'deterministic code' and 'chaotic AI'. Because the real world is probabilistic, every system—whether Software 1.0 or 2.0—fundamentally requires a 'try/catch' clause or convergence loop somewhere in its architecture to handle inevitable physical or statistical deviation.",
  "status": "active",
  "tags": ["software1.0", "software2.0", "determinism", "physics", "error_handling", "hallucination_17"],
  "edges": [
      {"target": events[0]["id"], "relation": "supported_by"},
      {"target": events[1]["id"], "relation": "supported_by"},
      {"target": "node:concept_pure_determinism", "relation": "contrasts_with"},
      {"target": "node:concept_determinism", "relation": "extends"}
  ]
}

with open("nodes/node_concept_probabilistic_predictability.json", "w") as f:
    json.dump(node, f, indent=2)

print("Pillar 17 events and node materialized.")
