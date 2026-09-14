# Part B — Research → Product
Window: last 90 days (2026-06-16 to 2026-09-14). Qualifying products: 15 (3 new, 12 previously reported, 0 flagged). Announced-only: 4. Open releases moved to Part A: 0.

---
## Wan3.0-Video / Wan3.0-Video-Prime (万相3.0)
- **Company:** Alibaba (Tongyi Wanxiang / Bailian)
- **Status:** GA · **Released:** 2026-08-06 (wan3.0-video), 2026-08-20 (wan3.0-video-prime) · **New**
- **Surface:** Cloud API (Alibaba Cloud Model Studio / Bailian model catalog)
- **Primary source:** https://help.aliyun.com/zh/model-studio/newly-released-models
- **Underlying research:** arXiv:2503.20314, "Wan: Open and Advanced Large-Scale Video Generative Models" (Team Wan / Alibaba Tongyi Lab — foundational technical report for the Wan model family; no separate Wan3.0-specific paper found) — https://arxiv.org/abs/2503.20314
- **Availability:** Listed as production model IDs `wan3.0-video` and `wan3.0-video-prime` (fast/turbo variant) in Alibaba Cloud Model Studio's model catalog, China-North-2 (Beijing) region table; billed API access, not open-weights.

**What shipped (≤3 sentences):** Alibaba's Bailian model catalog added Wan3.0-Video, described as an "all-in-one" video generation model unifying reference-generation, editing, replication (复刻) and character-driving (驱动) into one model, with four-modality full reference input and up to 30-second video generation. A faster "Prime" variant matching the standard model's quality followed two weeks later with reduced end-to-end latency.
**What research it translates (≤3 sentences):** The Wan series originates from Alibaba Tongyi Lab's diffusion-transformer video foundation models described in the March 2025 "Wan" technical report (arXiv:2503.20314); Wan3.0 is a further, undocumented-in-public-paper iteration of that lineage that the vendor's own catalog entry credits with the "驱动" (character-driving/motion-transfer) capability previously associated with the separate Wan-Animate model line.
**Practical significance (≤3 sentences):** Alibaba's catalog copy states the model provides "生产级角色一致性保持" (production-grade character consistency) and "音画真实" (realistic audio-video sync), positioning it as a production tool rather than a demo. The catalog frames it as capable of parsing files, web pages and complex images as reference input for video generation.
**Engineering details (≤3 sentences):** Exposed as two API model IDs (`wan3.0-video`, `wan3.0-video-prime`) on Bailian; supports "four-modality" (四模态) reference input and video outputs up to 30 seconds. No separate architecture paper or parameter count is disclosed in the catalog entry.
**Limitation / caveats (≤3 sentences):** All detail comes from a one-paragraph catalog blurb (no dedicated product/model page could be reached — direct doc-page URL guesses returned soft-404s); pricing, exact latency figures, and international availability are not stated in the source. The "character animation" framing rests on the catalog's own "驱动"/"角色一致性" wording rather than a dedicated animation-product page.

---
## Markerless Motion Capture (EA Create Capture)
- **Company:** Electronic Arts
- **Status:** GA (internal studio tool, in active production use) · **Released:** 2026-08-07 · **New**
- **Surface:** studio tool (motion-capture pipeline used to produce shipped/shipping games)
- **Primary source:** https://www.ea.com/news/ea-markerless-motion-capture
- **Underlying research:** no traceable paper
- **Availability:** Internal EA Create Capture tool (not externally licensed/sold). Uses high-resolution cameras + AI/computer-vision tracking, no marker suits, works indoors or outdoors, setup "within minutes" with fewer cameras than a traditional volume. No pricing, region, or third-party licensing information disclosed.

