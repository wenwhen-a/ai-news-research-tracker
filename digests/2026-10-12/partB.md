# Part B — Research → Product
Window: last 90 days (2026-07-14 to 2026-10-12). Weekly full sweep. Products: 3 new, 0 updated.

---
## Automatic Translation for Text-to-Speech
- **Company:** Roblox
- **Status:** GA (default-on, self-serve) · **Released:** 2026-10-08
- **Surface:** Engine AI API / in-experience voice feature
- **Primary source:** https://devforum.roblox.com/t/automatic-translation-for-text-to-speech/4922029
- **Underlying research:** no traceable paper identified this sweep (search-tool budget exhausted before this could be checked)
- **Availability:** Live now; `AudioTextToSpeech.AutoLocalize` property defaults to `true`; supports 11 languages.

**What shipped:** Roblox's text-to-speech API now automatically translates spoken text into a player's local language across 11 supported languages, on by default via the new `AutoLocalize` property. No separate opt-in or beta flag is required.
**What research it translates:** Likely builds on Roblox's existing in-house voice/translation and TTS stack, but no specific paper could be confirmed this sweep; treat lineage as unverified.
**Practical significance:** Roblox states experience creators get automatic multilingual narration/dialogue without manually authoring or licensing per-language voice lines.
**Engineering details:** Implemented as a property-level default (`AudioTextToSpeech.AutoLocalize = true`) on the existing text-to-speech API surface, rather than a new API family.
**Limitation / caveats:** Translation quality/latency and the exact language list were not independently checked beyond the devforum post; underlying research link unverified this sweep.

---
## Collision Summaries API
- **Company:** Roblox
- **Status:** GA (live engine API, no opt-in required) · **Released:** 2026-10-06
- **Surface:** Engine / Studio scripting API
- **Primary source:** https://devforum.roblox.com/t/collision-summaries-api-detailed-collision-data-from-the-engine/4918568
- **Underlying research:** no traceable paper (physics-solver engineering feature, not an AI/ML research translation)
- **Availability:** Live now for all Roblox experiences; new `BasePart:BindToCollisionSummaries` method, no beta flag.

**What shipped:** Roblox added a new engine API, `BasePart:BindToCollisionSummaries`, exposing per-contact collision data — contact points, normals, and relative/impact velocity — directly from the physics solver. It ships live, not gated behind Studio Beta Features.
**What research it translates:** This is a physics-engine instrumentation feature rather than a published research translation; no arXiv or research-blog source was found backing it.
**Practical significance:** Roblox frames this as useful "for impact FX, sound, and damage systems," letting developers drive effects from solver-level contact data instead of approximating it from velocity deltas.
**Engineering details:** The API binds a callback on a `BasePart` that fires with structured collision summaries (contact points, normals, relative velocity) sourced from the engine's physics solver each simulation step.
**Limitation / caveats:** Only verified via the devforum announcement post; no independent performance/scale data (e.g. overhead at high contact counts) was available.

---
## Gemini Enterprise Live Avatar
- **Company:** Google / DeepMind (Google Cloud / Gemini)
- **Status:** GA (default avatar, within Gemini Enterprise) — custom avatar-from-reference-image is enterprise-allowlisted only · **Released:** 2026-09-24
- **Surface:** Cloud API / enterprise app feature (Gemini Enterprise, Live API, Google Cloud console)
- **Primary source:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-with-live-avatar/
- **Underlying research:** no traceable paper (the post links only to an internal model card for "Gemini 3.8 audio," not a research paper)
- **Availability:** Rolled out starting 2026-09-24 inside Gemini Enterprise, accessed via the Google Cloud console and the Live API; existing Enterprise customers can self-serve enable the default avatar. Generating a custom avatar from a reference image is limited to enterprise allowlisting.

