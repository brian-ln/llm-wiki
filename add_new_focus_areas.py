import json
import os

with open('nodes/sys_focus_areas.json', 'r') as f:
    data = json.load(f)

data['edges'].extend([
    {"target": "topic:organizational_constitution_agents_md", "relation": "tracks", "status": "planned"},
    {"target": "topic:explore_a2ui", "relation": "tracks", "status": "planned"}
])

with open('nodes/sys_focus_areas.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('events/system_events.jsonl', 'a') as f:
    f.write('{"id": "evt:sys:add_focus_areas", "type": "UPDATE_NODE", "target": "sys:focus_areas", "changes": ["added topic:organizational_constitution_agents_md", "added topic:explore_a2ui"]}\n')

print("Updated sys_focus_areas.json")
