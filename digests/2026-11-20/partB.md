# Part B — Research → Product
Window: last 90 days (2026-08-22 to 2026-11-20). Light check of ~10 primary surfaces for items dated 2026-11-13 to 2026-11-20 (today is not a Monday, so no full sweep). Qualifying products: 3 (1 new, 2 updated). Announced-only: 0.

---
## Roblox Web Play — WebGPU rendering backend (Creator Beta)
- **Company:** Roblox
- **Status:** Public beta/preview (Creator Beta) · **Released:** 2026-11-19 · **New**
- **Surface:** Engine / client (browser-based play)
- **Primary source:** https://devforum.roblox.com/t/sharper-web-play-rendering-with-webgpu/4996719
- **Underlying research:** no traceable paper (adoption of the public WebGPU browser-graphics standard; no company research paper tied to it)
- **Availability:** Opt-in Creator Beta only (Web Play itself launched 2026-10-29); requires a WebGPU-capable browser/device; not yet open to regular players; ships weekly alongside the desktop client.

**What shipped (≤3 sentences):** Roblox switched the renderer for its browser-based "Web Play" Creator Beta from WebGL to WebGPU. Roblox states this fixes missing grass/terrain-decoration rendering, color-pixel artifacts on Intel Macs, blurry UI and emissive surfaces, distorted avatars and lighting quality, while adding texture streaming and faster instancing.
**What research it translates (≤3 sentences):** This is engineering adoption of the WebGPU browser graphics API (the successor to WebGL across major browsers), not a result from a specific Roblox research paper.
**Practical significance (≤3 sentences):** Roblox states this is a rendering-quality and performance upgrade for creators testing their games in-browser during the Web Play Creator Beta, ahead of a planned wider release to players. It directly fixes several previously reported visual bugs (avatar distortion, broken terrain decoration) that blocked reliable testing.
**Engineering details (≤3 sentences):** WebGPU support is now required; Roblox says it will run a device probe before opening Web Play to players and block unsupported devices with an explanatory message. Early Playtesting stays disabled on web until General Availability; regular Studio playtesting in Web Play continues to work.
**Limitation / caveats (≤3 sentences):** Still Creator Beta only — not available to regular players yet, and some devices that worked under WebGL beta no longer qualify. Roblox lists remaining known issues: music dropouts, hitching when entering new areas, higher memory use than the native client, and Chrome defaulting to an integrated GPU on dual-GPU Windows machines.

---
## Kling 4.0 — native 4K and HDR added to the video-generation API
- **Company:** Kuaishou (Kling)
- **Status:** GA · **Released:** 2026-11-19 · **Update**
- **Surface:** Cloud API (video generation)
- **Primary source:** https://kling.ai/document-api/updates/api.md
- **Underlying research:** no traceable paper for this specific capability (a related system, Kling-Omni, has a technical report at arXiv:2512.16776, but it is not confirmed to be the same model generation as Kling 4.0)
- **Availability:** Kling 4.0 and Kling 4.0 Flash text-to-video, image-to-video and omni-reference-to-video API endpoints; `settings.resolution` now accepts `4k`; new `settings.dynamic_range` parameter enables HDR at 1080p or 4K; HDR adds a per-second fee.

