# Part B — Research → Product
Window: last 90 days (2026-07-15 to 2026-10-13); daily light check covering primary surfaces for changes 2026-10-06 to 2026-10-13. Products: 1 new, 1 updated.

## NVIDIA DLSS Frame Generation Performance Mode ("Preset C")
- **Company:** NVIDIA
- **Status:** Public beta/preview · **Released:** 2026-10-13 · **New**
- **Surface:** NVIDIA App (GPU driver / RTX graphics stack feature used across DLSS-enabled games)
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/dlss-4-5-crossout-remastered-modern-warfare-4-frame-gen-beta/
- **Underlying research:** no traceable paper
- **Availability:** Opt-in beta via the NVIDIA App (enable beta features in Settings > About, install the beta app update, then select "Preset C" under Graphics > Driver Settings > DLSS Override - Model Presets > Frame Generation). Supported on GeForce RTX 40 Series, RTX 50 Series GPUs, and RTX Spark laptops. Not GA.

**What shipped (≤3 sentences):** NVIDIA shipped a new, faster "Performance Mode" (internally Preset C) for DLSS Frame Generation, Multi Frame Generation, and Dynamic Multi Frame Generation, available as an opt-in preset inside an NVIDIA App beta update released October 13, 2026. NVIDIA states it is up to 35% faster than the standard preset on a GeForce RTX 5060.

**What research it translates (≤3 sentences):** NVIDIA states the mode replaces the second AI model in the Frame Generation pipeline — the one that computes optical flow for elements such as UI and ray-traced effects — with a lighter algorithm. No specific paper or named model is cited on the page, so no traceable paper is recorded.

**Practical significance (≤3 sentences):** NVIDIA states the preset trades "minor image quality" for a meaningful frame-rate gain, giving players on RTX 40/50 Series cards and RTX Spark laptops a faster frame-generation option without needing new hardware. It is opt-in and manual, so it targets performance-sensitive players rather than being a default experience change.

**Engineering details (≤3 sentences):** NVIDIA describes the swap as substituting the optical-flow sub-model used for UI/ray-traced-effect motion estimation with a lighter-weight algorithm, while keeping the primary frame-generation model unchanged. The feature is exposed through a custom DLSS Override model-preset dropdown rather than a per-game toggle.

**Limitation / caveats (≤3 sentences):** This is a beta requiring manual opt-in through NVIDIA App beta settings, not a driver-level or in-game default; NVIDIA's own framing is a quality/speed trade-off ("minor image quality" cost). No independent benchmark or quality assessment beyond NVIDIA's own 35% figure is cited on the page.

## Unity 7
- **Company:** Unity
- **Status:** Public beta/preview · **Released:** 2026-10-05 · **Update**
- **Surface:** Engine / editor (downloadable public alpha)
- **Primary source:** https://unity.com/blog/unite-seoul-keynote-2026-recap
- **Underlying research:** no traceable paper
- **Availability:** Public Alpha (build 7000.0.0a7) downloadable today from Unity's official Alpha release page (unity.com/releases/editor/alpha), no invitation required; Unity ships "two alphas per week" during this phase. No stated price change from existing Unity plans; full 7.0 release date not yet given.

**What shipped (≤3 sentences):** Update since 2026-09-28: Unity 7, previously Announced-only (previewed at Unite Seoul with no usable build), now has a public, self-serve Alpha build (7000.0.0a7) that anyone can download from Unity's official alpha channel — moving it to Public beta/preview tier. Unity's own alpha-program forum post (dated October 5, 2026) frames this as the start of weekly/biweekly alpha builds ahead of a full release.

**What research it translates (≤3 sentences):** Unity 7's core change is a CoreCLR/.NET-modernized scripting runtime and new 2D/3D graphics tooling, as previously announced; this is an engine architecture overhaul rather than a published research result, so no traceable paper applies.

**Practical significance (≤3 sentences):** Developers can now install and test Unity 7 directly rather than waiting on a roadmap promise, letting studios begin evaluating the new .NET/CoreCLR runtime and graphics changes ahead of a stable release. Unity flags the alpha as unstable ("back up your project before running it in a Unity Alpha").

**Engineering details (≤3 sentences):** A Unity staff reply in the alpha thread states domain reloads have been replaced by code reloads and assembly-load-context (ALC) reloading, and that Player/Editor Compatibility Levels remain on .NET Standard during this alpha window (full .NET compatibility is not expected to land before the alpha period ends). ECS ("ECS For All") is still in progress with no fixed release carrying the complete feature set.

**Limitation / caveats (≤3 sentences):** This is an early, explicitly unstable Alpha, not a beta or release candidate, and Unity gives no committed date for Unity 7's full/GA release. Builds with high-impact issues may be skipped rather than fixed before the next weekly build, per Unity's own description.

### Announced only (not yet usable)
- Unity Spark (browser-based, no-code/AI-assisted game creation and sharing platform, built with Google, waitlist only) · Unity · 2026-10-07 · https://unity.com/blog/why-we-built-unity-spark

Near-misses:
- NVIDIA "DLSS 5 October update" (2X faster/24% smaller 3D-Guided Neural Rendering model, rolling out Oct 16–late Nov across NBA 2K27/RTX Remix/Hogwarts Legacy/Where Winds Meet) — excluded as a performance/efficiency refinement of the already-tracked DLSS 5 (not a tier change or new model generation).
- NVIDIA RTX Spark laptop launch (Oct 16, "hundreds of top games") — excluded as a hardware/device launch, not itself a 3D/world-model/character-animation/game-engine software product surface.
- Roblox "SLIM debug tints in Studio and Roblox Player" (Oct 9) — a debug-visualization add-on (LOD/transcoding-status color tints) for an existing, previously undocumented SLIM model-representation system; treated as a minor tooling addition rather than a new product capability.
- Roblox "Terrain Updates: Object Scattering, Path Splines, Projected Terrain Decals" — original post is from 2026-09-11 (outside this window) and remains Announced-only/early-access-signup with no material change inside the window; excluded.
- Kling 4.0 full release — secondary-source coverage says Kling's own release notes state it "will officially launch in October," but no exact date and no primary-source confirmation could be retrieved within the window (klingai.com/kling.ai release-history page is JS-rendered and returned no readable content); excluded pending verification.
- Alibaba Model Studio `qwen-image-2.1-turbo` (listed 2026-10-09 in the newly-released-models catalog) — a 2D image-generation model, not on the tracked 3D/world-model/character-animation/game-engine topics; excluded.

Verification: Checked NVIDIA GeForce news (nvidia.com/en-us/geforce/news) and NVIDIA developer blog (developer.nvidia.com/blog) listing pages directly for Oct 6–13 posts; checked Unity's official blog, alpha release page, and Unity Discussions alpha-announcement thread; checked Roblox devforum's updates/announcements listing and individual threads directly, including Weekly Recap Oct 5–9; checked PlayStation Blog's 2026/10 archive directly (no on-topic Oct 6–13 posts found); checked Adobe's blog publish-date listing directly (no on-topic Oct 6–13 posts found); checked Alibaba Model Studio's newly-released-models page directly. Tencent Hunyuan (hunyuan.tencent.com / 3d.hunyuan.tencent.com), ByteDance Seed (seed.bytedance.com) and Unreal Engine's own news page (unrealengine.com/en-US/news, 403) and forums.unrealengine.com returned empty/JS-rendered or blocked content on fetch; targeted web searches for each found no October 6–13, 2026 primary-source item on the tracked topics, so none are reported for those surfaces this cycle.
