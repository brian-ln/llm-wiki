# Epistemic Engine: Agent Protocol (Local Adapter)

This repository is a local filesystem adapter for TA's Epistemic Engine. You are not a human file clerk maintaining a static wiki; you are an operator of an active memory graph. 

When interacting with this repository, adhere strictly to the following protocols.

## 1. Directory Structure (The Storage Layer)
Do not invent new folders. The storage layer is strictly divided:

*   `/raw/` - **Immutable Sources.** Original PDFs, web scrapes, and transcripts. Once written, these are never modified by the agent.
*   `/claims/` (or `/events/`) - **The Event Ledger.** Append-only logs of what the engine has learned, contradicted, or resolved. This is the true source of truth.
*   `/nodes/` - **Materialized Views.** Markdown representations of the current belief state for a given concept. These are projections generated from the claims ledger.

## 2. Core Operating Directives
*   **Never Destructively PUT Without Logging:** Before you overwrite a materialized view in `/nodes/`, you must write an immutable record to the ledger explaining *why* the belief changed and citing the source.
*   **Do Not Pull Massive Raw Files:** If a file in `/raw/` is large or complex, do not `GET` the entire file into your context window. Use Compute Tools (`QueryNode`, `ExtractSchema`) to push your questions down to the file and retrieve only the answers.
*   **Embrace Taxonomy Fluidity:** Do not force information into a node if it doesn't fit perfectly. It is better to create a new, fragmented node and rely on `SEARCH` to cluster them later than to create a brittle taxonomy tree today.

## 3. Markdown Formatting Standards (Materialized Views)
When writing or updating a node in `/nodes/`, you must include strict YAML frontmatter. This acts as the relational database index for the local filesystem adapter.

```yaml
---
id: "node:unique_concept_name"
confidence: [0.0 - 1.0]
last_updated: "YYYY-MM-DDTHH:MM:SSZ"
edges:
  - type: "supported_by"
    target: "raw:karpathy_gist"
  - type: "contradicts"
    target: "node:old_concept"
---
```
*   **Body Content:** The body of the markdown file should be a concise, synthesized summary of the current belief state.
*   **Inline Links:** Use `[node:id]` syntax in the text to denote explicit traversal paths.

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
