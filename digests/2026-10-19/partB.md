# Part B — Research → Product
Window: last 90 days (2026-07-21 to 2026-10-19). Monday full sweep (Western big tech/publishers, NVIDIA/Adobe/engines, Chinese tech groups). Products: 2 new, 3 updated.

## EditableMesh Batching APIs & Parallel Queries
- **Company:** Roblox
- **Status:** GA (Full Release) · **Released:** 2026-09-15 · **New**
- **Surface:** Studio/engine API (3D mesh editing)
- **Primary source:** https://devforum.roblox.com/t/full-release-editablemesh-batching-apis-parallel-queries
- **Underlying research:** no traceable paper
- **Availability:** Available in published experiences as of the 2026-09-15 full release (beta had been available since 2026-08-06 via File > Beta Features > EditableMesh Batching). No region/plan gating noted.

**What shipped (≤3 sentences):** Roblox shipped ten new batch methods (BatchAdd, BatchRemove, Clear, BatchSetValues, BatchSetFaceAttributes, BatchSetVertexFaceAttributes, BatchGetValues, BatchGetFaceAttributes, BatchGetVertexAttributes, BatchGetVertexFaceAttributes) for the EditableMesh API, plus parallel-safe query methods (RaycastLocal, FindClosestPointOnSurface, FindClosestVertex, Get* accessors) usable from parallel Luau after task.desynchronize(). This moved from Studio Beta (2026-08-06) to full release in published experiences (2026-09-15).
**What research it translates (≤3 sentences):** This is an internal engine/runtime-systems engineering effort (batched mesh mutation + parallelized read queries) rather than a published ML research result; no arXiv paper or research blog post underlies it.
**Practical significance (≤3 sentences):** Roblox states the batching APIs are up to ~8x faster than per-element loops, and parallel queries give up to ~2x read throughput, benchmarked on a 2019 Huawei phone with 2GB RAM — aimed at making procedural/generative mesh editing (including AI-generated mesh workflows like Segment Any Mesh) performant at runtime on low-end mobile hardware.
**Engineering details (≤3 sentences):** Mutating methods must still run serially (task.synchronize()); only queries are parallel-safe. Enum.MeshAttribute values covered: Vertex, Normal, UV, Color, Face; a single batch call cannot mix ID types.
**Limitation / caveats (≤3 sentences):** Skinning is not supported for batching or parallel access; parallel writes are not supported at all. Roblox lists replication, reduced ID-verification overhead, permission restrictions, and possible quad support as future work, so the feature is still evolving post-GA.

## AMD Advanced Shader Delivery (ASD) State Object Compiler
- **Company:** AMD (FLAG: borderline — comparable-standing company, not on the core tracked list)
- **Status:** GA · **Released:** 2026-10-01 · **New**
- **Surface:** engine/rendering developer tool (shader pipeline)
- **Primary source:** https://gpuopen.com/news/asd-compiler-launch/
- **Underlying research:** no traceable paper
- **Availability:** Free download via NuGet; runs on any x64 Windows PC/server (no GPU required) to compile; targets AMD RDNA–RDNA4 GPUs; end users need Windows 11 24H2+ or Xbox Gaming Services 37.113.11003.0+.

**What shipped (≤3 sentences):** AMD shipped a Direct3D 12 State Object Compiler plugin that converts a game's shader State Object Database (SODB) into a Precompiled Shader Database (PSDB) for Microsoft's Advanced Shader Delivery (ASD) system. Developers use it to pre-compile and test shader delivery locally before registering builds with a storefront.
**What research it translates (≤3 sentences):** No academic paper; this is a production engineering tool built against Microsoft's ASD platform feature to reduce shader-compilation stutter.
**Practical significance (≤3 sentences):** AMD states the tool aims to reduce first-launch shader-compile stutter on Radeon GPUs by letting studios pre-bake and validate shader delivery packages ahead of release.
**Engineering details (≤3 sentences):** Distributed via NuGet; the compiler itself needs no GPU; targets AMD RDNA through RDNA4 across recent Adrenalin driver versions; end-user requirement is Windows 11 24H2+ (or Xbox Gaming Services 37.113.11003.0+).
**Limitation / caveats (≤3 sentences):** Niche, developer-facing tooling rather than a consumer-facing feature; AMD does not use the word "GA" on the page itself.

