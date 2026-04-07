# Narrative: The Road to an Epistemic Engine

## Session 1: From Markdown Wiki to Abstract Graph
**Date:** 2026-04-07

### 1. The Spark: Karpathy's LLM Wiki
We began by analyzing Andrej Karpathy's "LLM Wiki" gist. The core thesis was compelling: traditional RAG is ephemeral and rediscovers knowledge from scratch every time. A better pattern is a **compounding, LLM-maintained markdown graph** where an LLM acts as the programmer/maintainer of a Wiki (using Obsidian as the IDE).
> **Commit:** `a870f33` (docs: add LLM Wiki gist by Karpathy)
> **File:** [`llm_wiki.md`](file:///Users/bln/play/projects/proj-20260407-092747/llm_wiki.md) (Blob: `f367a72`)

### 2. The Pivot: Erasing the Filesystem
While the markdown/Obsidian pattern is great for a local desktop, we realized it is too coupled to a traditional filesystem. We want this engine to run anywhere:
- Locally (Bun/Node with `fs`)
- At the edge (Cloudflare Workers/D1/Vectorize)
- In the browser (IndexedDB/OPFS)

To achieve this, we had to abstract away the concept of "files", "directories", and `grep`. We realized this isn't a CMS; it is an **Active Epistemic Engine**—a computational substrate for the seed actor's (TA's) memory and belief state.
> **Commit:** `704b729` (docs: define MVP goals for TA's memory engine)
> **File:** [`GOKR.md`](file:///Users/bln/play/projects/proj-20260407-092747/GOKR.md) (Blob: `830436f`)

### 3. Defining the Abstract Primitives
We initially stripped the engine down to four primitives: `GET`, `PUT`, `LOG`, and `SEARCH`. We quickly realized a graph needs topology, so we added `TRAVERSE` (to follow explicit edges like `depends_on` or `contradicts`). 

We then fell into a trap: assuming that if the backend is "dumb" (e.g., just a flat filesystem), the LLM must manually maintain a master `index.md` node to perform searches. 
> **Commit:** `526d79a` (docs: define TA memory engine operations)
> **File:** [`OPERATIONS.md`](file:///Users/bln/play/projects/proj-20260407-092747/OPERATIONS.md) (initial version)

### 4. Questioning the Assumptions
Upon rigorous questioning, we realized we were forcing the LLM to act like a human file clerk, mimicking human taxonomies. We documented these fragile assumptions (see `ASSUMPTIONS.md`). Key realizations:
- **Taxonomy Debt:** Forcing the LLM to categorize knowledge into discrete "nodes" prematurely is brittle.
- **Destructive PUTs:** Overwriting nodes destroys the history of how a belief evolved. Pure Event Sourcing (`APPEND`) might be superior.
- **Compute to Data:** If nodes are massive (books) or protected (enterprise data), the LLM shouldn't `GET` them. It should use abstract Compute Tools (e.g., `QueryNode`) to push the processing down to the data layer.
> **Commit:** `80b4954` (docs: capture narrative, assumptions, and refine operations based on epistemic engine pivot)
> **File:** [`ASSUMPTIONS.md`](file:///Users/bln/play/projects/proj-20260407-092747/ASSUMPTIONS.md) (Blob: `b9b3daa`)

### 5. The Current State
We redesigned `OPERATIONS.md` to reflect an engine that separates the dumb storage primitives (`GET`, `LOG`) from smart compute tools (`QueryNode`, `SearchScope`), moving away from treating the LLM as a naive database maintainer.
> **Commit:** `80b4954` (docs: capture narrative, assumptions, and refine operations based on epistemic engine pivot)
> **File:** [`OPERATIONS.md`](file:///Users/bln/play/projects/proj-20260407-092747/OPERATIONS.md) (Blob: `e888e1a`)
> **File:** [`NARRATIVE.md`](file:///Users/bln/play/projects/proj-20260407-092747/NARRATIVE.md) (this file)

### 6. Removing Human Constraints & Embracing the Algorithmic Partnership
After formalizing the `OPERATIONS.md` protocol, we explicitly called out several unexamined assumptions we were holding—specifically around using Markdown (a human document format) for machine mutation (`PUT`), and how to handle concurrency in a multi-agent system.

**The breakthrough:** We realized we were over-indexing on making the system "readable" for humans, forcing legacy human-centric workflows onto an algorithmic partner. The system is for "us"—Human and Algorithmic intelligence working together. By removing the ego and the need to prematurely optimize for human understanding, the number of "one-way doors" collapses. 
We can store data as JSON, Triples, or Event Streams if it's better for the machine. We can defer complex concurrency, identity, and tenancy (auth/scope) problems to later iterations, leaning on our prior art (e.g., `know`, Dolt).

> **Commit:** `920b4cd` (docs: rename open questions to DESIGN_DECISIONS and capture human/algorithmic alignment)
> **File:** [`DESIGN_DECISIONS.md`](file:///Users/bln/play/projects/proj-20260407-092747/DESIGN_DECISIONS.md) (Replaced `OPEN_QUESTIONS.md`)
