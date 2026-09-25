**[B01] Roblox Studio — Texture Generation Tools, Segment Any Mesh, and Image Previews**
- **Company:** Roblox
- **Status:** Public beta/preview (rolling out via Studio Assistant) · **Released:** 2026-09-23 · **New**
- **Surface:** studio tool (Roblox Studio Assistant)
- **Primary source:** <https://devforum.roblox.com/t/introducing-new-texture-generation-tools-segment-any-mesh-and-image-previews/4890084>
- **Underlying research:** no traceable paper
- **Availability:** Invoked from Roblox Studio's Assistant panel via ribbon buttons, right-click menus, or slash commands (`/generate_texture`, `/segment_mesh`, `/generate_procedural_model`, `/generate_mesh`); no region or plan restriction is stated, though community replies on the announcement thread report being denied access, suggesting a gradual rollout.

**What shipped:** Roblox added three Assistant-driven tools to Studio: texture generation to restyle one or more selected meshes, "Segment Any Mesh" to split an imported mesh into up to five named parts per operation, and image previews that surface four generated options (with optional reference-image input) for models made via `/generate_procedural_model` or `/generate_mesh`.
**What research it translates:** No traceable paper — the announcement describes the shipped commands and workflow without citing external research.
**Practical significance:** Roblox states the generated textures are "meant to be a starting point for you to continue to build on," framing the feature as a first-draft accelerator for creators building mesh variants and reskins rather than a finished-art pipeline.
**Engineering details:** Segmentation is capped at five named parts per invocation, requiring the command to be re-run on new parts for further splitting; texture generation and mesh generation can take a reference image as input by switching the Assistant's input mode from "Prompt" to "Image."
