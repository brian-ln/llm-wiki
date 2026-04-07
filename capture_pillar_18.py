import json
import uuid
import datetime
from pathlib import Path
import re

# Setup paths
EVENTS_DIR = Path("events")
NODES_DIR = Path("nodes")
IDEAS_FILE = Path("BRIANS_CRAZY_IDEAS_AND_HALLUCINATIONS.md")


def create_event(evt_type, title, details):
    evt_id = f"evt:brian:{uuid.uuid4().hex[:8]}"
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


# 1. Log the core Brian insight
evt_id = create_event(
    "CORE_PILLAR_DEFINED",
    "Constraint Surfaces over Determinism",
    "Brian formalized the core architectural philosophy of the Epistemic Engine: We don't need determinism. We need constraint surfaces that force chaotic systems to converge.",
)

# 2. Materialize the Concept
schema_description = """
The architectural principle that complex, high-entropy AI systems (Software 2.0) cannot and should not be made perfectly deterministic. 

Instead of fighting chaos, the system architecture provides rigid, low-dimensional boundaries (JSON schemas, append-only ledgers, IAC consensus thresholds). These are 'Constraint Surfaces'. 

They do not dictate *how* the chaotic LLM engine reasons (preserving its high-dimensional creativity), but they guarantee that its outputs mechanically *converge* into a usable, predictable, and measurable state. It shifts the engineering goal from 'impossible deterministic perfection' to 'managed probability'.
"""

create_node(
    "node_constraint_surfaces",
    "Constraint Surfaces over Determinism",
    schema_description.strip(),
    ["epistemology", "brians_ideas", "software_2_0", "convergence", "architecture"],
    [{"target": evt_id, "relation": "defined_by"}],
)

# 3. Update BRIANS_CRAZY_IDEAS_AND_HALLUCINATIONS.md
if IDEAS_FILE.exists():
    with open(IDEAS_FILE, "r") as f:
        content = f.read()

    pillar_text = """
### Pillar 18: Constraint Surfaces over Determinism
We do not need strict Software 1.0 determinism in AI systems. The goal is not to force a chaotic, high-dimensional probability engine (an LLM) to act like a rigid `while` loop. Instead, we build **Constraint Surfaces**—low-dimensional, rigid boundaries like JSON schemas, append-only event ledgers, and Independent Agent Convergence (IAC) thresholds. These surfaces don't control *how* the system thinks; they force the chaotic outputs to mechanically *converge* into a reliable, predictable state.
"""
    if "Pillar 18" not in content:
        content += "\n" + pillar_text.strip() + "\n"
        with open(IDEAS_FILE, "w") as f:
            f.write(content)
        print("Pillar 18 added to BRIANS_CRAZY_IDEAS_AND_HALLUCINATIONS.md")
    else:
        print("Pillar 18 already exists.")
else:
    print("Ideas file not found.")
