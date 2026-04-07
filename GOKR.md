# GOKR: TA's Memory Engine MVP

## Goal
Establish a persistent, environment-agnostic memory engine for TA (the seed actor) that compounds knowledge over time without relying on a rigid filesystem structure.

## Objectives
1.  **Define the Universal Interface**: Create the abstraction layer (the schema/protocol) that allows TA to read, write, and link knowledge nodes regardless of whether the backend is a local filesystem (Bun/Node), D1 (Cloudflare), or IndexedDB (Browser).
2.  **Implement the Local File Adapter**: Build the first concrete implementation using the local filesystem (`~/knowledge` or similar directory) so we can immediately start using and testing the engine with existing tools.
3.  **Establish the Ingest Workflow**: Create the mechanism for TA to take raw input (like the Karpathy gist), extract entities/concepts, and write them into the memory graph.

## Key Results (Fitness Function)
*   **KR1 (Agnosticism):** The core agent logic for reading/writing memory must contain zero `fs`, `path`, or shell command references. It must only use the defined interface methods (e.g., `GetNode`, `PutNode`, `Search`).
*   **KR2 (Persistence):** After ingesting a new piece of information in Session A, TA must be able to successfully retrieve and synthesize that exact information in a completely isolated Session B.
*   **KR3 (Traceability):** Every node created or modified must automatically include provenance metadata (source ID, timestamp) linking it back to the raw input that generated it.
