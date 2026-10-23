**[B01] Quality Mode for Texture Generation (Roblox Studio AI texture tool)**
- **Company:** Roblox
- **Status:** Public beta/preview · **Released:** 2026-10-16 · **New**
- **Surface:** studio tool
- **Primary source:** <https://devforum.roblox.com/t/beta-introducing-quality-mode-for-texture-generation/4938282>
- **Underlying research:** no traceable paper (the devforum post does not cite or name any underlying generative model or research paper)
- **Availability:** Beta, available now in Roblox Studio via the Texture button in the Model ribbon (with a model selected), right-click > Generate > Texture, or the Assistant command /generate_texture with a mesh selected. Supports multi-part meshes; no stated region or account-tier restriction.

**What shipped:** Roblox Studio's AI Texture Generation feature added a "Quality" mode alongside the existing "Fast" mode.
**What research it translates:** No traceable paper — Roblox does not name an underlying model or cite research for this feature.
**Practical significance:** Roblox states Quality mode gives creators higher-fidelity, game-ready PBR texture maps directly in Studio, intended to reduce manual texturing work for 3D assets, and that it performs better on higher-resolution source meshes.
**Engineering details:** Accessible via Studio's Model ribbon, right-click context menu, or the in-Studio Assistant chat command /generate_texture.
**Limitation / caveats:** Roblox-acknowledged limitations: alpha channels (transparency/glass) are not supported; normal maps on input meshes are currently ignored (support "coming soon"); the generator cannot see Assistant chat history or game context, so prompts must be self-contained; some Toolbox assets' permissions block retexturing.
