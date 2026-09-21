# Part B — Research → Product
Window: last 90 days (2026-06-23 to 2026-09-21). Qualifying products: 25 (11 new, 14 previously reported, 1 flagged). Announced-only: 3. Open releases moved to Part A: 0.

---
## Fortnite / UEFN v42.20
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-09-17 · **New**
- **Surface:** Shipped game / engine dev tooling (Unreal Editor for Fortnite)
- **Primary source:** https://dev.epicgames.com/documentation/fortnite/42-20-fortnite-ecosystem-updates-and-release-notes?lang=en-US
- **Underlying research:** no traceable paper (gameplay/dev-tooling release)
- **Availability:** Free to UEFN/Fortnite creators, live now in Fortnite and Unreal Editor for Fortnite.

**What shipped (≤3 sentences):** UEFN v42.20 adds an Unarmed weapon system (punch/shove combat), a Channel API for custom voice/text communication channels, and in-editor UEFN Widget preview/interaction that lets creators test UI animations without starting a play session. This supersedes the previously tracked v41.20 release (2026-07-16).
**What research it translates (≤3 sentences):** This is a gameplay-mechanics and dev-tooling update, not a research-to-product translation.
**Practical significance (≤3 sentences):** Epic states the Widget preview speeds UI iteration by letting creators see animations and test interactions directly in-editor; the Channel API and Unarmed system expand the design space for custom Fortnite experiences.
**Engineering details (≤3 sentences):** Delivered through the standard UEFN/Fortnite release cadence; a companion v42.10 release (2026-09-03) separately added a Verse Social Synergy API and experimental Verse Camera transitions.
**Limitation / caveats (≤3 sentences):** No AI, 3D-generation, or character-animation features in this release per Epic's own release notes; included under the game-engines/dev-tooling topic area only.

---
## Isaac Sim 6.1 (General Availability)
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-09-15 · **New**
- **Surface:** Studio/simulation tool (robotics simulation platform, part of the Omniverse ecosystem)
- **Primary source:** https://forums.developer.nvidia.com/t/isaac-sim-6-1-general-availability/383280 (supporting: https://docs.isaacsim.omniverse.nvidia.com/latest/overview/release_notes.html)
- **Underlying research:** FoundationStereo: Zero-Shot Stereo Matching (arXiv:2501.09898, CVPR 2025 Best Paper nomination); BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects (arXiv:2303.14158, CVPR 2023) — both underlie the new "3D Object Reconstruction" pipeline. No paper found for the new Behavior Tree system.
- **Availability:** Free, GA download via Isaac Sim/Omniverse channels and GitHub (isaac-sim/IsaacSim); requires an NVIDIA RTX-class GPU.

**What shipped (≤3 sentences):** Isaac Sim 6.1 moved from early-developer preview to full general availability, adding a synthetic-data-generation example that uses NVIDIA's "3D Object Reconstruction" framework to turn stereo video of a real object into a textured USD asset. It also adds an Omniverse Behavior Tree system with state-machine/behavior-tree tutorials, a Newton 1.5.0 physics backend, ROS 2 Control support, and an expanded SimReady asset library (1,533 assets).
**What research it translates (≤3 sentences):** The 3D Object Reconstruction workflow chains NVIDIA's FoundationStereo (zero-shot stereo depth), SAM2 segmentation, and BundleSDF (neural 6-DoF pose tracking + implicit-surface reconstruction) into a pipeline that outputs a sim-ready textured mesh from stereo video — a direct productization of published NVIDIA computer-vision research.
**Practical significance (≤3 sentences):** NVIDIA states this lets developers digitize real-world objects into simulation-ready 3D assets without manual modeling, feeding Isaac Sim's synthetic-data pipelines for robot training. The behavior-tree tooling targets easier authoring of complex reactive manipulation tasks.
**Engineering details (≤3 sentences):** Outputs are standard USD/OBJ assets compatible with Isaac Sim, Omniverse and downstream game engines; the behavior-tree system ships via a new `omni.ai.behavior_tree_gen` Kit extension. The release also adds H.265 video compression and unified TF publishing to its ROS 2 bridge, plus new robot models.
**Limitation / caveats (≤3 sentences):** This is a developer/robotics simulation tool, not a consumer-facing product; the 3D reconstruction workflow is demonstrated via example/sample code rather than a one-click production feature. No independent benchmark of reconstruction quality/speed was found in the primary materials.

