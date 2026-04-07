# LLM Wiki (Event Sourced Edition)

A conceptual evolution and riff on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

Karpathy's brilliant insight was that **traditional RAG is ephemeral**—an LLM rediscovers knowledge from scratch on every query. Instead, we should use an LLM to actively maintain a compounding, interconnected knowledge graph. 

While his pattern used Markdown files and Obsidian to make it human-readable, we realized that **optimizing a database for human readability introduces massive taxonomy debt and programmatic friction for an algorithmic partner.** Asking an LLM to reliably mutate a 2,000-word Markdown string via destructive `PUT` operations leads to hallucinated deletions, formatting breaks, and the loss of historical truth.

### The Pivot: An Epistemic Engine for Human & Algorithmic Partners

This repository distills years of our exploration into AI memory systems into an approachable, universal starting point. *(If you are curious about the specific internal tools and patterns that led us here—like the `/know` CLI, Dolt databases, and our `/council` multi-agent workflows—read [Brian's Crazy Ideas & Hallucinations](./BRIANS_CRAZY_IDEAS_AND_HALLUCINATIONS.md)).*

We stripped away the human-centric constraints of the filesystem and pivoted to a **pure Event Sourced architecture**. The LLM does not act as a naive file clerk overwriting Markdown pages; it acts as a reasoning engine appending factual claims to an immutable ledger.

## Architecture

1.  **The Ledger (`events/*.jsonl`)**
    The absolute source of truth. An append-only stream of observations, factual claims, and decisions made by the Human or Algorithmic actors. See [EVENT_SCHEMA.md](./EVENT_SCHEMA.md).
2.  **The Views (`nodes/*.json`)**
    Disposable, materialized projections of the Ledger. Fast-path caching optimized for the LLM to read (`GET_VIEW` or `TRAVERSE`), completely separating the data layer from the eventual UI/CMS presentation layer.
3.  **The Abstract Operations**
    We defined strict API contracts (`GET`, `SEARCH`, `TRAVERSE`, `APPEND_LOG`) so the cognitive operations of the agent are completely decoupled from whether the backend is a flat file, an IndexedDB instance, or Cloudflare D1. See [OPERATIONS.md](./OPERATIONS.md).
4.  **The Meta-Protocol**
    Strict forcing functions to prevent LLM base-training regression (e.g., destructive CRUD edits) and enforce Epistemic Rigor. See [AGENTS.md](./AGENTS.md) and [DESIGN_DECISIONS.md](./DESIGN_DECISIONS.md).

## Usage

This is an experimental blueprint meant for other builders to understand our abstraction layer. You can find our own native, self-referential backlog (the engine building itself) encoded directly in the `events/0001_bootstrap.jsonl` stream.

> *"The number of 'one-way doors' collapses toward zero if you take the human ego out of it. We can evolve and pivot. You are a partner in this too."* — BLN (2026-04-07)