**What shipped (≤3 sentences):** EA's motion-capture group (EA Create Capture) has moved markerless mocap — tracking actor movement via cameras and AI/computer vision without marker suits or a dedicated volume — into production use for EA SPORTS FC (player movement/ball interactions) and EA SPORTS UFC (martial-arts technique capture). Senior Motion Capture Manager Nigel Nunn describes crews now able to "go to the people" and shoot indoors or outdoors with fewer cameras.
**What research it translates (≤3 sentences):** Markerless human pose/motion capture from multi-camera video is a well-established computer-vision research area; EA's post does not cite a specific paper or internal SEED publication, so the exact lineage of their pipeline is unconfirmed.
**Practical significance (≤3 sentences):** EA states the approach cuts setup time and location constraints compared to marker-suit volumes, letting the studio capture more, and more varied, motion data for FC and UFC titles. This is a production-pipeline efficiency claim from EA, not an independently verified benchmark.
**Engineering details (≤3 sentences):** Described as camera-based (no suits, no fixed studio requirement), usable both indoors and outdoors, with reduced camera-count requirements versus prior EA mocap setups. No specific frame rates, camera models, SDK, or software stack were disclosed in the source.
**Limitation / caveats (≤3 sentences):** This is an internal production tool, not a product or API available to external customers/developers — EA explicitly frames it as an "ongoing exploration" rather than a formal product launch, with no rollout timeline, pricing, or licensing given. No underlying research paper could be traced.

