# TA Memory Engine: Operations (v3 - Event Sourced)

This engine is built on Event Sourcing. The fundamental truth of the system is the chronological log of events and claims. "Nodes" (markdown files) are merely disposable, materialized views of that log.

## 1. The Primary Write Primitive
*   **`APPEND_LOG(event_type, payload, provenance)`**: The *only* way to mutate the state of the engine. You do not overwrite facts; you append new observations, claims, or deprecations.

## 2. The Primary Read Primitives
*   **`QUERY_LOG(filters)`**: Reads the stream of events. Used to understand *how* a belief evolved or to process raw buffered observations.
*   **`GET_VIEW(node_id)`**: (Formerly `GET`). Retrieves the *current computed state* of a concept. This is a fast-path read of the materialized markdown file.
*   **`SEARCH(query)`**: Probabilistic entry point. Finds relevant views or log entries based on semantic meaning.
*   **`TRAVERSE(node_id, direction)`**: Deterministic entry point. Follows explicit structural edges between computed views.

## 3. Background System Operations (The Engine loop)
These are not called by the reasoning agent directly; they are triggered by the system.
*   **`MATERIALIZE_VIEW(node_id)`**: (Formerly `PUT`). When the log receives new claims about an entity, the system (or a background agent) reads the log, synthesizes the new truth, and overwrites the markdown file in `/nodes/`. It is a destructive overwrite, but it is safe because the `LOG` retains the immutable history.

## 4. Compute Tools (Edge Execution)
*   **`QueryNode(node_id, question)`**: Push compute to large/secure materialized views.
*   **`ExtractSchema(raw_source_id, schema)`**: Push compute to raw ingested files to extract claims for the `LOG`.
