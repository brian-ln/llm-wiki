# Narrative: The Road to an Epistemic Engine

## Session 1: From Markdown Wiki to Abstract Graph
**Date:** 2026-04-07

### 1. The Spark: Karpathy's LLM Wiki
We began by analyzing Andrej Karpathy's "LLM Wiki" gist. The core thesis was compelling: traditional RAG is ephemeral and rediscovers knowledge from scratch every time. A better pattern is a **compounding, LLM-maintained markdown graph** where an LLM acts as the programmer/maintainer of a Wiki (using Obsidian as the IDE).

### 2. The Pivot: Erasing the Filesystem
While the markdown/Obsidian pattern is great for a local desktop, we realized it is too coupled to a traditional filesystem. We want this engine to run anywhere:
- Locally (Bun/Node with `fs`)
- At the edge (Cloudflare Workers/D1/Vectorize)
- In the browser (IndexedDB/OPFS)

To achieve this, we had to abstract away the concept of "files", "directories", and `grep`. We realized this isn't a CMS; it is an **Active Epistemic Engine**—a computational substrate for the seed actor's (TA's) memory and belief state.

### 3. Defining the Abstract Primitives
We initially stripped the engine down to four primitives: `GET`, `PUT`, `LOG`, and `SEARCH`. We quickly realized a graph needs topology, so we added `TRAVERSE` (to follow explicit edges like `depends_on` or `contradicts`). 

We then fell into a trap: assuming that if the backend is "dumb" (e.g., just a flat filesystem), the LLM must manually maintain a master `index.md` node to perform searches. 

### 4. Questioning the Assumptions
Upon rigorous questioning, we realized we were forcing the LLM to act like a human file clerk, mimicking human taxonomies. We documented these fragile assumptions (see `ASSUMPTIONS.md`). Key realizations:
- **Taxonomy Debt:** Forcing the LLM to categorize knowledge into discrete "nodes" prematurely is brittle.
- **Destructive PUTs:** Overwriting nodes destroys the history of how a belief evolved. Pure Event Sourcing (`APPEND`) might be superior.
- **Compute to Data:** If nodes are massive (books) or protected (enterprise data), the LLM shouldn't `GET` them. It should use abstract Compute Tools (e.g., `QueryNode`) to push the processing down to the data layer.

### 5. The Current State
We are redesigning `OPERATIONS.md` to reflect an engine that separates the dumb storage primitives (`GET`, `LOG`) from smart compute tools (`QueryNode`, `SearchScope`), moving away from treating the LLM as a naive database maintainer.
