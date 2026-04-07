# TA Memory Engine: Operations

This defines the exact operations that make up the memory engine. They are split into two layers: the low-level storage primitives (the interface) and the high-level cognitive operations (the agent workflows).

## 1. Storage Primitives (The Interface)
These are the atomic I/O functions. The agent uses these to interact with the backend (Filesystem, D1, IndexedDB).

*   **`Search(query, limit)`**: Performs semantic or keyword search across the graph. Returns a list of relevant Node IDs and confidence scores.
*   **`GetNode(id)`**: Retrieves the current state (content, metadata, edges) of a specific node.
*   **`PutNode(id, content, edges)`**: Creates a new node or overwrites an existing one. Replaces the old state with the new synthesized truth.
*   **`AppendEvent(action, payload)`**: Writes an immutable record to the chronological ledger (e.g., "Assimilated Source X", "Merged Node Y and Z").

## 2. Cognitive Operations (Agent Workflows)
These are the actual thought-loops TA executes. They sequence the primitives above to achieve epistemic goals.

*   **`Assimilate` (Ingest & Integrate)**
    *   **Meaning**: The act of taking raw, external information and weaving it into the existing graph. It is not just saving a file; it is updating beliefs.
    *   **Sequence**: `Search` (what do I already know?) -> `GetNode` (read current beliefs) -> LLM Compute (find deltas/new info) -> `PutNode` (write updated beliefs) -> `AppendEvent` (log the assimilation).

*   **`Recall` (Contextualize)**
    *   **Meaning**: The act of pulling a localized subgraph into the working context window before answering a prompt or making a decision.
    *   **Sequence**: `Search` (find entry points) -> `GetNode` (fetch the core nodes) -> `GetEdges` (traverse to neighbors if necessary) -> Assemble context for the LLM.

*   **`Resolve` (Converge & Lint)**
    *   **Meaning**: The background maintenance process of finding contradictory claims, stale information, or duplicated concepts and merging them into a single coherent truth.
    *   **Sequence**: `Search` (find overlaps/conflicts) -> `GetNode` (read the conflicting nodes) -> LLM Compute (deliberate and synthesize) -> `PutNode` (write the merged truth) -> `AppendEvent` (log the resolution).
