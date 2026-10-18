**[B01 · Update] Roblox Studio — Texture Generation Tools (Quality Mode update)**
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta/Assistant) · **Released:** 2026-10-16 · **Update**
- **Surface:** Studio tool (Assistant-driven texture generation for 3D meshes)
- **Primary source:** <https://devforum.roblox.com/t/beta-introducing-quality-mode-for-texture-generation/4938282>
- **Underlying research:** no traceable paper
- **Availability:** Opt-in Studio Beta / Assistant feature, free to Roblox creators; accessed via Model > Texture menu, right-click Generate > Texture, or the `/generate_texture` Assistant command.

**What shipped:** Update since 2026-09-23: Roblox added a "Quality" mode to its in-Studio AI texture generation tool (first shipped as the Fast-only "Texture Generation Tools" beta), alongside the existing "Fast" option.
**What research it translates:** Roblox does not cite an underlying paper or model architecture for this release; the devforum post describes only the product-facing behavior (PBR map generation, text preservation, multi-part mesh support).
**Practical significance:** Roblox states Quality mode "preserves text better and adds detail" compared with Fast mode, and that texture generation "now works on meshes with multiple parts," letting creators generate production-grade PBR materials for 3D assets directly inside Studio instead of only flat color textures.
**Engineering details:** Output maps are color (albedo), roughness, and metalness; normal maps are explicitly not yet supported.
**Limitation / caveats:** Roblox states normal maps are not generated in this release.
