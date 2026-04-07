import json
import uuid
import datetime
from pathlib import Path

# Setup paths
EVENTS_DIR = Path("events")
NODES_DIR = Path("nodes")
EVENTS_DIR.mkdir(exist_ok=True)
NODES_DIR.mkdir(exist_ok=True)


def create_event(evt_type, title, details):
    evt_id = f"evt:stream:{uuid.uuid4().hex[:8]}"
    evt = {
        "id": evt_id,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "type": evt_type,
        "title": title,
        "details": details,
    }
    with open(EVENTS_DIR / "stream_events.jsonl", "a") as f:
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
    with open(NODES_DIR / f"{node_id.replace(':', '_')}.json", "w") as f:
        json.dump(node, f, indent=2)


# 1. Agentic Streams Concept
evt1 = create_event(
    "CONCEPT_DISCOVERY",
    "Define Agentic Streams",
    "Formalizing conversations as continuous event ledgers rather than static documents.",
)
create_node(
    "node:agentic_stream",
    "Agentic Stream",
    "A sequence of agent-user interactions, tool uses, and state mutations represented as a continuous, queryable event ledger (an execution trace). Unlike 'chat', a stream is a programmatic data structure.",
    ["streams", "event_sourcing", "execution_trace"],
    [{"target": evt1, "relation": "defined_by"}],
)

# 2. Stream Forking
evt2 = create_event(
    "CONCEPT_DISCOVERY",
    "Define Stream Forking",
    "The ability to branch execution traces, akin to git branches.",
)
create_node(
    "node:stream_forking",
    "Stream Forking",
    "Creating a divergent execution path from a specific point in an Agentic Stream. This allows exploring alternative solutions ('what if we used Rust instead of Python?') without polluting or destroying the primary context.",
    ["streams", "version_control", "branching"],
    [
        {"target": evt2, "relation": "defined_by"},
        {"target": "node:agentic_stream", "relation": "capability_of"},
    ],
)

# 3. Time Travel (Replay)
evt3 = create_event(
    "CONCEPT_DISCOVERY",
    "Define Stream Time Travel",
    "Navigating backwards in the event ledger to recover context or state.",
)
create_node(
    "node:stream_time_travel",
    "Stream Time Travel",
    "Because streams are append-only event ledgers, the system can deterministically reconstruct the exact context window and state graph of any past moment, enabling true reversibility and state inspection.",
    ["streams", "event_sourcing", "reversibility"],
    [
        {"target": evt3, "relation": "defined_by"},
        {"target": "node:agentic_stream", "relation": "capability_of"},
    ],
)

# 4. Agent Experience (AX)
evt4 = create_event(
    "CONCEPT_DISCOVERY",
    "Map AX (Agent Experience) to Streams",
    "Interfaces must be designed for programmatic API consumption by agents, not just visual UX.",
)
create_node(
    "node:ax_agent_experience",
    "Agent Experience (AX)",
    "The design discipline of creating affordances, protocols, and interfaces specifically optimized for autonomous LLM agents. Good AX for streams includes clear schema boundaries, explicit error states, and deterministic navigation tools.",
    ["ax", "ux", "design_patterns"],
    [{"target": evt4, "relation": "defined_by"}],
)

# Update the status of the planned topic
topic_path = NODES_DIR / "topic_ux_ax_sx_streams.json"
if topic_path.exists():
    with open(topic_path, "r") as f:
        topic_data = json.load(f)

    topic_data["status"] = "active"
    topic_data["description"] += (
        " [UPDATE: Concepts materialized for Streams, Forking, Time Travel, and AX.]"
    )
    topic_data["edges"].extend(
        [
            {"target": "node:agentic_stream", "relation": "explored_in"},
            {"target": "node:stream_forking", "relation": "explored_in"},
            {"target": "node:stream_time_travel", "relation": "explored_in"},
            {"target": "node:ax_agent_experience", "relation": "explored_in"},
        ]
    )

    with open(topic_path, "w") as f:
        json.dump(topic_data, f, indent=2)

print("Stream concepts formalized successfully.")
