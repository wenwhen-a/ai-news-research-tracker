# Part B — Research → Product (Light Check)
Window: last 7 days (2026-10-22 to 2026-10-29). Surfaces checked: NVIDIA developer blog & GeForce news, Unreal Engine news/forums, Unity blog, Roblox newsroom/devforum, Adobe blog, Tencent Hunyuan, ByteDance Seed/Volcano Engine, Alibaba Model Studio, Kuaishou Kling, PlayStation Blog. Qualifying items: 4 new, 1 update. Announced-only: 1.

---

## NVIDIA ACE — Nemotron 3.5 Bolt E4B (4GB) via the In-Game Inferencing (IGI) SDK
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-10-27 · **New**
- **Surface:** on-device AI model + SDK (ACE / In-Game Inferencing SDK) for AI game characters
- **Primary source:** https://developer.nvidia.com/blog/nvidia-rtx-spark-powers-neural-rendering-and-ai-characters-in-games/
- **Underlying research:** arXiv 2610.33039, "Nemotron 3.5 Bolt 74B-A9B 24GB: A Hybrid Vision-Language Model for Local AI" — same Nemotron 3.5 Bolt model family; the paper documents the 74B-A9B 24GB variant, not the shipped E4B 4GB variant specifically
- **Availability:** Free download via the IGI SDK; runs locally on GeForce RTX and RTX Spark; no waitlist stated

