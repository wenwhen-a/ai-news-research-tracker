**[B02] Roblox Studio — Tunable Collision Geometry (CollisionFidelity = Tunable)**
- **Company:** Roblox
- **Status:** GA · **Released:** 2026-09-17 · **New**
- **Surface:** studio tool
- **Primary source:** <https://devforum.roblox.com/t/collision-geometry-workflow-improvements-tunable-precision-and-better-visualizations/4878198>
- **Underlying research:** no traceable paper
- **Availability:** Available now to all Roblox Studio users; non-breaking (opt-in per MeshPart via a new CollisionFidelity = Tunable setting); no waitlist, application, or beta flag mentioned in the post.

**What shipped:** Roblox added a CollisionPrecision slider under a new CollisionFidelity = Tunable option, letting developers fine-tune the performance/precision tradeoff of mesh collision on a per-part basis, plus improved collision visualization (adjustable transparency, property-based filtering, automatic geometry preview).
**What research it translates:** no traceable paper — Roblox frames this as an engine/tooling workflow improvement, not as based on a specific cited research paper.
**Practical significance:** Roblox states the feature helps developers handle "meshes with thin components and complex details" that previously struggled under the old fixed collision-fidelity presets, and that intelligent per-mesh-size defaults reduce the amount of manual tuning needed.
**Engineering details:** Applies per MeshPart inside Roblox Studio; existing games and meshes are unaffected unless a developer explicitly switches a part's CollisionFidelity to Tunable.
**Limitation / caveats:** Roblox acknowledges complex meshes (large vertex/face counts) can see up to ~5-second initial processing delays in Studio before the slider becomes smooth to use (cached afterward); the company is still soliciting developer feedback on how resizing should affect existing tuned collision geometry.