**What shipped:** Google added "Live Avatar" to Gemini 3.8 Live, giving its real-time voice assistant a generated, animated on-screen persona that can listen, see (via camera/screen share) and speak back with lip-sync and turn-taking cues, with SynthID watermarking on the generated video output.
**What research it translates:** Pairs Gemini's real-time multimodal/voice stack with a near-real-time video-generation model to drive a talking avatar from a single reference image; no specific paper or technical report is cited on the announcement.
**Practical significance:** Google positions this as giving enterprise AI agents a face without filming or animating a real presenter; it ships inside a paid enterprise tier rather than the free consumer Gemini app, so uptake is bounded to existing Google Cloud/Gemini Enterprise customers.
**Engineering details:** The avatar is generated video (not a 3D/game-engine rigged character) driven in near real time alongside the speech stream; default avatars are available immediately, a custom avatar from a user's own photo requires enterprise allowlist approval.
**Limitation / caveats:** No pricing, rendering methodology, or research citation is given; "custom from your own photo" fails the self-serve bar; it is a 2D generated-video avatar, not a 3D character-animation pipeline, so its fit with this tracker's "character animation" topic is adjacent rather than exact.

---

### Announced only (not yet usable)
(none met the bar this week — NVIDIA RTX Spark + Windows AI agent platform, 2026-10-07, was considered but excluded: it is general AI-PC hardware/OS tooling, not a 3D/world-model/animation/game-engine-specific product.)

Near-misses (19): Ubisoft NEO NPC (still closed testing/R&D, no dated shipped surface); Meta Muse Image/Video/Spark 1.1 (shipped, but general image/video/text generation — outside this tracker's 3D/world-model/animation/engine scope); Google Genie 3 (still a limited research preview, no GA/beta surface, original unveiling predates the window); Sony "Mockingbird" facial-animation tool (disclosed outside the 90-day window); NVIDIA DLSS 4.5 shipping in four more titles — STAR WARS: Galactic Racer, Dragon's Dogma 2: Dark Arisen, Clive Barker's Hellraiser: Revival, DYNASTY WARRIORS 3: Complete Edition Remastered (one more game adopting an already-tracked feature, not a new capability); Call of Duty: Modern Warfare 4 day-one DLSS 4.5 (campaign early access not live until 2026-10-16); NVIDIA RTX Spark/Microsoft Execution Containers (general AI-PC platform, out of topic scope); Roblox "Create IP-Based Avatar Items With Marketplace Licenses" (licensing/business feature, not AI/3D); Roblox SLIM debug tints and "[Studio Beta] if local" Luau syntax (dev tooling, not AI/3D); Fortnite/UEFN v42.30 (release-note detail page JS-rendered, unverifiable this sweep); Intel XeSS/Arc, Qualcomm Snapdragon/Adreno, Autodesk 3ds Max, AMD FSR/GPUOpen, Adobe Substance 3D/Firefly (primary pages returned 403 or empty JS shells, could not be verified this sweep); HoYoverse AI investment reports up to $14.6bn (investment announcement, not a shipped product); NetEase 《蛋仔派对》DeepSeek V4 UGC integration (earnings-call mention only, outside the 7-day update window, not yet on a primary changelog); Alibaba qwen-image-2.1-turbo added 2026-10-09 to Model Studio (image-generation model, outside 3D/world-model/animation/engine scope); Tencent GIGA game-playing agent framework (re-confirmed unchanged, still Announced only, deployed inside existing titles rather than as a standalone product).
Verification: all three company-group sweeps (Western big tech/publishers; NVIDIA/Adobe/engines; Chinese tech) checked primary sources directly — company blogs, docs, changelogs, devforum posts — per `references/product-sources.md`; trade press was used only as leads, never as the cited source. Every item above was cross-checked against `state/product_seen.json` before being marked new. Coverage gaps: the session's shared WebSearch quota was exhausted partway through all three sweeps, so later checks relied on direct WebFetch only; Intel, Qualcomm, Autodesk, AMD, Unreal Engine's own blog/news, MetaHuman news, Tencent Hunyuan 3D Studio, HoYoverse news, and Kling's release-notes SPA returned HTTP 403 or JS-only shells and could not be fetched — flagged as open follow-ups for the next sweep, not asserted as "no change." `scripts/github_releases.py` (lead generator) returned 0 of 27 repo queries successfully this run (API reachable, all requests errored) — a pipeline/network issue, not evidence of "no releases."
