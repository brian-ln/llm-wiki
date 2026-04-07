import json
import datetime
import uuid

def make_claim_event(claim, source="agent_research:skillsmith_inspection"):
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
    make_claim_event("[MEASURED] Skills use 'Progressive Disclosure' (Context Enrichment). The SKILL.md file acts as a routing table. It does not contain all the code; instead, it contains trigger conditions (if X, then load file Y). This explicitly manages the LLM's context window (RAM), preventing overflow by only paging in the specific documentation or scripts needed for the current branch of execution."),
    make_claim_event("[MEASURED] Skills utilize 'Context Isolation' (Forking). Research skills use `context: fork` and `agent: Explore` in their frontmatter. This tells the Agent OS to spin up a child process (a sub-agent) with a fresh, empty context window to perform a deep search without polluting the main thread's memory."),
    make_claim_event("[MEASURED] Skills use the 'No-Args Card' pattern (Ambient Vocabulary). If a skill is invoked with no arguments, it returns a hardcoded 20-line reference card instead of executing logic. This allows the skill's name (e.g., `/gokr`) to function simultaneously as an executable command (SW 1.0) and as semantic vocabulary injected into the LLM's context (SW 2.0)."),
    make_claim_event("[MEASURED] Skills employ 'Model Invocation Disabling' (`disable-model-invocation: true`). For purely deterministic tasks (e.g., triggering a bash build script), the OS reads the YAML and executes the binary/script directly, explicitly bypassing the LLM to guarantee 100% deterministic execution and save compute.")
]

with open("events/paradigm_events.jsonl", "a") as f:
    for evt in events:
        f.write(json.dumps(evt) + "\n")

node = {
  "id": "node:concept_skill_architecture_techniques",
  "type": "concept",
  "title": "Architectural Techniques of Agent Skills",
  "description": "[MEASURED] Structurally, skills in the ~/.claude/skills/ ecosystem employ several advanced techniques to bridge Software 1.0 and 2.0. 1. **Progressive Disclosure**: Skills act as routing tables, dynamically 'paging' files into the LLM's Context Window (RAM) only when triggered, rather than dumping everything at once. 2. **Context Isolation**: Using `context: fork`, skills spawn sub-agents (child processes) with fresh memory to prevent polluting the main thread. 3. **Execution Bypassing**: Using `disable-model-invocation: true`, a skill can force the Agent OS to execute a deterministic script directly, bypassing the probabilistic LLM entirely. 4. **Ambient Vocabulary**: Using the 'No-Args Card' pattern, a skill can inject a static definition of itself into the context window, allowing its name to act as both a runnable command and a semantic concept.",
  "status": "active",
  "tags": ["skills", "architecture", "software1.0", "software2.0", "context_management", "routing"],
  "edges": [
      {"target": events[0]["id"], "relation": "supported_by"},
      {"target": events[1]["id"], "relation": "supported_by"},
      {"target": events[2]["id"], "relation": "supported_by"},
      {"target": events[3]["id"], "relation": "supported_by"},
      {"target": "node:concept_hybrid_markdown_programs", "relation": "implements"}
  ]
}

with open("nodes/node_concept_skill_architecture_techniques.json", "w") as f:
    json.dump(node, f, indent=2)

print("Skill architectural techniques synthesized and logged.")