**What shipped (≤3 sentences):** Update since 2026-10-15: Kling's API changelog (dated 2026-11-19) shows the Kling 4.0 video-generation API now actually supports 4K resolution and HDR output. This closes a gap explicitly flagged as pending at the October 15 full launch, when "4K/1080p/21:9 output ... still future-tense" per the standing product_seen.json entry.
**What research it translates (≤3 sentences):** Kuaishou does not cite a specific new paper for this change; it is a capability/parameter extension of the already-shipped Kling 4.0 model rather than a new model generation.
**Practical significance (≤3 sentences):** Kuaishou's own API documentation states developers can now request native 4K and HDR output directly from the existing Kling 4.0 and Kling 4.0 Flash endpoints across text-to-video, image-to-video and omni-reference workflows.
**Engineering details (≤3 sentences):** Resolution is set via `settings.resolution: "4k"`; HDR is toggled via a new `settings.dynamic_range: "hdr"` parameter, available at the 1080p and 4K tiers; billing adds a per-second surcharge for HDR output.
**Limitation / caveats (≤3 sentences):** The changelog gives no latency figures or regional availability limits for the new tiers, and HDR playback requires HDR-capable display/decoding to show any benefit. A separate Nov 14 changelog entry also added 4:3/3:4 aspect ratios to Kling 4.0 and Kling 4.0 Flash, but that is a minor parameter addition, not reported here as a material update.

---
## Roblox Studio — Animation Graphs: State Machines and Luau Expressions reach Full Release
- **Company:** Roblox
- **Status:** GA · **Released:** 2026-11-19 · **Update**
- **Surface:** Engine / studio tool (Animation Graph Editor; usable in Studio and live games)
- **Primary source:** https://devforum.roblox.com/t/full-release-state-machines-and-luau-expressions-in-animation-graphs/4997058
- **Underlying research:** no traceable paper (internal engine/tooling feature)
- **Availability:** Free, built into Roblox Studio's Animation Graph Editor for all creators; now usable in published, live experiences, not just Studio.

**What shipped (≤3 sentences):** Update since 2026-10-09: Roblox moved State Machine and Luau Expression nodes in its Animation Graph Editor out of Studio Beta into full release, per a Nov 19 devforum post — a tier change from Public beta/preview to GA. Beta-built graphs continue to work unchanged.
**What research it translates (≤3 sentences):** No external research paper; this is a visual node-graph tool for authoring character-animation state machines and inline Luau expressions, built on Roblox's existing Animation Graph system (full-released July 2026).
**Practical significance (≤3 sentences):** Roblox states creators can now ship these state-machine-driven animation graphs — e.g., combo systems where a swing can only follow another swing, not idle — in live, published games rather than only prototyping them in Studio.
**Engineering details (≤3 sentences):** Adds live preview that highlights the active state/transition during playtest, immediate application of expression/condition edits without reloading the graph, parameter-less graph wiring, and fixes to state renaming/duplicate-naming bugs. Also adds "Wait For: Finished" firing correctly from looping states, `nil`-comparison support (`==`/`~=`) in expressions, and editor UX additions (Break Connections, a frames/seconds toggle, right-click node selection).
**Limitation / caveats (≤3 sentences):** Luau Expressions still cannot use loops, functions, tables, `require()`, method calls, other libraries, or DataModel access — they can only read graph parameters, so gameplay logic must still set those parameters from scripts. Several beta-era bugs (double-advancing looping clips, a respawn memory leak, trigger parameters not firing from server scripts) are fixed in this release but were not externally quantified.

### Announced only (not yet usable)
- none found in this window

Near-misses: 3 — NVIDIA SOMA Retargeter v0.2 (developer.nvidia.com, 2026-11-13): an open-source tool retargeting human motion to humanoid robots; robotics-focused and an open-source code drop, so it belongs in Part A, not here. ByteDance Seedance 2.5 4K video API reportedly opened to developers (~2026-11-16/17 per TechNode and other secondary outlets): no primary ByteDance Seed or Volcano Engine page could be found confirming date, scope, or pricing, so this is unverified and dropped. Unity CLI 1.0 reaching production readiness (unity.com, 2026-11-17): legitimate Unity product news, but it is general build/project-management tooling with AI-agent integrations, not specifically a 3D/world-model/character-animation/game-engine-graphics feature, so it is flagged as borderline rather than listed.
Verification: every item above was checked against its primary source (devforum.roblox.com posts and kling.ai's own API changelog, fetched directly) for date, company, tier and claims; product_seen.json was checked to confirm each is either genuinely new or a change not already recorded in that entry's `updates` list.