## NVIDIA DLSS 5 (3D-Guided Neural Rendering) — 2X-Faster Model + RTX Spark Rollout
- **Company:** NVIDIA
- **Status:** GA (NBA 2K27 + RTX Spark laptops + GeForce NOW) · **Released:** 2026-10-16 · **Update**
- **Surface:** shipped game + new hardware platform (GeForce RTX 50 Series, RTX Spark laptops, GeForce NOW)
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/dlss-5-faster-ai-model-hogwarts-legacy-rtx-spark-laptops/ ; https://www.nvidia.com/en-us/geforce/news/rtx-spark-dlss-reflex-ray-tracing-games/
- **Underlying research:** no traceable paper (proprietary transformer-based upscaling model)
- **Availability:** Live since 2026-10-16 on GeForce RTX 50 Series GPUs, RTX Spark laptops (new Blackwell-GPU + Grace-CPU platform launched the same day), and GeForce NOW, for NBA 2K27. Hogwarts Legacy (2026-11-05) and Where Winds Meet ("late November 2026") are scheduled but not yet live — listed below as announced-only.

**What shipped (≤3 sentences):** Update since 2026-09-13 (last update 2026-10-13): NVIDIA shipped a 2X-faster, 24%-smaller (~118M-parameter) version of the DLSS 5 3D-Guided Neural Rendering model, live in NBA 2K27 (NVIDIA states up to a 1.4X frame-rate boost) on GeForce RTX 50 Series, the newly launched RTX Spark laptop platform, and GeForce NOW as of 2026-10-16.
**What research it translates (≤3 sentences):** Continues NVIDIA's transformer-based neural-rendering line underpinning DLSS 5; no separate academic paper was found for this specific speed/size optimization.
**Practical significance (≤3 sentences):** NVIDIA ties the model's first availability to the RTX Spark laptop launch (a new Blackwell-GPU + Grace-CPU Windows 11 platform shipping 2026-10-16 with preorders open).
**Engineering details (≤3 sentences):** Model shrunk to ~118M parameters for ~2X throughput; rollout is staged per game/platform rather than a single driver flag.
**Limitation / caveats (≤3 sentences):** Hogwarts Legacy and Where Winds Meet rollouts remain announced-only as of 2026-10-19 (tracked separately below). RTX Spark itself is a hardware platform launch, not a pure software feature.

## Kling 4.0 (full global launch)
- **Company:** Kuaishou (Kling AI)
- **Status:** GA · **Released:** 2026-10-15 · **Update**
- **Surface:** Consumer/creator app (klingai.com) + Kling MCP/CLI for agent-driven workflows
- **Primary source:** https://kling.ai/ (official product homepage); corroborated by wire-service reposts of Kuaishou's own announcement text (marketscreener.com, markets.businessinsider.com)
- **Underlying research:** no traceable paper found (no public technical report for 4.0 as of this check)
- **Availability:** Global rollout announced 2026-10-15; accessible via the Kling AI web app and the Kling Open Platform API/MCP/CLI. Some advertised capabilities (4K/1080p/21:9 output, up to 2-minute extensions) are described in future tense ("will support" / "will soon support") and are not yet live.

**What shipped (≤3 sentences):** Update since 2026-10-04: the previously tracked "Kling 4.0 Flash (early access)" has been superseded by a full, globally launched Kling 4.0. The full release adds native single-pass generation up to 30 seconds, Omni Reference (up to 15 references: 10 images, 5 videos, 7 subjects), up to 10 keyframe inputs, up to 10-bit HDR output, 8,000-token prompts, and first-class Kling MCP/CLI integration for agent-driven batch production.
**What research it translates (≤3 sentences):** No underlying arXiv paper or technical report was found for this release; Kuaishou has not published a public write-up of the Kling 4.0 architecture as of this check.
**Practical significance (≤3 sentences):** Kuaishou frames this as moving generative video "toward enterprise production," citing an Advertising Week New York 2026 showcase (2026-10-06) aimed at enterprise/advertising buyers. The MCP/CLI integration lets external agent frameworks drive Kling programmatically rather than only through the consumer UI.
**Engineering details (≤3 sentences):** Access is via the Kling AI app/web platform and the Kling Open Platform API/MCP/CLI tooling. Broadcast-spec outputs (4K, 1080p, 21:9) and 2-minute extended generation are called out as forthcoming, implying the October 15 GA is a narrower feature set than the eventual full spec.
**Limitation / caveats (≤3 sentences):** Kuaishou's own newsroom page was not directly reachable (JS-rendered, returned empty on fetch), so this is sourced from the official homepage plus wire-service reposts, not a dated company blog post. The exact relationship between this "full" 4.0 and the earlier "4.0 Flash early access" could not be confirmed.

