**[B01] Mutable real-time character customization — Production-Ready in Unreal Engine 5.8**
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-10-27
- **Surface:** Engine feature / studio tool (Unreal Engine runtime character customization toolset)
- **Primary source:** <https://www.unrealengine.com/news/mutable-sample-for-runtime-character-customization-now-updated-for-ue-5-8>
- **Underlying research:** no traceable paper (Mutable is middleware Epic acquired from Anticto in 2021, not a published research result)
- **Availability:** Ships as part of Unreal Engine 5.8 (free with the engine); an updated sample project and documentation, built on a MetaHuman "Ada" preset and Fab MetaHuman assets, accompanies the release.

**What shipped:** Epic states the Mutable real-time character customization toolset "is now Production-Ready in Unreal Engine 5.8," shipping alongside a substantially updated sample project.
**What research it translates:** No traceable paper — Mutable originates from Anticto, a character-customization middleware company Epic acquired, and this release is an engine/tooling maturity milestone (beta → Production-Ready) rather than a paper-to-product translation.
**Practical significance:** Epic states Mutable lets teams compose large casts of visually distinct characters at runtime — combining body shapes, skin tones, decal "Projectors" (e.g. tattoos/logos) and materials — with Mutable reshaping garment meshes to fit the deformed body "at composition time." The showcase level isolates each capability (Basic Customizable Object, Color Patterns and Skin Tone, Projectors, Edit Material, Data Tables, Macros) so teams can inspect and adopt pieces incrementally.
**Engineering details:** Ships in Unreal Engine 5.8; the updated sample and docs include a new "Basic CO" walkthrough, and a customizable-weapon example demonstrates driving options from a Data Table node plus reusable graph logic via Macros.
