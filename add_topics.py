import json
import datetime
import uuid

def make_event(action, payload):
    return {
        "id": f"evt:topic:{uuid.uuid4().hex[:8]}",
        "timestamp": datetime.datetime.now().isoformat() + "Z",
        "actor": "algo",
        "action": action,
        "payload": payload
    }

events = [
    make_event("ASSERT_NODE", {
        "node_id": "topic:ux_ax_sx_streams",
        "type": "concept",
        "title": "UX/AX/SX of Agentic Streams",
        "description": "Exploration of the interaction paradigms for agentic event logs: forking, joining, annotating, tagging, 'choose your own adventure', time travel, and refining based on new information."
    }),
    make_event("ASSERT_NODE", {
        "node_id": "topic:software_2_0_mapping",
        "type": "concept",
        "title": "Software 1.0 to 2.0 Classical Computing Mapping",
        "description": "Mapping classical computing concepts (CPU, RAM, OS, syscalls, stdin) to their Software 2.0 equivalents (Neural Nets, Context Windows, Agents, Skills, Prompts)."
    }),
    make_event("ASSERT_NODE", {
        "node_id": "topic:markdown_as_dag",
        "type": "concept",
        "title": "Markdown as a DAG / Graph DB",
        "description": "Treating markdown files not as flat text, but as a directed acyclic graph (DAG) with a DOM-like structure, semantic line indexing, and hyperlinked graph database capabilities."
    })
]

with open("events/topic_events.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

# Materialize Focus Areas Index
focus_areas = {
    "id": "sys:focus_areas",
    "type": "protocol",
    "title": "Active Research Topics & Focus Areas",
    "description": "A materialized index of the active and planned research threads we are exploring in the Epistemic Engine.",
    "status": "active",
    "tags": ["system", "topics", "backlog"],
    "edges": [
        {"target": "topic:ux_ax_sx_streams", "relation": "tracks"},
        {"target": "topic:software_2_0_mapping", "relation": "tracks"},
        {"target": "topic:markdown_as_dag", "relation": "tracks"}
    ]
}

with open("nodes/sys_focus_areas.json", "w") as f:
    json.dump(focus_areas, f, indent=2)

# Materialize UX Topic Node
ux_node = {
    "id": "topic:ux_ax_sx_streams",
    "type": "concept",
    "title": "UX/AX/SX of Agentic Streams",
    "description": "Future exploration area: If AI conversations are event logs (traces), we need new interfaces (UX/AX) to manipulate them. This includes forking a conversation, joining branches, annotating streams, 'time travel' (reverting to a past state and branching), and markup of streams.",
    "status": "planned",
    "tags": ["ux", "ax", "agent_experience", "event_sourcing"],
    "edges": [{"target": events[0]["id"], "relation": "defined_by"}]
}
with open("nodes/topic_ux_ax_sx_streams.json", "w") as f:
    json.dump(ux_node, f, indent=2)

print("Topics and focus areas formalized.")