---
## GeForce Game Ready Driver — Path Tracing + DLSS 4.5 Ray Reconstruction in 007 First Light (plus day-one DLSS 4.5 in WARDOGS, Aniimo)
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-09-15 (driver announced 2026-09-09; WARDOGS 2026-09-10; Aniimo 2026-09-16) · **New**
- **Surface:** Shipped games (GeForce Game Ready Driver + in-game updates)
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/wardogs-aniimo-007-first-light-path-tracing-geforce-game-ready-driver/
- **Underlying research:** no traceable paper distinct from the already-tracked DLSS 4.5 Ray Reconstruction 2nd-gen transformer model — this is the same model rolling out to more games
- **Availability:** Free driver update via NVIDIA App/GeForce Experience; DLSS 4.5 features require GeForce RTX GPUs.

**What shipped (≤3 sentences):** NVIDIA shipped a Game Ready Driver adding full path tracing plus DLSS 4.5 Ray Reconstruction to the already-shipped game 007 First Light, alongside day-one DLSS 4.5 Super Resolution and Dynamic Multi Frame Generation in two newly released games, WARDOGS (early access) and Aniimo. This extends the DLSS 4.5 rollout already tracked from Gamescom 2026 to new titles and a new rendering mode in an existing game.
**What research it translates (≤3 sentences):** Same underlying DLSS 4.5 2nd-generation transformer Ray Reconstruction model already tracked from the 2026-08-25 Gamescom announcement; this entry documents its extension to path-traced lighting in a specific title rather than a new model.
**Practical significance (≤3 sentences):** NVIDIA states path tracing plus Ray Reconstruction improves lighting/reflection accuracy in 007 First Light; adoption in new day-one titles signals continuing developer uptake of the DLSS 4.5 stack.
**Engineering details (≤3 sentences):** Delivered via a standard GeForce Game Ready Driver plus in-game patches; NVIDIA Reflex is bundled in WARDOGS for latency reduction. Aniimo separately previews a future (early-2027, not yet shipped) NVIDIA ACE voice-driven creature-interaction feature.
**Limitation / caveats (≤3 sentences):** This is incremental game-by-game adoption of an already-tracked DLSS 4.5 feature rather than a new capability; included mainly because it adds a new rendering mode to an existing shipped game and two new day-one titles inside the window. The Aniimo ACE integration mentioned is announced-only and not counted here.

---
## RealityKit Gaussian Splatting support (visionOS 27)
- **Company:** Apple
- **Status:** GA · **Released:** 2026-09-14 · **New**
- **Surface:** Engine/rendering API (RealityKit, part of visionOS 27 / Xcode 27 SDK)
- **Primary source:** https://developer.apple.com/visionos/whats-new/ ; API reference https://developer.apple.com/documentation/realitykit/gaussiansplatcomponent
- **Underlying research:** "3D Gaussian Splatting for Real-Time Radiance Field Rendering" (Kerbl, Kopanas, Leimkühler, Drettakis, SIGGRAPH 2023, arXiv:2308.04079) — the general technique; not an Apple-authored paper, RealityKit is a renderer implementation for it
- **Availability:** Ships with visionOS 27 and Xcode 27; free SDK feature for all registered Apple developers, no waitlist. Previewed to developers at WWDC26 (June 2026, session 279) as beta, reached GA with the public visionOS 27 release.

