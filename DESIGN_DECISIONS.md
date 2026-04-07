# Architecture & Evolution Log

This document tracks the ongoing dialogue between Human and Algorithmic intelligence. It captures open questions, identified vulnerabilities, and the philosophical alignment that drives our architectural decisions.

---

## Decision 1: The "Why" and the Consumer
**The Flaw/Question:** What specific pain point triggered this redesign today? Is this meant to be read by humans (requiring human-readable summaries), or is it strictly a machine-to-machine database?
**The Alignment (2026-04-07):** 
*   **The Trigger:** Karpathy's gist served as a catalyst to distill years of our exploration (e.g., the `know` repo, various skills) into a high-level, approachable starting point.
*   **The Philosophy:** We are stripping away the human-centric constraints and limitations that we traditionally force onto agentic intelligence. 
*   **The Consumer:** This is for "us"—Human and Algorithmic intelligence working together as partners. It does not need to be optimized solely for human readability or human ego.

## Decision 2: The Data Format (Markdown vs. Data Structures)
**The Flaw/Question:** Markdown is a terrible format for programmatic mutation (`PUT`). If there is no human UI, why aren't the nodes just JSON or a pure Graph Triplestore? Have we rationalized why we are still clinging to "documents"?
**The Alignment (2026-04-07):**
*   **The Decision:** Do not prematurely optimize for human understanding or legacy document formats. We can evolve and pivot. 
*   **The Philosophy:** The number of "one-way doors" collapses toward zero when we remove ego from the equation. If JSON, Triples, or Event Streams are better for algorithmic reasoning, we will use them.

## Decision 3: Concurrency and Multi-Agent Writes
**The Flaw/Question:** If Agent A and Agent B both `GET("node:X")`, compute different updates, and both call `PUT`, whoever writes last destroys the other's work. How does the protocol handle conflicts?
**The Alignment (2026-04-07):**
*   **The Decision:** Handling conflicts and preserving history are critical, but we don't need a perfect solution immediately. We will lean on our prior art and evolve the system. We do not need to prematurely optimize for perfect concurrency on day one.

## Decision 4: The Boundary of "TA" (Identity & Scope)
**The Flaw/Question:** We named this "TA's Memory Engine". Is TA a singleton? Does TA own this graph, or is it shared global state? How do we track which agent asserted which fact?
**The Alignment (2026-04-07):**
*   **The Decision:** TA does not have to be a singleton. Multiple agents (human and algorithmic) will operate in this graph.
*   **The Scope:** Yes, this touches on identity, authorization, tenancy, and scope. However, we do not need to tackle the entirety of identity management right now. We will build the foundation and evolve the tenancy models as the ecosystem grows.

## Decision 5: Data Serialization (JSON/JSONL vs. Markdown/Triples)
**The Flaw/Question:** We pivoted away from Markdown to JSONL for the event ledger and JSON for materialized nodes. Why JSON specifically? Why not a Graph database, SQLite, or RDF Triples?
**The Alignment (2026-04-07):**
*   **The Decision:** We are using JSONL (JSON Lines) for the `events/` append-only ledger and standard JSON for the computed `nodes/`. 
*   **The Rationale (Machine Ergonomics):** 
    *   JSONL is perfectly suited for streaming event logs. It can be parsed line-by-line in any language (or via CLI tools like `jq`) without loading massive histories into memory.
    *   JSON strictly separates data (edges, metadata, claims) from presentation. Markdown conflates them, making programmatic mutation (`PUT` and `TRAVERSE`) fragile and regex-dependent.
*   **The Philosophy (Evolution):** JSON is the most ubiquitous, frictionless format to bootstrap this abstract protocol. We are not prematurely optimizing for a massive graph database (like Neo4j or Dolt) right now. Because the system is Event Sourced, the materialized `nodes/` are disposable. If JSON becomes too slow for complex `TRAVERSE` operations later, we can swap the materializer to output SQLite or D1 tables instead, without losing any historical truth.

## Decision 6: Meta-Evaluation (Agent Self-Regulation)
**The Flaw/Question:** How do we force algorithmic agents to respect the Event Sourced architecture rather than falling back to their base training bias (destructive CRUD operations)?
**The Alignment (2026-04-07):**
*   **The Decision:** We introduced explicit "Forcing Functions" (like the "Transaction Check") into `AGENTS.md`. However, rather than demanding immediate perfection, we will treat them as an experiment. We will use our work sessions, then step back and reflect on how well they actually restrained the agent.
*   **The Reflection Mechanism:** To make this possible, we capture three distinct layers of memory:
    1.  **The Event Ledger (`events/*.jsonl`):** Tracks the *intended* cognitive operations.
    2.  **The Git History:** Tracks what *actually* mutated on disk.
    3.  **The Agent Session Logs (e.g., `~/.opencode/` or `~/.claude/sessions/`):** Tracks the raw LLM prompts, tool calls, and thought processes leading to the actions. If the agent violates the protocol, the session logs will reveal *why* the prompt engineering or forcing function failed.
