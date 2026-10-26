# Part B — Research → Product
Window: last 90 days (2026-07-28 to 2026-10-26). Qualifying products: 6 new, 1 updated. Announced-only: 0. Open releases moved to Part A: 0.

---
## RTX Remix 1.6.1 — DLSS 5 3D-Guided Neural Rendering in the modding toolkit
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-10-23 · **New**
- **Surface:** Studio tool / modding plugin (RTX Remix)
- **Primary source:** https://github.com/NVIDIAGameWorks/rtx-remix/releases/tag/remix-1.6.1
- **Underlying research:** no traceable paper
- **Availability:** Free download via GitHub; adds Windows-on-ARM (ARM64/ARM64EC) support with day-one Portal RTX, Half-Life 2 RTX Demo and RTX Remix for Minecraft (Beta); requires NVIDIA driver 616.92+; supersedes remix-1.5.2 (2026-06-16).

**What shipped (≤3 sentences):** NVIDIA shipped RTX Remix 1.6.1, bringing DLSS 5 with "3D-Guided Neural Rendering" and live artistic controls into the RTX Remix modding toolkit, alongside a beta Frame Generation performance preset, 5x/6x Multi Frame Generation, and ComfyUI 2.0 replacing the legacy AI texture/mesh generation tools. It also adds a headless Toolkit host with an MCP server for coding-agent-driven modding.
**What research it translates (≤3 sentences):** This retrofits the DLSS 5 3D-Guided Neural Rendering model NVIDIA introduced for NBA 2K27 in September 2026 into classic-game remastering workflows; the release notes cite no separate research paper.
**Practical significance (≤3 sentences):** NVIDIA's release notes state modders can apply the same neural-rendering, ray-reconstruction and AI-asset-generation pipeline used in modern DLSS 5 titles to decades-old D3D8/9 games remastered through RTX Remix, including on Windows-on-ARM devices from day one.
**Engineering details (≤3 sentences):** The release adds global/per-material model-selection controls (Preset A/B/C) for the frame-generation and neural-rendering models, a compact-GBuffer sparse-rendering path paired with DLSS Ray Reconstruction, and OpenEXR texture/skybox support without an 8-bit intermediate conversion.
**Limitation / caveats (≤3 sentences):** Minimum required driver jumps to 616.92 and legacy DLSS CNN presets are removed, breaking older configurations; the MCP server's default transport changes to Streamable HTTP, a breaking change for existing client setups; ComfyUI 2.0 is a breaking replacement for the legacy AI Tools pipeline.

