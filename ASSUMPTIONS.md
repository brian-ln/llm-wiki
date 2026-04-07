# Foundational Assumptions and Vulnerabilities

## 1. The Granularity Assumption: Discrete "Nodes"
*   **The Assertion:** The system stores information as discrete entities/pages (e.g., `node:auth`, `node:dolt`), mirroring a Wiki or relational database.
*   **The Vulnerability:** It forces the LLM to categorize knowledge prematurely. Reality is fluid. Forcing the LLM to decide exactly *where* a new fact belongs (does it go in `node:auth` or `node:security`?) introduces friction and taxonomy debt.
*   **Alternative:** Maybe there are no discrete nodes. The system is just an append-only stream of facts/fragments (`LOG`), and "pages" are dynamically generated at query time based on what the user asks.

## 2. The Topology Assumption: Explicit Links
*   **The Assertion:** We need explicit references (`[depends_on: node_id]`) and a `TRAVERSE` capability.
*   **The Vulnerability:** Maintaining explicit links is hard, whether the LLM does it or a database does it. Furthermore, it assumes the *structure* of knowledge is static. 
*   **Alternative:** Rely entirely on overlapping semantic spaces (`SEARCH`). If two concepts are related, their vectors or content will naturally pull them together at query time without manual linking.

## 3. The State Assumption: Destructive PUTs
*   **The Assertion:** The LLM reads a node, updates the text, and overwrites it (`PUT`).
*   **The Vulnerability:** `PUT` destroys history. If the LLM hallucinates or makes a bad synthesis, the previous state is gone (unless we rely heavily on the `LOG`). It also causes race conditions if two agents run in parallel.
*   **Alternative:** Pure Event Sourcing. The only write primitive is `APPEND`. The LLM never overwrites a node; it just appends a new claim: `"Update: Cloudflare D1 now supports vectors."` The `GET` primitive is actually a compute function that reads the stream of claims and compiles the "current truth" on the fly.

## 4. The Edge Compute Assumption: Tools must be pushed to the data
*   **The Assertion:** If a node is massive or secure, the LLM uses a tool like `QueryNode(id, prompt)` rather than reading the data directly into context.
*   **The Vulnerability:** Context windows are now approaching millions of tokens. The cost/complexity of pushing compute to the edge (building local RAG tools, maintaining local models) might be higher than simply dumping the entire document into the context window of a frontier model.
*   **Alternative:** Assume massive context windows are the default. The only primitive needed is `GET`, and the LLM handles everything in-prompt, eliminating complex tool orchestration.

## 5. The LLM Clerk Assumption: Manual Index Maintenance
*   **The Assertion:** If we only have `GET/PUT`, the LLM must manually edit an `index.md` file to keep track of what exists (acting as the search index).
*   **The Vulnerability:** It is incredibly brittle. LLMs are probabilistic text generators; relying on them to maintain deterministic, machine-readable database indexes is asking for corruption. 
*   **Alternative:** We accept that a "dumb" backend is a myth. Even if it's just a filesystem, we *must* have deterministic code (a background script) that builds the index/search capabilities. We should not ask the LLM to do clerical database maintenance.

## 6. The Tertiary Source Assumption (Wikipedia for Architecture)
*   **The Assertion:** Using Wikipedia (`raw/diffusion_model.md` and `raw/mixture_of_experts.md`) is sufficient grounding for defining the 'Instruction Set Architectures' of Software 2.0.
*   **The Vulnerability:** Wikipedia is a tertiary source that focuses on academic definitions and chronological history, not necessarily the applied engineering framing of "Software 2.0" (which is a conceptual metaphor popularized by Andrej Karpathy and industry practitioners). By using Wikipedia as the primary grounding material for these nodes, I am assuming the underlying mathematical descriptions (e.g., Markov chains for Diffusion, gating functions for MoE) perfectly map to the "Neural Processor / ISA" metaphor without hallucinating the connection.
*   **Alternative / Mitigation:** If this mapping proves fragile, the Null Hypothesis (Kill Switch) would be finding that practitioners do *not* treat these architectures interchangeably as different "processor ISAs", but rather as entirely distinct paradigms that cannot be unified under the Software 2.0 umbrella. To fix this, I must explicitly tag my syntheses as `[HYPOTHESIS]` or `[AGENT-RESEARCH]` when connecting the strict math of Wikipedia to the Software 2.0 metaphor, until primary sources (like Karpathy's essays or deep learning engineering blogs) explicitly confirm the mapping.
