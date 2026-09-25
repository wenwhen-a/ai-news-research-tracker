**[B02] Roblox Studio Beta — Quad Support for EditableMesh APIs**
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta, opt-in) · **Released:** 2026-09-23 · **New**
- **Surface:** engine / studio tool (EditableMesh API)
- **Primary source:** <https://devforum.roblox.com/t/studio-beta-quad-support-for-editablemesh-apis/4890142>
- **Underlying research:** no traceable paper
- **Availability:** Opt-in via Roblox Studio File > Beta Features; available to any creator who enables the beta flag, no waitlist stated.

**What shipped:** Roblox's EditableMesh API gained a new `AddFace()` method accepting either three or four vertex IDs, letting creators build four-sided quad faces directly instead of manually splitting every quad into two triangles.
**What research it translates:** No traceable paper — this is an engine API change, not a research-derived feature.
**Practical significance:** Roblox states quads can be mixed with triangles on the same mesh, giving "cleaner topology for quad-based workflows like box modeling," while existing EditableMesh operations (`GetFaceNormals()`, `SetFaceVertices()`) continue to work with the new face type.
**Engineering details:** Quads are automatically triangulated internally at render time; Roblox published example place files demonstrating subdivision-surface algorithms and interactive mesh editing built on the new API.
**Limitation / caveats:** The feature requires manually enabling Studio Beta (File > Beta Features); Roblox states "each quad counts as two triangles towards EditableMesh's existing 20,000-triangle limit," so it does not raise the effective mesh-complexity ceiling.
