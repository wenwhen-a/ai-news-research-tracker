**[B01] UEFN Semantic Search — AI-powered Content Browser search**
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-11-18 · **New**
- **Surface:** Engine / studio tool (UEFN Content Browser)
- **Primary source:** <https://forums.unrealengine.com/t/semantic-search-is-now-live-in-uefn-v43-12>
- **Underlying research:** no traceable paper

**What shipped:** Epic's UEFN v43.12 update adds an AI search mode to the Content Browser: toggling an "AI" button next to any search bar lets a creator type a natural-language description (e.g. "rusted metal barrel") and get matching assets by visual appearance/type rather than literal filename match (Epic's own example: that query surfaces an asset named `M_OldOilDrum`).
**What research it translates:** No external research paper is cited; Epic's forum post frames it as an embedding/semantic-matching search layer over the existing asset library's appearance and type metadata.
**Practical significance:** Epic states the feature is "now live" for all UEFN creators as of the v43.12 update, letting creators find assets by describing them instead of knowing their exact names.
**Engineering details:** Surfaced as an opt-in toggle inside the existing Content Browser search bar; matches on visual appearance and asset type rather than name strings.
**Limitation / caveats:** Epic's own post states the feature "currently works best with English queries," with no stated support for other languages yet; Epic does not label a separate beta/GA rollout tier beyond "now live."
