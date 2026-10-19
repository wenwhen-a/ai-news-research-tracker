**[B01] EditableMesh Batching APIs & Parallel Queries**
- **Company:** Roblox
- **Status:** GA (Full Release) · **Released:** 2026-09-15 · **New**
- **Surface:** Studio/engine API (3D mesh editing)
- **Primary source:** <https://devforum.roblox.com/t/full-release-editablemesh-batching-apis-parallel-queries>
- **Underlying research:** no traceable paper
- **Availability:** Available in published experiences as of the 2026-09-15 full release (beta had been available since 2026-08-06 via File > Beta Features > EditableMesh Batching). No region/plan gating noted.

**What shipped:** Roblox shipped ten new batch methods (BatchAdd, BatchRemove, Clear, BatchSetValues, BatchSetFaceAttributes, BatchSetVertexFaceAttributes, BatchGetValues, BatchGetFaceAttributes, BatchGetVertexAttributes, BatchGetVertexFaceAttributes) for the EditableMesh API, plus parallel-safe query methods (RaycastLocal, FindClosestPointOnSurface, FindClosestVertex, Get* accessors) usable from parallel Luau after task.desynchronize().
**What research it translates:** This is an internal engine/runtime-systems engineering effort (batched mesh mutation + parallelized read queries) rather than a published ML research result; no arXiv paper or research blog post underlies it.
**Practical significance:** Roblox states the batching APIs are up to ~8x faster than per-element loops, and parallel queries give up to ~2x read throughput, benchmarked on a 2019 Huawei phone with 2GB RAM — aimed at making procedural/generative mesh editing (including AI-generated mesh workflows like Segment Any Mesh) performant at runtime on low-end mobile hardware.
**Engineering details:** Mutating methods must still run serially (task.synchronize()); only queries are parallel-safe.
**Limitation / caveats:** Skinning is not supported for batching or parallel access; parallel writes are not supported at all.
