import json
import uuid
import datetime
from pathlib import Path

EVENTS_DIR = Path("events")
NODES_DIR = Path("nodes")


def create_event(evt_type, title, details):
    evt_id = f"evt:cbt:{uuid.uuid4().hex[:8]}"
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


# 1. Log the CBT Correction
evt_id = create_event(
    "EPISTEMIC_CORRECTION",
    "CBT Audit: Dismantling 'Absolute' Goals",
    "Applied Cognitive Behavioral Therapy (CBT) framing to identify 'All-or-Nothing' thinking in the definition of GOKR. Goals are not absolute coordinates; they are provisional directional vectors.",
)

# 2. Materialize the Reframed Concept
schema_description = """
Applying a CBT-style cognitive restructuring to systems architecture:

- The Distortion (All-or-Nothing Thinking): 'GOKR defines the absolute X/Y/Z coordinates of Done.'
- The Reality: In complex, high-dimensional spaces, 'Done' is never absolute. As an agent executes, it uncovers hidden constraints (e.g., undocumented API limits, structural tech debt). If Key Results are treated as absolute physics, the system falls victim to Goodhart's Law (optimizing the metric while destroying the actual value).
- The Reframe: GOKR and Fitness Functions are *Provisional Heuristics* and *Directional Vectors*. They act as a compass, not a fixed GPS coordinate. They provide enough local gravity to induce convergence, but the 'destination' itself is a living hypothesis that must be constantly renegotiated by the agent and the human as reality pushes back.
"""

create_node(
    "node_provisional_heuristics",
    "Provisional Heuristics over Absolute Goals",
    schema_description.strip(),
    ["epistemology", "cbt", "gokr", "heuristics", "goodharts_law"],
    [
        {"target": evt_id, "relation": "defined_by"},
        {"target": "node_gokr_fitness_landscape", "relation": "refines"},
    ],
)

print("CBT correction materialized: Provisional Heuristics over Absolute Goals.")