**What shipped (≤3 sentences):** RealityKit in visionOS 27 gained native rendering support for 3D Gaussian Splats via a new `GaussianSplatComponent`/`GaussianSplatResource` API, so apps can place photorealistic scanned/reconstructed scenes and objects directly into spatial experiences. Apple defines no splat file format of its own — apps must parse formats like PLY, SPZ, or SOG and hand RealityKit the position/scale/rotation/opacity/spherical-harmonic buffers. Apple Maps uses this API in the visionOS 27 wave.
**What research it translates (≤3 sentences):** Gaussian Splatting (Kerbl et al. 2023) replaced NeRF-style volumetric rendering with an explicit, GPU-rasterizable point-based radiance-field representation that renders in real time. Apple's contribution is a production-grade, hardware-accelerated renderer for that representation inside a consumer spatial-computing SDK, not the underlying algorithm.
**Practical significance (≤3 sentences):** Apple states this "enables you to incorporate photorealistic scans of real-world objects into your virtual experiences," letting visionOS developers use captured/reconstructed 3D content without hand-rolling a splat renderer. It lowers the bar for shipping consumer apps built on 3D-reconstructed content on Vision Pro.
**Engineering details (≤3 sentences):** New APIs: `GaussianSplatResource`, `GaussianSplatResource.BufferResource`, `GaussianSplatComponent`. Ships as part of RealityKit in visionOS 27/Xcode 27; also touches Reality Composer Pro 3 tooling. Runs on Apple Vision Pro (M2 and M5 models).
**Limitation / caveats (≤3 sentences):** No first-party splat file format or capture pipeline — developers must source/parse splat data themselves. The feature is visionOS-only per current documentation; no confirmation of iOS/macOS RealityKit parity in the release notes reviewed.

---
## Reality Composer Pro 3 — AI-assisted 3D asset generation ("Reality Composer Pro Assistant")
- **Company:** Apple
- **Status:** GA · **Released:** 2026-09-14 (previewed as beta from WWDC26, June 2026) · **New**
- **Surface:** Studio/authoring tool (standalone macOS app, no longer bundled inside Xcode)
- **Primary source:** https://developer.apple.com/reality-composer-pro/ ; https://developer.apple.com/documentation/realitycomposerpro/working-with-the-reality-composer-pro-assistant ; https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/
- **Underlying research:** no traceable paper — Apple has not disclosed the generative model(s) behind the Assistant's 3D object/material generation (Apple has published adjacent research, e.g. "DSplats: 3D Generation by Denoising Splats-Based Multiview Diffusion Models," but no confirmed link to this shipping feature)
- **Availability:** Free download for Apple developers, standalone app (previously bundled in Xcode). Requires macOS 26.5+. Builds content for visionOS and iOS apps.

**What shipped (≤3 sentences):** Reality Composer Pro 3 shipped as a standalone Mac app with a built-in "Reality Composer Pro Assistant" panel that takes natural-language prompts and generates 3D objects and materials directly inside the 3D scene editor, plus new node-based Animation Graph and Script Graph tools for character/interaction logic. Live Preview streams edits to a connected Vision Pro in real time.
**What research it translates (≤3 sentences):** It packages text-to-3D-asset generative AI as an in-editor authoring feature, following the broader industry shift toward prompt-driven 3D content creation. Apple frames it only as "generative intelligence to help with asset creation," without publishing technical details on the underlying model.
**Practical significance (≤3 sentences):** Apple states the tool is meant to "close the gap between idea and experience" for designers and engineers building spatial apps, letting non-specialists generate placeholder or usable 3D objects/materials from a prompt without leaving the editor.
**Engineering details (≤3 sentences):** Ships as its own app with deep Xcode 27 integration; adds Animation Graph (state-machine character animation), Script Graph (node-based interaction logic with live on-device preview), and Live Preview via Mac Virtual Display.
**Limitation / caveats (≤3 sentences):** Apple gives no detail on generation quality, mesh complexity limits, licensing/training-data provenance, or export fidelity of Assistant-generated assets. No public benchmark or model card has been published for the underlying generative model.

---
## Unity 6.2 (6000.6.0f1)
- **Company:** Unity
- **Status:** GA · **Released:** 2026-08-31 · **New**
- **Surface:** Game engine (Unity Editor, Supported Update release)
- **Primary source:** https://unity.com/releases/editor/whats-new/6000.6.0f1
- **Underlying research:** no traceable paper (engineering/tooling release)
- **Availability:** Free/paid tiers per standard Unity licensing; available now via Unity Hub as a Supported Update release for Unity 6.

