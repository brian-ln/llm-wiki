import json
from pathlib import Path

NODES_DIR = Path("nodes")
focus_file = NODES_DIR / "sys_focus_areas.json"

if focus_file.exists():
    with open(focus_file, "r") as f:
        data = json.load(f)

    # Add the UI/IDE to the deferred/planned list if we have a way to represent it,
    # or just append to description.
    data["description"] += (
        "\n[DEFERRED]: UI/UX implementation and visual schema design for Agentic Streams and Skill Governance (The 'Agentic Stream IDE'). Parked for later."
    )

    with open(focus_file, "w") as f:
        json.dump(data, f, indent=2)
    print("Updated sys_focus_areas.json to park UI design.")
else:
    print("sys_focus_areas.json not found.")
