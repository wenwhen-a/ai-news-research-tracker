**[B01] Roblox Studio — Scene Generation (image/prompt → editable 3D scene)**
- **Company:** Roblox
- **Status:** Public beta/preview · **Released:** 2026-10-30 · **New**
- **Surface:** studio tool
- **Primary source:** <https://devforum.roblox.com/t/introducing-scene-generation-prototype-scenes-faster/4966611>
- **Underlying research:** arXiv:2503.15475 "Cube: A Roblox View of 3D Intelligence" (describes text-to-scene generation via 3D shape tokenization)
- **Availability:** Studio beta; reachable via the Assistant `/generate_scene` command or a right-click viewport "Generate > Scene" menu option; no region/plan gating stated; not GA.

**What shipped:** Roblox shipped a Studio beta feature, Scene Generation, that creates an editable scene of models, textures, and terrain from a source image, a text prompt, or both, reachable via the Assistant `/generate_scene` command or a right-click "Generate > Scene" menu option.
**What research it translates:** The feature builds on Roblox's "Cube" 3D foundation-model research (arXiv:2503.15475, "Cube: A Roblox View of 3D Intelligence"), which describes text-to-scene generation via 3D shape tokenization; Roblox states the generated scene elements are "procedural models" that can be edited manually or through Assistant/MCP-connected agents.
**Practical significance:** Roblox states the tool lets creators "fill a blank canvas quickly" to prototype and test ideas, with each generation taking "between 2-3 minutes"; the company frames it as a starting point requiring manual editing, not a finished scene.
**Engineering details:** Access is via Studio's Assistant chat (`/generate_scene`, currently limited to a single image input) or a right-click viewport menu (supports multiple images); generated content is a mix of procedural models and meshes that can be individually repositioned, resized, and edited; a Generate tab in Studio's ribbon and expanded multi-image/Assistant parity are planned.