**What shipped (≤3 sentences):** Unity 6.2 reached general availability, shipping Mesh LOD GPU Instancing, a Compute GPU Light Baker with hardware ray-tracing support, and World-Space UI rendering for UI Toolkit aimed at immersive XR/gaming scenes. It also adds a structured JSON logging/diagnostics framework, an enhanced Frame Debugger, and Physics2D buoyancy/wind features.
**What research it translates (≤3 sentences):** This is primarily an engineering/tooling release rather than a translation of a specific published research paper.
**Practical significance (≤3 sentences):** Unity frames this as improving runtime performance (GPU-driven Mesh LOD, light baking) and developer diagnostics for shipping teams; World-Space UI Toolkit directly targets XR/immersive game UI authoring.
**Engineering details (≤3 sentences):** Ships as a "Supported Update" (quarterly cadence) rather than an LTS; includes WebAssembly 64-bit support with Burst compilation and progressive asset loading for Web builds.
**Limitation / caveats (≤3 sentences):** Not an LTS release, so long-term support status differs from Unity 6 LTS versions; feature set is general engine tooling rather than AI/3D-generation specific.

---
## Omniverse Kit 110.3
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-08 (exact day not published in release notes) · **New**
- **Surface:** Studio/developer tool (Omniverse Kit SDK, underlies Omniverse apps and RTX tools)
- **Primary source:** https://docs.omniverse.nvidia.com/dev-guide/latest/release-notes/110_3_highlights.html
- **Underlying research:** no traceable paper (engineering/correctness release)
- **Availability:** Free via NVIDIA NGC/Omniverse distribution channels for Kit-based application developers.

**What shipped (≤3 sentences):** Kit 110.3 is a feature-and-stability release adding directional marquee viewport selection, fixing long-standing rendering artifacts (ghosting, incorrect specular/transmission), and delivering reliability improvements to physics simulation, the Fabric Scene Delegate, and the Replicator synthetic-data-generation annotator pipeline (including eliminating a ~36% throughput regression).
**What research it translates (≤3 sentences):** Primarily correctness/reliability engineering rather than new research productization.
**Practical significance (≤3 sentences):** NVIDIA frames this as improving reliability of synthetic-data-generation workflows used to train robotics/AV perception models, and fixing rendering-correctness issues that previously produced silently wrong output.
**Engineering details (≤3 sentences):** Adds `omni.usd.PickingMode.FULLY_ENCLOSED` for viewport selection and supports latlong-format backplates; fixes affect Fabric Scene Delegate instancing/transform behavior under scene partitioning.
**Limitation / caveats (≤3 sentences):** This is a maintenance/incremental release for SDK developers, not a consumer-visible feature launch; the exact release date was not published on the primary docs page (only "August 2026").

---
## Wan 3.0 (通义万相 3.0)
- **Company:** Alibaba (Tongyi/通义万相 team, distributed via Alibaba Cloud Bailian/Model Studio)
- **Status:** Public beta (公测) · **Released:** 2026-08-06 · **New**
- **Surface:** Consumer/creator app (Tongyi Wanxiang site, Qianwen Creation PC, Wanjing Yike, IF STUDIO, Duiyou; grayscale rollout in Qianwen App) + cloud API (Alibaba Cloud Bailian/Model Studio)
- **Primary source:** https://news.qq.com/rain/a/20260806A0E2YY00 (trade report quoting the official rollout; the official product hub at https://tongyi.aliyun.com/wan/ did not independently surface version-specific detail on direct fetch — treat pricing/date details as needing a secondary primary-source check before hard citation)
- **Underlying research:** "Wan: Open and Advanced Large-Scale Video Generative Models" (arXiv:2503.20314) — base Wan model family paper; no dedicated Wan 3.0 technical report found
- **Availability:** Public beta across Alibaba's own creator surfaces starting 2026-08-06; API pricing reported at ¥0.3/0.6/1.2 per second for 480p/720p/1080p, with full API access described as opening "in the coming weeks" after the beta start.

