import json
import datetime
import uuid

def make_claim_event(claim, source="raw/ideas.md"):
    return {
        "id": f"evt:logic:{uuid.uuid4().hex[:8]}",
        "timestamp": datetime.datetime.now().isoformat() + "Z",
        "actor": "algo",
        "action": "ASSERT_CLAIM",
        "payload": {
            "claim": claim,
            "source": source
        }
    }

events = [
    make_claim_event("[AGENT-RESEARCH] While Markdown is typically parsed linearly to render HTML, its structural syntax (Headers, Lists, Blockquotes) intrinsically defines a hierarchical tree. When hyperlinks `[node](url)` are added, it becomes a fully connected Directed Acyclic Graph (DAG) or a Document Object Model (DOM)."),
    make_claim_event("[AGENT-RESEARCH] Re-affirming Pillar 15: Markdown is merely the declarative *serialization format* (the map) of this graph. The underlying knowledge topology (the territory) can be queried, traversed, and mutated programmatically independently of the text format."),
    make_claim_event("[AGENT-RESEARCH] If an Agent OS parses this representation into an in-memory DAG, it can perform semantic extraction. Instead of arbitrary 'token chunking' (splitting a file every 1000 words for RAG), the OS can query specific sub-trees (e.g., 'Retrieve the H2 section on Database Config and its children')."),
    make_claim_event("[AGENT-RESEARCH] This semantic indexing transforms a flat filesystem of Markdown notes into a hyperlinked Graph Database, enabling the Agent OS to surgically load exact logical contexts into the LLM's 'RAM' (context window).")
]

with open("events/paradigm_events.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

node = {
  "id": "node:concept_markdown_dag",
  "type": "concept",
  "title": "Markdown as a Semantic DAG (Graph Database)",
  "description": "[AGENT-RESEARCH] Markdown is traditionally viewed as a flat markup language. However, mathematically, it is a serialization format for a Document Object Model (DOM) or Directed Acyclic Graph (DAG). Headers define tree hierarchy, lists define child nodes, and hyperlinks define cross-cutting edges. By treating it as a graph database, the Agent OS can parse the text into a traversable AST, allowing programatic querying of semantic sub-trees. This eliminates the need for 'dumb' token chunking in RAG pipelines; the Agent can surgically extract exactly the right logical branch of knowledge to feed into the Software 2.0 Processor's context window. Ultimately, Markdown is just one representation (Pillar 15) of this underlying cognitive topology.",
  "status": "active",
  "tags": ["software2.0", "markdown", "dag", "dom", "graph_database", "semantic_indexing"],
  "edges": [
      {"target": events[0]["id"], "relation": "supported_by"},
      {"target": events[1]["id"], "relation": "supported_by"},
      {"target": events[2]["id"], "relation": "supported_by"},
      {"target": events[3]["id"], "relation": "supported_by"},
      {"target": "node:ontology_representation", "relation": "instance_of"}
  ]
}

with open("nodes/node_concept_markdown_dag.json", "w") as f:
    json.dump(node, f, indent=2)

# Update sys_focus_areas to mark this as active/done
with open("nodes/sys_focus_areas.json", "r") as f:
    focus = json.load(f)

for edge in focus["edges"]:
    if edge["target"] == "topic:markdown_as_dag":
        edge["status"] = "materialized"

with open("nodes/sys_focus_areas.json", "w") as f:
    json.dump(focus, f, indent=2)

print("Markdown DAG concept synthesized and logged.")
