**[B01] Custom Terrain Materials (Roblox Studio/engine — full launch)**
- **Company:** Roblox
- **Status:** GA (Full Launch) · **Released:** 2026-10-22 · **New**
- **Surface:** engine / studio tool (terrain rendering system)
- **Primary source:** <https://devforum.roblox.com/t/full-launch-publish-games-with-custom-terrain-materials-and-performance-improvements/4950620>
- **Underlying research:** no traceable paper (the devforum post does not cite or name any underlying research)
- **Availability:** Fully supported for all published, playable Roblox experiences; no beta flag or invitation required. Creators enable it via "Expanded Terrain" in Studio Workspace properties; places edited during the prior Early Access period must re-enable it.

**What shipped:** Roblox moved Custom Terrain Materials — letting creators define up to 62 paintable terrain materials (of 64 total slots, with Water and Air read-only) — out of Early Access to full launch, alongside the first round of rendering, storage and delivery performance improvements for terrain.
**What research it translates:** No traceable paper — Roblox does not cite or name an underlying research project for this engine feature.
**Practical significance:** Roblox states any player can now play published experiences using custom terrain materials, and that published terrain is ejected as its own asset (capped at 250MB) rather than counting against the overall place publish-size limit.
**Engineering details:** Roblox states the changes "reduced CPU memory overhead by 90% and meshing latency by 45%" in one benchmark, and improve terrain's contribution to streaming and load times.
**Limitation / caveats:** The 62-material cap (of 64 total slots) is a hard limit; places that used custom materials during Early Access must manually re-enable Expanded Terrain after this launch or materials can render as grass; the iOS streaming-crash fix had not yet shipped at post time.
