# Part B — Research → Product
Window: last 90 days (2026-06-27 to 2026-09-25). Qualifying products: 31 (2 new, 29 previously reported, 0 flagged). Announced-only: 0 new. Open releases moved to Part A: 0.

---
## Roblox Studio — Texture Generation Tools, Segment Any Mesh, and Image Previews
- **Company:** Roblox
- **Status:** Public beta/preview (rolling out via Studio Assistant) · **Released:** 2026-09-23 · **New**
- **Surface:** studio tool (Roblox Studio Assistant)
- **Primary source:** https://devforum.roblox.com/t/introducing-new-texture-generation-tools-segment-any-mesh-and-image-previews/4890084
- **Underlying research:** no traceable paper
- **Availability:** Invoked from Roblox Studio's Assistant panel via ribbon buttons, right-click menus, or slash commands (`/generate_texture`, `/segment_mesh`, `/generate_procedural_model`, `/generate_mesh`); no region or plan restriction is stated, though community replies on the announcement thread report being denied access, suggesting a gradual rollout.

**What shipped (≤3 sentences):** Roblox added three Assistant-driven tools to Studio: texture generation to restyle one or more selected meshes, "Segment Any Mesh" to split an imported mesh into up to five named parts per operation, and image previews that surface four generated options (with optional reference-image input) for models made via `/generate_procedural_model` or `/generate_mesh`.

**What research it translates (≤3 sentences):** No traceable paper — the announcement describes the shipped commands and workflow without citing external research.

**Practical significance (≤3 sentences):** Roblox states the generated textures are "meant to be a starting point for you to continue to build on," framing the feature as a first-draft accelerator for creators building mesh variants and reskins rather than a finished-art pipeline.

**Engineering details (≤3 sentences):** Segmentation is capped at five named parts per invocation, requiring the command to be re-run on new parts for further splitting; texture generation and mesh generation can take a reference image as input by switching the Assistant's input mode from "Prompt" to "Image."

**Limitation / caveats (≤3 sentences):** The post does not state a rollout percentage or waitlist, but multiple creators replying on the thread report access being denied when trying the feature, indicating the rollout is not yet universal; Roblox does not disclose the underlying generative model.

---
## Roblox Studio Beta — Quad Support for EditableMesh APIs
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta, opt-in) · **Released:** 2026-09-23 · **New**
- **Surface:** engine / studio tool (EditableMesh API)
- **Primary source:** https://devforum.roblox.com/t/studio-beta-quad-support-for-editablemesh-apis/4890142
- **Underlying research:** no traceable paper
- **Availability:** Opt-in via Roblox Studio File > Beta Features; available to any creator who enables the beta flag, no waitlist stated.

**What shipped (≤3 sentences):** Roblox's EditableMesh API gained a new `AddFace()` method accepting either three or four vertex IDs, letting creators build four-sided quad faces directly instead of manually splitting every quad into two triangles.

**What research it translates (≤3 sentences):** No traceable paper — this is an engine API change, not a research-derived feature.

**Practical significance (≤3 sentences):** Roblox states quads can be mixed with triangles on the same mesh, giving "cleaner topology for quad-based workflows like box modeling," while existing EditableMesh operations (`GetFaceNormals()`, `SetFaceVertices()`) continue to work with the new face type.

**Engineering details (≤3 sentences):** Quads are automatically triangulated internally at render time; Roblox published example place files demonstrating subdivision-surface algorithms and interactive mesh editing built on the new API.

**Limitation / caveats (≤3 sentences):** The feature requires manually enabling Studio Beta (File > Beta Features); Roblox states "each quad counts as two triangles towards EditableMesh's existing 20,000-triangle limit," so it does not raise the effective mesh-complexity ceiling.

