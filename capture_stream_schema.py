import json
import uuid
import datetime
from pathlib import Path

# Setup paths
EVENTS_DIR = Path("events")
NODES_DIR = Path("nodes")


def create_event(evt_type, title, details):
    evt_id = f"evt:schema:{uuid.uuid4().hex[:8]}"
    evt = {
        "id": evt_id,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "type": evt_type,
        "title": title,
        "details": details,
    }
    with open(EVENTS_DIR / "protocol_updates.jsonl", "a") as f:
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


# 1. Log the protocol design
evt_id = create_event(
    "PROTOCOL_DESIGN",
    "Define Agentic Stream Event Ontology",
    "Formalized the JSON schema event types required to capture Software 2.0 execution traces (Agentic Streams), bridging the hybrid execution gap.",
)

# 2. Create the Ontology Node
schema_description = """
The formal ontology for serializing Agentic Streams into an event ledger. To capture the Software 1.0/2.0 hybrid architecture, the ledger must record specific state transitions beyond just 'user message' and 'assistant message'.

Core Event Types:
1. CONTEXT_ENRICHMENT: Triggered when progressive disclosure occurs (e.g., reading a `docs/` file because SKILL.md lacked detail). Records `file_path` and `bytes_loaded`.
2. SUBAGENT_FORK: Triggered by `context: fork`. Records the `parent_stream_id`, the new `child_stream_id`, and the `task_prompt`.
3. EXECUTION_BYPASS: Triggered by `disable-model-invocation: true`. Records the `command_executed` directly, bypassing the LLM reasoning step.
4. EPISTEMIC_ASSERTION: Triggered when the agent applies a rigor tag ([MEASURED], [CITED]). Records the `claim_text`, the `rigor_tag`, and the `evidence_pointer`.
5. HYBRID_INVOCATION: Triggered when a skill is called. Records the `skill_name`, `arguments`, and whether it rendered a `no-args_card` or executed a subprocess.
"""

create_node(
    "node_stream_event_ontology",
    "Agentic Stream Event Ontology",
    schema_description.strip(),
    ["schema", "event_sourcing", "streams", "ontology"],
    [{"target": evt_id, "relation": "defined_by"}],
)

# 3. Create a Topic for Future Exploration
topic_id = "topic_stream_ledger_implementation"
create_node(
    topic_id,
    "Stream Ledger Implementation",
    "Exploration of how to implement the Agentic Stream Event Ontology into the physical local database. How do we intercept these state changes during live execution and write them to SQLite/JSONL without blocking the agent's token stream?",
    ["implementation", "database", "streams"],
    [{"target": "node_stream_event_ontology", "relation": "implements"}],
)

print("Stream Event Ontology and Implementation Topic successfully recorded.")
