## AMD ADLX 2.0 — AI Extensions for Graphics Control
- **Company:** AMD (FLAG: borderline)
- **Status:** GA · **Released:** 2026-09-16 · **New**
- **Surface:** studio/developer tool (SDK)
- **Primary source:** https://gpuopen.com/learn/adlx-2-0-extending-graphics-control-to-ai-agents-apps/
- **Underlying research:** no traceable paper
- **Availability:** Public download from AMD/GPUOpen (source code, docs, executables, examples); no stated license or platform restriction beyond "AMD graphics hardware and PCs." Not labeled "GA" explicitly but shipped with a working download.

**What shipped (≤3 sentences):** AMD released ADLX 2.0, an update to its Device Library eXtra SDK, adding an "AI Extensions" framework so AI agents and agentic apps can read live GPU telemetry, query capabilities, and change supported settings. It ships with Python bindings and Model Context Protocol (MCP) servers for direct agent integration.
**What research it translates (≤3 sentences):** No underlying academic paper; this is an engineering SDK response to the broader trend of agentic/MCP-based tool use rather than a published research result.
**Practical significance (≤3 sentences):** Lets developers build AI agents/copilots that can monitor and tune AMD GPU settings programmatically (e.g., for game optimization assistants), per AMD's GPUOpen post. AMD describes this first release as covering "foundational capabilities" with more planned.
**Engineering details (≤3 sentences):** Ships as Python bindings plus MCP servers; works alongside existing ADLX C++/C# bindings. No specific GPU-generation or OS restriction stated on the page beyond general AMD graphics hardware.
**Limitation / caveats (≤3 sentences):** AMD does not use the term "GA"; scope is described as an initial/foundational release. No pricing/license terms were stated on the page itself (points to the ADLX download page for terms).

## AMD Advanced Shader Delivery (ASD) State Object Compiler
- **Company:** AMD (FLAG: borderline)
- **Status:** GA · **Released:** 2026-10-01 (v32.0.32015.2008 noted as a September 2026 build) · **New**
- **Surface:** engine/rendering developer tool (shader pipeline)
- **Primary source:** https://gpuopen.com/news/asd-compiler-launch/
- **Underlying research:** no traceable paper
- **Availability:** Free download via NuGet; runs on any x64 Windows PC/server (no GPU required) to compile; targets AMD RDNA–RDNA4 GPUs; end users need Windows 11 24H2+ or Xbox Gaming Services 37.113.11003.0+.

**What shipped (≤3 sentences):** AMD shipped a Direct3D 12 State Object Compiler plugin that converts a game's shader State Object Database (SODB) into a Precompiled Shader Database (PSDB) for Microsoft's Advanced Shader Delivery (ASD) system. Developers use it to pre-compile and test shader delivery locally before registering builds with a storefront.
**What research it translates (≤3 sentences):** No academic paper; this is a production engineering tool built against Microsoft's ASD platform feature to reduce shader-compilation stutter.
**Practical significance (≤3 sentences):** Aims to reduce first-launch shader-compile stutter on Radeon GPUs by letting studios pre-bake and validate shader delivery packages ahead of release, per AMD's GPUOpen announcement.
**Engineering details (≤3 sentences):** Distributed via NuGet; compiler itself needs no GPU; targets AMD RDNA through RDNA4 across recent Adrenalin driver versions; end-user requirement is Windows 11 24H2+ (or Xbox Gaming Services 37.113.11003.0+).
**Limitation / caveats (≤3 sentences):** Niche, developer-facing tooling rather than a consumer-facing feature; relevance to the 3D/world-model/character-animation remit is limited (rendering-pipeline tooling only). AMD does not use the word "GA" on the page.

