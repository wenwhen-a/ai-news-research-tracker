# Part B — Research → Product: NVIDIA / Adobe / engines group
Window: 2026-06-30 to 2026-09-28 (today 2026-09-28 UTC)
Scope: NVIDIA, Adobe, Intel, Qualcomm, Unity, Epic Games, Roblox
Topics: 3D generation, world models, character animation, game engines/tooling

## Summary of findings
This company group already has extensive coverage in `state/product_seen.json` from prior runs (10 NVIDIA items, 1 Adobe item, 2 Epic Games items, 1 Unity item, and 8 Roblox items — the most recent dated as late as 2026-09-24/25). After checking every primary source in `product-sources.md` for this group plus fresh leads, **one genuinely new GA item qualified: Qualcomm Adreno Neural Fusion (ANF)** — Qualcomm's first entry in this tracker. **One new Announced-only item qualified: Unity 7** (previewed at Unite Seoul 2026). No new qualifying items were found for NVIDIA, Adobe, Intel, Epic Games, or Roblox beyond what is already recorded — their primary sources were checked through 2026-09-28 and nothing new on the 4 tracked topics has appeared since the last-recorded entries.

## Previously reported (from product_seen.json, this group — not re-verified in depth)
- NVIDIA — DLSS 5 / 3D-Guided Neural Rendering (NBA 2K27) — GA, 2026-09-03
- NVIDIA — DLSS 4.5 Ray Reconstruction 2nd-gen transformer model (early access) — Public beta, 2026-08-25
- NVIDIA — ACE Game Agent SDK (beta) + ACE plugins for UE5 — GA(plugins)/beta(SDK), 2026-06-16
- NVIDIA — RTX Remix 1.5.2 (Remix Skills) — GA, 2026-06-16
- NVIDIA — 007 First Light path tracing + DLSS 4.5 Ray Reconstruction — GA, 2026-09-15
- NVIDIA — Isaac Sim 6.1 (General Availability) — GA, 2026-09-15
- NVIDIA — GeForce Game Ready Driver (007 First Light, WARDOGS, Aniimo) — GA, 2026-09-15
- NVIDIA — RTX Kit 2026.3 + ACE SDK update (RTX Character Rendering 1.4, RTX Mega Geometry 2.0, etc.) — GA, 2026-09-22
- NVIDIA — Omniverse Kit 110.3 — GA, 2026-08-16
- NVIDIA — DLSS 4.5 + Dynamic Multi Frame Generation in Control: Resonant — GA, 2026-09-24
- Adobe — Substance 3D Painter 12.1 / Designer 16 / Sampler update (OpenPBR) — GA, 2026-07-21
- Epic Games — Fortnite/UEFN v41.20 (Control Rig for Sidekicks, LLM-powered NPCs) — GA, 2026-07-16
- Epic Games — Unreal Engine 5.8 (MetaHuman Animator markerless capture, MegaLights, Mesh Terrain, MCP plugin) — GA, 2026-06-17
- Epic Games — Fortnite/UEFN v42.20 — GA, 2026-09-17
- Unity — Unity 6.2 (6000.6.0f1) — GA, 2026-08-31
- Roblox — Build mobile AI creation tab (public alpha) — Public beta, 2026-07-28
- Roblox — Scene Generator — Announced only, 2026-09-11
- Roblox — RDC 2026 roadmap items (NPC Dynamic Behavior, New Default Movement, Layered Clothing) — Announced only, 2026-09-12
- Roblox — Animation Graphs full release — GA, 2026-07-15
- Roblox — Tunable Collision Geometry — GA, 2026-09-17
- Roblox — Creator Roadmap 2026 Fall Update — Announced only, 2026-09-22
- Roblox — Texture Generation Tools, Segment Any Mesh, Image Previews — Public beta, 2026-09-23
- Roblox — Studio Beta Quad Support for EditableMesh APIs — Public beta, 2026-09-23
- No status-tier changes or clear new versions observed on any of the above during this run.
- Note: Epic's MetaHuman Devkit (OpenRigLogic, MIT-licensed rig-evaluation library) and the "ISKM" crowd-rendering tech were announced at the **same** June 16–18, 2026 Unreal Fest Chicago event as the already-recorded Unreal Engine 5.8 release (same release_date, same announcement bundle) — treated as part of that existing entry, not counted as new.

---

