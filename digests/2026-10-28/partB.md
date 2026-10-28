# Part B — Research → Product
Window: last 90 days (2026-07-30 to 2026-10-28). Products: 0 new, 1 updated.

---
## Fortnite / UEFN — Conversations upgraded to ElevenLabs Eleven v4 Turbo with sentence streaming
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-09-13 · **Update**
- **Surface:** shipped game / creator platform (Unreal Editor for Fortnite — Conversations AI-NPC dialogue system)
- **Primary source:** https://forums.unrealengine.com/t/conversations-now-uses-eleven-v4-turbo-with-sentence-streaming/2845418
- **Underlying research:** no traceable paper (ElevenLabs' Eleven v4 Turbo is a third-party proprietary TTS model, not an Epic/tracked-company research output)
- **Availability:** Automatic, no creator action required; rolled out to all UEFN islands using the Conversations system on 2026-10-26.

**What shipped (≤3 sentences):** Update since 2026-09-13: Epic upgraded the voice backend for UEFN's "Conversations" AI-NPC dialogue system (first reported as part of Fortnite/UEFN v41.20's "LLM-powered NPCs") from ElevenLabs' Eleven v3 to Eleven v4 Turbo. The announcement states this delivers "improved AI-generated dialogue and more responsive character interactions," with no island migration needed.
**What research it translates (≤3 sentences):** Epic's own post names no underlying paper; the change is a vendor TTS-model swap (ElevenLabs Eleven v4 Turbo) layered onto Epic's existing LLM-driven NPC dialogue pipeline, not a new Epic research result.
**Practical significance (≤3 sentences):** Epic states sentence streaming lets NPCs "begin speaking before their full response is generated," cutting perceived latency, and that voice performances are "more expressive" with facial animation that "follows the audio more closely." This is a quality/latency upgrade to an already-shipped feature rather than new functionality.
**Engineering details (≤3 sentences):** The swap is server-side (TTS model version bump from Eleven v3 to Eleven v4 Turbo plus sentence-level streaming of synthesized audio into the existing facial-animation driver); no new plugin, SDK, or UEFN version is required. Applies within Unreal Editor for Fortnite / Fortnite Creative only, not to generic Unreal Engine projects.
**Limitation / caveats (≤3 sentences):** Scope is limited to Fortnite/UEFN's built-in Conversations tool, not a general-purpose Unreal Engine or MetaHuman feature. No benchmark numbers or A/B data were published alongside the announcement — the improvement claims are Epic's own characterization.

### Announced only (not yet usable)
(none found)

Near-misses: NVIDIA Nemotron 3.5 Bolt E4B for ACE (secondary coverage only, no verifiable primary source confirming a shipped product surface); Alibaba Cloud Model Studio's new Tripo-brand 3D-generation/AutoRig/AnimationRetarget API endpoints (genuine Alibaba primary source, but Tripo AI is a non-tracked third party being resold, not Alibaba's own research); RTX Remix 1.6 Minecraft Java Edition community mod (another game adopting an already-tracked feature, not a new item); MetaHuman Creator web app discontinuation (deprecation, not a product ship).

Verification: all items checked against their stated primary sources (NVIDIA developer blog, GeForce news, blogs.nvidia.com; Unreal Engine forums; Unity release pages; Roblox devforum updates category; Adobe blog/research news; Tencent Cloud Hunyuan product page; ByteDance seed.bytedance.com and Volcano Engine docs; Alibaba Cloud help.aliyun.com Model Studio catalog; Kling's kling.ai; PlayStation Blog) for the 2026-10-21–2026-10-28 window; no items fabricated or inferred from secondary/trade-press coverage alone.
