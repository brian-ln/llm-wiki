# Event Ledger: Schema & Vocabulary

This document defines the formal schema for Layer 1 of the Epistemic Engine: The Immutable Ledger (`events/*.jsonl`). 

Every entry in the ledger must conform to the Base Event shape, utilizing one of the approved `action` verbs in its payload.

## 1. Base Event Structure
Every line in a `.jsonl` event file is a valid JSON object with the following envelope:

```json
{
  "id": "evt:unique_hash_or_sequence",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ",
  "actor": "string (e.g., 'human', 'algo', 'human_algo_council')",
  "action": "ACTION_VERB",
  "payload": { ... }
}
```

## 2. Core Action Verbs (The Vocabulary)

### Data / Entity Operations
*   **`ASSERT_NODE`**: Declares the existence of a new entity or concept.
    *   *Payload:* `{"node_id": "...", "type": "...", "title": "..."}`
*   **`UPDATE_NODE`**: Records a mutation to a node's state. 
    *   *Payload:* `{"node_id": "...", "change": "description", "patch": {...}}`
*   **`ASSERT_EDGE`**: Defines a topological relationship between two nodes.
    *   *Payload:* `{"source": "node_A", "target": "node_B", "relation": "depends_on|contradicts|supports"}`

### Epistemic / Knowledge Operations
*   **`INGEST_RAW`**: Records the introduction of an external, immutable source document into the system.
    *   *Payload:* `{"source_uri": "...", "local_path": "...", "title": "..."}`
*   **`ASSERT_CLAIM`**: Records a factual, philosophical, or logical statement made by an actor. This is the atomic unit of belief.
    *   *Payload:* `{"claim": "...", "source": "evt_id | raw_id | null"}`

### Domain-Specific Extensions (e.g., System Building)
*   **`ASSERT_CAPABILITY`**: A specialized `ASSERT_NODE` used for tracking the engine's own development backlog.
    *   *Payload:* `{"node_id": "sys:cap:...", "title": "...", "description": "...", "status": "planned|active|done"}`

## 3. Extensibility
This schema is not frozen. As Human and Algorithmic intelligence evolve new use cases (e.g., tracking confidence intervals, deprecating claims), new `ACTION_VERB`s can be introduced. However, they must be documented here before use to ensure the `Materializer` can parse them.
