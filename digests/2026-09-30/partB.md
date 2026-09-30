# Part B — Research → Product
Window: last 90 days (2026-07-02 to 2026-09-30). Light check (non-Monday): ~10 primary surfaces checked for material changes in the last 7 days (2026-09-23 to 2026-09-30). Products: 1 new, 0 updated.

---

## Roblox Frustum Streaming
- **Company:** Roblox
- **Status:** GA · **Released:** 2026-09-29
- **Surface:** Roblox Studio / engine (client-side instance streaming)
- **Primary source:** https://devforum.roblox.com/t/frustum-streaming-stream-what-your-players-see/4904553
- **Underlying research:** no traceable paper
- **Availability:** Opt-in, available today to all Roblox Studio developers via the new `FrustumStreaming` property on `Player`. Free, no waitlist.

**What shipped (≤3 sentences):** Roblox shipped Frustum Streaming, a camera-based instance-streaming mode that loads objects within a player's camera view cone instead of streaming equally in all directions around the player. It is controlled via a new `FrustumStreaming` property on `Player` with three modes — Automatic (engine-managed), Enabled, and Disabled — and Roblox states "Starting today, you can now stream in instances based on a player's camera view with Frustum Streaming."
**What research it translates (≤3 sentences):** No paper or research blog post is cited; this is an engineering change to Roblox's existing streaming/level-of-detail system rather than a published research result.
**Practical significance (≤3 sentences):** Roblox states Automatic mode can activate frustum-aware streaming based on narrow field of view, high player velocity, or a distant camera, which developers can use to cut memory/bandwidth for off-screen content in large or fast-traversal worlds. It is opt-in per experience and non-breaking by default.
**Engineering details (≤3 sentences):** Implemented as a `Player` property (`FrustumStreaming = Automatic/Enabled/Disabled`) layered on Roblox's existing instance-streaming system; no engine version number is given since Roblox Studio updates continuously.
**Limitation / caveats (≤3 sentences):** Feature is opt-in, so most existing experiences are unaffected until a developer enables it; Roblox does not give performance benchmarks in the announcement, only qualitative guidance on when Automatic mode engages.

### Announced only (not yet usable)
- Roblox Terrain (Object Scattering, Path Splines, Projected Terrain Decals, Virtual Texturing, SDFs) · Roblox · 2026-09-30 · https://devforum.roblox.com/t/terrain-updates-object-scattering-path-splines-projected-terrain-decals-and-more/4865617 (Terrain Early Access Program — application required, not self-serve)

Near-misses: HappyOyster 2 Preview (Alibaba ATH) — dated one day outside window, source states not yet officially released. ByteDance Doubao PixelDance & Seaweed — invite-only internal testing, not self-serve, and general video generation rather than the tracked topics. "Kling 4.0" marketing-page mention — no verifiable in-window release date found. Unity 6000.6.3f1 — routine patch on the already-tracked Unity 6.2 line, not a material change. Roblox "Collision Geometry Workflow Improvements" post — restates the already-logged Tunable Collision Geometry feature (first_seen 2026-09-17), no new material change. Nothing qualifying found on: NVIDIA Developer Blog (game-dev/rendering tag), Unreal Engine news/forum, Adobe blog / research.adobe.com, Tencent Hunyuan 3D/main site, ByteDance Seed site, PlayStation Blog (tech/graphics posts).
Verification: each item above was checked against its stated primary source (devforum.roblox.com post); no PDF/secondary-source substitution was used.