## NVIDIA DLSS 5 (3D-Guided Neural Rendering) — 2X-Faster Model + RTX Spark Rollout
- **Company:** NVIDIA
- **Status:** GA (NBA 2K27 + RTX Spark laptops) / Announced for Hogwarts Legacy & Where Winds Meet · **Released:** 2026-10-16 · **Update**
- **Surface:** shipped games + new hardware platform (GeForce RTX 50 Series, RTX Spark laptops, GeForce NOW)
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/dlss-5-faster-ai-model-hogwarts-legacy-rtx-spark-laptops/ ; https://www.nvidia.com/en-us/geforce/news/rtx-spark-dlss-reflex-ray-tracing-games/
- **Underlying research:** no traceable paper (proprietary transformer-based upscaling model; no arXiv companion found)
- **Availability:** Live now (2026-10-16) on GeForce RTX 50 Series GPUs, RTX Spark laptops (new Blackwell-GPU + Grace-CPU laptop platform, launched 2026-10-16), and GeForce NOW, for NBA 2K27. Rollout to Hogwarts Legacy is dated 2026-11-05; to Where Winds Meet, "late November 2026" — both still pending as of 2026-10-19.

**What shipped (Update since 2026-09-13, last_update 2026-10-13):** Update since 2026-09-13: NVIDIA shipped a 2X-faster, 24%-smaller (≈118M-parameter) version of the DLSS 5 3D-Guided Neural Rendering model, live now in NBA 2K27 (boosting frame rates up to 1.4X) on GeForce RTX 50 Series, the newly launched RTX Spark laptop platform, and GeForce NOW as of 2026-10-16. Hogwarts Legacy and Where Winds Meet support is dated 2026-11-05 and "late November 2026" respectively and had not shipped as of this check (2026-10-19).
**What research it translates (≤3 sentences):** Continues NVIDIA's transformer-based neural-rendering line underpinning DLSS 5; no separate academic paper was found for the specific speed/size optimization.
**Practical significance (≤3 sentences):** NVIDIA attributes up to a 1.4X frame-rate boost in NBA 2K27 to the faster model, and ties its first availability to the RTX Spark laptop launch (a new Blackwell-GPU + Grace-CPU Windows 11 platform shipping 2026-10-16 with preorders open).
**Engineering details (≤3 sentences):** Model shrunk to ~118M parameters (from the prior DLSS 5 model) for ~2X throughput; rollout mechanism is per-game/per-platform staged deployment rather than a single driver flag. RTX Spark day-one game list includes Fortnite, Cyberpunk 2077, The Witcher 3 Remastered, Gears of War: E-Day, 007 First Light, and others already tracked under separate entries.
**Limitation / caveats (≤3 sentences):** Hogwarts Legacy (2026-11-05) and Where Winds Meet ("late November 2026") rollouts are still announced-only, not yet usable as of 2026-10-19 — tracked separately below. RTX Spark itself is a hardware platform launch, not a pure software feature, so its day-one game-support list is informational context rather than a standalone Part B product claim.

### Announced only (not yet usable)
- DLSS 5 (3D-Guided Neural Rendering) in Hogwarts Legacy · NVIDIA · scheduled 2026-11-05 · https://www.nvidia.com/en-us/geforce/news/dlss-5-faster-ai-model-hogwarts-legacy-rtx-spark-laptops/
- DLSS 5 (3D-Guided Neural Rendering) in Where Winds Meet · NVIDIA · scheduled "late November 2026" · https://www.nvidia.com/en-us/geforce/news/dlss-5-faster-ai-model-hogwarts-legacy-rtx-spark-laptops/
- Unity Spark (browser-based AI game creation, with Google) · Unity · confirmed still waitlist-only as of 2026-10-07 blog post, no beta/GA date given · https://unity.com/blog/why-we-built-unity-spark (status unchanged from prior first_seen 2026-10-13; not re-flagged as an update)

Near-misses: 3 (Intel "Gamer Days 2026 AAA Gaming Bundle & Partnerships" (2026-08-10) is a marketing/retail bundle with partners, not a shippable tech product/feature, so dropped; AMD Radeon GPU Analyzer 2.15 source-to-ISA correlation (2026-10-06, gpuopen.com) is a real shipped dev tool but too niche/low-relevance to the 3D/world-model/animation/engine remit to warrant a full entry; Qualcomm, Adobe (beyond already-tracked Substance 3D release), Epic Games (beyond already-tracked UE5.8/Fortnite items), Autodesk, and most of Intel's own sites returned 403/blocked or empty content to automated fetch this sweep and no new qualifying item could be found or verified via an accessible primary source — flagged as coverage gaps, not confirmed absence of news.)