---
## RTX Remix 1.5
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-06-16 · **New**
- **Surface:** studio tool (free game-modding/remastering toolkit + runtime, distributed via GitHub/NVIDIA)
- **Primary source:** https://github.com/NVIDIAGameWorks/rtx-remix/releases/tag/remix-1.5.2 (official NVIDIAGameWorks repo; full changelog also at https://docs.omniverse.nvidia.com/kit/docs/rtx_remix/latest/docs/changelog/remix-releasenotes.html)
- **Underlying research:** no traceable paper (engineering release; builds on NVIDIA's existing RTX/neural-rendering stack, e.g. NRC)
- **Availability:** Free; Toolkit + Runtime components; Windows/D3D9 games; downloadable via GitHub releases and NVIDIA's RTX Remix site.

**What shipped (≤3 sentences):** NVIDIA shipped RTX Remix 1.5.2, adding "Remix Skills" — text-based context files that let AI coding agents act as collaborators to add features and bring previously-unsupported D3D9 titles into RTX Remix compatibility. The release also adds RTXIO-based texture packing/compression, GPU/CPU-generated smooth normals for D3D9 geometry, 32-bit index buffer support, GPU-driven instancer culling for scenes with millions of objects, translucent volumetric light transmission, and an overhauled particle system (2.0) with automatic migration.
**What research it translates (≤3 sentences):** This is primarily a shipping-tool update rather than a direct paper-to-product translation; it packages NVIDIA's existing neural radiance caching (NRC) and RTX path-tracing/neural-rendering pipeline into modding tooling. No specific arXiv paper underlies this release.
**Practical significance (≤3 sentences):** NVIDIA states RTXIO compression and packaging changes cut mod install sizes substantially (trade press reports up to ~37% smaller, and the Half-Life 2 RTX demo shrinking from roughly 80GB to 50GB). "Remix Skills" is pitched as lowering the technical barrier for community modders to add RTX path-traced remasters of classic D3D9 games without deep engine coding knowledge.
**Engineering details (≤3 sentences):** Runtime adds GPU/CPU smooth normals, 32-bit index buffers, PointInstancer GPU culling (~2M objects), a Unity Y-axis clip-space rendering fix, and CJK/Cyrillic UTF-8 text handling; DebugView statistics overhead was cut from ~42ms to ~1ms at 4K. Toolkit adds override flattening, an auto-save extension, a unified lights menu, and a rewritten Stage Manager for large scenes.
**Limitation / caveats (≤3 sentences):** Applies only to Direct3D 9 titles (the RTX Remix scope), not modern engines or later D3D versions. Remix itself is a free community-modding tool rather than a first-party studio product, and NVIDIA's own release notes give no case-study data on how widely "Remix Skills" is actually being used by modders yet.

### Previously reported (still in window)
- NVIDIA DLSS 5 with 3D-Guided Neural Rendering (in NBA 2K27) · NVIDIA · GA · Released 2026-09-03 · https://www.nvidia.com/en-us/geforce/news/nba-2k27-dlss-5-3d-guided-neural-rendering-geforce-game-ready-driver/
- NVIDIA DLSS 4.5 Ray Reconstruction, 2nd-generation transformer model (early access) · NVIDIA · Public beta/preview · Released 2026-08-25 · https://www.nvidia.com/en-us/geforce/news/gamescom-2026-dlss-4-5-ray-reconstruction-release-announcements-trailers/
- Roblox Build — mobile AI creation tab (public alpha, New Zealand) · Roblox · Public beta/preview · Released 2026-07-28 · https://about.roblox.com/newsroom/2026/07/build-without-limits-on-roblox
- Autodesk 3ds Max 2027.2 — native 3D Gaussian Splat support · Autodesk (borderline) · GA · Released 2026-07-22 · https://help.autodesk.com/cloudhelp/2027/ENU/3dsMax-WhatsNew/files/GUID-D11D1F34-C9FF-4981-AAE3-5A969986FCF4.html
- Adobe Substance 3D Painter 12.1, Designer 16 and Sampler update (OpenPBR) · Adobe · GA · Released 2026-07-21 · https://blog.adobe.com/en/publish/2026/07/21/adobe-substance-3d-unveils-new-innovations-deliver-faster-workflows-openpbr-everywhere-digital-twins-scale
- Fortnite / UEFN v41.20 — Control Rig for Sidekicks, in-world UMG widgets, LLM-powered NPCs · Epic Games · GA · Released 2026-07-16 · https://dev.epicgames.com/documentation/fortnite/41-20-fortnite-ecosystem-updates-and-release-notes-in-fortnite
- Upgraded PSSR in Doom: The Dark Ages on PS5 Pro (Free Update 4) · Sony Interactive Entertainment · GA · Released 2026-07-07 · https://blog.playstation.com/2026/06/24/upgraded-pssr-comes-to-doom-the-dark-ages-on-ps5-pro/
- 《逆水寒：新世界》 (Justice Online: New World) character rendering upgrade · NetEase · GA · Released 2026-06-26 · https://h.163.com/news/official/20260612/37231_1304115.html
- AMD FSR SDK 2.3 — FSR Upscaling 4.1.1 on RDNA 3 · AMD (borderline) · GA · Released 2026-06-24 · https://gpuopen.com/learn/amd-fsr-sdk-2-3-blog/
- Unreal Engine 5.8 (MetaHuman Animator markerless capture, MetaHuman Collections, Mesh Terrain, MegaLights, MCP plugin) · Epic Games · GA · Released 2026-06-17 · https://forums.unrealengine.com/t/unreal-engine-5-8-released/2729274
- HappyOyster 1.0 (快乐生蚝 1.0) — real-time interactive world model · Alibaba (ATH Innovation Business Group) · Public beta/preview · Released 2026-06-17 · https://www.happyoyster.cn
- NVIDIA ACE Game Agent SDK (beta) and ACE plugins for Unreal Engine 5 · NVIDIA · GA (UE5 plugins) / Public beta (Game Agent SDK) · Released 2026-06-16 · https://developer.nvidia.com/blog/build-on-device-ai-companions-with-the-nvidia-ace-game-agent-sdk-and-unreal-engine-5-plugins/

### Announced only (not yet usable)
- Roblox Scene Generator (prompt + reference image → full game scene/layout, in Build and Studio) · Roblox · 2026-09-11 · https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play (stated "launching later in 2026")
- Unity 7 ("zero rebuild" next-gen engine roadmap) · Unity · 2026-07-21 · announced at Unite Seoul 2026 (trade coverage: Inven Global; no shipping build or date given)
- Qualcomm Adreno Neural Fusion (dedicated AI "Matrix Cores" + 18MB HPM for on-GPU super resolution/frame generation; Unity and Unreal engine support already integrated at SDK level) · Qualcomm (borderline) · 2026-09-02 · https://www.qualcomm.com/news/onq/2026/09/adreno-neural-fusion-ai-rendering (tied to an unnamed "next generation of flagship platforms," no shipping chip named)
- NVIDIA ACE in Aniimo (locally-hosted fine-tuned Nemotron SLM for natural-language creature interaction) · NVIDIA/PlaySide (Aniimo) · announced 2026-09-09 for early-2027 launch · https://www.nvidia.com/en-us/geforce/news/wardogs-aniimo-007-first-light-path-tracing-geforce-game-ready-driver/

Near-misses:
- PS5 "Enhanced PSSR" default-on system update — trade press (MSN/Gaming Bible, PlayFront) reported a PS5 system software update (~v14.0) making the upgraded PSSR the default, sourced to "beta tester" leaks and expected "by end of September 2026"; no official blog.playstation.com post could be located confirming this, and it was not GA within the window, so it fails both the primary-source and GA/window requirements.
- DeepMind SIMA 2 / "Aura Guidance" in EVE Online (blog post 2026-08-21) — off-topic for Part B: game-playing/instruction-following agent research, not 3D generation, a world model, character animation, or a game engine product.
- Genie 3 / Project Genie (deepmind.google/models/genie/) — checked for a tier change; remains an "experimental research prototype" via Google Labs, unchanged status, so excluded per the technical-preview exclusion rule.
- Meta Horizon Worlds / Quest release notes, Meta.com/blog, Meta Hyperscape — no qualifying 3D/world-model/character-animation/engine product posts could be located dated in the window via the pages and searches available this session.
- Apple visionOS 26.6 (released ~2026-07-27) — release-note coverage found referenced Siri/tvOS/HomePod updates; no RealityKit or Object Capture feature specifics could be confirmed via primary Apple sources this session.
- Microsoft Muse/Xbox world-model, Azure AI Foundry 3D models, Ubisoft NEO NPC/Anvil-Snowdrop shipped-game features, Amazon/AWS GameTech 3D-AI products, Sony mocopi/Sony AI — no qualifying items in the window could be found or verified from primary sources this session.
- Roblox "Dream Racers" text-to-vehicle generation via Cube AI — only covered by trade press (GamesBeat, Sep 1 2026); no primary Roblox product/blog post found, and the underlying Cube 3D/4D foundation model itself predates the window.
- NVIDIA Cosmos 3 Edge (4B-parameter world model), launched 2026-07-16 — open-weights physical-AI/robotics model release with no games/creator-facing product surface identified; Part A (open-weights) territory, not Part B.
- Roblox "Studio MCP" multi-agent/AI-client improvements (2026-08-19) — a shipping feature, but generic AI-coding-agent tooling for Studio automation, not on-topic for this tracker's four areas.
- Adobe Premiere in-timeline AI video/sound generation and audio source separation (2026-09-08, IBC) — a real shipping Adobe product update, but video/audio generation rather than 3D/world-model/character-animation/game-engine — out of scope.
- Intel XeSS 3 SDK — GA in March 2026, outside the 90-day window; no new Intel XeSS/graphics news found dated within the window.
- HappyHorse (快乐小马) · Alibaba ATH Innovation Business Group — a companion video-generation platform to the already-reported HappyOyster; its Bailian-catalog snapshot is dated 2026-06-16, but the product's own self-description is generic text/image-to-video, not clearly framed as 3D/world-model/character-animation/game-engine, so topic-fit is unconfirmed.
- Tencent Design Miora (miora.design) · Tencent — mentioned in an Aug 5, 2026 PR Newswire release as a "creative studio" handling "3D and user interfaces" via AI agents, but the product's own (JS-rendered) site yielded no verifiable launch date, feature detail, or availability.
- Kling Video 3.0 / Video 3.0 Omni · Kuaishou — Kling's marketing page advertises an "All-New KlingAI 3.0 Series," and a `kling-v3-turbo-video-generation` variant appears in Alibaba's third-party Bailian catalog dated 2026-08-27, but Kling's own JS-rendered release log could not be verified for a primary-source launch date (may predate the window).
- Tencent Hunyuan3D (3d.hunyuan.tencent.com) · Tencent — the live product page states it is based on "Hunyuan 3D Generation Model version 2.5" (text-to-3D, image-to-3D, 3D animation, texture generation — squarely on-topic), but no page content indicated when version 2.5 shipped, so window verification could not be established.

Verification: every listed item was checked against a primary source (company blog/newsroom, official docs/release notes, or official GitHub release) for release date, releasing organization, on-topic fit, and status tier before inclusion; previously-reported items were matched by primary-source URL against `state/product_seen.json` rather than re-verified from scratch.

**Coverage-gap note (session-wide):** This week's sweep hit an exhausted WebSearch budget partway through the Western-companies pass and before the NVIDIA/Adobe/engines and Chinese-companies passes began, so research on those two passes relied on direct WebFetch/curl against primary URLs (plus a Bing News text-proxy for the Western pass). As a result: Microsoft, Amazon, Apple, Ubisoft, and Sony (Western pass) and ByteDance/TikTok, NetEase, Baidu, miHoYo/HoYoverse, and Kuaishou's own channels (China pass, mostly JS-rendered SPAs that return an empty shell to non-browser fetches) could not be systematically verified this run beyond the near-misses recorded above. Treat this run's "nothing new found" for those companies as low-confidence rather than a confirmed empty result; a re-run with working search access is recommended.