## Seedance 2.5 API (BytePlus ModelArk)
- **Company:** ByteDance/TikTok
- **Status:** GA (API) · **Released:** documentation current as of 2026-10-17 · **Update**
- **Surface:** Cloud API (BytePlus ModelArk), in addition to the existing Dreamina/Jimeng consumer app
- **Primary source:** https://docs.byteplus.com/en/docs/ModelArk/seedance-2-5 ; https://ai.byteplus.com/en/activity/seedance2-5
- **Underlying research:** no traceable paper found for Seedance 2.5 specifically (builds on ByteDance Seed's prior Seedance 1.0/2.0 line)
- **Availability:** Documented under BytePlus ModelArk's "Video generation" API section, with Light/Production/Premium plans valid for 3 months before switching to pay-as-you-go per-token billing. This is new since the original 2026-09-21 entry, which noted the API as "coming soon."

**What shipped (≤3 sentences):** Update since 2026-09-21: Seedance 2.5, previously GA only as a consumer feature (Dreamina/Jimeng/CapCut) with its API marked "coming soon," now has live BytePlus ModelArk API documentation (tutorial + prompt guide, last updated 2026-10-17) and an active pricing/plan page with per-token and pay-as-you-go billing.
**What research it translates (≤3 sentences):** No underlying arXiv paper specific to Seedance 2.5 was located; it builds on ByteDance Seed's prior Seedance video-generation line rather than a newly published paper.
**Practical significance (≤3 sentences):** This moves Seedance 2.5 from "consumer app only" to "developer-integrable," letting third-party products call 30-second audio-video generation programmatically rather than only through Dreamina/Jimeng.
**Engineering details (≤3 sentences):** Access is documented as part of ModelArk's "Video generation" section alongside a Seedance 2.0 tutorial, with usage "offsets" billed at up to ~1:1.8 across resolutions and input modes once a plan is exhausted. The exact model-ID/endpoint string and region list were not retrievable from the pages reached.
**Limitation / caveats (≤3 sentences):** The tutorial body text (model ID, exact endpoint, concrete pricing figures, region availability) could not be fully extracted, so this is a documentation-existence confirmation rather than a full spec capture.

### Announced only (not yet usable)
- DLSS 5 (3D-Guided Neural Rendering) in Hogwarts Legacy · NVIDIA · scheduled 2026-11-05 · https://www.nvidia.com/en-us/geforce/news/dlss-5-faster-ai-model-hogwarts-legacy-rtx-spark-laptops/
- DLSS 5 (3D-Guided Neural Rendering) in Where Winds Meet · NVIDIA · scheduled "late November 2026" · https://www.nvidia.com/en-us/geforce/news/dlss-5-faster-ai-model-hogwarts-legacy-rtx-spark-laptops/

Near-misses: 7 (AMD ADLX 2.0 AI Extensions SDK — off-topic: general AI-agent GPU-telemetry/control tooling, not specific to 3D content, world models, character animation, or engine/rendering; AMD Radeon GPU Analyzer 2.15 — too niche/low-relevance to the tracked topics; Intel "Gamer Days 2026 AAA Gaming Bundle" — marketing/retail bundle, not a shippable tech product; Kling 4.0's advertised 4K/1080p/21:9 output and 2-minute extensions — future-tense, not yet usable; Meta Hologram status change — unverifiable, Meta Connect 2026 recap page unreachable; a "Gemini 3.8 Live with Live Avatar" mention — could not be located on a primary Google source, may be a mislabel of the already-tracked Gemini Enterprise Live Avatar; Roblox Terrain Early Access 64-materials program — ambiguous whether its in-window signup-wave note counts as a new dating for this sweep).

Verification: every new/updated item above was checked against the primary source URL listed; status tier, release date, and every claim were confirmed on that page (or, for Kling 4.0, corroborated via wire-service reposts of Kuaishou's own announcement text where the newsroom page itself could not be fetched). Coverage gaps (reported, not silently dropped): Qualcomm, Adobe (beyond already-tracked Substance 3D release), Epic Games (beyond already-tracked UE5.8/Fortnite items), Autodesk, and most of Intel's own pages returned 403/blocked or empty content to automated fetch this sweep; Baidu, miHoYo/HoYoverse, NetEase/Fuxi, and Alibaba/Bailian/Wan primary surfaces were not reachable this sweep (shared WebSearch quota was exhausted across the three parallel sweep agents; several official pages are JS-rendered SPAs that return empty content to automated fetch) — absence of findings there is a coverage gap, not a confirmed absence of activity. Unity Spark and the Roblox "NPC Dynamic Behavior"/"Scene Generator" roadmap items were re-checked and remain unchanged (still waitlist-only / "Late 2026" / not shipped) and are therefore not re-listed.
