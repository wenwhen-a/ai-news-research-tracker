# Part B — Research → Product
Window: last 90 days (2026-08-06 to 2026-11-04). Retrieval: daily light check (~10 primary surfaces: NVIDIA developer blog & GeForce news, Unreal Engine news, Unity blog, Roblox DevForum announcements, Adobe Substance 3D release notes, Tencent Hunyuan 3D, ByteDance Volcano Engine/Seed, Alibaba Cloud Model Studio release notes, Kuaishou Kling release notes, PlayStation Blog). Products: 1 new, 0 updated.

---
## Roblox Studio — Scene Generation (image/prompt → editable 3D scene)
- **Company:** Roblox
- **Status:** Public beta/preview · **Released:** 2026-10-30 · **New**
- **Surface:** studio tool
- **Primary source:** https://devforum.roblox.com/t/introducing-scene-generation-prototype-scenes-faster/4966611
- **Underlying research:** arXiv:2503.15475 "Cube: A Roblox View of 3D Intelligence" (describes text-to-scene generation via 3D shape tokenization)
- **Availability:** Studio beta; reachable via the Assistant `/generate_scene` command or a right-click viewport "Generate > Scene" menu option; no region/plan gating stated; not GA.

**What shipped (≤3 sentences):** Roblox shipped a Studio beta feature, Scene Generation, that creates an editable scene of models, textures, and terrain from a source image, a text prompt, or both, reachable via the Assistant `/generate_scene` command or a right-click "Generate > Scene" menu option.
**What research it translates (≤3 sentences):** The feature builds on Roblox's "Cube" 3D foundation-model research (arXiv:2503.15475, "Cube: A Roblox View of 3D Intelligence"), which describes text-to-scene generation via 3D shape tokenization; Roblox states the generated scene elements are "procedural models" that can be edited manually or through Assistant/MCP-connected agents.
**Practical significance (≤3 sentences):** Roblox states the tool lets creators "fill a blank canvas quickly" to prototype and test ideas, with each generation taking "between 2-3 minutes"; the company frames it as a starting point requiring manual editing, not a finished scene.
**Engineering details (≤3 sentences):** Access is via Studio's Assistant chat (`/generate_scene`, currently limited to a single image input) or a right-click viewport menu (supports multiple images); generated content is a mix of procedural models and meshes that can be individually repositioned, resized, and edited; a Generate tab in Studio's ribbon and expanded multi-image/Assistant parity are planned.
**Limitation / caveats (≤3 sentences):** Roblox states Assistant-based access "is currently limited to a single image; we'll bring this to parity soon," and that results depend on prompt detail (recommending creators state what to include and exclude). Developer-forum replies were mixed, with some creators criticizing Roblox's continued AI-feature focus (observed, not stated by Roblox).

### Announced only (not yet usable)
(none found this check)

Near-misses: NVIDIA developer blog (2026-11-02) referenced "Cosmos3-Nano" checkpoints and a `cosmos3:2.0.0` NIM container image inside a how-to/tutorial post on using the existing Cosmos platform; the post does not state a GA/beta/release date or status for these specific checkpoints/package, so it was not verifiable as a new product item and is noted here rather than listed. NVIDIA GeForce news items in the window (DLSS 5 3D-Guided Neural Rendering added to Hogwarts Legacy, War Thunder, Where Winds Meet; a Game Ready Driver extending the same feature) are additional games adopting an already-tracked feature, not qualifying updates per the tracker's own-change rule, so they were excluded.
Verification: Checked primary sources for NVIDIA (developer blog, GeForce news), Unreal Engine news (page blocked, HTTP 403), Unity blog, Roblox DevForum announcements, Adobe Substance 3D release notes (page blocked, HTTP 403), Tencent Hunyuan 3D site (no content returned), ByteDance Volcano Engine/Seed (web search only — results too inconsistent/undated to verify a primary-source hit in window), Alibaba Cloud Model Studio release notes, Kuaishou Kling release notes (no content returned), and PlayStation Blog, for items dated 2026-10-28 through 2026-11-04 on the four tracked topics (3D, world models, character animation, game engines). No material tier-change updates to previously tracked products were found and verified.
