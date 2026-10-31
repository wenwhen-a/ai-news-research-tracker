**[B01] Roblox Studio — Prompt-to-Avatar (Generate Game Characters)**
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta, opt-in via File > Beta Features) · **Released:** 2026-10-29 · **New**
- **Surface:** studio tool (Avatar Setup panel in Roblox Studio; also exposed via Assistant and Studio MCP)
- **Primary source:** <https://devforum.roblox.com/t/studio-beta-generate-game-characters-with-prompt-to-avatar/4964945>
- **Underlying research:** arXiv 2503.15475, "Cube: A Roblox View of 3D Intelligence" (Roblox's own foundation-model paper for text-to-shape/text-to-scene 3D generation) — not explicitly cited in this post; Roblox's other text-to-3D tools (Cube 3D Generation, Procedural Models) are built on Cube, but this specific announcement names no underlying model
- **Availability:** Free, opt-in Studio Beta; staged rollout (staff noted full rollout took longer than a day); no stated region restriction

**What shipped:** Roblox shipped a beta Avatar Setup tool that generates a full Roblox-ready 3D character model from a text prompt: a creator describes a character, refines a generated 2D concept image, then builds the 3D model with a choice of built-in clothing or a bare body, static or dynamic head, and R15 or Advanced R15 rig.
**What research it translates:** Roblox's Cube foundation model (arXiv 2503.15475) describes a 3D shape tokenizer supporting text-to-shape and text-to-scene generation built to work with LLMs for 3D content creation; Prompt-to-Avatar is consistent with that text-to-3D generation lineage already used in Roblox's Cube 3D Generation and Scene Generation tools, though the devforum post does not name Cube directly.
**Practical significance:** Roblox states this lets a creator generate a usable, riggable in-game character from a written description instead of modeling or commissioning one, directly inside Studio; generation takes roughly 3-6 minutes (longer with a dynamic head).
