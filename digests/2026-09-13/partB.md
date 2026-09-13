# Part B — Research → Product
Window: last 90 days (2026-06-15 to 2026-09-13). Qualifying products: 12 (12 new, 0 previously reported, 3 flagged). Announced-only: 4. Open releases moved to Part A: 1. Retrieval: GitHub Releases API (rate-limited after 41 repo queries; NVIDIA orgs only, no qualifying leads) plus per-company newsroom/docs sweep via web search and fetch of primary pages. No prior `product_seen.json`, so every item is New.

---
## NVIDIA DLSS 5 with 3D-Guided Neural Rendering (in NBA 2K27)
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-09-03 · **New**
- **Surface:** shipped game feature (driver + game integration)
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/nba-2k27-dlss-5-3d-guided-neural-rendering-geforce-game-ready-driver/
- **Underlying research:** no traceable paper (NVIDIA's post cites none)
- **Availability:** GeForce RTX 50 Series GPUs only at launch; requires GeForce Game Ready Driver 616.64 WHQL; first and only title is NBA 2K27; no extra cost beyond the game and GPU.

**What shipped:** NVIDIA states "DLSS 5 is available now in the newly-released NBA 2K27" and that DLSS 5 introduces "3D-Guided Neural Rendering, infusing games with lifelike lighting and materials using advanced artist-guided AI models." It ships alongside Game Ready Driver 616.64.
**What research it translates:** NVIDIA describes an AI model that takes per-frame game colour and motion data and infers lighting and materials, positioned as the successor to the upscaling and frame-generation stages of earlier DLSS versions. No paper is cited.
**Practical significance:** Owners of RTX 50 Series hardware and NBA 2K27 get AI-modified lighting and materials (skin, hair, contact shadows per NVIDIA's description) in a shipped title today. NVIDIA reports NBA 2K27 reaching "370 FPS at 4K at Ultra Settings, with ray tracing, on a GeForce RTX 5090" with DLSS enabled.
**Engineering details:** Delivered through the GeForce driver and a game-side integration; inputs are the game's rendered colour and motion vectors; RTX 50 Series exclusive at launch.
**Limitation / caveats:** NVIDIA states RTX 40 Series support is planned but not available at launch. Only one game supports DLSS 5 as of the window's end (observed, not stated).

---
## NVIDIA DLSS 4.5 Ray Reconstruction, 2nd-generation transformer model (early access)
- **Company:** NVIDIA
- **Status:** Public beta/preview (NVIDIA App early access) · **Released:** 2026-08-25 · **New**
- **Surface:** app feature / driver
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/gamescom-2026-dlss-4-5-ray-reconstruction-release-announcements-trailers/
- **Underlying research:** no traceable paper
- **Availability:** Opt in via NVIDIA App (Settings > About > Early Access releases); requires GeForce Game Ready Driver 580.88 WHQL or newer; applicable to 30 games at time of writing (Alan Wake 2, Cyberpunk 2077, Portal with RTX, Indiana Jones and the Great Circle, Star Wars Outlaws among them). NVIDIA states "an official release will follow in September."

**What shipped:** NVIDIA states a "new 2nd generation transformer model" for DLSS Ray Reconstruction with "35% more compute capability" that "processes 20% more parameters, while maintaining similar performance to the previous model." It is available now as an early-access download.
**What research it translates:** An updated neural denoiser/reconstruction model for ray- and path-traced imagery in the DLSS Ray Reconstruction line. No paper is named.
**Practical significance:** Owners of RTX GPUs can apply the new model to 30 existing titles through the NVIDIA App without waiting for per-game patches.
**Engineering details:** Distributed via NVIDIA App override rather than game updates; driver 580.88 or newer required.
**Limitation / caveats:** Early-access status; NVIDIA gives only "September" for the official release and no numeric image-quality metrics. Whether the official release landed before 2026-09-13 was not confirmed from a primary source (observed, not stated).

---
## Autodesk 3ds Max 2027.2 — native 3D Gaussian Splat support
- **Company:** Autodesk — FLAG: not on the tracked list; comparable DCC vendor, included for the reader to judge
- **Status:** GA · **Released:** 2026-07-22 per trade press (CG Channel, 80.lv, CGPress); Autodesk's own pages are undated — FLAG · **New**
- **Surface:** studio tool (DCC application)
- **Primary source:** https://help.autodesk.com/cloudhelp/2027/ENU/3dsMax-WhatsNew/files/GUID-D11D1F34-C9FF-4981-AAE3-5A969986FCF4.html
- **Underlying research:** no traceable paper (Autodesk does not cite the 3DGS literature on the page)
- **Availability:** Included in the 3ds Max 2027.2 update for subscribers; Arnold for 3ds Max (MAXtoA) 5.9.3.0 bundled.

**What shipped:** Autodesk states "New 3D Gaussian Splat (3DGS) support in 3ds Max 2027.2 provides fast rendering, simple editing, and hyper-accurate output," with a new point object type and point-data modifiers to "edit 3DGS data or create point data from scratch." Arnold "now works with native 3ds Max 3DGS data."
**What research it translates:** Gaussian-splat radiance-field captures become a native, editable asset type in a mainstream DCC tool.
**Practical significance:** 3ds Max users can import, edit with standard modifiers, and render splat captures in Arnold without third-party plugins, per Autodesk.
**Engineering details:** New Points object type and Point Instance modifier (also usable for render-time instancing); Arnold 5.9.3.0 adds 3DGS rendering, a Shader to RGBA node and denoiser updates. Trade coverage lists PLY, SPZ and LCC import formats; the Autodesk What's New page fetched does not list formats.
**Limitation / caveats:** Release date not stated on Autodesk's own documentation pages (observed, not stated). No performance numbers given for splat rendering.

---
## Adobe Substance 3D Painter 12.1, Designer 16 and Sampler update (OpenPBR)
- **Company:** Adobe
- **Status:** GA · **Released:** 2026-07-21 · **New**
- **Surface:** studio tool
- **Primary source:** https://blog.adobe.com/en/publish/2026/07/21/adobe-substance-3d-unveils-new-innovations-deliver-faster-workflows-openpbr-everywhere-digital-twins-scale
- **Underlying research:** no traceable paper
- **Availability:** Substance 3D Collection desktop apps; Adobe states it released its "production-proven OpenPBR implementation as open source on GitHub."

**What shipped:** Adobe states Painter 12.1 adds Skew Map Painting, Auto Rebake (rebakes only affected mesh portions), a Hard Surface Auto UV mode and OpenPBR support; Designer 16 adds a Shape Splatter v2 node, Signed Distance Field nodes, a 3D Viewer node and new displacement controls; Sampler adds Material Creation Templates.
**What research it translates:** Adoption of the open OpenPBR shading model across the texturing pipeline, plus procedural-geometry (SDF) authoring inside Designer.
**Practical significance:** Adobe states the Assets library now holds 23,516 assets and that "14,000+ materials, decals, and atlases are being converted to OpenPBR," giving artists a portable material standard across tools.
**Engineering details:** OpenPBR supported end to end from Sampler through Painter; SDF and 3D Viewer nodes in Designer 16; open-source OpenPBR implementation on GitHub.
**Limitation / caveats:** No generative (Firefly) 3D features are mentioned in this release (observed, not stated). Pricing and subscription terms are not stated in the post.

---
## Fortnite / UEFN v41.20 — Control Rig for Sidekicks, in-world UMG widgets, LLM-powered NPCs
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-07-16 (LLM NPC publishing exits Experimental 2026-07-30) · **New**
- **Surface:** shipped game / creator tool (UEFN)
- **Primary source:** https://dev.epicgames.com/documentation/fortnite/41-20-fortnite-ecosystem-updates-and-release-notes-in-fortnite
- **Underlying research:** no traceable paper
- **Availability:** Live for all UEFN creators; LLM-powered NPC islands publishable from 2026-07-30.

**What shipped:** Epic's release notes state Control Rig support for Sidekicks arrives with "three archetypes — Dog Large, Dog Small, and Cat Small" built on Epic's internal rig structures; creators can "drag your UMG User Widget from the content browser into the viewport to display your UI in the level"; and on July 30 LLM conversations "exit Experimental and you'll be able to publish islands with LLM-powered NPCs and characters."
**What research it translates:** Epic's internal animation-rig tooling exposed to creators, and an LLM dialogue system for NPCs moving from experimental to publishable status.
**Practical significance:** Epic states it provides "consistent voices and personas to 36 Fortnite characters when used as NPCs," so creators can ship voiced, LLM-driven NPCs without engine code.
**Engineering details:** Control Rig limited to the three archetypes at launch; in-world widgets keep existing UMG functionality including Verse fields and UI animations.
**Limitation / caveats:** Epic states 36 characters get voices "with more coming over time," so coverage is partial at launch.

---
## Roblox Build — mobile AI creation tab (public alpha, New Zealand)
- **Company:** Roblox
- **Status:** Public beta/preview (public alpha) · **Released:** 2026-07-28 (announced 2026-07-16) · **New**
- **Surface:** app feature
- **Primary source:** https://about.roblox.com/newsroom/2026/07/build-without-limits-on-roblox
- **Underlying research:** no traceable paper
- **Availability:** Roblox states select Build features "will be available in public alpha to users in New Zealand beginning July 28," for age-checked users 9 and older; published games playable globally by age-checked users 16 and older; wider rollout "over the coming months."

**What shipped:** Roblox states a mobile-first creation tab inside the Roblox app that uses its AI tools, including Cube, which "turns a prompt into game-ready objects, from simple props to vehicles that drive and weapons that shoot," and already-launched Procedural Models.
**What research it translates:** Roblox's in-house 3D generative model (Cube) applied to an on-device, agentic creation flow for non-Studio users.
**Practical significance:** Users in one region can build and publish playable experiences from a phone without Roblox Studio, per Roblox.
**Engineering details:** Age-gated (9+ to build, 16+ to publish); region-gated (New Zealand first).
**Limitation / caveats:** Roblox states a scene-generation model and playtesting, analytics and experiment agents are "coming soon" rather than included; the alpha is limited to one country.

---
## Upgraded PSSR in Doom: The Dark Ages on PS5 Pro (Free Update 4)
- **Company:** Sony Interactive Entertainment (platform feature; post authored by id Software's Billy Khan on the PlayStation Blog)
- **Status:** GA · **Released:** 2026-07-07 · **New**
- **Surface:** shipped game / console platform feature
- **Primary source:** https://blog.playstation.com/2026/06/24/upgraded-pssr-comes-to-doom-the-dark-ages-on-ps5-pro/
- **Underlying research:** no traceable paper
- **Availability:** PS5 Pro only; free update shipping with Doom: The Dark Ages | Revelations on 2026-07-07.

**What shipped:** The PlayStation Blog states the upgraded PlayStation Spectral Super Resolution (PSSR) ML upscaler is applied to Doom: The Dark Ages on PS5 Pro from the July 7 update.
**What research it translates:** id Software's Billy Khan writes that PSSR "uses information such as motion, depth, exposure and sub-pixel sampling" from the idTech renderer to reconstruct a higher-resolution frame. No paper or model name is given.
**Practical significance:** PS5 Pro owners of the game receive the new upscaler at no cost; the post presents it as a clarity improvement most visible in motion.
**Engineering details:** Runs on PS5 Pro's ML reconstruction hardware with engine-provided motion, depth and exposure buffers; PS5 Pro exclusive.
**Limitation / caveats:** The post states its comparison images should be read "less as a color-grading comparison and more as a clarity comparison"; no numeric quality or performance figures are given.

---
## 《逆水寒：新世界》 (Justice Online: New World) character rendering upgrade
- **Company:** NetEase
- **Status:** GA · **Released:** 2026-06-26 · **New**
- **Surface:** shipped game (live MMO update)
- **Primary source:** https://h.163.com/news/official/20260612/37231_1304115.html
- **Underlying research:** no traceable paper
- **Availability:** Delivered in the existing 逆水寒 client (China); free-to-play title.

**What shipped:** NetEase's official channel states the New World version brings "全新超精度面部模型" (a new ultra-high-precision facial model) with improved contours, texture and lighting, a lighting system where hair stays clear when backlit ("逆光也清晰、发丝会呼吸"), and a "立体进化" (3D evolution) of hair-strand and cloth dynamics.
**What research it translates:** An internal character-rendering and simulation pipeline overhaul; no method or paper is named.
**Practical significance:** Existing players receive the upgraded characters automatically with the 2026-06-26 patch.
**Engineering details:** NetEase states improvements across facial geometry, muscle definition, hair lighting and hair/cloth dynamics; no engine, middleware or hardware targets are disclosed.
**Limitation / caveats:** The source is a patch announcement, not a technical document; no performance or platform specifics (observed, not stated).

---
## AMD FSR SDK 2.3 — FSR Upscaling 4.1.1 on RDNA 3
- **Company:** AMD — FLAG: not on the tracked list; comparable GPU vendor, included for the reader to judge
- **Status:** GA · **Released:** 2026-06-24 · **New**
- **Surface:** SDK
- **Primary source:** https://gpuopen.com/learn/amd-fsr-sdk-2-3-blog/
- **Underlying research:** no traceable paper
- **Availability:** AMD states "AMD FSR SDK 2.3 binaries and limited source are now available on GitHub"; ML-based FSR Upscaling 4.1.1 now supports Radeon RX 7000 Series (RDNA 3) discrete GPUs.

**What shipped:** SDK bundling FSR Upscaling 4.1.1, FSR Frame Generation 4.0.1 and FSR Ray Regeneration 1.2.0, extending the ML upscaler from RDNA 4 to RDNA 3 cards.
**What research it translates:** AMD's machine-learning upscaling model family made available to a previous GPU generation.
**Practical significance:** AMD states RDNA 3 owners get "image quality that closely matches what is already available on" RDNA 4, once developers integrate the SDK.
**Engineering details:** Frame Generation and Ray Regeneration remain "AMD Radeon RX 9000 Series GPUs and above" with analytical fallbacks for older hardware; distributed as binaries plus limited source.
**Limitation / caveats:** Requires per-game integration by developers; AMD gives no numeric performance metrics; RDNA 2 not included.

---
## Unreal Engine 5.8 (MetaHuman Animator markerless capture, MetaHuman Collections, Mesh Terrain, MegaLights, MCP plugin)
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-06-17 · **New**
- **Surface:** engine
- **Primary source:** https://forums.unrealengine.com/t/unreal-engine-5-8-released/2729274 (Epic staff announcement; the unrealengine.com news page returned HTTP 403 to fetch)
- **Underlying research:** no traceable paper
- **Availability:** "Download now on the Epic Games Launcher, GitHub, or our Linux page"; standard UE licensing.

**What shipped:** Epic states "MetaHuman Animator now supports markerless motion capture, enabling full-body and facial performance capture using something as simple as a single webcam"; MetaHuman Collections for scalable crowds; Mesh Terrain, "a new 3D mesh-based landscape system"; MegaLights "now Production-Ready"; a new MCP plugin that "connects LLMs directly to Unreal Engine"; and Lumen Lite.
**What research it translates:** Markerless video-based performance capture for MetaHuman characters and a production-ready many-light renderer.
**Practical significance:** Developers can capture body and face animation from a single webcam and light scenes with large numbers of dynamic shadowed lights, per Epic. Epic states Lumen Lite is "up to twice as fast as Lumen High Quality."
**Engineering details:** Hotfix 5.8.1 followed on 2026-07-28 with "over 260 fixes and updates" per Epic staff; 5.8.2 followed later.
**Limitation / caveats:** Mesh Terrain and MetaHuman Collections are labelled experimental in Epic's announcement; markerless capture quality is not quantified.

---
## HappyOyster 1.0 (快乐生蚝 1.0) — real-time interactive world model
- **Company:** Alibaba (ATH Innovation Business Group) — FLAG: attribution comes from consistent trade coverage (GeekPark, IT之家, Leiphone) and the site is served from Alibaba's CDN; no Alibaba newsroom statement was found
- **Status:** Public beta/preview · **Released:** 2026-06-17 per GeekPark; date not shown on the product site — FLAG · **New**
- **Surface:** consumer web app
- **Primary source:** https://www.happyoyster.cn
- **Underlying research:** no traceable paper
- **Availability:** Web app with open registration and daily free credits per GeekPark's report; the product site states API access will open soon ("近期还会全面开放 API 接口").

**What shipped:** The product site describes "一款实时可交互的开放世界模型产品" (a real-time interactive open-world model product) with a 执导 (Directing) mode to steer a continuously evolving world by text, voice or image, and a 漫游 (Wandering) mode for first-person exploration.
**What research it translates:** Described as a natively multimodal world model with joint audio-video generation and long-horizon consistency; no architecture or paper is named on the site.
**Practical significance:** Anyone can register and generate an explorable world from a sentence or image, per the site; stated target uses are games, short drama, virtual companions and tourism.
**Engineering details:** Text, voice and image input; first-person navigation; synchronized audio-video output; API not yet live.
**Limitation / caveats:** No pricing, quota, region or hardware details on the site; company attribution and release date are not stated on the primary page (observed, not stated).

---
## NVIDIA ACE Game Agent SDK (beta) and ACE plugins for Unreal Engine 5
- **Company:** NVIDIA
- **Status:** GA (UE5 plugins) / Public beta (Game Agent SDK) · **Released:** 2026-06-16 · **New**
- **Surface:** SDK / engine plugin
- **Primary source:** https://developer.nvidia.com/blog/build-on-device-ai-companions-with-the-nvidia-ace-game-agent-sdk-and-unreal-engine-5-plugins/
- **Underlying research:** no traceable paper (the post references NVIDIA's open-source Kimodo motion project without an arXiv id; see Part A open releases)
- **Availability:** NVIDIA states "a new suite of NVIDIA ACE plugins is now available" for UE5 and that developers can "download the NVIDIA ACE Game Agent SDK in beta"; on-device inference.

**What shipped:** An on-device conversational-companion pipeline for games: ASR ("nemo-conformer-ctc-120m"), a "Qwen 3.5 4B model" for function calling, and the "Chatterbox Turbo 350M TTS model," packaged as UE5 plugins and an SDK.
**What research it translates:** NVIDIA's ACE digital-human stack repackaged around small open models for local NPC dialogue; NVIDIA also describes Kimodo as "an open source project for promptable, controllable human motion."
**Practical significance:** UE5 developers can add local, non-cloud voice-interactive companions today, per NVIDIA.
**Engineering details:** Referenced against Unreal Engine 5.7; components are swappable open models; hardware requirements are not stated in the post.
**Limitation / caveats:** The SDK itself is labelled beta; no latency or quality figures are given.

### Announced only (not yet usable)
- Unity 7 roadmap (early beta targeted December 2026) · Unity · 2026-07-21 · https://unity.com/news/unity-7-roadmap-revealed-at-unite-seoul
- Adreno Neural Fusion (AI rendering pipeline for an unreleased Snapdragon) · Qualcomm · 2026-09-02 · https://www.qualcomm.com/news/onq/2026/09/adreno-neural-fusion-ai-rendering
- Roblox scene-generation model and playtesting/analytics/experiment agents ("coming soon") · Roblox · 2026-07-16 · https://about.roblox.com/newsroom/2026/07/build-without-limits-on-roblox
- NVIDIA ACE in Aniimo ("early 2027") · NVIDIA · 2026-08-25 · https://www.nvidia.com/en-us/geforce/news/gamescom-2026-dlss-4-5-ray-reconstruction-release-announcements-trailers/

Near-misses: PUBG "Ally Duo" AI companion beta (Krafton, borderline company; time-limited beta 2026-06-17 to 07-01, not usable today; https://pubg.com/en/news/10179) · NVIDIA Omniverse Kit 110.3 (August 2026 maintenance release, no feature on the four topics) · visionOS 27 RealityKit Gaussian splatting (Apple; developer beta 2026-06-08 before window, GA 2026-09-14 after window) · NVIDIA Cosmos 3 (2026-06-01, before window; open weights) · ByteDance Seedance 2.5 API (2026-08-07; general video generation, off-topic) · Huawei-hosted MoWorld-3D (developer is untracked MoCore; Huawei provides compute only) · Kling (no in-window feature verified from a primary source) · Meta "Hologram" avatar calling (app teardown only, unverified) · AWS "open source 3D game asset generation" post (tutorial, not a product) · Xbox Gaming Copilot on console (trade press only, no Microsoft primary source) · Tencent MagicDawn NDGI and 代号Craft (announced 2026-05-27/28, before window) · Intel, Baidu, miHoYo, Microsoft, Google, Meta, Amazon, Apple, Ubisoft, EA: no verified in-window items on the four topics.
Verification: every item above was double-checked by fetching the listed primary URL in a second pass (date, company, tier and quoted claims confirmed); the two flagged dates and the HappyOyster attribution could not be confirmed from a primary page and are marked as such.
