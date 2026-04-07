import json
import uuid
import datetime
from pathlib import Path

# Setup paths
EVENTS_DIR = Path("events")
EVENTS_DIR.mkdir(exist_ok=True)


def create_event(evt_type, title, details):
    evt_id = f"evt:sys:{uuid.uuid4().hex[:8]}"
    evt = {
        "id": evt_id,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "type": evt_type,
        "title": title,
        "details": details,
    }
    with open(EVENTS_DIR / "system_events.jsonl", "a") as f:
        f.write(json.dumps(evt) + "\n")
    return evt_id


# 1. Log discovery event
create_event(
    "SYSTEM_DISCOVERY",
    "Locate Opencode Logs",
    "Found active session SQLite database and append-only JSONL logs in ~/.local/share/opencode/ and ~/.local/state/opencode/. Confirmed local execution trace is durable.",
)

print("System events recorded successfully.")
