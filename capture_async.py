import json
import uuid
import datetime
from pathlib import Path

# Setup paths
EVENTS_DIR = Path("events")
NODES_DIR = Path("nodes")


def create_event(evt_type, title, details):
    evt_id = f"evt:refinement:{uuid.uuid4().hex[:8]}"
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


# 1. Log the conceptual refinement
evt_id = create_event(
    "CONCEPT_REFINEMENT",
    "Asynchronous Agentic Threads",
    "Corrected the assumption that sidechains are strictly synchronous. /bg enables true parallel background processing, while /ug acts as the shared memory/IPC layer.",
)

# 2. Create the Node for Asynchronous Agentic Streams
schema_description = """
In the Software 2.0 Agent OS metaphor, 'sidechains' are not just synchronous blocking function calls; they are fully asynchronous worker threads.

1. Background Daemons (/bg): The user or main agent can spawn a background task (e.g., long-running research or refactoring). The main execution thread (the CLI REPL) immediately returns control to the user, allowing parallel work.
2. Shared Memory & IPC (/ug): Because these threads run asynchronously, they cannot simply return a single string to a blocking caller. They must coordinate via a shared state layer. The Universal Graph System (/ug) and the event ledgers serve as this Inter-Process Communication (IPC) layer, where background agents write their findings, and the main thread reads them.
"""

create_node(
    "node_async_agentic_threads",
    "Asynchronous Agentic Threads",
    schema_description.strip(),
    ["concurrency", "software_2_0", "ipc", "sidechains"],
    [
        {"target": evt_id, "relation": "defined_by"},
        {"target": "node_stream_event_ontology", "relation": "extends"},
    ],
)

print("Asynchronous thread ontology successfully captured.")
