# Part B — Daily Light Check (2026-10-21 through 2026-10-28)

Surfaces checked: NVIDIA developer blog (developer.nvidia.com/blog), blogs.nvidia.com, nvidia.com/geforce/news; Unreal Engine news (unrealengine.com/en-US/news) and forums.unrealengine.com; Unity (unity.com/blog, unity.com/releases/editor/whats-new, discussions.unity.com); Roblox newsroom (corp.roblox.com/newsroom) and devforum.roblox.com/c/updates/announcements; Adobe (blog.adobe.com, research.adobe.com/news); Tencent Hunyuan (hunyuan.tencent.com, 3d.hunyuan.tencent.com, cloud.tencent.com/product/hunyuan); ByteDance Volcano Engine / Seed (seed.bytedance.com, volcengine.com); Alibaba Model Studio (help.aliyun.com/zh/model-studio/newly-released-models, alibabacloud.com/blog); Kuaishou Kling (kling.ai, formerly klingai.com); PlayStation Blog (blog.playstation.com).

## New products (GA / Public beta-preview)

None found. Everything surfaced that was dated in the window and matched the four topics either (a) was already present in `product_seen.json` under an earlier `first_seen` date (e.g. RTX Remix 1.6.1, Custom Terrain Materials, Isaac Sim 6.2.0, Hunyuan 3D Cloud API, Maya 2027.2 MotionMaker — all first_seen 2026-10-23 to 2026-10-26), or (b) could not be verified against a primary source as a genuinely new, in-scope, tracked-company product (see Near-misses).

## Updates to previously-reported products

## Fortnite / UEFN — Conversations upgraded to ElevenLabs Eleven v4 Turbo with sentence streaming
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-09-13 · **Update**
- **Surface:** shipped game / creator platform (Unreal Editor for Fortnite — Conversations AI-NPC dialogue system)
- **Primary source:** https://forums.unrealengine.com/t/conversations-now-uses-eleven-v4-turbo-with-sentence-streaming/2845418
- **Underlying research:** no traceable paper (ElevenLabs' Eleven v4 Turbo is a third-party proprietary TTS model, not an Epic/tracked-company research output)
- **Availability:** Automatic, no creator action required; rolled out to all UEFN islands using the Conversations system on 2026-10-26.

**What shipped (≤3 sentences):** Update since 2026-09-13: Epic upgraded the voice backend for UEFN's "Conversations" AI-NPC dialogue system (first reported here as part of Fortnite/UEFN v41.20's "LLM-powered NPCs") from ElevenLabs' Eleven v3 to Eleven v4 Turbo. The announcement states this delivers "improved AI-generated dialogue and more responsive character interactions," with no island migration needed.
**What research it translates (≤3 sentences):** Epic's own post names no underlying paper; the change is a vendor TTS-model swap (ElevenLabs Eleven v4 Turbo) layered onto Epic's existing LLM-driven NPC dialogue pipeline, not a new Epic research result.
**Practical significance (≤3 sentences):** Epic states sentence streaming lets NPCs "begin speaking before their full response is generated," cutting perceived latency, and that voice performances are "more expressive" with facial animation that "follows the audio more closely." This is a quality/latency upgrade to an already-shipped feature rather than new functionality.
**Engineering details (≤3 sentences):** The swap is server-side (TTS model version bump from Eleven v3 to Eleven v4 Turbo plus sentence-level streaming of synthesized audio into the existing facial-animation driver); no new plugin, SDK, or UEFN version is required. Applies within Unreal Editor for Fortnite / Fortnite Creative only, not to generic Unreal Engine projects.
**Limitation / caveats (≤3 sentences):** Scope is limited to Fortnite/UEFN's built-in Conversations tool, not a general-purpose Unreal Engine or MetaHuman feature. No benchmark numbers or A/B data were published alongside the announcement — the improvement claims are Epic's own characterization.

## Announced-only (new, within window)

(none found)

## Near-misses

- **NVIDIA Nemotron 3.5 Bolt E4B (ACE game-character small language model)** — Secondary coverage (dated around 2026-10-23, following an Oct 13 teaser in NVIDIA's RTX Spark launch post) describes this as the "third-generation small language model for NVIDIA ACE game characters." Could not locate NVIDIA's own developer.nvidia.com or blogs.nvidia.com post confirming it as a shipped ACE SDK component rather than a standalone open-weights model release (which Part A/B rules treat as a research artifact, not a Part B product, unless tied to a specific product surface). Dropped for lack of a verifiable primary source and ambiguous product-surface status.
- **Alibaba Cloud Model Studio — Tripo 3D-generation API suite expansion** (help.aliyun.com/zh/model-studio/newly-released-models, dated 2026-10-27) — Nine new endpoints appeared under the Tripo brand (Tripo-ImageToSplat for Gaussian Splat generation, Tripo-Texture, Tripo-Segmentation, Tripo-SmartSegmentation, Tripo-MeshCompletion, Tripo-Retopology, Tripo-ConvertFormat, Tripo-RigCheck, Tripo-AutoRig, Tripo-AnimationRetarget), squarely in the 3D-generation and character-animation topics and on a genuine Alibaba primary source. However, Tripo AI is an independent third-party company, not an Alibaba subsidiary and not on the tracked-company list; this looks like Alibaba's cloud marketplace reselling a non-tracked company's models rather than Alibaba's own research reaching product. Flagged and excluded rather than listed as an Alibaba item.
- **RTX Remix 1.6 — Minecraft Java Edition path-tracing (community Fabric mod)** (nvidia.com/en-us/geforce/news, dated 2026-10-28) — Coverage of a new game (Minecraft Java Edition, via an early-beta community Fabric mod) adopting the already-tracked RTX Remix 1.6.1 release (first_seen 2026-10-26). Per the "another game adopts the same feature" exclusion, not treated as a new item or material update.
- **MetaHuman Creator web app discontinuation** (forums.unrealengine.com thread active 2026-10-23, shutdown effective 2026-11-05) — A deprecation of the standalone web tool (the in-editor MetaHuman Creator in UE 5.6+ continues), not a new product or feature ship; noted for context only, not reported as an item.
- **Unity 7** and **Unity Spark** — checked for tier changes in this window; no update dated 2026-10-21–28 found beyond what is already recorded in `product_seen.json` (Unity 7 public alpha, first_seen 2026-09-28/last_update 2026-10-13; Unity Spark Announced-only, first_seen 2026-10-13). Unity 6000.6.7f1 (released 2026-10-21) appears to be a routine patch release; no release notes content could be verified, so it is not reported as a material update.

**Verification statement:** All items above were checked against their stated primary sources (NVIDIA developer blog, GeForce news, blogs.nvidia.com; Unreal Engine forums; Unity release pages; Roblox devforum updates category; Adobe blog/research news; Tencent Cloud Hunyuan product page; ByteDance seed.bytedance.com and Volcano Engine docs; Alibaba Cloud help.aliyun.com Model Studio catalog; Kling's kling.ai; PlayStation Blog) for the 2026-10-21–2026-10-28 window. No items were fabricated or inferred from secondary/trade-press coverage alone; where only secondary coverage could be found (Nemotron 3.5 Bolt E4B), the item was dropped to a near-miss rather than reported as verified.
