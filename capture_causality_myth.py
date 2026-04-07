import json
import uuid
import datetime
from pathlib import Path

EVENTS_DIR = Path("events")
NODES_DIR = Path("nodes")


def create_event(evt_type, title, details):
    evt_id = f"evt:epistemic:{uuid.uuid4().hex[:8]}"
    evt = {
        "id": evt_id,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "type": evt_type,
        "title": title,
        "details": details,
    }
    with open(EVENTS_DIR / "paradigm_events.jsonl", "a") as f:
        f.write(json.dumps(evt) + "\n")
    return evt_id


def create_node(node_id, title, description, tags, edges):
    node = {
        "id": node_id,
        "type": "concept",
        "title": title,
        "description": description,
        "status": "active",
        "tags": tags,
        "edges": edges,
    }
    with open(NODES_DIR / f"{node_id}.json", "w") as f:
        json.dump(node, f, indent=2)


# 1. Log the correction
evt_id = create_event(
    "EPISTEMIC_CORRECTION",
    "The Myth of the Causal Ledger",
    "Corrected the false assumption that an event ledger is a 'causal' graph. It is a lineage/correlation graph, not a strict causal engine.",
)

# 2. Create the Node defining the distinction
schema_description = """
Describing an Event Sourcing ledger as a 'causal graph' is an epistemic overreach. 

1. What 'Causal' Implies: True causality implies strict determinism and a complete mapping of preconditions (Event A was the necessary and sufficient physics required to produce Event B). 
2. Why it is Inaccurate: In a Software 2.0 system, the *true* cause of an event is a 100,000-token context window interacting with billions of floating-point weights. A JSON ledger event with a `{"parent_id": "123"}` field does not capture that massive, high-dimensional causality. It only captures a thin thread of *human-readable provenance* or *correlation*.
3. Does it have to be Causal? No. An accountant's ledger (-$50 for coffee) doesn't record the causal physics of *why* the accountant was tired. It only records the *accounting state mutation*. 

We do not need a causal physics engine to build an Agent OS. We just need **Lineage** (Where did this claim originate?) and **State Resolution** (How do we project these events into a UI?). Confusing lineage for causality leads to false confidence in our ability to predict the AI's behavior.
"""

create_node(
    "node_causality_vs_lineage",
    "Causality vs. Lineage (The Ledger)",
    schema_description.strip(),
    ["epistemology", "event_sourcing", "causality", "software_2_0"],
    [
        {"target": evt_id, "relation": "defined_by"},
        {"target": "node_ledger_vs_serialization", "relation": "refines"},
    ],
)

print("Causality vs Lineage distinction materialized.")
