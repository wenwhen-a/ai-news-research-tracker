**[B01] Roblox Studio — Automatic In-Game Image Text Translation (Beta)**
- **Company:** Roblox
- **Status:** Public beta/preview · **Released:** 2026-11-10 · **New**
- **Surface:** Studio / Creator Hub localization tool (engine feature)
- **Primary source:** <https://create.roblox.com/docs/production/localization/image-translations>
- **Underlying research:** no traceable paper
- **Availability:** Beta ("functionality and availability are subject to change," per Roblox's own docs). Opt-in per target language via the Languages tab plus a new "Automatic Image Capture" setting; developers then enable translated-content on a per-image basis. Supported languages at launch: French, German, Indonesian, Italian, Korean, Portuguese, Spanish. Free, included in Roblox Studio/Creator Hub; no separate pricing. Translations are not instant — Roblox states capture and generation can take "up to a few days."

**What shipped:** Roblox shipped a beta that automatically detects and translates text baked into in-game images (signs, UI graphics, textures) rather than only text rendered through TextLabel/TextButton objects, which earlier automatic-translation tooling covered.
**What research it translates:** Roblox's docs give no model name or citation, and no matching paper was found via arXiv search on "image text translation," "scene text editing," or "visual text localization" tied to Roblox.
**Practical significance:** This extends Roblox's existing automatic-translation system (previously text-only, then speech-to-speech via Automatic Translation for Text-to-Speech shipped Oct 8, 2026) to in-game visual assets, closing a localization gap that previously required artists to manually re-author translated textures per locale.
