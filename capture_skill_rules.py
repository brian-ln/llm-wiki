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
    evt_id = f"evt:rule:{uuid.uuid4().hex[:8]}"
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
        "type": "protocol",
        "title": title,
        "description": description,
        "status": "active",
        "tags": tags,
        "edges": edges,
    }
    with open(NODES_DIR / f"{node_id.replace(':', '_')}.json", "w") as f:
        json.dump(node, f, indent=2)


# 1. The Core Event
evt1 = create_event(
    "PROTOCOL_SYNTHESIS",
    "Formalize Skill Governance Rules",
    "Extracted the engineering methodologies and auditing dimensions enforced by the skillsmith meta-skill, including MFT, Progressive Context, and Adversarial Review.",
)

# 2. Progressive Context Enrichment
create_node(
    "node:progressive_context_enrichment",
    "Progressive Context Enrichment",
    "A context RAM management protocol. The primary skill interface (SKILL.md) acts as a lean routing table (<500 lines). Heavy documentation, scenario logic, and templates are isolated in docs/ and loaded dynamically only when the agent explicitly requests them. Prevents LLM context exhaustion.",
    ["context_management", "software_2_0", "optimization"],
    [{"target": evt1, "relation": "defined_by"}],
)

# 3. Mechanism-First Testing (MFT) & Scenario Design
create_node(
    "node:mechanism_first_testing",
    "Mechanism-First Testing (MFT) & Scenario Design",
    "A testing philosophy demanding that fallback paths, error states, and capability assumptions be explicitly tested against non-mock backends. Requires scenario-based fixtures (tests/fixtures/) and ensures that silent failures (e.g., zero-row returns) break the build. Vital for skills dealing with measurement or benchmarks.",
    ["testing", "epistemic_rigor", "mft"],
    [{"target": evt1, "relation": "defined_by"}],
)

# 4. Multi-Dimensional Auditing
create_node(
    "node:skill_audit_dimensions",
    "Multi-Dimensional Skill Auditing",
    "Skills are evaluated across orthogonal axes: Implementation Match (Review), Epistemic Contract (Rigor), Path Coverage (Test-Coverage), Safety (Security), and Agent Experience (AX). Failure in one dimension (e.g., missing fallback test) does not block others, ensuring precise fault isolation.",
    ["auditing", "governance", "ax"],
    [{"target": evt1, "relation": "defined_by"}],
)

# 5. Adversarial Review & Epistemic Contracts
create_node(
    "node:adversarial_review_contract",
    "Adversarial Review & Epistemic Contracts",
    "Mandates that measurement skills explicitly declare an 'epistemic-contract' in their YAML frontmatter. Claims must be tagged (MEASURED, CITED, etc.). Adversarial review enforces strict causal language discipline and tests performance against worst-case distributions to prevent LLM overclaiming.",
    ["epistemology", "rigor", "governance"],
    [{"target": evt1, "relation": "defined_by"}],
)

# 6. Agent Experience (AX) Dimensions
create_node(
    "node:ax_audit_dimensions",
    "Agent Experience (AX) Audit Dimensions",
    "Metrics for programmatic consumption: Vocabulary Ergonomics, State Machine Clarity, Error Signal Fidelity, Scope Transparency, Operational Guarantees (idempotency), Structured Output Formats, and Next-Action Guidance.",
    ["ax", "ux", "metrics"],
    [{"target": evt1, "relation": "defined_by"}],
)

print(
    "Skill governance rules and methodologies successfully materialized to the graph."
)
