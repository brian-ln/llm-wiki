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


# 1. Log the destruction of the binary
evt_id = create_event(
    "EPISTEMIC_AUDIT",
    "Dismantling the Deterministic/Non-Deterministic Binary",
    "Realized that treating Software 1.0 as 'deterministic' and Software 2.0 as 'non-deterministic' is a comforting but false binary. All complex systems are chaotic; the true axis is about constraint surfaces and systemic convergence.",
)

# 2. Create the Node defining the new paradigm
schema_description = """
The dialectic of 'Deterministic (Software 1.0) vs. Non-Deterministic (Software 2.0)' is a flawed mental model.

1. Software 1.0 is rarely deterministic in the wild. Network latency, thread scheduling, race conditions, and distributed state (CAP theorem) make traditional code highly chaotic. We just spend massive engineering effort (locks, retries, queues) to create the *illusion* of determinism.
2. Software 2.0 (LLMs) is fundamentally deterministic math (matrix multiplication). The same weights + same context + temperature 0 = exact same output. The perception of 'non-determinism' comes from the system's massive dimensionality and extreme sensitivity to initial conditions (prompt variations), not from actual randomness.

The correct way to view the architecture is through the lens of **High-Dimensionality vs. Low-Dimensionality Constraints**, or **Convergence vs. Divergence**. We use rigid, low-dimensional structures (schemas, event ledgers, type systems) to constrain high-dimensional pattern matchers (LLMs) so that the overall system *converges* on a reliable state, regardless of micro-variance.
"""

create_node(
    "node_false_dialectic",
    "The False Dialectic of Determinism",
    schema_description.strip(),
    ["epistemology", "software_2_0", "complex_systems", "convergence"],
    [
        {"target": evt_id, "relation": "defined_by"},
        {"target": "node_pure_determinism", "relation": "contradicts"},
        {"target": "node_probabilistic_predictability", "relation": "expands"},
    ],
)

print("False dialectic dismantled and recorded.")
