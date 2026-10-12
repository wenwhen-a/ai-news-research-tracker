**[B01] Automatic Translation for Text-to-Speech**
- **Company:** Roblox
- **Status:** GA (default-on, self-serve) · **Released:** 2026-10-08
- **Surface:** Engine AI API / in-experience voice feature
- **Primary source:** <https://devforum.roblox.com/t/automatic-translation-for-text-to-speech/4922029>
- **Underlying research:** no traceable paper identified this sweep (search-tool budget exhausted before this could be checked)
- **Availability:** Live now; `AudioTextToSpeech.AutoLocalize` property defaults to `true`; supports 11 languages.

**What shipped:** Roblox's text-to-speech API now automatically translates spoken text into a player's local language across 11 supported languages, on by default via the new `AutoLocalize` property. No separate opt-in or beta flag is required.
**What research it translates:** Likely builds on Roblox's existing in-house voice/translation and TTS stack, but no specific paper could be confirmed this sweep; treat lineage as unverified.
**Practical significance:** Roblox states experience creators get automatic multilingual narration/dialogue without manually authoring or licensing per-language voice lines.
**Engineering details:** Implemented as a property-level default (`AudioTextToSpeech.AutoLocalize = true`) on the existing text-to-speech API surface, rather than a new API family.
**Limitation / caveats:** Translation quality/latency and the exact language list were not independently checked beyond the devforum post; underlying research link unverified this sweep.
