# Part B — Research → Product
Window: last 90 days (2026-06-26 to 2026-09-24). Qualifying products: 30 (1 new, 29 previously reported, 0 flagged). Announced-only: 0 new. Open releases moved to Part A: 0.

---
## NVIDIA DLSS 4.5 Ray Reconstruction + Dynamic Multi Frame Generation in Control: Resonant
- **Company:** NVIDIA (feature shipped in Remedy Entertainment's Control: Resonant, built on Remedy's Northlight Engine)
- **Status:** GA · **Released:** 2026-09-24 · **New**
- **Surface:** shipped game (GeForce RTX PCs/laptops and GeForce NOW)
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/control-resonant-path-tracing-dlss-4-5-ray-reconstruction/
- **Underlying research:** no traceable paper (DLSS 4.5 Ray Reconstruction's "2nd generation transformer model" was previously reported as an NVIDIA App early-access feature on 2026-08-25; this entry is its first integration into a specific shipped title)
- **Availability:** GeForce RTX PCs/laptops and GeForce NOW, available at Control: Resonant's launch (2026-09-24, 7am PT), via a dedicated "CONTROL Resonant" GeForce Game Ready Driver

**What shipped (≤3 sentences):** NVIDIA states Control: Resonant launches September 24, 2026 with the full DLSS 4.5 feature set — Ray Reconstruction (neural-network denoising), Dynamic Multi Frame Generation (up to 6X), and path-traced direct/indirect illumination and reflections — on GeForce RTX PCs/laptops and GeForce NOW, alongside a dedicated Game Ready Driver.

**What research it translates (≤3 sentences):** This ships the DLSS 4.5 Ray Reconstruction 2nd-generation transformer model — already tracked as an NVIDIA App early-access release on 2026-08-25 — into a specific title for the first time; NVIDIA's post discloses no new model research.

**Practical significance (≤3 sentences):** NVIDIA reports (its own benchmarks, Ultra preset with path tracing) 4K performance of 320 FPS on RTX 5090 and 220 FPS on RTX 5080; 1440p of 380 FPS on RTX 5090 and 240 FPS on RTX 5070 Ti; 1080p of 480 FPS on RTX 5090 and 215 FPS on RTX 5060 Ti.

**Engineering details (≤3 sentences):** Built on Remedy's proprietary Northlight Engine; supports 3840×2160, 2560×1440, and 1920×1080 desktop resolutions plus 2560×1600 for laptops; ships alongside a dedicated Game Ready Driver available at launch.

**Limitation / caveats (≤3 sentences):** NVIDIA's post does not state minimum GPU requirements beyond the RTX 50-series cards it benchmarks; all performance figures are NVIDIA's own benchmarks, not independently verified.

### Previously reported (still in window)
- NVIDIA RTX Kit 2026.3 + ACE SDK update (RTX Character Rendering 1.4, RTX Neural Shading 1.4, RTX Mega Geometry 2.0, ACE Nemotron Speech 3.5 Streaming ASR, Qwen3 TTS) · NVIDIA · GA · Released 2026-09-22 · https://developer.nvidia.com/blog/whats-new-for-game-developers-dlss-5-with-3d-guided-neural-rendering-nvidia-ace-updates-and-new-rtx-kit-capabilities/
- Roblox Creator Roadmap 2026 Fall Update (AI texture generation, scene generation, motion matching, animation graph improvements, root motion, Avatar FACS upgrade, unified agentic permissions) · Roblox · Announced only · Released 2026-09-22 · https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208
- HappyOyster 1.0 "Adventure" mode (happyoyster-1.0-adventure) via Alibaba Cloud Model Studio Open API · Alibaba (ATH Innovation Business Group / Bailian) · GA · Released 2026-09-17 · https://help.aliyun.com/zh/model-studio/newly-released-models
- Fortnite / UEFN v42.20 · Epic Games · GA · Released 2026-09-17 · https://dev.epicgames.com/documentation/fortnite/42-20-fortnite-ecosystem-updates-and-release-notes?lang=en-US
- Roblox Studio — Tunable Collision Geometry (CollisionFidelity = Tunable) · Roblox · GA · Released 2026-09-17 · https://devforum.roblox.com/t/collision-geometry-workflow-improvements-tunable-precision-and-better-visualizations/4878198
- HappyOyster Directing (happyoyster-1.0-directing) — world-model Open API · Alibaba (ATH Innovation Business Group / Bailian) — borderline unit, flagged · Announced only · Released 2026-09-17 · https://help.aliyun.com/zh/model-studio/newly-released-models#happyoyster-1.0-directing
- HappyOyster Acting (happyoyster-1.0-acting) — character role-play/interaction model Open API · Alibaba (ATH Innovation Business Group / Bailian) — borderline unit, flagged · Announced only · Released 2026-09-17 · https://help.aliyun.com/zh/model-studio/newly-released-models#happyoyster-1.0-acting
- 007 First Light — Path Tracing & DLSS 4.5 Ray Reconstruction Update · NVIDIA (feature shipped in IO Interactive's 007 First Light) · GA · Released 2026-09-15 · https://www.nvidia.com/en-us/geforce/news/007-first-light-path-tracing-dlss-4-5-ray-reconstruction-update-out-now/
- Isaac Sim 6.1 (General Availability) · NVIDIA · GA · Released 2026-09-15 · https://forums.developer.nvidia.com/t/isaac-sim-6-1-general-availability/383280
- GeForce Game Ready Driver — Path Tracing + DLSS 4.5 Ray Reconstruction in 007 First Light (plus WARDOGS, Aniimo) · NVIDIA · GA · Released 2026-09-15 · https://www.nvidia.com/en-us/geforce/news/wardogs-aniimo-007-first-light-path-tracing-geforce-game-ready-driver/
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
- 《逆水寒：新世界》(Justice Online: New World) character rendering upgrade · NetEase · GA · Released 2026-06-26 · https://h.163.com/news/official/20260612/37231_1304115.html

### Announced only (not yet usable)
(none new this run)

Near-misses: Kling AI release notes page (kling.ai / kling.ai) lists "Cinema-Grade Native 4K", "Team Features", and "Video 3.0 Motion Control" updates, but the page renders no publish dates in this environment, so recency could not be verified from the primary source — omitted rather than guessed. Adobe's 2026-09-23 Topaz Labs acquisition announcement (AI video/image enhancement) is outside the tracker's four topics (3D, world models, character animation, game engines) — not included.

Verification: Light check (non-Monday) of 10 primary surfaces — NVIDIA developer blog, GeForce news, Unreal Engine news, Unity blog, Roblox newsroom, Adobe blog, Tencent Hunyuan, ByteDance Seed, Alibaba Cloud blog, Kling AI, PlayStation Blog — for items dated 2026-09-17 to 2026-09-24 on the four tracked topics. The one new item (Control: Resonant DLSS 4.5) was double-verified against its NVIDIA primary source (publish date, features, platforms, benchmarks, engine, driver all confirmed present on the fetched page). Items already in state/product_seen.json were not re-verified per the incremental rule.
