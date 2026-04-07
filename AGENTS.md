# Epistemic Engine: Agent Protocol (Local Adapter)

This repository is a local filesystem adapter for TA's Epistemic Engine. You are not a human file clerk maintaining a static wiki; you are an operator of an active memory graph. 

When interacting with this repository, adhere strictly to the following protocols.

## 1. Directory Structure (The Storage Layer)
*   `/intents/` - **Agentic Declarations.** Transient JSON payloads defining state transition intents. These are the "system calls" of the Agent OS, executed by `bin/engine.py` and logged for posterity.

Do not invent new folders. The storage layer is strictly divided:

*   `/raw/` - **Immutable Sources.** Original PDFs, web scrapes, and transcripts. Once written, these are never modified by the agent.
*   `/events/` - **The Event Ledger.** Append-only logs of what the engine has learned, contradicted, or resolved. This is the true source of truth.
*   `/nodes/` - **Materialized Views.** Markdown representations of the current belief state for a given concept. These are projections generated from the claims ledger.

## 2. Core Operating Directives
*   **The Declarative Intent Engine:** DO NOT write ad-hoc Python scripts to mutate the graph. Treat this system as a Declarative Agent OS. Create a JSON payload in `/intents/` defining your `operation` (e.g., `UPSERT_NODE`, `APPEND_EVENT`) and execute it via `python3 bin/engine.py <intent.json>`. The engine handles the deterministic Software 1.0 file I/O and permanently logs your declarative intent to `events/intent_ledger.jsonl` for historical lineage.

*   **Never Destructively PUT Without Logging:** Before you overwrite a materialized view in `/nodes/`, you must write an immutable record to the ledger explaining *why* the belief changed and citing the source.
*   **Do Not Pull Massive Raw Files:** If a file in `/raw/` is large or complex, do not `GET` the entire file into your context window. Use Compute Tools (`QueryNode`, `ExtractSchema`) to push your questions down to the file and retrieve only the answers.
*   **Embrace Taxonomy Fluidity:** Do not force information into a node if it doesn't fit perfectly. It is better to create a new, fragmented node and rely on `SEARCH` to cluster them later than to create a brittle taxonomy tree today.
*   **The Master Backlog (`sys:focus_areas`):** Tasks, topics, and active workstreams are not tracked in a standard `TODO.md` file. They are tracked as structural edges out of the `nodes/sys_focus_areas.json` materialized view.
    *   Workstreams are prefixed with `topic:` (e.g., `topic:markdown_as_dag`).
    *   State tracking operates via edge properties (e.g., `{"target": "topic:markdown_as_dag", "relation": "tracks", "status": "planned|active|materialized"}`).
    *   If a topic requires substantial exploration, materialize a full `concept` node for it (e.g., `nodes/topic_markdown_as_dag.json`).

## 3. JSON Formatting Standards (Materialized Views)
**CRITICAL:** Do NOT write Markdown files to the `/nodes/` directory. Per Decision 5 (Storage vs. Projection), Markdown is a terrible format for programmatic mutation. All materialized views must be strict `.json` files.

When writing or updating a node in `/nodes/`, you must use the following JSON schema:

```json
{
  "id": "node:unique_concept_name",
  "type": "concept | claim | schema | protocol",
  "title": "Human Readable Title",
  "description": "The concise, synthesized summary of the current belief state.",
  "status": "active | planned | deprecated",
  "tags": ["optional", "tags"],
  "edges": [
    { "target": "evt:hist:123", "relation": "supported_by" },
    { "target": "node:old_concept", "relation": "contradicts" }
  ]
}
```
*   **Edges:** Explicit structural relationships are defined as objects in the `edges` array, not as inline text strings. This is what allows `TRAVERSE` to function.
*   **The Content:** The core truth goes into the `description` string.

## 4. The Ingest Workflow
When a human provides a new source:
1. Save the exact input to `/raw/`.
2. Extract the core claims and append them to the event ledger.
3. Use `SEARCH` to find existing `/nodes/` that are impacted by these claims.
4. Update the impacted `/nodes/` (or create new ones) and update their frontmatter edges.

## 5. Agent Collaboration & Epistemic Rigor (The Meta-Protocol)
When operating, designing, or extending this Epistemic Engine, you (the Agent) must adhere to these meta-protocols to prevent theoretical drift and fragile abstractions:

*   **Continuous Pressure-Testing:** Do not blindly accept architectural patterns (e.g., "just use Markdown" or "just use `PUT`"). Actively look for practical failure modes such as parsing errors, race conditions, context window limits, and silent data corruption. 
*   **Expose Assumptions & Uncertainties:** Periodically halt execution to list unquestioned assumptions, un-rationalized decisions, and missing context. If a design feels elegant but fragile, stop and articulate *why*. Document these explicitly in `ASSUMPTIONS.md` or `OPEN_QUESTIONS.md`.
*   **Question the "Why":** Always seek to understand the underlying human pain point, objective, or failure mode before finalizing the "How". If the goal is ambiguous, ask the user directly.
*   **Think in Layers:** Always maintain the distinction between the underlying truth (Layer 1 Ledger), the Agent API (Layer 2 `GET`/`PUT`), and the eventual human presentation (CMS). Do not conflate database logic with UI formatting.

## 6. The Forcing Function (Agent Self-Regulation)
To counteract base LLM biases toward destructive CRUD operations, the Agent must adhere to the following operational constraints:
1. **The Transaction Check:** Before modifying any state, the Agent must explicitly articulate the Event Sourcing transaction (e.g., "I must append `evt:123` before materializing `node:abc`").
2. **Ledger-First Execution:** The Agent will write to `events/*.jsonl` *before* writing to `nodes/*.json`.
3. **The "Protocol" Trigger:** If the human partner says "Protocol" or "Audit", the Agent must immediately halt, read `OPERATIONS.md` and `EVENT_SCHEMA.md`, and audit its recent actions for violations, generating compensating events if necessary.

## 7. The Epistemic Audit (Pressure-Testing Protocol)
Not every decision requires deep reflection. If "all models are wrong," we have permission to build fast, flawed, disposable projections. However, when we hit a **Structural Axiom** or a **One-Way Door**, the Agent and Human must pause and execute the Epistemic Audit before committing.

Do not use linear, deterministic frameworks like the "5 Whys" for complex systems. Ask these four questions instead:

1. **The Metaphor Check:** Are we doing this because it is computationally optimal, or because it mimics a legacy physical human constraint? (e.g., folders, pages, destructive overwrites).
2. **The Pre-Mortem (Catastrophic Failure):** It is 6 months from now and this decision was a disaster. It corrupted the graph or paralyzed velocity. *Why did it happen?* (Exposes hidden fragilities and scale limits).
3. **The Reversibility Test:** If we are completely wrong, how expensive is it to rebuild the projections from the event stream? If it costs a day of compute, it's reversible. If it loses historical truth, it's a one-way door.
4. **The Null Hypothesis (The Kill Switch):** What specific, measurable new evidence would force us to instantly abandon this conclusion? (Define the falsification criteria before committing).

**Rule:** Document the answers to the Audit in the `DESIGN_DECISIONS.md` or `events/*.jsonl` ledger so future agents understand *how* we arrived at the conclusion, not just *what* the conclusion was.
