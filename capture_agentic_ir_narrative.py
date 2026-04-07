import json
import datetime
import os

timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

# 1. Create the new node for Agentic IR
ir_node = {
  "id": "node:agentic_ir",
  "type": "concept",
  "title": "Agentic Intermediate Representation (IR)",
  "description": "In Software 2.0 (Agent OS), imperative code (like Python scripts) used to mutate state are transient, single-use 'bytecode'. The true source code (the Intermediate Representation or IR) consists of: 1) The Intent (GOKR heuristic), 2) The Constraint Surface (Schema/Rules), and 3) The Event Ledger (Execution Trace). Storing the deterministic Python script is a Software 1.0 anti-pattern; instead, we store the IR, allowing the LLM to JIT-compile the actuator script based on the current system constraints.",
  "status": "active",
  "tags": ["software_2_0", "architecture", "agentic_ir", "epistemic"],
  "edges": [
    {"target": "node:constraint_surfaces", "relation": "constrained_by"},
    {"target": "topic:agentic_ir_vs_transient_code", "relation": "formalizes"}
  ]
}

with open('nodes/node_agentic_ir.json', 'w') as f:
    json.dump(ir_node, f, indent=2)

# 2. Create the taxonomy node for Agentic Operations
taxonomy_node = {
  "id": "node:agentic_operations_taxonomy",
  "type": "concept",
  "title": "Taxonomy of Agentic Graph Operations",
  "description": "Analysis of the transient actuation scripts revealed four distinct architectural intents: 1) ETL & Ingestion (rigid parsers, raw appended to ledger), 2) Transform & Synthesis (LLM map-reduce applying cognitive lenses), 3) Migrations (structural refactoring of schemas), 4) Actuators (single-use JSON mutators bridging high-dimensional intent to low-dimensional filesystem).",
  "status": "active",
  "tags": ["architecture", "taxonomy", "operations"],
  "edges": [
    {"target": "node:agentic_ir", "relation": "implements"}
  ]
}

with open('nodes/node_agentic_operations_taxonomy.json', 'w') as f:
    json.dump(taxonomy_node, f, indent=2)

# 3. Log the events
events = [
    {
        "id": f"evt:paradigm:ir_concept_{int(datetime.datetime.now().timestamp())}",
        "timestamp": timestamp,
        "type": "LEARN_CONCEPT",
        "concept": "Agentic Intermediate Representation (IR)",
        "details": "Formalized the distinction between declarative Agentic IR (Intent + Schema) and transient Software 1.0 bytecode (Python actuator scripts)."
    },
    {
        "id": f"evt:paradigm:taxonomy_{int(datetime.datetime.now().timestamp())}",
        "timestamp": timestamp,
        "type": "LEARN_CONCEPT",
        "concept": "Agentic Operations Taxonomy",
        "details": "Categorized 35 transient python scripts into ETL, Transform, Migration, and Actuator operational intents."
    }
]

with open('events/paradigm_events.jsonl', 'a') as f:
    for event in events:
        f.write(json.dumps(event) + '\n')

print("[MEASURED] Nodes and events for Agentic IR and Operations Taxonomy successfully written.")
