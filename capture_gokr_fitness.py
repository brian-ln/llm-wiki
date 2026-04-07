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


# 1. Log the synthesis
evt_id = create_event(
    "CONCEPT_SYNTHESIS",
    "GOKR and Fitness Functions as Attractors",
    "Connected the concept of 'Constraint Surfaces' to GOKR, fitness functions, and evaluation loops. These define the 'gravity' that pulls chaotic execution toward a success state.",
)

# 2. Materialize the Concept
schema_description = """
If an Agent OS is a constraint surface bounding a chaotic Software 2.0 fluid, then GOKR (Goals, Objectives, Key Results) and Fitness/Evaluation functions are the 'attractors' or 'gravity' on that surface.

Because we cannot write step-by-step Software 1.0 instructions for how an LLM should solve a novel problem, we must instead define the coordinate system of success.
- GOKR provides the absolute coordinates of the destination.
- Key Results (falsifiable metrics) act as the sensors.
- Fitness/Evaluation functions act as the gradient. 

The agent's execution loop (internal self-reflection via `/converge`) and external verification (via `/council` or human review) continually measure the agent's current state against the fitness function, steering the probability wave until it collapses into the defined success criteria.
"""

create_node(
    "node_gokr_fitness_landscape",
    "GOKR as the Fitness Landscape",
    schema_description.strip(),
    ["epistemology", "gokr", "software_2_0", "convergence", "eval"],
    [
        {"target": evt_id, "relation": "defined_by"},
        {"target": "node_constraint_surfaces", "relation": "implements"},
    ],
)

print("GOKR and Fitness functions materialized as constraint attractors.")
