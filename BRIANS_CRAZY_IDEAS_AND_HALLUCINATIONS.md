# Brian's Crazy Ideas and Hallucinations

If you are reading through the history or design decisions of this repository (like `NARRATIVE.md` or `DESIGN_DECISIONS.md`), you will see references to terms like **TA**, the **`/know` skill**, **Dolt**, and **`/council`**.

This document is here to translate our internal jargon. We have been building and using AI-agent tooling for years. The `llm-wiki` repository is an attempt to distill the *lessons* from those heavy, complex tools into a universal, approachable protocol. You don't need any of these tools to understand or use this repository, but this is the prior art that shaped our thinking.

This entire repository is a direct riff on [Andrej Karpathy's LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Our ultimate strategy to make this easy and approachable is to build the engine here, and then regularly distill our findings and patterns *back* into a Gist (or maybe multiple Gists). You shouldn't have to navigate a complex repository just to grab the core ideas and bootstrap your own epistemic engine.

---

## 1. The `/know` CLI Skill
**What it was:** A custom skill/tool we built for our agents (like Claude Code or OpenCode) to proactively capture, search, and organize insights into a local git repository (`~/knowledge`).
**What it taught us:** Agents are terrible at mutating large markdown files. When we asked the `/know` agent to update a cross-reference in a 2,000-word markdown file, it would frequently hallucinate deletions or break formatting. We realized that forcing agents to act like human file-clerks causes massive friction.

## 2. Dolt (Git-for-Data)
**What it is:** [Dolt](https://github.com/dolthub/dolt) is a SQL database that supports Git-style branching, merging, and time-travel querying.
**What it taught us:** The power of version-controlled data. When an agent hallucinates a bad fact into a SQL table, you need the ability to roll it back. However, standing up a full Dolt SQL server is heavy infrastructure just to give an agent some working memory. 
**The Evolution:** In this repo, we recreated that version-control power using simple, append-only **JSONL Event Sourcing** (the `LOG` primitive), giving us the rollback capability of Dolt without the heavy SQL requirement.

## 3. TA (The Seed Actor)
**What it is:** "TA" is the name of our persistent, primary cognitive agent (the "seed actor"). TA maintains context across all of our conversational sessions. 
**What it taught us:** An agent like TA needs a brain—a long-term, queryable memory graph. But TA shouldn't have to scan 50 markdown files to remember a decision we made yesterday. It needs a structured API (`GET`, `SEARCH`, `TRAVERSE`). That is what we are building here: an *Epistemic Engine* for TA.

## 4. Multi-Agent Coordination (`/council`)
**What it is:** A workflow where we spin up multiple independent agents to debate a topic, read different documents, or resolve a contradiction before writing a final synthesis.
**What it taught us:** If multiple agents are reading and writing to the same knowledge base simultaneously, destructive file updates (`PUT`) cause massive race conditions (last-writer-wins). 
**The Evolution:** This is why we pivoted to the **Immutable Ledger**. If 5 agents append claims (`LOG`) simultaneously, no data is lost. A background process can read the ledger and materialize the final view later.

---

### The Goal of This Repository
We took all of these complex, heavy, personalized tools and distilled them into the simplest possible abstraction: A stream of JSON events, materialized into JSON nodes, operated on by abstract primitives (`GET`, `PUT`, `LOG`, `SEARCH`, `TRAVERSE`). 

By open-sourcing this, we hope to share the architecture of algorithmic memory without forcing anyone to install our specific CLI tools or SQL databases.
