import json
import datetime
import uuid

def make_claim_event(claim, source="user_inquiry:determinism"):
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
    make_claim_event("[AGENT-RESEARCH] Theoretical Determinism: A system is deterministic if, given the exact same initial state and inputs, it will always traverse the exact same sequence of states and produce the exact same output. No randomness is involved."),
    make_claim_event("[AGENT-RESEARCH] Software 1.0 Illusion: Classical computing is built on the *assumption* of determinism. We design digital abstractions (logic gates, ISAs, TCP/IP) specifically to squash and hide the inherent chaos of the physical analog world (thermal noise, voltage fluctuations, quantum effects)."),
    make_claim_event("[AGENT-RESEARCH] Physical Non-Determinism: In physical reality, computers are rarely perfectly deterministic. They suffer from Single-Event Upsets (cosmic rays flipping bits), network packet drops, race conditions in multi-threading, and non-associative floating-point math differences across hardware architectures."),
    make_claim_event("[AGENT-RESEARCH] Software 2.0 Determinism: Ironically, the forward pass of an LLM is a strictly deterministic mathematical equation. However, it *becomes* non-deterministic in practice for two reasons: 1) Hardware: Highly parallel GPUs sum floating-point numbers in unpredictable orders, causing microscopic rounding differences that cascade. 2) Artificial Entropy: We intentionally inject randomness ('Temperature') during token sampling because strict determinism leads to repetitive, degenerate output loops.")
]

with open("events/paradigm_events.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

node = {
  "id": "node:concept_determinism",
  "type": "concept",
  "title": "The Illusion of Determinism in Computing",
  "description": "[AGENT-RESEARCH] Determinism strictly means that a specific input to a specific state always yields the exact same output. In Software 1.0, determinism is a heavily engineered illusion—logic gates are designed to squash analog noise into discrete 1s and 0s. Yet, true determinism constantly leaks via race conditions, hardware faults (cosmic rays), and asynchronous network latency. In Software 2.0, the core mathematical operations (matrix multiplications) are technically deterministic, but execution on massively parallel GPUs introduces floating-point non-associativity (hardware non-determinism). Furthermore, the paradigm intentionally injects entropy (Temperature > 0) to avoid degenerate, repetitive outputs, shifting the system from deterministic to probabilistic.",
  "status": "active",
  "tags": ["software1.0", "software2.0", "determinism", "physics", "hardware", "probability"],
  "edges": [
      {"target": events[0]["id"], "relation": "supported_by"},
      {"target": events[1]["id"], "relation": "supported_by"},
      {"target": events[2]["id"], "relation": "supported_by"},
      {"target": events[3]["id"], "relation": "supported_by"}
  ]
}

with open("nodes/node_concept_determinism.json", "w") as f:
    json.dump(node, f, indent=2)

print("Determinism concept synthesized and logged.")
