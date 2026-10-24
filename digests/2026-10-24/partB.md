# Part B — Research → Product
Window: last 90 days (2026-07-26 to 2026-10-24). Qualifying products: 1 new, 0 updated. Announced-only: 0. Open releases moved to Part A: 0.

---
## Custom Terrain Materials (Roblox Studio/engine — full launch)
- **Company:** Roblox
- **Status:** GA (Full Launch) · **Released:** 2026-10-22 · **New**
- **Surface:** engine / studio tool (terrain rendering system)
- **Primary source:** https://devforum.roblox.com/t/full-launch-publish-games-with-custom-terrain-materials-and-performance-improvements/4950620
- **Underlying research:** no traceable paper (the devforum post does not cite or name any underlying research)
- **Availability:** Fully supported for all published, playable Roblox experiences; no beta flag or invitation required. Creators enable it via "Expanded Terrain" in Studio Workspace properties; places edited during the prior Early Access period must re-enable it.

**What shipped (≤3 sentences):** Roblox moved Custom Terrain Materials — letting creators define up to 62 paintable terrain materials (of 64 total slots, with Water and Air read-only) — out of Early Access to full launch, alongside the first round of rendering, storage and delivery performance improvements for terrain.
**What research it translates (≤3 sentences):** No traceable paper — Roblox does not cite or name an underlying research project for this engine feature.
**Practical significance (≤3 sentences):** Roblox states any player can now play published experiences using custom terrain materials, and that published terrain is ejected as its own asset (capped at 250MB) rather than counting against the overall place publish-size limit.
**Engineering details (≤3 sentences):** Roblox states the changes "reduced CPU memory overhead by 90% and meshing latency by 45%" in one benchmark, and improve terrain's contribution to streaming and load times. A known crash on some iOS devices during terrain streaming in live experiences is fixed in an upcoming release. Roblox describes this as the first of several planned terrain optimizations.
**Limitation / caveats (≤3 sentences):** The 62-material cap (of 64 total slots) is a hard limit; places that used custom materials during Early Access must manually re-enable Expanded Terrain after this launch or materials can render as grass; the iOS streaming-crash fix had not yet shipped at post time.

### Announced only (not yet usable)
(none)

Near-misses: DLSS 4.5 rolling out to Call of Duty: Modern Warfare 4 and Cyberpunk 2077 (NVIDIA, 2026-10-21) is the same already-tracked feature reaching more games, not a new product or tier change — excluded per criteria. Roblox "[Studio Beta] Text-to-Speech Asset Creation Support in Lua" (2026-10-24) is off-topic (speech/audio tooling, not 3D/world-models/character-animation/game-engines) — excluded. Three Alibaba Model Studio "newly released models" (MiniMax-M3.1-Flash, Xiaomi MiMo-V2.6-Pro-Ultraspeed, DeepSeek-V4.1-Flash, 2026-10-17 to 10-21) are general multimodal/text LLMs, off-topic and not from a tracked company — excluded. A secondary-outlet (Italian/French) report that DLSS 5 reached RTX Remix via Streamline on 2026-10-23 has no primary NVIDIA confirmation found — excluded as unverifiable.
Verification: all ~10 primary surfaces (NVIDIA developer blog & GeForce news, Unreal Engine news/forum, Unity blog, Roblox devforum/newsroom, Adobe blog, Tencent Hunyuan, ByteDance Seed/Volcano Engine, Alibaba Model Studio, Kuaishou Kling, PlayStation Blog) were checked directly against their primary pages; the one qualifying item was independently confirmed on its devforum primary source, including original post date and content, before inclusion.
