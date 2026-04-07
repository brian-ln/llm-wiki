import json
import uuid
import datetime
from pathlib import Path

# Setup paths
EVENTS_DIR = Path("events")
NODES_DIR = Path("nodes")


def create_event(evt_type, title, details):
    evt_id = f"evt:paradigm:{uuid.uuid4().hex[:8]}"
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


# 1. Log the definition
evt_id = create_event(
    "CONCEPT_DISCOVERY",
    "Define Deterministic Ledger",
    "Formalized the definition and critical necessity of the deterministic ledger (Event Sourcing) in taming Software 2.0 entropy.",
)

# 2. Create the Node
schema_description = """
A Deterministic Ledger is an append-only, immutable log of discrete state-mutating events (like financial transactions in an accounting ledger). 

In the Software 1.0 / Software 2.0 hybrid architecture, it is the ultimate 'Source of Truth'. Because LLMs are probabilistic, their outputs are treated as volatile. Instead of allowing an LLM to destructively overwrite a file or database row (CRUD), the system forces the LLM to append a 'Mutation Event' to the ledger.

If you delete the entire materialized knowledge graph (the `nodes/` directory) and replay the ledger from the beginning, the rigid Software 1.0 materializer will deterministically reconstruct the exact same graph every single time.
"""

create_node(
    "node_deterministic_ledger",
    "Deterministic Ledger (Event Sourcing)",
    schema_description.strip(),
    ["event_sourcing", "software_1_0", "architecture", "epistemology"],
    [
        {"target": evt_id, "relation": "defined_by"},
        {"target": "node_pure_determinism", "relation": "implements"},
        {"target": "node_probabilistic_predictability", "relation": "tames"},
    ],
)

print("Deterministic Ledger concept materialized.")
