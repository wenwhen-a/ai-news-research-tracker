# Part B — Research → Product: NVIDIA / AMD / Intel / Qualcomm / Adobe / Unity / Epic Games / Autodesk
Weekly sweep — window 2026-07-28 to 2026-10-26 — compiled 2026-10-26

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
(none found this sweep for these 8 companies)

### Monday recheck (Task 2) — material changes found
Three of the 26 rechecked items turned out to have been superseded by a new major version, which is reported above as a **New** item per the dedup rule (new version = new primary-source URL), not duplicated here as an Update:
- RTX Remix 1.5.2 (2026-09-14) → superseded by **RTX Remix 1.6.1** (2026-10-23, see above).
- Isaac Sim 6.1 GA (2026-09-21) → superseded by **Isaac Sim 6.2.0 GA** (2026-10-14, see above).
- Omniverse Kit 110.3 (2026-09-21) → superseded by **Omniverse Kit 110.4** (October 2026, see above).

All other rechecked items (NBA 2K27 DLSS 5, DLSS 4.5 Ray Reconstruction early-access page, 3ds Max 2027.2 Gaussian Splat, Adobe Substance 3D Jul-2026 update, Fortnite/UEFN v41.20 and v42.20, AMD FSR SDK 2.3, Unreal Engine 5.8 [only a 5.8.4 hotfix found — minor, not flagged], ACE Game Agent SDK [still Beta], 007 First Light update, GeForce driver page, Unity 6.2 [patched to 6000.6.7f1 — minor, not flagged], RTX Kit 2026.3 + ACE SDK, Control: Resonant, Qualcomm Adreno Neural Fusion SDK [page body could not be re-fetched this run — no update found elsewhere], Unity 7 [still "Preview launches in December / full release Q1" per its own page — no change beyond the already-logged Oct 13 alpha update], Witcher 3 Remastered, Gears of War: E-Day, AMD FSR plugin for UE 5.8, DLSS Frame Gen Performance Mode beta [still Beta], Unity Spark [still waitlist-only], AMD ASD Compiler) showed no material tier/version/availability change beyond what is already logged in `state/product_seen.json`.

Near-misses: 6 — AMD ADLX 2.0 (AI-agent GPU control SDK, Sep 16 2026 — off-topic, not a 3D/character-animation/world-model/game-engine feature); AMD FSR "Redstone" Radiance Caching (outside the 90-day window, originally posted Dec 2025); AMD GPUOpen research posts "Temporally Stable Generative Illumination" (Sep 9 2026) and "MiniDXNN v0.4.0" neural texture compression (Aug 13 2026) — both research/open-source code drops, Part A material rather than Part B; NVIDIA RTX Spark AI-PC hardware platform launch (Oct 7–16 2026) — a hardware platform enabling DLSS, not itself a 3D/engine software feature; Microsoft's Advanced Shader Delivery as enabled by NVIDIA/AMD drivers — Microsoft-authored shader-precompilation infrastructure, not an NVIDIA/AMD AI technique.
Verification: primary-source double-check done for all listed items.