## Qualcomm Adreno Neural Fusion (ANF)
- **Company:** Qualcomm
- **Status:** GA · **Released:** 2026-09-22 (SDK/GitHub introduction; publicly unveiled 2026-09-02, expanded at Snapdragon Summit 2026-09-22/24) · **New**
- **Surface:** GPU rendering SDK — native Vulkan integration, plus Unreal Engine 5 plugin and Unity 6.6+ support
- **Primary source:** https://www.qualcomm.com/developer/blog/2026/09/introducing-adreno-neural-fusion-sdk-for-snapdragon-mobile-platforms (overview: https://www.qualcomm.com/news/onq/2026/09/adreno-neural-fusion-ai-rendering)
- **Underlying research:** no traceable paper (Qualcomm's posts cite no arXiv paper or research-blog post for ANF's specific method; only USPTO patents on related temporal-accumulation techniques turned up, which are not treated as a "traceable paper" per the skill's rules)
- **Availability:** Requires Snapdragon 8 Elite Gen 6 / Extreme Gen 6 silicon (new "Adreno matrix core" hardware) — first commercial phones (e.g., Xiaomi 18 Pro Max) shipped 2026-09-23. SDK, docs and samples are public now on GitHub (SnapdragonGameStudios/adreno-neural-fusion, MIT-style dev sample license per Qualcomm), with an Unreal Engine 5 plugin, Unity 6.6+ support, and Snapdragon Profiler integration; no waitlist for developers. Qualcomm names 20+ partner titles (Diablo Immortal, Honkai: Star Rail, Monster Hunter Outlanders, Naraka: Bladepoint Mobile, War Thunder Mobile, and others).

**What shipped (≤3 sentences):** Qualcomm shipped Adreno Neural Fusion (ANF), an AI-driven rendering pipeline unifying neural super resolution (SR) and frame generation (FG) that runs on new "Adreno matrix core" AI-dedicated GPU cores paired with 18MB of on-chip Adreno HPM memory. Qualcomm states ANF is "the first mobile AI super resolution technology of its kind supported across major game engines and is commercially available," with a public SDK, Unreal Engine 5 plugin, and Unity 6.6+ support shipping alongside the Snapdragon 8 Elite Gen 6 / Extreme Gen 6 platforms. Qualcomm names over 20 studio partners integrating it, with live demos across four titles at Snapdragon Summit 2026.

**What research it translates (≤3 sentences):** ANF applies established temporal-accumulation upscaling and frame-interpolation techniques — sub-pixel camera jitter (Halton/Sobol sequences), motion-vector-guided reprojection, and depth-based disocclusion handling — conceptually similar to the temporal AI upscaling/frame-generation approach used by NVIDIA DLSS, AMD FSR and Intel XeSS, but run through Qualcomm's own trained models. Qualcomm's developer blog describes the SR and FG models' input/output contracts and dispatch mechanics in detail but does not cite a specific research paper as their basis, so no underlying paper can be traced.

**Practical significance (≤3 sentences):** Qualcomm states ANF lets mobile titles "render at half resolution and generate half as many real frames but deliver full-resolution output at double the submitted frame rate," and claims (per company materials) improved frame stability and reduced ghosting/shimmering versus prior mobile upscalers. Because it ships as engine plugins for Unreal Engine 5 and Unity 6.6+, Qualcomm says studios can adopt it "without custom implementations," a first for a mobile-GPU-vendor upscaler across both major engines simultaneously. Adoption depends on new Gen 6 silicon reaching consumers' hands, which only began 2026-09-23.

**Engineering details (≤3 sentences):** The architecture places one Adreno Matrix Core (running at 1.45GHz) in each of three GPU slices, backed by 18MB of Adreno High Performance Memory (HPM) so intermediate buffers stay on-chip. SR takes four inputs per frame (jittered half-res color, jittered half-res depth, unjittered half-res motion vectors, and the scalar jitter offset) and outputs one full-resolution frame; FG takes two consecutive full-resolution post-processed frames plus depth/motion vectors from frame N to synthesize one interpolated frame, at the cost of one extra frame of input latency. Both dispatches record into a primary Vulkan command buffer outside any render pass and run inference directly on the GPU-resident buffers without transferring data off-chip.

**Limitation / caveats (≤3 sentences):** ANF is hardware-gated to Snapdragon 8 Elite Gen 6 and higher — it will not run on any previously shipped Snapdragon chip, and "broader support" further down the roadmap is only "planned." The initial SDK release produces exactly one interpolated frame per real frame (no multi-frame generation yet, unlike NVIDIA DLSS 4/Intel XeSS 3 MFG). Real-world availability is currently limited to the roughly 20 named partner titles that have integrated the SDK, not a driver-level toggle for arbitrary games.

### Announced only (not yet usable)
- Unity 7 (CoreCLR/.NET-modernized engine core, 2D/3D graphics tooling, free built-in MCP server + CLI) · Unity · 2026-07-21 · https://unity.com/blog/unite-seoul-keynote-2026-recap — Unity's own post explicitly states "This post describes features, capabilities, and timing still in development... availability could differ materially," so it fails the GA/beta usability test; no ship date given beyond the keynote preview. Unity 6.2 (already recorded, GA 2026-08-31) remains the current shipping release.

Near-misses:
- Intel XeSS 3 / XeSS 3 Multi-Frame Generation — base XeSS 3 launched 2026-01-27 and the driver extending MFG to older Arc Alchemist/Battlemage GPUs (32.0.101.8509) shipped 2026-02-13 — both **before** the 90-day window; no qualifying new Intel item (on any of the 4 topics) was found dated within 2026-06-30–2026-09-28. Subsequent Arc driver releases in-window (e.g., 32.0.101.8974, 2026-08-14) were routine per-game performance/bugfix updates with no new AI/3D/animation feature.
- Adobe Firefly "Model Marketplace" (Aug 2026 update, described in secondary coverage as letting creators mix "one model for character animation while another handles background rendering") — could not confirm via an Adobe primary source (helpx.adobe.com / blog.adobe.com) in the time available, and the "character animation" framing reads like a generic marketing example rather than a documented 3D/character feature; excluded as unverified.
- Epic Games Fab marketplace AI-content transparency/labeling features — no dated primary-source post found placing this update within the 90-day window; excluded pending a dated Epic source.
- Epic's MetaHuman Creator (web app) discontinuation, announced 2026-09-16 (shutdown effective 2026-11-05) — a deprecation, not a new shipped capability, so out of scope for Part B regardless.

## Coverage gaps worth flagging
- Intel has had no qualifying Part B item in any recent run for this group (per `product_seen.json`, zero Intel entries exist); its AI-graphics activity (XeSS 3, Arc drivers) all predates this 90-day window, and Intel's developer blog surfaced no new 3D/character/world-model/engine-tooling product news in-window. Worth re-checking after Intel's Xe3/Panther Lake generation matures.
- Qualcomm is a first-time entrant in this tracker; its Adreno Neural Fusion SDK is hardware-gated to unreleased-until-this-week silicon, so real-world (consumer) impact should be re-checked in a future run as more Gen 6 devices ship.
