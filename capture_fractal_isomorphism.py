import json
import uuid
import datetime
from pathlib import Path

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


# 1. Log the Fractal Insight
evt_id = create_event(
    "CONCEPT_SYNTHESIS",
    "Fractal Systems Isomorphism (AI to Human Orgs)",
    "Realized that the architectural principles of Agent OS constraint surfaces map perfectly 1:1 onto human organizational design, management theory, and complex adaptive systems.",
)

# 2. Materialize the Reframed Concept
schema_description = """
The principles used to manage high-dimensional AI models (Software 2.0) are fractally isomorphic to the principles of managing human teams and complex organizations.

The Doomed Pursuit (Micromanagement): 'How do we make a human/team/org act like a deterministic bash script?' This is the failure mode of rigid bureaucracy, Waterfall planning, and micromanagement. It attempts to force a complex, probabilistic entity into a rigid, low-dimensional execution path, crushing adaptability and resilience.

The Convergent Approach (Leadership & Culture): 'How do we define the fitness landscape so the human/team/org naturally collapses its probability wave into the right answer?' This is the essence of effective leadership, autonomous squads, and incentive design. You do not dictate the step-by-step physics of execution; you define the GOKR (the attractor), establish the cultural boundaries (the constraint surfaces), and allow the high-dimensional entity to creatively navigate the terrain toward the goal.
"""

create_node(
    "node_fractal_systems_isomorphism",
    "Fractal Systems Isomorphism (Agents to Orgs)",
    schema_description.strip(),
    ["epistemology", "systems_theory", "organizational_design", "isomorphism"],
    [
        {"target": evt_id, "relation": "defined_by"},
        {"target": "node_constraint_surfaces", "relation": "generalizes"},
    ],
)

print("Fractal systems isomorphism materialized.")
