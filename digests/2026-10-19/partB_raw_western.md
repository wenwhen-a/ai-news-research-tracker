# Part B — Research → Product: Western Companies (Google/DeepMind, Microsoft, Meta, Amazon, Apple, EA, Ubisoft, Roblox, Sony)

Window: 2026-07-21 to 2026-10-19 (today, UTC)

Note on method: the shared WebSearch budget for this turn was exhausted early (other parallel group-agents used it up), so this sweep relied almost entirely on direct WebFetch of primary-source pages (company blogs/newsrooms, Apple/Microsoft/Google dev docs, Roblox DevForum/Discourse JSON search, PlayStation blog, EA/Ubisoft newsrooms). Several guessed primary-source URLs 404'd (Meta Connect 2026 recap page, specific Google blog post, Halo page), limiting coverage of Google, Meta, Microsoft, Apple, EA and Ubisoft this round relative to Roblox (whose DevForum JSON search endpoint was usable). Coverage of those companies should be treated as partial, not exhaustive.

---

## EditableMesh Batching APIs & Parallel Queries
- **Company:** Roblox
- **Status:** GA (Full Release) · **Released:** 2026-09-15 · **New**
- **Surface:** Studio/engine API (3D mesh editing)
- **Primary source:** https://devforum.roblox.com/t/full-release-editablemesh-batching-apis-parallel-queries
- **Underlying research:** no traceable paper
- **Availability:** Available in published experiences as of 2026-09-15 full release (beta had been available since 2026-08-06 via File > Beta Features > EditableMesh Batching). No region/plan gating noted.

**What shipped (≤3 sentences):** Roblox shipped ten new batch methods (BatchAdd, BatchRemove, Clear, BatchSetValues, BatchSetFaceAttributes, BatchSetVertexFaceAttributes, BatchGetValues, BatchGetFaceAttributes, BatchGetVertexAttributes, BatchGetVertexFaceAttributes) for the EditableMesh API, plus parallel-safe query methods (RaycastLocal, FindClosestPointOnSurface, FindClosestVertex, Get* accessors) usable from parallel Luau after task.desynchronize(). This moved from Studio Beta (Aug 6, 2026) to full release in published experiences (Sep 15, 2026).
**What research it translates (≤3 sentences):** This is an internal engine/runtime-systems engineering effort (batched mesh mutation + parallelized read queries) rather than a published ML research result; no arXiv paper or research blog post underlies it.
**Practical significance (≤3 sentences):** Roblox states the batching APIs are up to ~8x faster than per-element loops, and parallel queries give up to ~2x read throughput, benchmarked on a 2019 Huawei phone with 2GB RAM — i.e., aimed at making procedural/generative mesh editing (including AI-generated mesh workflows like Segment Any Mesh) performant at runtime on low-end mobile hardware.
**Engineering details (≤3 sentences):** Mutating methods must still run serially (task.synchronize()); only queries are parallel-safe. Enum.MeshAttribute values covered: Vertex, Normal, UV, Color, Face; a single batch call cannot mix ID types.
**Limitation / caveats (≤3 sentences):** Skinning is not supported for batching or parallel access; parallel writes are not supported at all. Roblox lists replication, reduced ID-verification overhead, permission restrictions, and possible quad support as future work, so the feature is still evolving post-GA.

---

### Announced only (not yet usable)

(No genuinely new announced-only items were confirmed this round beyond the already-tracked Roblox roadmap/Scene Generator items, which remain unchanged — RDC26 recap thread, checked 2026-10-19, still lists "NPC Dynamic Behavior" as a "Late 2026" plan with no shipped status, and "Scene Generator" returned no DevForum results at all, confirming it has not shipped.)

---

Near-misses: 3 (Meta Hologram status-change could not be verified against a reachable Meta Connect 2026 recap primary source — page 404'd on multiple guessed URLs; a "Gemini 3.8 Live with Live Avatar" post referenced only in a secondary blog-listing summary could not be located on blog.google itself, so it may simply be the already-tracked Gemini Enterprise Live Avatar re-surfacing under a different label and was not counted as new; Roblox Terrain Early Access — 64 custom materials & storage optimizations — is invite-only/waitlist (Announced-only tier) but its program opened 2026-06-25, before the window, with only a final signup-wave note dated 2026-07-24 inside the window, so it's ambiguous whether it counts as newly-dated for this sweep.)
