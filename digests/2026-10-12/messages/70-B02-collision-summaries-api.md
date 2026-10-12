**[B02] Collision Summaries API**
- **Company:** Roblox
- **Status:** GA (live engine API, no opt-in required) · **Released:** 2026-10-06
- **Surface:** Engine / Studio scripting API
- **Primary source:** <https://devforum.roblox.com/t/collision-summaries-api-detailed-collision-data-from-the-engine/4918568>
- **Underlying research:** no traceable paper (physics-solver engineering feature, not an AI/ML research translation)
- **Availability:** Live now for all Roblox experiences; new `BasePart:BindToCollisionSummaries` method, no beta flag.

**What shipped:** Roblox added a new engine API, `BasePart:BindToCollisionSummaries`, exposing per-contact collision data — contact points, normals, and relative/impact velocity — directly from the physics solver. It ships live, not gated behind Studio Beta Features.
**What research it translates:** This is a physics-engine instrumentation feature rather than a published research translation; no arXiv or research-blog source was found backing it.
**Practical significance:** Roblox frames this as useful "for impact FX, sound, and damage systems," letting developers drive effects from solver-level contact data instead of approximating it from velocity deltas.
**Engineering details:** The API binds a callback on a `BasePart` that fires with structured collision summaries (contact points, normals, relative velocity) sourced from the engine's physics solver each simulation step.
**Limitation / caveats:** Only verified via the devforum announcement post; no independent performance/scale data (e.g. overhead at high contact counts) was available.