---
## Call of Duty: Modern Warfare 4 — DLSS 4.5 at launch (plus Cyberpunk 2077 upgrade)
- **Company:** NVIDIA (feature shipped in Activision's Call of Duty: Modern Warfare 4)
- **Status:** GA · **Released:** 2026-10-23 (full launch) · **New**
- **Surface:** Shipped game (DLSS 4.5 feature)
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/dlss-4-5-cyberpunk-2077-planet-zoo-2-modern-warfare-4/
- **Underlying research:** no traceable paper
- **Availability:** GeForce RTX 40-series+ gets Frame Generation; RTX 50-series adds Dynamic Multi Frame Generation (up to 6x); same wave also brings an Oct 22 Cyberpunk 2077 update moving its Multi Frame Generation/Ray Reconstruction/Super Resolution to DLSS 4.5's second-generation transformer models, and adds DLSS 4.5 to Planet Zoo 2.

**What shipped (≤3 sentences):** NVIDIA states Call of Duty: Modern Warfare 4 ships with the full DLSS 4.5 feature set — Super Resolution, Frame Generation and Dynamic Multi Frame Generation — timed to its October 23 full launch, alongside a Cyberpunk 2077 update upgrading its existing DLSS integrations to DLSS 4.5.
**What research it translates (≤3 sentences):** This is a continued rollout of the DLSS 4.5 Ray Reconstruction second-generation transformer model NVIDIA previewed in early access in August 2026; no new research paper accompanies this game-adoption announcement.
**Practical significance (≤3 sentences):** NVIDIA frames Dynamic Multi Frame Generation (RTX 50-series) as a frame-rate boost for one of the year's highest-profile shooters at launch, giving the DLSS 4.5 model its broadest AAA test yet.
**Engineering details (≤3 sentences):** The accompanying Game Ready Driver also enables Microsoft's Advanced Shader Delivery for Call of Duty and Gears of War: E-Day, precompiling shaders server-side to reduce local shader-compilation stutter.
**Limitation / caveats (≤3 sentences):** Dynamic Multi Frame Generation is restricted to RTX 50-series GPUs; Advanced Shader Delivery is Microsoft's infrastructure feature (gated on DirectX 12/Windows 11/Agility SDK) that NVIDIA's driver merely enables, not an NVIDIA-authored AI technique.

---
## Isaac Sim 6.2.0 (General Availability)
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-10-14 · **New**
- **Surface:** Studio/developer tool (robotics & simulation platform)
- **Primary source:** https://github.com/isaac-sim/IsaacSim/releases/tag/v6.2.0
- **Underlying research:** no traceable paper
- **Availability:** Free GA release via GitHub/Omniverse channels; built on Omniverse Kit SDK 110.4.0; supersedes Isaac Sim 6.1 GA (2026-09-15). A parallel Isaac Sim 7.0.0 Alpha 1 pre-release also exists (2026-09-18).

**What shipped (≤3 sentences):** NVIDIA shipped Isaac Sim 6.2.0 as a full GA release, upgrading its Kit SDK to 110.4.0 and its Newton physics engine to 1.6.1 (with MuJoCo 3.12.0 and Warp 1.17.0). It adds automatic AI-model selection for synthetic action/event data generation and deformable-object synthetic data with 3D bounding boxes.
**What research it translates (≤3 sentences):** The release packages NVIDIA's Newton open physics engine and Replicator (1.13.38) synthetic-data-generation research into the shipped robotics-simulation product; no dedicated paper is cited for this specific version.
**Practical significance (≤3 sentences):** NVIDIA's release notes state the update targets robotics teams building sim-to-real training pipelines, with zero-copy live sensor-reading APIs and batched Newton actuator drives with gravity/Coriolis compensation.
**Engineering details (≤3 sentences):** The URDF exporter now supports UDIM texture export; RtxCamera can instantiate multiple camera prims from a path list or regex; `get_sensor_reading()` now returns an owned snapshot — a stated breaking API change from 6.1.
**Limitation / caveats (≤3 sentences):** The Cortex module was removed in this release; most changes are robotics/physics/tooling fixes and API breaks rather than new generative-3D or world-model capability.

---
## Omniverse Kit 110.4 — AI generative meshing from point clouds
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-10 · **New**
- **Surface:** Engine/SDK (Omniverse Kit, underlying Isaac Sim, USD Composer and other Omniverse apps)
- **Primary source:** https://docs.omniverse.nvidia.com/dev-guide/latest/release-notes/110_4_highlights.html
- **Underlying research:** no traceable paper
- **Availability:** GA, free; ships as the Kit SDK bundled into Isaac Sim 6.2.0 and other Omniverse applications; supersedes Kit 110.3 (2026-08-16).

**What shipped (≤3 sentences):** NVIDIA shipped Omniverse Kit 110.4 with a new "generative meshing" feature that uses AI models to turn point-cloud regions into textured 3D meshes, plus GPU-accelerated point-cloud-to-mesh conversion and DeepStream-powered GPU video textures (including RTSP streams, usable on Dome Lights).
**What research it translates (≤3 sentences):** This extends point-cloud-to-mesh AI reconstruction — in the same family as the "3D Object Reconstruction" framework NVIDIA introduced via Isaac Sim 6.1 for turning stereo video of real objects into textured USD assets — into a general Kit-level feature; the release notes name no specific paper.
**Practical significance (≤3 sentences):** NVIDIA states the feature lets developers convert scanned/point-cloud data directly into textured, simulation-ready meshes inside the same tool used across Isaac Sim, USD Composer and other Omniverse apps, aimed at robotics and digital-twin asset pipelines.
**Engineering details (≤3 sentences):** A new public Storage and Authentication API supports custom backends for the point-cloud workflow; OpenUSD is upgraded to 25.11; RTX Real-Time 2.0 scene partitioning now supports up to 32K indices (16,384 environments), and MDL materials now work inside USDZ packages.
**Limitation / caveats (≤3 sentences):** NVIDIA's release notes give no accuracy or quality benchmark for the generative-meshing AI models, nor whether the feature is usable outside Kit-based Omniverse apps; most other sections (CAD Converter, Fabric Scene Delegate) are bug fixes rather than new capability.

---
## Tencent Hunyuan 3D Cloud API — HY-3D 3.1 full pipeline (generation, rigging, retopology, texture, text-to-motion)
- **Company:** Tencent
- **Status:** GA · **Released:** on or before 2026-09-29 (doc "last updated" stamp; no explicit launch-announcement date found) · **New**
- **Surface:** cloud API (Tencent Cloud, under the Hunyuan product)
- **Primary source:** https://cloud.tencent.com/product/hunyuan (model catalog: https://cloud.tencent.com/document/product/1823/130082 ; HY-3D model doc: https://cloud.tencent.com/document/product/1823/137181 ; HY-3D-Motion doc: https://cloud.tencent.com/document/product/1823/137780)
- **Underlying research:** HY-3D-Motion corresponds to arXiv:2512.23464 "HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation" (comment links to the Tencent-Hunyuan GitHub org). The base hy-3d-3.0/3.1 generation line and the rigging/retopology/texture tools carry no cited paper on the product docs — "no traceable paper" for those specifically.
- **Availability:** Self-serve — any Tencent Cloud account can create an API key (sub-accounts need the `QcloudTokenhubFullAccess` policy); no invite or waitlist. No pricing is published on the docs pages or the general Hunyuan product page. Default concurrency: 3 simultaneous tasks for HY-3D-3.0/3.1 generation; 1 simultaneous task for HY-3D-Motion, HY-3D-Rigging, HY-3D-Retopology, HY-3D-Texture, HY-3D-UV, HY-3D-Component and HY-3D-Format.

**What shipped (≤3 sentences):** Tencent Cloud's Hunyuan product page now advertises "混元生3D 3.1模型" (model ID `hy-3d-3.1`), a higher-precision successor to `hy-3d-3.0`, alongside a full asset-pipeline suite of callable APIs: HY-3D-Motion (text-to-3D-character-motion, FBX output), HY-3D-Rigging (skeleton + skinning), HY-3D-Retopology, HY-3D-Texture, HY-3D-UV, HY-3D-Component (part splitting) and HY-3D-Format (format conversion). This is distinct from — and not previously tracked via — the consumer-facing 3d.hunyuan.tencent.com site, which separately advertises a "混元3D生成大模型2.5版本" creation platform.
**What research it translates (≤3 sentences):** HY-3D-Motion's text-to-motion capability lines up with Tencent's own "HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation" (arXiv:2512.23464), a flow-matching model for generating 3D human motion from text descriptions, tied to the Tencent-Hunyuan GitHub org. The base 3D-generation models continue Tencent's published Hunyuan3D 1.0/2.x line (e.g. arXiv:2411.02293), but no 3.0/3.1-specific paper is cited by the product.
**Practical significance (≤3 sentences):** Tencent's own docs describe an asynchronous submit/query job API (`/v1/api/3d/submit`, `/v1/api/3d/query`, task IDs valid 24 hours) that lets a developer go from a text or image prompt to a textured, rigged, retopologized, UV-unwrapped 3D asset — and now also generate skeletal character animation from a text prompt (1–12 seconds, default 5s) — entirely through Tencent Cloud rather than the Hunyuan 3D Studio web UI. HY-3D-Motion also supports retargeting generated motion onto an existing Hunyuan-generated model via a `retarget_file` parameter.
**Engineering details (≤3 sentences):** `hy-3d-3.1` drops the "LowPoly" generate_type option that `hy-3d-3.0` supports; both accept text (≤1024 UTF-8 chars), image, or up to ~6-angle multi-view input, with `face_count` tunable from 3,000 to 1,500,000 and output in obj/glb/stl/usdz/fbx. HY-3D-Motion's text prompt is capped at 128 characters, with optional `enable_mesh` (skinned FBX), `enable_rewrite` (prompt expansion) and `enable_duration_est` parameters.
**Limitation / caveats (≤3 sentences):** No press release or launch blog post was found for this suite — it was discovered via Tencent Cloud's own docs/model-catalog pages, so the exact public launch date is inferred from documentation "last updated" timestamps (2026-09-09 for Motion, 2026-09-29 for the base 3D doc) rather than a stated ship date. No pricing is published anywhere checked. Per-task concurrency is capped at 1 for every tool except base 3D generation (capped at 3), which limits throughput for production use.

---
## Wan 3.0 (通义万相 3.0) — General Availability confirmed
- **Company:** Alibaba
- **Status:** GA · **Released:** 2026-08-24 (GA announced; blog published 2026-08-27) · **Update**
- **Surface:** cloud API (Alibaba Cloud Model Studio) + consumer apps (Wanxiang website, Qianwen Creation PC client, Qianwen app)
- **Primary source:** https://www.alibabacloud.com/blog/wan3-0-at-general-availability-capabilities-benchmarks-pricing-and-the-workflows-it-changes_603505
- **Underlying research:** no traceable paper for Wan 3.0 specifically; the Wan line's earlier generations are documented in arXiv:2503.20314 ("Wan: Open and Advanced Large-Scale Video Generative Models"), not confirmed to cover 3.0.
- **Availability:** GA on Alibaba Cloud Model Studio and "supported international channels" (Alibaba states availability varies by region and may change). API pricing: $0.05/sec (480P), $0.10/sec (720P), $0.20/sec (1080P) — e.g. ~$1.50 for a 30-second 480P clip, ~$6.00 for a 30-second 1080P clip, before promotions.

**What shipped (≤3 sentences):** Update since 2026-09-21: Alibaba Cloud's own blog (published 2026-08-27, stating GA was announced 2026-08-24) confirms Wan 3.0 is now fully Generally Available with standard production pricing — a tier this tracker had recorded only as "Public beta/preview" (sourced from a news.qq.com article about the Aug 6 public-beta opening). The GA transition actually predates this tracker's first_seen date for the item, so this is a correction once a better primary source was found, not a change that happened this week.
**What research it translates (≤3 sentences):** No Wan 3.0-specific paper is cited in the GA post; it is presented as a direct successor to Wan2.7, continuing Alibaba's Wan video-generation line previously documented at arXiv:2503.20314.
**Practical significance (≤3 sentences):** Alibaba states Wan 3.0 natively generates up to 30 continuous seconds of video (versus Wan2.7's 2–15 seconds), with smart duration recommendation, video extension, and inputs spanning text, image, audio, video, documents (PDF/PPT/spreadsheets) and webpages. Alibaba also claims omni-reference and consistency for identity, voice and lip-sync, and carries forward Wan2.7's video-editing capability (altering visuals, plot or dialogue without full regeneration).
**Engineering details (≤3 sentences):** The post gives per-second resolution-tiered pricing (480P/720P/1080P) rather than a flat per-clip rate, with a time-limited launch discount mentioned but not quantified. Alibaba names no specific model ID or API endpoint in the post itself (the Model Studio catalog lists `wan3.0-video` / `wan3.0-video-prime` as the callable identifiers, both listed since 2026-08-06/08-20).
**Limitation / caveats (≤3 sentences):** Alibaba states audio texture and on-screen text rendering are "still maturing." No specific region list is given beyond "Model Studio and supported international channels." The GA announcement was found only via Alibaba Cloud's own blog, not the original news.qq.com tracking source, which had not been updated to reflect GA.

---
## Maya 2027.2 — MotionMaker "Bring Your Own Data" custom motion-model training
- **Company:** Autodesk (borderline — flagged per tracker rules)
- **Status:** GA · **Released:** 2026-07-22 (same release wave as 3ds Max 2027.2; Maya's own help pages give no explicit date) · **New**
- **Surface:** Studio tool (Maya character-animation feature)
- **Primary source:** https://help.autodesk.com/cloudhelp/2027/ENU/Maya-WhatsNew/files/GUID-49B18BA5-F029-4395-83B5-8B216DBE5914.htm
- **Underlying research:** no traceable paper
- **Availability:** Ships in Maya 2027.2, available to Maya subscribers now; MotionMaker is an existing Maya ML motion-generation tool, now extended with a custom-data training workflow.

**What shipped (≤3 sentences):** Autodesk added "Bring Your Own Data" (BYOD) to MotionMaker in Maya 2027.2, letting users train custom machine-learning motion-generation models from their own animation/mocap data, define custom "standard characters" for those models, and set a model frame rate that is stored with the trained model.
**What research it translates (≤3 sentences):** This productizes custom-data motion-model training inside Autodesk's existing MotionMaker character-animation tool; Autodesk's documentation names no specific research paper for the BYOD training method.
**Practical significance (≤3 sentences):** Autodesk states studios can now train and assign their own motion-style models — rather than relying only on Autodesk-provided styles — when assigning action styles to characters, aimed at making MotionMaker's generative locomotion usable with a studio's proprietary animation data.
**Engineering details (≤3 sentences):** The same 2027.2 update bundles Arnold for Maya 5.6.2, whose release notes state it adds native Gaussian Splat support and improved denoising, plus a USD for Maya 0.37 update with asset-path diagnostics.
**Limitation / caveats (≤3 sentences):** Autodesk's What's New page gives no benchmark, minimum-data-size requirement, or quality comparison for BYOD-trained models versus built-in MotionMaker styles, and does not state whether training runs locally or requires cloud compute.

### Announced only (not yet usable)
(none this week)

Near-misses: 17 — Western group (7): Google Project Genie (still an unreleased Labs research prototype, no product surface); two Amazon GameTech/Science posts (infra/ops, not 3D/animation/engine); a Microsoft Xbox/Godot sample (unrelated to AI/3D); EA's "Building EA's Next Chapter" corporate-strategy post (no named shipped tech); a cluster of new Roblox devforum posts (UGC avatar validation, Lua TTS asset creation, marketplace licensing — off-topic for 3D/world-models/character-animation/engines). NVIDIA/engines group (6): AMD ADLX 2.0 (AI-agent GPU control SDK, off-topic); AMD FSR "Redstone" Radiance Caching (outside the 90-day window); two AMD GPUOpen research posts (open-source code drops, Part A material); NVIDIA RTX Spark hardware platform launch (a hardware platform, not a software 3D/engine feature); Microsoft's Advanced Shader Delivery (Microsoft-authored infrastructure, not an NVIDIA/AMD AI technique). Chinese-tech group (4): Tencent-Hunyuan GitHub org open-weight drops (HY-World-2.0, Hunyuan3D-WorldClaw, Hunyuan3D-Buffalo 1.0, R-DMesh — Part A territory); several primary sources (Volcano Engine/Ark, Seed blog index, HoYoverse news, NetEase Fuxi, Kuaishou klingai.com changelog, Jianying/CapCut) are JS-rendered pages that returned no readable content this run; AMAP's own primary page for ABot-World could not be located (search budget exhausted); miHoYo/HoYoverse and Baidu yielded zero confirmable candidates this week (Baidu's research.baidu.com was under maintenance).
Verification: primary-source double-check done for every listed item (new and updated) across all three sweep groups; the Monday recheck of 50 previously-reported items across all groups found no further material changes beyond the Wan 3.0 tier correction above.
