**[B01 · Update] Fortnite / UEFN — Conversations upgraded to ElevenLabs Eleven v4 Turbo with sentence streaming**
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-09-13 · **Update**
- **Surface:** shipped game / creator platform (Unreal Editor for Fortnite — Conversations AI-NPC dialogue system)
- **Primary source:** <https://forums.unrealengine.com/t/conversations-now-uses-eleven-v4-turbo-with-sentence-streaming/2845418>
- **Underlying research:** no traceable paper (ElevenLabs' Eleven v4 Turbo is a third-party proprietary TTS model, not an Epic/tracked-company research output)
- **Availability:** Automatic, no creator action required; rolled out to all UEFN islands using the Conversations system on 2026-10-26.

**What shipped:** Update since 2026-09-13: Epic upgraded the voice backend for UEFN's "Conversations" AI-NPC dialogue system (first reported as part of Fortnite/UEFN v41.20's "LLM-powered NPCs") from ElevenLabs' Eleven v3 to Eleven v4 Turbo.
**What research it translates:** Epic's own post names no underlying paper; the change is a vendor TTS-model swap (ElevenLabs Eleven v4 Turbo) layered onto Epic's existing LLM-driven NPC dialogue pipeline, not a new Epic research result.
**Practical significance:** Epic states sentence streaming lets NPCs "begin speaking before their full response is generated," cutting perceived latency, and that voice performances are "more expressive" with facial animation that "follows the audio more closely." This is a quality/latency upgrade to an already-shipped feature rather than new functionality.
**Engineering details:** The swap is server-side (TTS model version bump from Eleven v3 to Eleven v4 Turbo plus sentence-level streaming of synthesized audio into the existing facial-animation driver); no new plugin, SDK, or UEFN version is required.
