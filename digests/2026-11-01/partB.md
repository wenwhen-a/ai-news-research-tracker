# Part B — Research → Product
Window: last 7 days (2026-10-25 to 2026-11-01), daily light check (not the Monday full sweep). Topics: 3D, world models, character animation, game engines. Products: 2 new, 0 updated.

---
## Mutable real-time character customization — Production-Ready in Unreal Engine 5.8
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-10-27
- **Surface:** Engine feature / studio tool (Unreal Engine runtime character customization toolset)
- **Primary source:** https://www.unrealengine.com/news/mutable-sample-for-runtime-character-customization-now-updated-for-ue-5-8
- **Underlying research:** no traceable paper (Mutable is middleware Epic acquired from Anticto in 2021, not a published research result)
- **Availability:** Ships as part of Unreal Engine 5.8 (free with the engine); an updated sample project and documentation, built on a MetaHuman "Ada" preset and Fab MetaHuman assets, accompanies the release.

**What shipped (≤3 sentences):** Epic states the Mutable real-time character customization toolset "is now Production-Ready in Unreal Engine 5.8," shipping alongside a substantially updated sample project. The sample assembles a MetaHuman's body, face, grooms and MetaHuman Cloth in the MetaHuman plugin, then drives the result through Mutable as what Epic calls a "dataless Customizable Object."

**What research it translates (≤3 sentences):** No traceable paper — Mutable originates from Anticto, a character-customization middleware company Epic acquired, and this release is an engine/tooling maturity milestone (beta → Production-Ready) rather than a paper-to-product translation.

**Practical significance (≤3 sentences):** Epic states Mutable lets teams compose large casts of visually distinct characters at runtime — combining body shapes, skin tones, decal "Projectors" (e.g. tattoos/logos) and materials — with Mutable reshaping garment meshes to fit the deformed body "at composition time." The showcase level isolates each capability (Basic Customizable Object, Color Patterns and Skin Tone, Projectors, Edit Material, Data Tables, Macros) so teams can inspect and adopt pieces incrementally.

**Engineering details (≤3 sentences):** Ships in Unreal Engine 5.8; the updated sample and docs include a new "Basic CO" walkthrough, and a customizable-weapon example demonstrates driving options from a Data Table node plus reusable graph logic via Macros.

**Limitation / caveats (≤3 sentences):** The source material describes workflow and examples but states no performance benchmarks or outstanding known issues for this release (not stated); exact minimum-version or platform constraints beyond "Unreal Engine 5.8" were not confirmed from the portion of the page retrieved (observed, not stated).

---
## Orthographic Camera (Studio Beta)
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta, opt-in; not usable in published games) · **Released:** 2026-10-30
- **Surface:** Studio / engine (camera / rendering system)
- **Primary source:** https://devforum.roblox.com/t/studio-beta-build-2d-isometric-and-top-down-games-with-orthographic-camera/4966772
- **Underlying research:** no traceable paper
- **Availability:** Studio-only beta today; Roblox states "Published games can't use orthographic cameras yet" and that the API may still change.

**What shipped (≤3 sentences):** Roblox added a new `Camera.ProjectionType` option, Orthographic, that renders the world without perspective so "objects keep the same size at any distance." It is aimed at 2D, isometric, top-down and minimap-style games; the existing Perspective mode remains the default, so current games are unaffected.

**What research it translates (≤3 sentences):** No traceable paper — this is a standard camera-projection feature (orthographic vs. perspective projection), not derived from a cited research result.

**Practical significance (≤3 sentences):** Roblox states creators can build side-scrollers, isometric and top-down games, puzzle games and minimaps using the new `OrthographicSize` (default 35 studs, the visible view height), `OrthographicMode` (Vertical/Horizontal/Diagonal/MaxAxis, controlling what `OrthographicSize` measures) and `ViewStretch` (0.5–2.0, shared with Perspective cameras) controls. Roblox states screen-to-world conversions "work automatically" under the new projection.

**Engineering details (≤3 sentences):** Exposed as a new value of the `Camera.ProjectionType` property, available now in Roblox Studio Beta; `ViewStretch` is shared across both Perspective and Orthographic camera types.

**Limitation / caveats (≤3 sentences):** Roblox states sun shadows render incorrectly under the new mode, `ViewportFrame` cameras still render in perspective, specular highlights and reflections "may look off," VR is unsupported, and the feature is Studio-only — published games cannot use it yet.

### Announced only (not yet usable)
(none newly found in this window)

Near-misses: Phantom Blade Zero DLSS 4.5 launch (another game adopting an already-reported feature); Fortnite/UEFN v43.00 release notes (unverifiable detail at check time); Fab "Bundles and UEFN source assets" (borderline off-topic marketplace feature); Unreal Engine 5.8.4 Hotfix (minor patch, excluded by rule); Kling 4.0 "full global availability" (no new primary-source confirmation this window, already in state); Alibaba Model Studio's newest window additions (off-topic text/audio models).

Verification: each included item's primary-source URL was fetched directly and its date, company, tier and quoted claims checked against the source page (Mutable item verified via two independent fetch passes; Orthographic Camera item verified via a direct page fetch plus a second fetch of the devforum announcements category listing confirming thread title, date and canonical URL/topic ID). No new or updated items were found on NVIDIA developer blog, GeForce news, Unity blog, Adobe blog, PlayStation Blog, Tencent Hunyuan, or ByteDance Seed/Volcano Engine within the window; qualifying activity on those surfaces duplicates entries already in `state/product_seen.json`.