### Previously reported (still in window)
- NVIDIA DLSS 4.5 Ray Reconstruction + Dynamic Multi Frame Generation in Control: Resonant · NVIDIA · GA · Released 2026-09-24 · https://www.nvidia.com/en-us/geforce/news/control-resonant-path-tracing-dlss-4-5-ray-reconstruction/
- Roblox Creator Roadmap 2026 Fall Update (AI texture generation, scene generation, motion matching, animation graph improvements, root motion, Avatar FACS upgrade, unified agentic permissions) · Roblox · Announced only · Released 2026-09-22 · https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208
- NVIDIA RTX Kit 2026.3 + ACE SDK update (RTX Character Rendering 1.4, RTX Neural Shading 1.4, RTX Mega Geometry 2.0, ACE Nemotron Speech 3.5 Streaming ASR, Qwen3 TTS) · NVIDIA · GA · Released 2026-09-22 · https://developer.nvidia.com/blog/whats-new-for-game-developers-dlss-5-with-3d-guided-neural-rendering-nvidia-ace-updates-and-new-rtx-kit-capabilities/
- Roblox Studio — Tunable Collision Geometry (CollisionFidelity = Tunable) · Roblox · GA · Released 2026-09-17 · https://devforum.roblox.com/t/collision-geometry-workflow-improvements-tunable-precision-and-better-visualizations/4878198
- HappyOyster Directing (happyoyster-1.0-directing) — world-model Open API · Alibaba (ATH Innovation Business Group / Bailian) — borderline unit, flagged · Announced only · Released 2026-09-17 · https://help.aliyun.com/zh/model-studio/newly-released-models#happyoyster-1.0-directing
- HappyOyster Acting (happyoyster-1.0-acting) — character role-play/interaction model Open API · Alibaba (ATH Innovation Business Group / Bailian) — borderline unit, flagged · Announced only · Released 2026-09-17 · https://help.aliyun.com/zh/model-studio/newly-released-models#happyoyster-1.0-acting
- HappyOyster 1.0 "Adventure" mode (happyoyster-1.0-adventure) via Alibaba Cloud Model Studio Open API · Alibaba (ATH Innovation Business Group / Bailian) · GA · Released 2026-09-17 · https://help.aliyun.com/zh/model-studio/newly-released-models
- Fortnite / UEFN v42.20 · Epic Games · GA · Released 2026-09-17 · https://dev.epicgames.com/documentation/fortnite/42-20-fortnite-ecosystem-updates-and-release-notes?lang=en-US
- Isaac Sim 6.1 (General Availability) · NVIDIA · GA · Released 2026-09-15 · https://forums.developer.nvidia.com/t/isaac-sim-6-1-general-availability/383280
- GeForce Game Ready Driver — Path Tracing + DLSS 4.5 Ray Reconstruction in 007 First Light (plus WARDOGS, Aniimo) · NVIDIA · GA · Released 2026-09-15 · https://www.nvidia.com/en-us/geforce/news/wardogs-aniimo-007-first-light-path-tracing-geforce-game-ready-driver/
- 007 First Light — Path Tracing & DLSS 4.5 Ray Reconstruction Update · NVIDIA (feature shipped in IO Interactive's 007 First Light) · GA · Released 2026-09-15 · https://www.nvidia.com/en-us/geforce/news/007-first-light-path-tracing-dlss-4-5-ray-reconstruction-update-out-now/
- RealityKit Gaussian Splatting support (visionOS 27) · Apple · GA · Released 2026-09-14 · https://developer.apple.com/visionos/whats-new/
- Reality Composer Pro 3 — AI-assisted 3D asset generation ("Reality Composer Pro Assistant") · Apple · GA · Released 2026-09-14 · https://developer.apple.com/reality-composer-pro/
- RDC 2026 roadmap items — NPC Dynamic Behavior, New Default Movement, Silhouette-preserving Layered Clothing (character animation) · Roblox · Announced only · Released 2026-09-12 · https://devforum.roblox.com/t/rdc26-what-we-announced/4865880
- Roblox Scene Generator (prompt-to-scene for Build & Studio) · Roblox · Announced only · Released 2026-09-11 · https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play
- NVIDIA DLSS 5 with 3D-Guided Neural Rendering (in NBA 2K27) · NVIDIA · GA · Released 2026-09-03 · https://www.nvidia.com/en-us/geforce/news/nba-2k27-dlss-5-3d-guided-neural-rendering-geforce-game-ready-driver/
- Unity 6.2 (6000.6.0f1) · Unity · GA · Released 2026-08-31 · https://unity.com/releases/editor/whats-new/6000.6.0f1
- NVIDIA DLSS 4.5 Ray Reconstruction, 2nd-generation transformer model (early access) · NVIDIA · Public beta/preview (NVIDIA App early access) · Released 2026-08-25 · https://www.nvidia.com/en-us/geforce/news/gamescom-2026-dlss-4-5-ray-reconstruction-release-announcements-trailers/
- Omniverse Kit 110.3 · NVIDIA · GA · Released 2026-08-16 · https://docs.omniverse.nvidia.com/dev-guide/latest/release-notes/110_3_highlights.html
- Markerless Motion Capture (EA Create Capture) · Electronic Arts · GA (internal studio tool) · Released 2026-08-07 · https://www.ea.com/news/ea-markerless-motion-capture
- Wan 3.0 (通义万相 3.0) · Alibaba · Public beta/preview · Released 2026-08-06 · https://news.qq.com/rain/a/20260806A0E2YY00
- Seedance 2.5 · ByteDance · GA (consumer surface); API coming soon · Released 2026-07-31 · https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
- Roblox Build — mobile AI creation tab (public alpha, New Zealand) · Roblox · Public beta/preview (public alpha) · Released 2026-07-28 · https://about.roblox.com/newsroom/2026/07/build-without-limits-on-roblox
- Autodesk 3ds Max 2027.2 — native 3D Gaussian Splat support · Autodesk · GA · Released 2026-07-22 · https://help.autodesk.com/cloudhelp/2027/ENU/3dsMax-WhatsNew/files/GUID-D11D1F34-C9FF-4981-AAE3-5A969986FCF4.html
- Adobe Substance 3D Painter 12.1, Designer 16 and Sampler update (OpenPBR) · Adobe · GA · Released 2026-07-21 · https://blog.adobe.com/en/publish/2026/07/21/adobe-substance-3d-unveils-new-innovations-deliver-faster-workflows-openpbr-everywhere-digital-twins-scale
- Fortnite / UEFN v41.20 — Control Rig for Sidekicks, in-world UMG widgets, LLM-powered NPCs · Epic Games · GA · Released 2026-07-16 · https://dev.epicgames.com/documentation/fortnite/41-20-fortnite-ecosystem-updates-and-release-notes-in-fortnite
- ABot-World (ABot-World-0 / ABot-3DWorld-0) · Alibaba (AMAP/高德 CV Lab, subsidiary) · Public preview · Released 2026-07-16 · https://finance.yahoo.com/technology/ai/articles/alibabas-amap-unveils-abot-world-072100723.html
- Animation Graphs — full release (Roblox Studio) · Roblox · GA · Released 2026-07-15 · https://devforum.roblox.com/t/full-release-animation-graphs-create-complex-character-motion-visually/4739840
- Upgraded PSSR in Doom: The Dark Ages on PS5 Pro (Free Update 4) · Sony Interactive Entertainment (platform feature; post authored by id Software's Billy Khan on the PlayStation Blog) · GA · Released 2026-07-07 · https://blog.playstation.com/2026/06/24/upgraded-pssr-comes-to-doom-the-dark-ages-on-ps5-pro/

### Announced only (not yet usable)
(none new this run)

Near-misses: none identified beyond items already excluded in prior runs; no new "announced only" or academic-adjacent leads surfaced this run's checks.

Verification: Light check (non-Monday) of 10 primary surfaces — NVIDIA developer blog, GeForce news, Unreal Engine news, Unity blog, Roblox newsroom/devforum, Adobe blog, Tencent Hunyuan, ByteDance Seed/Volcano Engine, Alibaba Cloud Model Studio, Kling AI, PlayStation Blog — for items dated 2026-09-18 to 2026-09-25 on the four tracked topics. Coverage gaps: unrealengine.com/en-US/news returned HTTP 403 and blog.adobe.com's topic page returned HTTP 404 in this environment, so those two surfaces could not be checked directly this run (no substitute source was used in their place). The two new Roblox items were verified against their devforum primary-source pages (publish date, feature description, availability caveats). Items already in state/product_seen.json were not re-verified per the incremental rule.
