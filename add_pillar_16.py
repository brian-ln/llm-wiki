import json
import datetime
import uuid

def make_claim_event(claim, source="user_input:20260407"):
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
    make_claim_event("Conversations with agentic AI are event logs, not just chat transcripts. They can be stored, remembered, replayed, reflected on, forked, joined, and annotated."),
    make_claim_event("The existing 'paper metaphors' (linear chat documents) limit our ability to truly work with AI conversations as a rich medium."),
    make_claim_event("Agentic conversations should be a first-class citizen in the llm-wiki concept, treated as a traversable graph of execution traces rather than a flat string of text.")
]

with open("events/paradigm_events.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

node = {
  "id": "node:concept_agentic_conversation",
  "type": "concept",
  "title": "Agentic Conversations as Event Logs",
  "description": "[USER-INSIGHT] The linear chat interface (a 'paper metaphor') fundamentally limits Human-AI collaboration. Under the Software 2.0 paradigm, a conversation with an agent is not a text document; it is an event log (or an execution trace). Because it is a structured ledger of actions, state changes, and logic, it can be replayed, forked, joined, and annotated as a first-class citizen within the knowledge graph. It transforms ephemeral chat into queryable, version-controlled cognitive topology.",
  "status": "active",
  "tags": ["software2.0", "paradigm", "event_sourcing", "conversation", "topology", "hallucination_16"],
  "edges": [
      {"target": events[0]["id"], "relation": "supported_by"},
      {"target": events[1]["id"], "relation": "supported_by"},
      {"target": events[2]["id"], "relation": "supported_by"}
  ]
}

with open("nodes/node_concept_agentic_conversation.json", "w") as f:
    json.dump(node, f, indent=2)

print("Pillar 16 logged and materialized.")