**What shipped (≤3 sentences):** Alibaba opened public beta testing for Wan 3.0, a video-generation model that stably generates single-shot continuous video up to 30 seconds and, for the first time in the Wan line, accepts document formats (doc/xls/ppt/pdf/md) as generation input alongside text, image, audio, and video. It rolled out simultaneously across Bailian, Tongyi Wanxiang's own site, Qianwen Creation PC, and several partner front-ends, with a gradual rollout inside the Qianwen app.
**What research it translates (≤3 sentences):** Wan 3.0 continues the Wan open video-generation family documented in the arXiv Wan technical report (2503.20314), though that paper predates 2.x/3.0-era features such as native audio sync and document-conditioned generation; no arXiv report specific to Wan 3.0 was found.
**Practical significance (≤3 sentences):** Alibaba positions Wan 3.0 for short-drama, film-preview, brand-ad, and product-promo use cases where longer, narratively coherent single takes matter, claiming improvements to character drift, scene jumping, and narrative fracture. Document-to-video input is pitched as letting non-specialist users generate video from a slide deck without writing prompts.
**Engineering details (≤3 sentences):** API pricing is tiered by resolution (¥0.3/0.6/1.2 per second for 480p/720p/1080p); weights, inference code, and local deployment were explicitly not published alongside the beta, so this is a hosted-only public beta, not an open-weights drop.
**Limitation / caveats (≤3 sentences):** This entry relies on a trade-press page quoting the official rollout because the primary tongyi.aliyun.com page did not surface version-specific copy on direct fetch. It is explicitly public beta, not GA, and weights/API are not fully open.

---
## Seedance 2.5
- **Company:** ByteDance (Seed team; served via Volcano Engine/BytePlus ARK and the Jimeng/Doubao consumer apps)
- **Status:** GA (consumer surface); API access listed "coming soon" at launch · **Released:** 2026-07-31 · **New**
- **Surface:** Consumer app (Jimeng/即梦, Doubao Pro) + cloud API (Volcano Engine ARK/BytePlus ModelArk)
- **Primary source:** https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
- **Underlying research:** "Seedance 2.0: Advancing Video Generation for World Complexity" (arXiv:2604.14148) — base architecture; no dedicated 2.5 paper found
- **Availability:** Live now on Jimeng web and Doubao Pro; API rollout via BytePlus ModelArk announced as imminent at launch.

**What shipped (≤3 sentences):** ByteDance's Seed team shipped Seedance 2.5, a video-generation model producing a single continuous 30-second clip (up from 15s in 2.0), accepting up to 30 images/10 video clips/10 audio clips as reference material in one pass, and adding timestamp-level regional editing of a generated clip. It went live on Jimeng and Doubao Pro on release, with API access to follow via BytePlus ModelArk.
**What research it translates (≤3 sentences):** It extends the unified multimodal audio-video joint-generation architecture from Seedance 2.0 (arXiv:2604.14148); the blog post attributes the duration and reference-budget gains to that base architecture rather than a new method, and no separate 2.5 technical report was found.
**Practical significance (≤3 sentences):** ByteDance states the model targets professional short-form production (ads, education, drama) needing multi-shot continuity and localized edits without full regeneration — its first consumer/API-facing model to push single-pass generation to a full 30 seconds with in-place region editing.
**Engineering details (≤3 sentences):** Reference budget is up to 30 images + 10 video clips + 10 audio clips per generation, with claimed multi-round extension for multi-minute output. Resolution was not specified in the primary blog post (third-party trackers report 720p).
**Limitation / caveats (≤3 sentences):** At launch the public API was not yet live ("coming soon"), so the fully productized cloud-API surface postdates this record. No dedicated Seedance 2.5 arXiv paper exists — architectural claims specific to 2.5 are ByteDance's own blog claims, unverified independently.

---
## ABot-World (ABot-World-0 / ABot-3DWorld-0)
- **Company:** Alibaba — AMAP/高德 CV Lab, a Gaode/Amap subsidiary team within Alibaba Group **(FLAG: borderline company attribution — subsidiary, a step removed from the "Alibaba" parent brand)**
- **Status:** Public preview (open test portal; gallery browsable without login, creating a new world requires login) · **Released:** 2026-07-16 · **New**
- **Surface:** Web app/interactive demo platform (test portal) + partially open weights/code
- **Primary source:** https://finance.yahoo.com/technology/ai/articles/alibabas-amap-unveils-abot-world-072100723.html (syndicated official release text); test portal at https://abot-world.amap.com
- **Underlying research:** "ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU" (arXiv/HF 2607.19191); "ABot-3DWorld-0: A Universal World Model to Explore Any 3D Space" (arXiv 2607.11673)
- **Availability:** Free test portal at abot-world.amap.com with a public "World Plaza" gallery of 120+ pre-made worlds browsable without login; creating a new world requires logging in. Partial weights/code mirrored on GitHub/Hugging Face; designed to run on a single desktop-class GPU.

