# TA Memory Engine: Operations Protocol Stack

This document defines the protocol and contracts for the memory engine, modeled as layers of abstraction. Agents interact with the high-level API, while the system guarantees the low-level integrity.

## Layer 1: The Ledger / Truth Layer (Low-Level)
This is the immutable history of the system. Agents rarely interact with this directly.
*   **`APPEND_LOG(event)`**: The fundamental write. Records a state change, observation, or provenance.
*   **`READ_STREAM(query)`**: The fundamental read. Replays history to understand how a belief formed.

## Layer 2: The Agent API (The Interface)
These are the ergonomic primitives the LLM uses to think and act. They abstract away the complexity of the ledger.

*   **`GET(node_id)`**: Fetch the *current materialized state* of a concept.
    *   *Contract:* Returns the most recent synthesis. Fast, $O(1)$ read.
*   **`PUT(node_id, state, edges)`**: Overwrite the current materialized state.
    *   *Contract:* To the agent, this is a simple, destructive update to the working memory. Under the hood, the system *automatically* translates this into an `APPEND_LOG` event (recording the diff and provenance) before updating the view. The agent does not need to call `LOG` manually when using `PUT`.
*   **`TRAVERSE(node_id, direction, edge_type)`**: Navigate explicit topological relationships.
    *   *Contract:* Relies on the explicit `edges` defined in previous `PUT` calls.
*   **`SEARCH(query)`**: Probabilistic entry point based on semantic/lexical similarity.

## Layer 3: Cognitive Operations (Workflows)
How the agent sequences the Layer 2 API to perform epistemic work.
*   **`Assimilate`**: `SEARCH` -> `GET` -> compute delta -> `PUT`.
*   **`Recall`**: `SEARCH` -> `GET` -> `TRAVERSE` -> assemble context.
*   **`Resolve`**: `SEARCH` (find conflicts) -> `GET` -> compute synthesis -> `PUT`.

## Layer 4: Compute Tools (Edge Execution)
Used when Layer 2 `GET` is inappropriate due to data size or security.
*   **`QueryNode(node_id, prompt)`**: Push compute to the data. Returns answers, not raw files.

## 4. Resilient Fetching Protocol
If the standard `webfetch` tool fails due to anti-bot protections (e.g., HTTP 403 Forbidden on Medium or other strict sites):
*   Do not immediately give up.
*   Fallback to using `curl` combined with reader APIs (e.g., `https://r.jina.ai/<URL>`).
*   Alternatively, write a short Python script using `urllib` with a standard browser `User-Agent` header.
*   If all automated methods fail, explicitly ask the human partner to provide the text.

## 5. Strict Raw Immutability & Provenance
*   **No Frontmatter:** NEVER add YAML frontmatter, headers, or metadata directly to files in the `/raw/` directory. They must remain byte-for-byte identical to the original scraped source.
*   **Ledger-Based Provenance:** The origin of a raw file is tracked *exclusively* via an `INGEST_RAW` event in the ledger (`events/*.jsonl`). 
*   **The Index:** The materialized view `nodes/sys_raw_index.json` serves as the dynamic catalog linking local raw files to their original URIs and ingest timestamps.

## 6. Epistemic Rigor Tagging
When making analogical leaps or mapping formal academic concepts to industry metaphors (e.g., mapping DDPM math to a "Software 2.0 ISA"), the Agent must:
1.  Tag the claim and node descriptions with `[HYPOTHESIS]` and `[AGENT-RESEARCH]`.
2.  Conduct an `EPISTEMIC_AUDIT` event in the ledger, explicitly stating the rationalization and defining the Null Hypothesis (the criteria that would prove the analogy false).
