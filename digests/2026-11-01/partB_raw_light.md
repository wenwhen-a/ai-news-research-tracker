# Part B — Daily Light Check (Research → Product)

Run type: **daily light check** (not the Monday full weekly sweep).
Window: last 7 days, 2026-10-25 to 2026-11-01. Topics: 3D, world models, character animation, game engines.
Surfaces checked (~10): NVIDIA developer blog, GeForce news, Unreal Engine news + forum announcements, Unity blog, Roblox newsroom + devforum announcements, Adobe blog, Tencent Hunyuan (3d.hunyuan.tencent.com / hunyuan.tencent.com), ByteDance Volcano Engine / Seed, Alibaba Model Studio release notes, Kuaishou Kling, PlayStation Blog.

Checked against `state/product_seen.json` (not modified by this run). Qualifying new items: **2** (0 updates, 0 announced-only, 6 near-miss notes below).

---

## Mutable real-time character customization — Production-Ready in Unreal Engine 5.8
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-10-27 · **New**
- **Surface:** Engine feature / studio tool (Unreal Engine runtime character customization toolset)
- **Primary source:** https://www.unrealengine.com/news/mutable-sample-for-runtime-character-customization-now-updated-for-ue-5-8
- **Underlying research:** no traceable paper (Mutable is middleware Epic acquired from Anticto in 2021, not a published research result)
- **Availability:** Ships as part of Unreal Engine 5.8 (free with the engine); an updated sample project and documentation, built on a MetaHuman "Ada" preset and Fab MetaHuman assets, accompanies the release.

**What shipped (≤3 sentences):** Epic states the Mutable real-time character customization toolset "is now Production-Ready in Unreal Engine 5.8," shipping alongside a substantially updated sample project. The sample assembles a MetaHuman's body, face, grooms and MetaHuman Cloth in the MetaHuman plugin, then drives the result through Mutable as what Epic calls a "dataless Customizable Object."

**What research it translates (≤3 sentences):** No traceable paper — Mutable originates from Anticto, a character-customization middleware company Epic acquired, and this release is an engine/tooling maturity milestone (beta → Production-Ready) rather than a paper-to-product translation.

**Practical significance (≤3 sentences):** Epic states Mutable lets teams compose large casts of visually distinct characters at runtime — combining body shapes, skin tones, decal "Projectors" (e.g. tattoos/logos) and materials — with Mutable reshaping garment meshes to fit the deformed body "at composition time." The showcase level isolates each capability (Basic Customizable Object, Color Patterns and Skin Tone, Projectors, Edit Material, Data Tables, Macros) so teams can inspect and adopt pieces incrementally.

**Engineering details (≤3 sentences):** Ships in Unreal Engine 5.8; the updated sample and docs include a new "Basic CO" walkthrough, and a customizable-weapon example demonstrates driving options from a Data Table node plus reusable graph logic via Macros.

**Limitation / caveats (≤3 sentences):** The retrieved source material describes workflow and examples but states no performance benchmarks or outstanding known issues for this release (not stated); exact minimum-version or platform constraints beyond "Unreal Engine 5.8" were not confirmed from the portion of the page retrieved (observed, not stated).

---

## Orthographic Camera (Studio Beta)
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta, opt-in; not usable in published games) · **Released:** 2026-10-30 · **New**
- **Surface:** Studio / engine (camera / rendering system)
- **Primary source:** https://devforum.roblox.com/t/studio-beta-build-2d-isometric-and-top-down-games-with-orthographic-camera/4966772
- **Underlying research:** no traceable paper
- **Availability:** Studio-only beta today; Roblox states "Published games can't use orthographic cameras yet" and that the API may still change.

**What shipped (≤3 sentences):** Roblox added a new `Camera.ProjectionType` option, Orthographic, that renders the world without perspective so "objects keep the same size at any distance." It is aimed at 2D, isometric, top-down and minimap-style games; the existing Perspective mode remains the default, so current games are unaffected.

**What research it translates (≤3 sentences):** No traceable paper — this is a standard camera-projection feature (orthographic vs. perspective projection), not derived from a cited research result.

