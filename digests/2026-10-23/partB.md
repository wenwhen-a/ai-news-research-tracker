# Part B — Research → Product
Window: last 90 days (2026-07-25 to 2026-10-23). Qualifying products: 1 new, 0 updated. Announced-only: 0. Open releases moved to Part A: 0.

---
## Quality Mode for Texture Generation (Roblox Studio AI texture tool)
- **Company:** Roblox
- **Status:** Public beta/preview · **Released:** 2026-10-16 · **New**
- **Surface:** studio tool
- **Primary source:** https://devforum.roblox.com/t/beta-introducing-quality-mode-for-texture-generation/4938282
- **Underlying research:** no traceable paper (the devforum post does not cite or name any underlying generative model or research paper)
- **Availability:** Beta, available now in Roblox Studio via the Texture button in the Model ribbon (with a model selected), right-click > Generate > Texture, or the Assistant command /generate_texture with a mesh selected. Supports multi-part meshes; no stated region or account-tier restriction.

**What shipped (≤3 sentences):** Roblox Studio's AI Texture Generation feature added a "Quality" mode alongside the existing "Fast" mode. Quality mode produces 4K PBR textures (color, roughness, metalness maps) in about 2 minutes, versus Fast mode's 1K color-only output in about 30 seconds.
**What research it translates (≤3 sentences):** No traceable paper — Roblox does not name an underlying model or cite research for this feature.
**Practical significance (≤3 sentences):** Roblox states Quality mode gives creators higher-fidelity, game-ready PBR texture maps directly in Studio, intended to reduce manual texturing work for 3D assets, and that it performs better on higher-resolution source meshes.
**Engineering details (≤3 sentences):** Accessible via Studio's Model ribbon, right-click context menu, or the in-Studio Assistant chat command /generate_texture. Outputs PBR map sets (color/roughness/metalness) for Quality mode vs. color-only for Fast mode; works on multi-part meshes.
**Limitation / caveats (≤3 sentences):** Roblox-acknowledged limitations: alpha channels (transparency/glass) are not supported; normal maps on input meshes are currently ignored (support "coming soon"); the generator cannot see Assistant chat history or game context, so prompts must be self-contained; some Toolbox assets' permissions block retexturing.

### Announced only (not yet usable)
(none)

Near-misses: Unity 6000.6.7f1 (2026-10-21) is a routine patch, not a substantial new feature — excluded. A reported ByteDance real-time 3D "world model" on Seedance for Pico VR is sourced only to anonymous Bloomberg-relayed reporting via secondary outlets, no primary confirmation — excluded as unverifiable. Kling 4.0 (Kuaishou) reportedly launched 2026-10-15 (just outside window) with conflicting/unclear GA status from primary sources — excluded. An NVIDIA developer-blog post on robot-walking simulation training is off-topic (robotics, not 3D/world-models/character-animation/game-engines) — excluded. A PlayStation Blog "Saros" dev interview appears to be a behind-the-scenes feature story, not a shipped tool — excluded.
Verification: all 10 primary surfaces checked by a sub-agent; the one qualifying item was independently re-verified by the orchestrator against its primary source (devforum.roblox.com) before inclusion.
