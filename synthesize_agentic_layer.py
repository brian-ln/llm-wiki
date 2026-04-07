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
    make_claim_event("[AGENT-RESEARCH] In classical computing, a 'prompt' is a hybrid of `stdin` (input data) and a compiler directive. Because Software 2.0 processors (LLMs) blur the line between code and data, the prompt acts as the initial execution environment that conditions the processor's state before generation begins."),
    make_claim_event("[AGENT-RESEARCH] Storing 'prompts' transforms ephemeral, stochastic queries into persistent, versionable assets. This is directly analogous to 'Stored Procedures' in SQL databases or functions in a standard library. It gives us behavioral reproducibility and composable abstractions."),
    make_claim_event("[AGENT-RESEARCH] If the neural network is the CPU, an 'Agent' is the Operating System (OS). It is a deterministic `while(true)` event loop that handles I/O, memory management (context window), and scheduling."),
    make_claim_event("[AGENT-RESEARCH] 'Skills' or 'Commands' are the system calls (syscalls) or the standard library (`stdlib`) of the Agent OS. They are deterministic Software 1.0 functions exposed to the probabilistic Software 2.0 processor to execute side-effects (e.g., read a file, fetch a URL).")
]

with open("events/paradigm_events.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

# Create nodes
nodes = [
    {
      "id": "node:concept_prompt",
      "type": "concept",
      "title": "Prompts as Execution Context",
      "description": "[AGENT-RESEARCH] Under the Software 2.0 paradigm, a 'prompt' is not code in the Software 1.0 sense (explicit instructions). It is the initial execution state (akin to `stdin` mixed with environment variables) that conditions the neural processor. It is a declarative request evaluated by a probabilistic engine.",
      "status": "active",
      "tags": ["software2.0", "prompt", "computing_analogy"],
      "edges": [{"target": events[0]["id"], "relation": "supported_by"}]
    },
    {
      "id": "node:concept_stored_prompt",
      "type": "concept",
      "title": "Stored Prompts as Behavioral Assets",
      "description": "[AGENT-RESEARCH] 'Storing' a prompt elevates it from a transient query to a version-controlled function signature. Much like a Stored Procedure in a database, it allows engineers to build composable libraries of probabilistic behaviors, enabling modularity in Software 2.0 development.",
      "status": "active",
      "tags": ["software2.0", "prompt", "storage", "asset"],
      "edges": [{"target": events[1]["id"], "relation": "supported_by"}]
    },
    {
      "id": "node:concept_agent_os",
      "type": "concept",
      "title": "Agents as Operating Systems",
      "description": "[AGENT-RESEARCH] If an LLM is a Software 2.0 processor, an 'Agent' is the Operating System. It provides the deterministic event loop that manages the processor's memory (context window) and I/O. 'Skills' and 'Commands' form the Standard Library (or syscall interface), allowing the probabilistic CPU to execute deterministic side-effects in the outside world.",
      "status": "active",
      "tags": ["software2.0", "agent", "os", "skills", "commands"],
      "edges": [
          {"target": events[2]["id"], "relation": "supported_by"},
          {"target": events[3]["id"], "relation": "supported_by"}
      ]
    }
]

for node in nodes:
    filename = f"nodes/{node['id'].replace(':', '_')}.json"
    with open(filename, "w") as f:
        json.dump(node, f, indent=2)

print("Agentic layer synthesis complete. Ledger appended and 3 nodes materialized.")