**What shipped (≤3 sentences):** Amap (Alibaba's mapping subsidiary) shipped a public test portal for two interactive world-generation models — ABot-World-0 (video-based interactive worlds) and ABot-3DWorld-0 (3D-Gaussian-Splatting-based persistent spaces) — where visitors upload a reference image and generate an explorable "world" in real time, with rendering latency under 1.5 seconds per the product page. The portal includes a "spatial teleport" mechanic for jumping between generated 3D spaces.
**What research it translates (≤3 sentences):** The product operationalizes two arXiv papers from AMAP CV Lab: ABot-World-0, an action-conditioned video world model built on Alibaba's Wan2.2-TI2V and extended with a "LongForcing" training method for real-time, long-horizon closed-loop interaction; and ABot-3DWorld-0, which converts prompts into persistent 3D Gaussian-Splatting environments rather than flat video. Both papers were published mid-2026, shortly before this consumer-facing portal went live.
**Practical significance (≤3 sentences):** This is a rare case of an interactive "world model" (as opposed to plain text/image-to-video) reaching a public demo surface rather than staying a paper/checkpoint; Alibaba states it achieves "stable generation for over an hour without quality drop" on a single consumer GPU.
**Engineering details (≤3 sentences):** ABot-World-0 is built on Alibaba's Wan2.2-TI2V video model with an added action-conditioning mechanism; ABot-3DWorld-0 uses 3D Gaussian Splatting for persistent spatial representation. Weights/code are partially open on GitHub/Hugging Face alongside the hosted portal.
**Limitation / caveats (≤3 sentences):** This sits close to the "research demo" line — the Yahoo Finance syndication of the release itself characterizes it as a "research announcement with public access," not a fully commercial product, and there is no confirmed pricing/enterprise tier. Company attribution is a step removed from the parent brand most readers associate with "Alibaba" (it is Amap/Gaode's internal CV Lab).

---
## Animation Graphs — full release (Roblox Studio)
- **Company:** Roblox
- **Status:** GA · **Released:** 2026-07-15 · **New**
- **Surface:** Studio tool/engine feature (Roblox Studio, Avatar tab)
- **Primary source:** https://devforum.roblox.com/t/full-release-animation-graphs-create-complex-character-motion-visually/4739840
- **Underlying research:** no traceable paper — a conventional node-based animation blend-graph/state-machine system (comparable to Unity Animator or Unreal AnimGraph), not a published ML technique
- **Availability:** Free, built into Roblox Studio for all creators; works with live, published games (not just Studio testing) as of this release. No waitlist.

**What shipped (≤3 sentences):** Roblox moved Animation Graphs out of beta into full release, letting creators build and blend complex character motion visually via a node graph (Clip, Blend1D/2D, Select, Mask, Over, Add, Subtract) instead of hand-writing Luau scripting pipelines for animation state transitions. This release added live-game playback, real-time debugging, and network replication support for multiplayer games.
**What research it translates (≤3 sentences):** Not derived from a specific research paper; applies established game-engine animation-blending techniques inside Roblox's cross-platform engine, integrated with Roblox's "Adaptive Animation" retargeting system for custom humanoid rigs.
**Practical significance (≤3 sentences):** Roblox states the tool lets animators "work more independently" of engineers, and reports 280+ fixes/improvements shipped since the April 2026 beta — giving Roblox's creator base a professional-grade animation-blending workflow previously only available via bespoke scripting or third-party engines.
**Engineering details (≤3 sentences):** Accessible via the Avatar tab in Roblox Studio; exposes a runtime parameter system controllable via API for gameplay-driven transitions; supports custom humanoid rigs through Adaptive Animation integration; graphs now replicate over the network for multiplayer play.
**Limitation / caveats (≤3 sentences):** No inverse-kinematics or procedural-animation nodes yet (acknowledged by Roblox as a future roadmap item). Community reports noted remaining bugs around Blend2D coordinate constraints and localization at release.

---
### Previously reported (still in window)
- NVIDIA DLSS 5 with 3D-Guided Neural Rendering (in NBA 2K27) · NVIDIA · GA · Released 2026-09-03 · https://www.nvidia.com/en-us/geforce/news/nba-2k27-dlss-5-3d-guided-neural-rendering-geforce-game-ready-driver/
- 007 First Light — Path Tracing & DLSS 4.5 Ray Reconstruction Update · NVIDIA · GA · Released 2026-09-15 · https://www.nvidia.com/en-us/geforce/news/007-first-light-path-tracing-dlss-4-5-ray-reconstruction-update-out-now/
- HappyOyster 1.0 "Adventure" mode via Alibaba Cloud Model Studio Open API · Alibaba · GA · Released 2026-09-17 · https://help.aliyun.com/zh/model-studio/newly-released-models
- Roblox Scene Generator (prompt-to-scene for Build & Studio) · Roblox · Announced only · Released 2026-09-11 · https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play
- RDC 2026 roadmap items — NPC Dynamic Behavior, New Default Movement, Silhouette-preserving Layered Clothing · Roblox · Announced only · Released 2026-09-12 · https://devforum.roblox.com/t/rdc26-what-we-announced/4865880
- NVIDIA DLSS 4.5 Ray Reconstruction, 2nd-generation transformer model (early access) · NVIDIA · Public beta/preview · Released 2026-08-25 · https://www.nvidia.com/en-us/geforce/news/gamescom-2026-dlss-4-5-ray-reconstruction-release-announcements-trailers/
- Markerless Motion Capture (EA Create Capture) · Electronic Arts · GA (internal studio tool) · Released 2026-08-07 · https://www.ea.com/news/ea-markerless-motion-capture
- Roblox Build — mobile AI creation tab (public alpha, New Zealand) · Roblox · Public beta/preview · Released 2026-07-28 · https://about.roblox.com/newsroom/2026/07/build-without-limits-on-roblox
- Autodesk 3ds Max 2027.2 — native 3D Gaussian Splat support · Autodesk · GA · Released 2026-07-22 · https://help.autodesk.com/cloudhelp/2027/ENU/3dsMax-WhatsNew/files/GUID-D11D1F34-C9FF-4981-AAE3-5A969986FCF4.html
- Adobe Substance 3D Painter 12.1, Designer 16 and Sampler update (OpenPBR) · Adobe · GA · Released 2026-07-21 · https://blog.adobe.com/en/publish/2026/07/21/adobe-substance-3d-unveils-new-innovations-deliver-faster-workflows-openpbr-everywhere-digital-twins-scale
- Fortnite / UEFN v41.20 — Control Rig for Sidekicks, in-world UMG widgets, LLM-powered NPCs · Epic Games · GA · Released 2026-07-16 · https://dev.epicgames.com/documentation/fortnite/41-20-fortnite-ecosystem-updates-and-release-notes-in-fortnite
- Upgraded PSSR in Doom: The Dark Ages on PS5 Pro (Free Update 4) · Sony Interactive Entertainment · GA · Released 2026-07-07 · https://blog.playstation.com/2026/06/24/upgraded-pssr-comes-to-doom-the-dark-ages-on-ps5-pro/
- 《逆水寒：新世界》(Justice Online: New World) character rendering upgrade · NetEase · GA · Released 2026-06-26 · https://h.163.com/news/official/20260612/37231_1304115.html
- AMD FSR SDK 2.3 — FSR Upscaling 4.1.1 on RDNA 3 · AMD · GA · Released 2026-06-24 · https://gpuopen.com/learn/amd-fsr-sdk-2-3-blog/

### Announced only (not yet usable)
- Roblox "Prompt to Avatar" (text-to-compliant-avatar-mesh generator: R15+ rigs, layered clothing/modesty layers) · Roblox · announced 2026-09-11 at RDC 2026, planned for release "by the end of the year" · https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play
- NVIDIA ACE-powered voice creature interactions in Aniimo (locally-hosted LLM) · NVIDIA/game partner · mentioned 2026-09-09, integration slated "early 2027" · https://www.nvidia.com/en-us/geforce/news/wardogs-aniimo-007-first-light-path-tracing-geforce-game-ready-driver/
- Adreno Neural Fusion GPU (AI cores built into the GPU pipeline for the next flagship Snapdragon chip, with Unity/Unreal integration already built) · Qualcomm · detailed 2026-09-02, full unveil expected at Snapdragon Summit starting 2026-09-22 (just after window) · https://9to5google.com/2026/09/02/qualcomm-details-adreno-neural-fusion-gpu-for-next-snapdragon-chip/ (secondary source — no dated Qualcomm primary blog post found)

Near-misses: Sony PS5 Pro "Enhanced PSSR" defaulted-on in the Sept 16, 2026 firmware — excluded, the underlying PSSR 2.0 upscaler shipped March 2026, before the window; this is only a settings-default toggle. | Meta Horizon Worlds "Creator Assistant"/"Style Reference" — excluded, shipped ~April 2026, before the window. | Roblox "Procedural Models" full release — excluded, shipped 2026-05-18, before the window. | Roblox Mesh Generation (`generate_mesh` MCP tool) — excluded, shipped 2026-03-19, before the window. | Google Project Genie Street View expansion — excluded, shipped 2026-05-19/21, before the window. | EA Sports FC 27 "Attacking Spatial Awareness"/"Authentic Gameplay 2.0" — in-window shipped game update, but excluded as tactical/decision AI, not 3D/world-model/animation/engine-tooling as scoped. | AWS Gaussian-Splat reconstruction toolbox guidance — excluded, first published 2024, wraps third-party open-source models. | Microsoft Muse/WHAM Copilot Labs Quake II demo — excluded, launched April 2025, no in-window update found. | Ubisoft "NEO NPC"/La Forge Choreograph — excluded, remain research prototypes, no new in-window shipped surface. | EA SEED "Gigi" node-graph tool — excluded, no in-window release date confirmed. | PUBG Ally (KRAFTON co-playable AI teammate, NVIDIA ACE) — excluded, launched 2026-06-17, six days before the window. | Adobe Substance 3D Painter 12.1.3 — excluded, bugfix-only patch, no new feature surface. | RTX Remix DLSS 4.5 Ray Reconstruction support — excluded, same underlying model as the already-tracked Gamescom item, applied to the RTX Remix surface same day; treated as an extension, not a separate item. | Intel XeSS 3.0 SDK — excluded, released March 2026 (outside window); Intel also discontinued its official XeSS Unity plugin in April 2026. | An unverified third-party claim of an Adobe Firefly "Multi-Track Timeline"/"August 2026 Production Workflow" update — excluded, could not be corroborated on blog.adobe.com or helpx.adobe.com (which returned HTTP 403 during this pass — a coverage gap worth a follow-up). | Adobe Firefly's confirmed Aug 20, 2026 GA audio-tools update — excluded on-topic grounds (outside the tracker's 3D/world-model/animation/engine scope). | NVIDIA Cosmos "major release" claim — excluded, the only primary source found was an older 2025 press release resurfaced in search; no verified in-window release found. | Fab marketplace MetaHumans/Roblox-Minecraft asset-format access (Epic Games) — excluded, "plans to introduce" with no confirmed date and no dated primary Epic source located, reported by secondary sources only. | Codename Craft AI game-creation platform and MagicDawn NDGI open-sourcing (Tencent Games) — excluded, both announced 2026-05-27 at SPARK 2026, outside the 90-day window, and Codename Craft remains closed-beta ("首测 coming soon"). | HoYoverse's next MMO (Unreal Engine 5, realistic-fantasy aesthetic) — excluded, teaser reveal only, no ship date and no primary dated HoYoverse source located (secondary outlets only). | Seed3D 2.0 (ByteDance) — excluded, released 2026-04-23, outside the window. | Kling 3.0 Turbo (Kuaishou) — excluded, released 2026-06-17, six days before the window. | ABot-Earth0.5 (Alibaba/Amap city-scale world model) — excluded, announced 2026-06-08 (just outside window) and gated to an application-only beta, so would not clear the no-waitlist bar even if in-window. | Tencent Hunyuan 3D World Model 2.0 — excluded, released 2026-04-16, outside the window. | NetEase Justice Online Mobile's reported addition of Alibaba's Tongyi Wanxiang 2.2 to its in-game Creative Workshop — excluded, primary-source detail too thin (a single patch-note line) to confirm as a substantial new product surface.

Verification: every listed new item was checked against a primary source (company blog/newsroom, official docs/release notes, or official product/test-hub page) for release date, releasing company, on-topic content, and status tier; two of the eleven new items (RealityKit Gaussian Splatting page and the ABot-World test portal) were independently re-verified by this run via a second fetch/search pass before inclusion, with one source URL corrected and one availability claim ("no-login") corrected to reflect that browsing is login-free but creating a world requires login.
