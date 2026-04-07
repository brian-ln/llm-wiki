# Open Questions & System Vulnerabilities

As of 2026-04-07, the following architectural and philosophical questions remain unresolved:

## 1. The "Why" and the Consumer
*   **The Trigger:** What specific failure mode or pain point in the current workflow (with `/know`, Dolt, etc.) triggered this exact redesign today?
*   **The Consumer:** Is this graph meant to be read by *humans* (requiring human-readable summaries), or is this strictly a machine-to-machine database where human readability is irrelevant?

## 2. The Data Format (Markdown vs. JSON/Triples)
*   **The Flaw:** If we are stripping away Obsidian and treating this as an API for an LLM (`GET` / `PUT`), **Markdown is a terrible format for programmatic mutation.** Asking an agent to rewrite a 2,000-word Markdown string in a `PUT` operation invites hallucinated deletions and formatting errors.
*   **The Question:** If there is no human UI, why aren't the nodes just JSON or a pure Graph Triplestore (Subject -> Predicate -> Object)? Have we rationalized why we are still clinging to "documents"?

## 3. Concurrency and Multi-Agent Writes
*   **The Flaw:** If Agent A and Agent B (e.g., via `/council`) both `GET("node:auth")`, compute different updates, and both call `PUT("node:auth", ...)`, whoever writes last destroys the other's work. 
*   **The Question:** How does the protocol handle conflicts? Does the `PUT` primitive require a version hash (Optimistic Concurrency Control), or does the system rely entirely on the underlying Event Log to merge them (CRDTs)?

## 4. The Boundary of "TA"
*   **The Flaw:** We named this "TA's Memory Engine". Is TA a singleton? Does TA *own* this graph, meaning other agents (like a generic `/ai` coding agent) have to ask TA to read/write from it? Or is this graph a shared global state that every agent mounts directly?
*   **The Question:** If it's shared, how do we track which agent asserted which fact? (Provenance needs an `agent_id`, not just a `source_id`).
