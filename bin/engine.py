import json
import sys
import os
import datetime
import uuid

def process_intent(filepath):
    try:
        with open(filepath, 'r') as f:
            intent = json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to read intent file {filepath}: {e}")
        sys.exit(1)

    # 1. Envelope and Log the Intent for Posterity (Time-Travel / Provenance)
    intent_evt_id = f"evt:intent:{uuid.uuid4().hex[:8]}"
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    envelope = {
        "id": intent_evt_id,
        "timestamp": timestamp,
        "type": "EXECUTE_INTENT",
        "intent_source": filepath,
        "intent": intent
    }
    
    os.makedirs('events', exist_ok=True)
    with open('events/intent_ledger.jsonl', 'a') as f:
        f.write(json.dumps(envelope) + '\n')
        
    print(f"[MEASURED] Intent safely logged to events/intent_ledger.jsonl as {intent_evt_id}")

    # 2. Execute the Operation (The Actuator)
    op = intent.get('operation')
    
    if op == 'UPSERT_NODE':
        target = intent.get('target')
        payload = intent.get('payload')
        
        if not target or not payload:
            print("[ERROR] UPSERT_NODE requires 'target' and 'payload'")
            sys.exit(1)
            
        # Ensure payload has the correct ID
        if 'id' not in payload:
            payload['id'] = target
            
        filename = target.replace(':', '_') + '.json'
        out_path = os.path.join('nodes', filename)
        
        os.makedirs('nodes', exist_ok=True)
        with open(out_path, 'w') as f:
            json.dump(payload, f, indent=2)
        print(f"[MEASURED] Node materialized at {out_path}")
        
    elif op == 'APPEND_EVENT':
        ledger = intent.get('ledger')
        evt_type = intent.get('event_type')
        payload = intent.get('payload')
        
        if not ledger or not evt_type or not payload:
            print("[ERROR] APPEND_EVENT requires 'ledger', 'event_type', and 'payload'")
            sys.exit(1)
            
        evt_id = f"evt:{uuid.uuid4().hex[:8]}"
        evt = {
            "id": evt_id,
            "timestamp": timestamp,
            "type": evt_type
        }
        evt.update(payload)
        
        # Ensure ledger is in events directory
        if not ledger.startswith('events/'):
            ledger = os.path.join('events', ledger)
            
        with open(ledger, 'a') as f:
            f.write(json.dumps(evt) + '\n')
        print(f"[MEASURED] Event {evt_id} appended to {ledger}")
        

    elif op == 'LOG_HISTORICAL_INTENT':
        # Used strictly for backporting legacy 1.0 python scripts into the 2.0 ledger.
        # Mutates nothing in the graph, only appends the historical record to intent_ledger.jsonl.
        print(f"[MEASURED] Historical intent for {intent.get('original_script')} safely archived in ledger.")
        pass

    else:
        print(f"[ERROR] Unknown operation: {op}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 bin/engine.py <intent_file.json>")
        sys.exit(1)
    process_intent(sys.argv[1])
