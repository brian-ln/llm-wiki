import json
import os
import datetime

# 1. Update the Focus Areas node
with open('nodes/sys_focus_areas.json', 'r') as f:
    data = json.load(f)

data['edges'].append({
    "target": "topic:agentic_ir_vs_transient_code",
    "relation": "tracks",
    "status": "planned"
})

with open('nodes/sys_focus_areas.json', 'w') as f:
    json.dump(data, f, indent=2)

# 2. Append Epistemic Audit and Update events
audit_event = {
    "id": "evt:sys:audit_ir_concept",
    "type": "EPISTEMIC_AUDIT",
    "target_id": "topic:agentic_ir_vs_transient_code",
    "audit_type": "VALIDATION",
    "rationalization": "Python actuation scripts are Software 1.0 bytecode, not Software 2.0 source code. The true source is the Intent + Constraint Schema.",
    "null_hypothesis": "If an LLM cannot reliably regenerate the 1.0 Python bytecode from the declarative IR (Intent + Schema), then the IR is an insufficient abstraction and we must version-control the deterministic scripts."
}

update_event = {
    "id": "evt:sys:add_ir_focus",
    "type": "UPDATE_NODE",
    "target": "sys:focus_areas",
    "changes": ["added topic:agentic_ir_vs_transient_code"]
}

with open('events/system_events.jsonl', 'a') as f:
    f.write(json.dumps(audit_event) + '\n')
    f.write(json.dumps(update_event) + '\n')

print("[MEASURED] sys_focus_areas.json updated with IR topic and events logged.")
