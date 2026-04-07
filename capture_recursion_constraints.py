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


# 1. Log the conceptual boundary
evt_id = create_event(
    "CONCEPT_DISCOVERY",
    "Hierarchical Agent Constraints (Recursive Delegation)",
    "Analyzed why Software 2.0 Agent OSs must place limits on recursive sub-agent invocation (agents spawning agents spawning agents).",
)

# 2. Create the Node for Hierarchical Constraints
schema_description = """
While the Agent OS allows hierarchical delegation (agents spawning sub-agents via tools like `task` or `/bg`), recursive depth is structurally constrained by several Software 2.0 realities:

1. Epistemic Degradation (The Telephone Game): Unlike deterministic Software 1.0 function arguments, passing a prompt down a chain of probabilistic LLMs results in fidelity loss. The 3rd-level sub-agent often loses the original user's intent.
2. Token Economics & Latency: LLM calls (Syscalls) are economically and temporally expensive. Deep recursion acts like a massive blocking loop or a runaway token burn.
3. State Synchronization (Deadlocks): If Sub-Agent B spawns Sub-Agent C, coordinating shared state via the Graph (/ug) becomes complex. C might overwrite B's assumptions before B completes.
4. Runaway Recursion (Software 2.0 Stack Overflow): Without strict depth limits or "circuit breakers", autonomous agents trying to fix failing sub-agents can infinitely loop, exhausting API limits.

Therefore, 'Agent OS' designs usually enforce a shallow, wide hierarchy (a coordinator spawning many parallel workers) rather than a deep, recursive one.
"""

create_node(
    "node_hierarchical_agent_constraints",
    "Hierarchical Agent Constraints",
    schema_description.strip(),
    ["recursion", "software_2_0", "constraints", "epistemology"],
    [
        {"target": evt_id, "relation": "defined_by"},
        {"target": "node_async_agentic_threads", "relation": "constrains"},
    ],
)

print("Hierarchical constraints successfully captured.")