**What shipped (≤3 sentences):** NVIDIA states Nemotron 3.5 Bolt E4B 4GB "is now available" to developers via the In-Game Inferencing (IGI) SDK, a small on-device LLM described as "purpose-built to power richer, faster in-game character interactions" that runs locally on GeForce RTX and RTX Spark hardware.
**What research it translates (≤3 sentences):** The Nemotron 3.5 Bolt family (arXiv 2610.33039) is a hybrid Mamba-Transformer vision-language model derived from Nemotron 3.5 Super VL 120B-A12B, using "Star Elastic compression with 2-bit Quantization-Aware Distillation" to fit memory-constrained local deployment; the shipped E4B 4GB variant is a smaller sibling of the exact size the paper benchmarks.
**Practical significance (≤3 sentences):** NVIDIA states the model offers "~40% higher average quality against our prior model on relevant benchmarks," with multi-turn tool use, configurable reasoning, a 64k context window, and support for 35 languages — letting developers run NPC dialogue/reasoning on-device instead of via a cloud round-trip.
**Engineering details (≤3 sentences):** Ships via the IGI SDK and runs locally on GeForce RTX / RTX Spark GPUs; released in the same post as an RTX Kit SDK bundle update and a DLSS 4.5 Unreal Engine plugin (v8.9.0) adding native Windows-on-Arm support for UE 5.8.
**Limitation / caveats (≤3 sentences):** The blog post gives no parameter count for the E4B 4GB variant itself (only the arXiv paper's 74B-A9B variant is benchmarked in detail), so the paper-to-product match is at the model-family level, not a confirmed one-to-one match.

---

## Alibaba Cloud Model Studio — Tripo 3D pipeline tools (Segmentation, SmartSegmentation, MeshCompletion, Retopology, ConvertFormat, RigCheck, AutoRig, AnimationRetarget, ImageToSplat, Texture)
- **Company:** Alibaba Cloud (Model Studio) — **flagged:** the underlying models are built by Tripo/VAST, which is not itself a tracked company; Alibaba operates and sells access to them via its own cloud catalog, which is the basis for inclusion
- **Status:** GA (listed in Model Studio's self-serve "newly released models" catalog; no invite/whitelist marker found on the page) · **Released:** 2026-10-27 · **New**
- **Surface:** cloud API (Alibaba Cloud Model Studio / Bailian Open API)
- **Primary source:** https://help.aliyun.com/zh/model-studio/newly-released-models
- **Underlying research:** arXiv 2504.12451, "One Model to Rig Them All: Diverse Skeleton Rigging with UniRig" — the catalog's own description of Tripo-AutoRig cites "the UniRig algorithm"; no traceable paper found for the other nine tools
- **Availability:** Open API, China North 2 (Beijing) region; Tripo's base generation models (Tripo-P1.0, Tripo-H3.1) have been on this catalog since 2026-04-27, but these ten part/rig/animation pipeline tools are newly listed as of 2026-10-27

**What shipped (≤3 sentences):** Alibaba's Model Studio catalog added ten new Tripo-branded 3D-pipeline tools on 2026-10-27 — mesh segmentation (standard and semantically-controlled), mesh completion, retopology, format conversion, rig-compatibility checking, automatic rigging, animation retargeting (against 100 preset animations), image-to-Gaussian-splat conversion, and automatic PBR texturing — extending Tripo's existing base 3D-generation models into a fuller generate-to-animate pipeline.
**What research it translates (≤3 sentences):** Per the catalog's own description, Tripo-AutoRig is "based on the UniRig algorithm" (arXiv 2504.12451), which reports "a 215% improvement in rigging accuracy and a 194% improvement in motion accuracy" over prior skeleton-rigging methods on its test datasets; no equivalent citation was found for the other nine tools.
**Practical significance (≤3 sentences):** The catalog's descriptions state the tools let a developer take an untextured, unsegmented, unrigged 3D mesh through an end-to-end pipeline as callable cloud APIs — segmenting parts, retopologizing for different LOD needs, auto-texturing, auto-rigging, and retargeting stock animations — rather than doing that work by hand in a 3D tool.
**Engineering details (≤3 sentences):** Exposed as Open API model IDs under the `Tripo/` namespace (e.g. `Tripo/Tripo-AutoRig`, `Tripo/Tripo-AnimationRetarget`) in Alibaba Cloud Model Studio's Beijing region; output formats and exact per-call pricing were not confirmed on this pass.
**Limitation / caveats (≤3 sentences):** The catalog page does not state whether any of these ten tools require an invitation/whitelist versus fully open self-serve access; because Tripo (the models' creator) is not itself a tracked company, this item is flagged for judgment on whether Alibaba's hosting/selling role is sufficient to count it as Alibaba's "own product."

---

## Roblox Studio — Upgraded Shapecasts (Margins, Size Gradients, CFrame/size overrides)
- **Company:** Roblox
- **Status:** GA · **Released:** 2026-10-28 · **New**
- **Surface:** engine/physics API (Roblox Studio + live games)
- **Primary source:** https://devforum.roblox.com/t/upgrading-shapecasts-margins-size-gradients-optimizations-and-more/4963119
- **Underlying research:** no traceable paper
- **Availability:** Live now in Studio and published games automatically for existing Blockcast/Spherecast/Shapecast calls (no opt-in needed); new `RaycastParams.Margin`, `RaycastParams.SizeGradient`, and `cframeOverride`/`sizeOverride` parameters on `WorldRoot:Shapecast` available now; in-Studio cast visualization via Visualization Modes or `settings().Physics.DrawShapecast`

**What shipped (≤3 sentences):** Roblox shipped a rewritten shapecast implementation (Blockcast, Spherecast, Shapecast) adding a `Margin` parameter that "inflates the cast shape by a constant distance in every direction," a `SizeGradient` parameter, CFrame/size override parameters, and new in-Studio visualization of cast shapes.
**What research it translates (≤3 sentences):** Not research-derived; this is an internal physics-engine optimization, so "no traceable paper" applies.
**Practical significance (≤3 sentences):** Roblox states existing calls automatically "run on a new implementation that is faster and more accurate, with no changes needed on your end," with casts running "up to 4.1× quicker," letting developers use more shapecasts per frame (e.g. melee hit detection, ground checks) without a performance penalty.
**Engineering details (≤3 sentences):** Ships as changes to `BasePart`/`WorldRoot` shapecast APIs and new `RaycastParams` fields; visualization is Studio-only, toggled under Visualization Modes > Physics Simulation > Shapecasts or via a plugin/Command Bar property.
**Limitation / caveats (≤3 sentences):** Forum commenters note the new visualization currently has a short, non-configurable display lifetime, and that raycasts (as opposed to shapecasts) are not yet covered by the new visualization tooling.

---

## Roblox Studio — UGC Validation Visualization (avatar body/mesh quality checks)
- **Company:** Roblox
- **Status:** GA · **Released:** 2026-10-22 · **New**
- **Surface:** studio tool (Avatar tab, Creator Marketplace asset QA)
- **Primary source:** https://devforum.roblox.com/t/improving-validation-checks-for-ugc-avatar-bodies-visualization-tool-and-asset-quality/4950522
- **Underlying research:** no traceable paper
- **Availability:** Available now in Studio's Avatar tab; covers bodies, heads, layered clothing, and rigid accessories; free, no opt-in stated

**What shipped (≤3 sentences):** Roblox added a Studio tool that visualizes UGC Marketplace validation errors (red) and warnings (yellow) directly on a selected 3D avatar asset, plus "Asset Quality" information covering attachment placement, mesh structure, geometry integrity, and vertex similarity for avatar bodies.
**What research it translates (≤3 sentences):** Not research-derived; "no traceable paper" — this is internal asset-QA tooling, not a generative or reconstruction method.
**Practical significance (≤3 sentences):** Roblox states the tool helps creators find and fix marketplace-validation problems on 3D assets before submission; Roblox explicitly notes Asset Quality "does not measure realism."
**Engineering details (≤3 sentences):** Implemented in the Studio Avatar tab's asset editor; checks currently cover avatar bodies, heads, layered clothing, and rigid accessories only.
**Limitation / caveats (≤3 sentences):** Roblox states animation- and makeup-specific validation visualization, automatic error fixes, and MCP-surfaced validation errors are still "planned," not yet shipped; this item's fit to the tracked "3D" topic is weaker than a generation tool, since it is QA/validation rather than content creation (observed, not stated).

---

## RTX Remix — Minecraft: Java Edition path-tracing beta (update to RTX Remix 1.6.1)
- **Company:** NVIDIA
- **Status:** GA (RTX Remix 1.6 release) / Public beta (the Minecraft integration specifically) · **Released:** 2026-10-28 · **Update**
- **Surface:** modding/rendering toolkit (RTX Remix) + consumer game (Minecraft: Java Edition)
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/remix-1-6-dlss-5-comfyui-2-0-minecraft-rtx-beta/
- **Underlying research:** no traceable paper
- **Availability:** Minecraft: Java Edition 1.21.1 (Microsoft account required); Windows 10/11 x64 or ARM64; GeForce RTX 30-series+ (driver 616.92 WHQL+) or RTX Spark (driver 621.01 WHQL+); open-source beta, free

**Update since 2026-10-26: what changed.** This GeForce News writeup of the RTX Remix 1.6 release (the same release already logged on 2026-10-26 as RTX Remix 1.6.1 from GitHub) adds a flagship-game integration not previously reported in `product_seen.json`: an open-source beta that renders Minecraft: Java Edition with DLSS-accelerated full path tracing, RTX Dynamic Illumination, RTX Global Illumination, volumetric lighting, caustics, and subsurface scattering, plus a ComfyUI 2.0-based pipeline replacing RTX Remix's legacy AI texture/mesh generation tools, and Multi Frame Generation extended to "up to 6X."
**What research it translates (≤3 sentences):** Not separately stated; builds on the same DLSS path-tracing/denoising and 3D-Guided Neural Rendering techniques already covered under the previously-logged DLSS 5 and DLSS 4.5 entries.
**Practical significance (≤3 sentences):** NVIDIA states the Minecraft beta ships with a sample world from Blockworks and an NVIDIA PBR materials pack, letting any Minecraft Java Edition player try path-traced rendering without installing a separate community mod.
**Engineering details (≤3 sentences):** Requires driver 616.92 WHQL+ (RTX) or 621.01 WHQL+ (RTX Spark); adds native Arm64 Windows support; ComfyUI 2.0 is a dedicated in-tool pipeline for texture/mesh generation, replacing the prior legacy tools.
**Limitation / caveats (≤3 sentences):** NVIDIA states mod compatibility and quality "may vary" until individual mod authors update their packages for 1.6; the Minecraft integration is explicitly labeled a "beta," not GA.

### Announced only (not yet usable)
- Roblox AnimatedImages (2D sprite/character animation system) · Roblox · 2026-10-27 · https://devforum.roblox.com/t/early-access-program-build-2d-games-with-animatedimages/4960734 — Early Access Program limited to selected creators; Studio-only; "you cannot publish places with these features yet."

Near-misses: 6 — (1) NVIDIA MotionBricks (arXiv 2604.24833), presented on NVIDIA's 2026-10-27 blog as "research code and models" only, with the Unreal Engine integration from the research demo explicitly not included — stays Part A/research material, not Part B. (2) Kuaishou Kling — kling.ai (klingai.com redirects there) names Kling 4.0 as current but carries no dated release note or version bump for this window. (3) Tencent Hunyuan (hunyuan.tencent.com, 3d.hunyuan.tencent.com, Tencent Cloud docs) — primary pages returned empty/JS-rendered content or unrelated documentation; no verifiable new release found in the window. (4) Unity blog — the only posts dated in the window (Oct 23, 26) are general game-design explainer articles, not product/feature releases. (5) Adobe blog (Substance 3D/Firefly 3D) — no post in the window; the nearest Substance-3D-related post (a Sony Pictures Imageworks case study) is dated Oct 2, outside the window. (6) PlayStation Blog — posts through Oct 28 cover game launches, accessories, and PS Plus lineups; none describe a new graphics/AI/3D feature dated in the window. Also checked and excluded as non-qualifying: Unreal Engine 5.8.4 hotfix (Oct 27, minor patch) and MetaHuman Creator web app discontinuation (Oct 23, a removal, not a new/updated capability).

Verification: double-checked each item's primary source, date, and tier.
