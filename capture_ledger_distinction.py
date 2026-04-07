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


# 1. Log the Epistemic Correction
evt_id = create_event(
    "EPISTEMIC_CORRECTION",
    "Separating the Ledger from its Serialization Format",
    "Realized that the JSONL file is merely a storage projection (a serialization format) of the Ledger, not the Ledger itself.",
)

# 2. Create the Node defining the True Ledger
schema_description = """
A common architectural fallacy is conflating the conceptual 'Ledger' with its physical storage format (e.g., a `.jsonl` file or a SQLite `.db`).

The true 'Ledger' is the mathematical, append-only set of state transitions (the causal graph of events). 

A `.jsonl` file is just a low-fidelity, 1D serialization format used to persist that mathematical set to a physical hard drive. It is a projection. If you switch from `.jsonl` to SQLite, or to a distributed Kafka stream, the Ledger itself has not changed—only its storage medium.

Conflating the two leads to false constraints, such as assuming the Ledger must be strictly ordered just because a text file is strictly ordered line-by-line.
"""

create_node(
    "node_ledger_vs_serialization",
    "Ledger vs. Serialization Format",
    schema_description.strip(),
    ["epistemology", "architecture", "event_sourcing", "data_structures"],
    [
        {"target": evt_id, "relation": "defined_by"},
        {"target": "node_deterministic_ledger", "relation": "refines"},
    ],
)

print("Ledger vs Serialization distinction materialized.")
