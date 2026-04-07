# Narrative: The Road to an Epistemic Engine

## Session 1: From Markdown Wiki to Abstract Graph
**Date:** 2026-04-07

### 1. The Spark: Karpathy's LLM Wiki
We began by analyzing Andrej Karpathy's "LLM Wiki" gist. The core thesis was compelling: traditional RAG is ephemeral and rediscovers knowledge from scratch every time. A better pattern is a **compounding, LLM-maintained markdown graph** where an LLM acts as the programmer/maintainer of a Wiki (using Obsidian as the IDE).
> **Commit:** `a870f33` (docs: add LLM Wiki gist by Karpathy)
> **File:** [`raw/karpathy_llm_wiki.md`](file:///Users/bln/play/projects/proj-20260407-092747/raw/karpathy_llm_wiki.md) (Blob: `f367a72`)

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

### 7. Eating Our Own Dog Food: The Native Backlog
We decided to build the list of capabilities (the backlog) we need to construct the engine. Instead of creating a simple human Markdown list, we decided to put the backlog *inside* the engine using its own format. 

We created the `events/` and `nodes/` directories. The backlog was ingested as an immutable append-only JSONL event stream (`events/0001_bootstrap.jsonl`), representing claims like `ASSERT_CAPABILITY` and `ASSERT_EDGE`. 

The system then "materialized" those events into discrete JSON nodes (`nodes/sys_cap_event_ledger.json`). This proves that the data layer doesn't need to be Markdown—JSON provides a much cleaner, programmatically mutable format for the machine, completely fulfilling the API contracts defined in `OPERATIONS.md`.

> **Commit:** `bc09db0` (feat: bootstrap system backlog as native event log and materialized JSON nodes)
> **Directory:** [`events/`](file:///Users/bln/play/projects/proj-20260407-092747/events/)
> **Directory:** [`nodes/`](file:///Users/bln/play/projects/proj-20260407-092747/nodes/)

## Session 2: The Agent OS and the Death of Ad-Hoc Scripts
**Date:** 2026-04-07

### 1. Formalizing Software 2.0 (The Epistemic Ontology)
We started by defining the actual theoretical framework underlying the engine. We moved past the mechanical "file clerk" and embraced Andrej Karpathy's "Software 2.0" metaphor. We recognized that treating LLMs as chaotic black boxes that need rigid `try/catch` loops (pure determinism) is a false dialectic. Instead, we architected **Constraint Surfaces** (JSON schemas, append-only ledgers) that force the high-dimensional fluid (the LLM) to converge on reliable outputs.

To prove this, the AI ingested source texts (Karpathy, Wikipedia) and materialized dozens of nodes defining *Provisional Heuristics*, *Independent Agent Convergence (IAC)*, and *GOKR* (Goals, Objectives, Key Results).
> **Commit:** `41da65b` (feat(epistemic): formalize Software 2.0 ontology, constraints, and GOKR heuristics)

### 2. The Actuator Anomaly: 35 Python Scripts
To materialize these new nodes and events, the AI (acting under strict instructions not to manually edit JSON files via text tools) wrote and executed over 35 distinct Python scripts (`synthesize_determinism.py`, `ingest_karpathy.py`, `fix_epistemic_rigor.py`). 

The root directory became littered with these single-use `1.0` actuator scripts. While they perfectly executed the task, they raised a profound architectural question: *If the Python script is just 1.0 bytecode, what is the actual 2.0 source code?*

### 3. The Revelation: Declarative Agentic IR
We realized that version-controlling these 35 Python scripts was a **Software 1.0 anti-pattern**. If the underlying JSON schema changed tomorrow, all 35 scripts would break. 

The true source code is the **Intermediate Representation (IR)**:
1.  **The Intent** (What the AI wants to do)
2.  **The Constraint Surface** (The rules of the environment)
3.  **The Event Ledger** (The execution trace)

The Python script was merely a disposable JIT-compiled actuator bridging the high-dimensional thought to the low-dimensional filesystem.
> **Commit:** `60f2929` (feat(epistemic): capture Agentic IR and Operations Taxonomy into memory graph)

### 4. Building the Agentic Engine (`bin/engine.py`)
To formalize this, we stripped the AI of its ability to write ad-hoc Python scripts. We built `bin/engine.py`—a single, deterministic Software 1.0 engine. 

From now on, the AI acts as an OS Kernel. To mutate the graph, it writes a declarative `.json` Intent (the Agentic IR) to the `/intents/` directory and executes `python3 bin/engine.py <intent.json>`. The engine automatically envelopes the intent, generates UUIDs/timestamps, permanently logs the cognitive intent to `events/intent_ledger.jsonl`, and then mutates the filesystem.
> **Commit:** `0be6277` (feat(system): build Agentic IR execution engine and bootstrap ledger)
> **Commit:** `4bdaf0b` (docs(system): formalize Agentic IR protocol in AGENTS.md and EVENT_SCHEMA.md)

### 5. Time Travel & The Great Backfill
We now had a pristine 2.0 pipeline, but a dirty 1.0 history (the 35 Python scripts). We couldn't just delete them, because we would lose the cognitive lineage of *how* the early graph was built.

We upgraded the engine to support `LOG_HISTORICAL_INTENT`. We wrote a final script that parsed all 35 legacy Python files, extracted their implied intent, embedded the raw Python source code as the `legacy_executable`, and appended them all to the `intent_ledger.jsonl`. 

Finally, we cross-referenced `git log` to extract the exact millisecond each script was originally authored, backdating the ledger timestamps to ensure perfect temporal causality. Once the history was safely sealed in the ledger, we executed `git rm *.py`, permanently purging the 1.0 actuators from the repository.

Our Epistemic Engine is now a fully declarative Agent OS.
> **Commit:** `a12a2ba` (chore(sys): backport legacy python scripts into historical intents and clean root directory)
> **Commit:** `bb17048` (fix(system): align historical intent timestamps with their causal execution)
