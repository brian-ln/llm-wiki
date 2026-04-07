# TA Memory Engine: Operations (v2)

This defines the operations that make up the memory engine, separated into Storage Primitives and Compute Tools. It reflects a shift away from forcing the LLM to act as a "human file clerk" towards a true Epistemic Engine.

## 1. Storage Primitives (The Data Layer)
These are the atomic I/O functions. The agent uses these to interact with the backend (Filesystem, D1, IndexedDB). They are intentionally dumb and environment-agnostic.

*   **`GET(id)`**: Retrieves the materialized state (content, metadata, edges) of a specific node or claim.
*   **`PUT(id, state, edges)`**: Creates a new node or overwrites an existing one. *(Note: See `ASSUMPTIONS.md` regarding the vulnerability of destructive PUTs. This is primarily a caching/materialized view mechanism.)*
*   **`LOG(action, payload)`** / **`APPEND(claim)`**: Writes an immutable record to the chronological ledger. This is the true source of truth for the Epistemic Engine (Event Sourcing).
*   **`TRAVERSE(id, direction)`**: Graph query. "Give me everything that explicitly links to/from X."
*   **`SEARCH(query, limit)`**: Performs semantic or keyword search across the graph. Returns a list of relevant Node IDs. This is implemented deterministically by the storage adapter, *not* manually maintained by the LLM.

## 2. Compute Tools (The Execution Layer)
When data is massive, secure, or requires targeted synthesis, the LLM pushes compute *to the data* using these tools, rather than pulling all data into its context window.

*   **`QueryNode(node_id, question)`**: Instead of downloading the file via `GET`, the agent asks a question *about* the file. The backend environment executes the query (via a local model or RAG) and returns only the answer.
*   **`ExtractSchema(node_id, json_schema)`**: "Read this node and return only the specific structured entities I need."
*   **`MapReduce(node_id, instruction)`**: "Apply this instruction across the entire massive document and give me the rolled-up result."

## 3. Cognitive Operations (Agent Workflows)
These are the high-level thought-loops TA executes. They sequence the primitives and tools above to achieve epistemic goals.

*   **`Assimilate` (Ingest & Integrate)**
    *   **Meaning**: The act of taking raw, external information and weaving it into the existing graph. It is not just saving a file; it is updating beliefs.
    *   **Sequence**: `SEARCH` (what do I already know?) -> `GET` / `QueryNode` (read current beliefs) -> LLM Compute (find deltas/new info) -> `PUT` / `APPEND` (write updated beliefs) -> `LOG` (record the assimilation).

*   **`Recall` (Contextualize)**
    *   **Meaning**: The act of pulling a localized subgraph into the working context window before answering a prompt or making a decision.
    *   **Sequence**: `SEARCH` (find entry points) -> `GET` (fetch the core nodes) -> `TRAVERSE` (traverse to neighbors if necessary) -> Assemble context for the LLM.

*   **`Resolve` (Converge & Lint)**
    *   **Meaning**: The background maintenance process of finding contradictory claims, stale information, or duplicated concepts and merging them into a single coherent truth.
    *   **Sequence**: `SEARCH` (find overlaps/conflicts) -> `GET` (read the conflicting nodes) -> LLM Compute (deliberate and synthesize) -> `PUT` / `APPEND` (write the merged truth) -> `LOG` (record the resolution).
