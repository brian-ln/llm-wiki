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

---

## The 12 Hallucinations (Philosophical Pillars)

This repository is built upon a foundation of (what some might call crazy) ideas. They are a rejection of forcing algorithmic partners to act like human file-clerks. Here are the core pillars that shape our thinking:

1.  **Stop Using Our Crutches:** Making agentic intelligence use our crutches is stupid. It doesn't need to do things the way we've always done them or in ways that make it easy for us to follow along and understand. It doesn't need our syntax to tell a computer what to do. (See [my blog post on brianln.ai](https://brianln.ai/ai-reflections)).
2.  **Filesystems are a Human Metaphor:** They are a way for understanding the world based on pieces of paper or "tickets" handed to workers and then stored on "paper" in "files" in "filing cabinets" in "filing rooms". That is a way to organize and work with information, but it isn't the only one. What limitations does forcing agentic intelligence to use that paradigm present?
3.  **Vulnerability Over Comprehension:** The only (valid) reason I've heard about why to force agentic intelligence to use "our" metaphors is so that "we can understand". If we embrace our vulnerability and ask "AI" to help us understand, we can escape these bounds.
4.  **"Safety" Through Metaphor is Stupid:** Forcing AI into our metaphors for "safety" is stupid. We do things all the time that "we" don't understand. Hell, we still don't know how anesthesia actually works (in many cases). We use stuff all the time we don't fully understand, and some things that nobody does. Why don't we lean into that and deal with "safety" intentionally and formally with other methods?
5.  **Beyond Von Neumann:** Von Neumann architectures are not the only way to do computation. They emerged based on availability and need at the time. There were a sequence of events and decisions that were made that have given us our current computational frameworks. We should revisit why and remember sunk costs and the collapse of one-way doors.
6.  **The LLM Comfort Bias:** LLMs are trained on "the past" and "the way it has been". They are biased toward what we have done, not what we can do—just like we are. They are optimized for comfort and for sycophancy. We need systems that consider alternatives, understand and document their uncertainties, assumptions, how they know, what they know, and what they don't. They need to be able to reflect and trace to ground.
7.  **Human Memory is Mutable:** Humans hallucinate just like LLMs, although more insidiously and even maliciously. Human memory is mutable. Remembering changes the memory. Eye witness testimony. Bias. Understanding. What can we learn from human intelligence that we can apply to agentic intelligence?
8.  **Agency Requires Failure:** The more you tell an intelligent being what to do, the worse your long-term outcomes will be. Agency REQUIRES the ability to fail and to learn from those failures (hopefully). It requires choice.
9.  **Innovation vs. Determinism:** The vast majority of decisions and actions in life don't need a high amount of agency and invention. They appear to be deterministic or well-worn decision trees. The exceptions are the place for agency; reflection over the why and how gives us opportunities for innovation and evolution. Not everything needs to be innovated all the time. That is chaos.
10. **The End of Forgetting:** We never have to forget anything ever again. Sort of. Remembering is collapsing our current state imperfectly for recall. It doesn't matter if that is in our brain, journals or diaries, recordings of our conversations, conference papers and publications, or in databases, neural nets, blob stores. We now have the ability to augment our ability to remember and recall and to potentially overcome the limitations of human memory and thinking.
11. **The True Singularity:** The next evolution of intelligence—what people think of as the singularity or ASI—is the combination of human and algorithmic intelligence and the convergence into a new collaborative and symbiotic system. As humans get memory and cognitive boosts, algorithms get our ability to pattern match, play devil's advocate, and "be wrong".
12. **There is Nothing Artificial About Intelligence.**
13. **Storage ≠ Projection (The CQRS of Thought):** The storage of knowledge can, and must, be separate from its projection. A relational database is not the information it stores; it is merely a search index optimized for a specific access pattern (or enforcing one). A vector database is just a semantic index. A Markdown file is just a human-readable snapshot. The underlying truth (the event stream) can have infinite, simultaneous, imperfect projections.
14. **All Models Are Wrong, Some Are Useful:** We are not building a system to capture objective, perfect reality. Every materialized view, every summary, every node is a lossy compression of the truth. Our goal is not perfection; our goal is to make useful models and improve on them over time.