**Practical significance (≤3 sentences):** Roblox states creators can build side-scrollers, isometric and top-down games, puzzle games and minimaps using the new `OrthographicSize` (default 35 studs, the visible view height), `OrthographicMode` (Vertical/Horizontal/Diagonal/MaxAxis, controlling what `OrthographicSize` measures) and `ViewStretch` (0.5–2.0, shared with Perspective cameras) controls. Roblox states screen-to-world conversions "work automatically" under the new projection.

**Engineering details (≤3 sentences):** Exposed as a new value of the `Camera.ProjectionType` property, available now in Roblox Studio Beta; `ViewStretch` is shared across both Perspective and Orthographic camera types.

**Limitation / caveats (≤3 sentences):** Roblox states sun shadows render incorrectly under the new mode, `ViewportFrame` cameras still render in perspective, specular highlights and reflections "may look off," VR is unsupported, and the feature is Studio-only — published games cannot use it yet.

---

### Announced only (not yet usable)
(none newly found in this window)

### Near-misses / notable but not qualifying
- **Phantom Blade Zero DLSS 4.5 launch** (NVIDIA GeForce news, 2026-10-28, https://www.nvidia.com/en-us/geforce/news/phantom-blade-zero-path-tracing-dlss-4-5-ray-reconstruction/) — another shipped game adopting the already-reported DLSS 4.5 / Dynamic Multi Frame Generation feature set (same tech already logged for Control: Resonant, Witcher 3 Remastered, Gears of War: E-Day, Modern Warfare 4, Cyberpunk 2077). Per the "another game adopts the same feature" rule, not logged as new.
- **Fortnite / UEFN v43.00 release notes** (dev.epicgames.com, last-forum-activity 2026-11-01) — the official release-notes page returned only a table-of-contents stub when fetched and could not be verified for on-topic (3D/animation/engine) content in this window; not included for lack of verifiable detail.
- **"Bundles and UEFN source assets have arrived on Fab!"** (forums.unrealengine.com, 2026-10-31) — a Fab asset-marketplace merchandising feature; borderline on-topic (not clearly a 3D/engine/animation feature), not included.
- **Unreal Engine 5.8.4 Hotfix** (forums.unrealengine.com, 2026-10-27) — routine bugfix hotfix, excluded per the minor-patch rule.
- **Kling 4.0 "full global availability"** — third-party trackers give conflicting dates (Oct 15 vs. Oct 16) for Kling 4.0's move out of early access; no new primary-source (klingai.com/kling.ai) confirmation could be fetched in this window, and the item is already recorded in `product_seen.json` (first_seen 2026-10-04, last update 2026-10-15).
- **Alibaba Cloud Model Studio** — no new 3D/world-model/animation entries found dated 2026-10-27 to 2026-11-01 beyond the Tripo 3D-pipeline tools already logged on 2026-10-27; the newest visible catalog additions in the window (`qwen3.8-flash`, `antdigital/Ling-3.1-flash`, `qwen-audio-3.1-realtime-flash`) are text/vision/audio models, off-topic for this tracker.

No new or updated items were found on NVIDIA developer blog (beyond the already-logged RTX Spark/ACE Nemotron 3.5 Bolt post), Unity blog, Adobe blog, PlayStation Blog, Tencent Hunyuan (3d.hunyuan.tencent.com / hunyuan.tencent.com / Tencent Cloud), or ByteDance Seed/Volcano Engine within the 2026-10-25 to 2026-11-01 window; all qualifying activity found on those surfaces in the window duplicates entries already present in `state/product_seen.json` (e.g. RTX Remix 1.6.1 writeup, Roblox Scene Generator beta, Roblox Prompt-to-Avatar beta, Roblox AnimatedImages early access, Roblox Custom Terrain Materials full launch, Roblox Upgraded Shapecasts).

Verification pass: each included item's primary-source URL was fetched and its date, company, tier and quoted claims checked directly against the source page (Mutable item verified via two independent fetch passes of the same URL; Orthographic Camera item verified via direct page fetch plus a second fetch of the devforum announcements category listing confirming the thread title, date and canonical URL/topic ID).
