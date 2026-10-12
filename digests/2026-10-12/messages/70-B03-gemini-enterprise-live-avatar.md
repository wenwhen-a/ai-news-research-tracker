**[B03] Gemini Enterprise Live Avatar**
- **Company:** Google / DeepMind (Google Cloud / Gemini)
- **Status:** GA (default avatar, within Gemini Enterprise) — custom avatar-from-reference-image is enterprise-allowlisted only · **Released:** 2026-09-24
- **Surface:** Cloud API / enterprise app feature (Gemini Enterprise, Live API, Google Cloud console)
- **Primary source:** <https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-with-live-avatar/>
- **Underlying research:** no traceable paper (the post links only to an internal model card for "Gemini 3.8 audio," not a research paper)
- **Availability:** Rolled out starting 2026-09-24 inside Gemini Enterprise, accessed via the Google Cloud console and the Live API; existing Enterprise customers can self-serve enable the default avatar. Generating a custom avatar from a reference image is limited to enterprise allowlisting.

**What shipped:** Google added "Live Avatar" to Gemini 3.8 Live, giving its real-time voice assistant a generated, animated on-screen persona that can listen, see (via camera/screen share) and speak back with lip-sync and turn-taking cues, with SynthID watermarking on the generated video output.
**What research it translates:** Pairs Gemini's real-time multimodal/voice stack with a near-real-time video-generation model to drive a talking avatar from a single reference image; no specific paper or technical report is cited on the announcement.
**Practical significance:** Google positions this as giving enterprise AI agents a face without filming or animating a real presenter; it ships inside a paid enterprise tier rather than the free consumer Gemini app, so uptake is bounded to existing Google Cloud/Gemini Enterprise customers.
