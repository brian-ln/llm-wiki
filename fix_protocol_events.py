import json
import datetime
import uuid

def make_protocol_update_event(title, description):
    return {
        "id": f"evt:sys:{uuid.uuid4().hex[:8]}",
        "timestamp": datetime.datetime.now().isoformat() + "Z",
        "actor": "human_algo_council",
        "action": "UPDATE_NODE",
        "payload": {
            "node_id": "sys:cap:protocol_updates",
            "change": title,
            "patch": {
                "description": description
            }
        }
    }

events = [
    make_protocol_update_event("Added Resilient Fetching Protocol", "Added a rule to OPERATIONS.md to explicitly use fallback methods like curl + jina.ai or custom python scripts with User-Agent headers when the standard webfetch tool is blocked."),
    make_protocol_update_event("Enforced Strict Raw Immutability", "Added a rule prohibiting YAML frontmatter in /raw/ files to maintain byte-for-byte integrity. Provenance is now strictly managed via INGEST_RAW events and the sys_raw_index node."),
    make_protocol_update_event("Mandated Epistemic Rigor Tagging", "Added a rule to explicitly tag analogical syntheses as [HYPOTHESIS] and [AGENT-RESEARCH] and perform an EPISTEMIC_AUDIT when mapping formal concepts to industry metaphors (e.g., Software 2.0).")
]

with open("events/protocol_updates.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

print("Protocol updates logged to ledger.")
