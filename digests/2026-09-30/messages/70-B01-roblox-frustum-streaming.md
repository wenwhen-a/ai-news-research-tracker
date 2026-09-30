**[B01] Roblox Frustum Streaming**
- **Company:** Roblox
- **Status:** GA · **Released:** 2026-09-29
- **Surface:** Roblox Studio / engine (client-side instance streaming)
- **Primary source:** <https://devforum.roblox.com/t/frustum-streaming-stream-what-your-players-see/4904553>
- **Underlying research:** no traceable paper
- **Availability:** Opt-in, available today to all Roblox Studio developers via the new `FrustumStreaming` property on `Player`. Free, no waitlist.

**What shipped:** Roblox shipped Frustum Streaming, a camera-based instance-streaming mode that loads objects within a player's camera view cone instead of streaming equally in all directions around the player.
**What research it translates:** No paper or research blog post is cited; this is an engineering change to Roblox's existing streaming/level-of-detail system rather than a published research result.
**Practical significance:** Roblox states Automatic mode can activate frustum-aware streaming based on narrow field of view, high player velocity, or a distant camera, which developers can use to cut memory/bandwidth for off-screen content in large or fast-traversal worlds.
**Engineering details:** Implemented as a `Player` property (`FrustumStreaming = Automatic/Enabled/Disabled`) layered on Roblox's existing instance-streaming system; no engine version number is given since Roblox Studio updates continuously.
**Limitation / caveats:** Feature is opt-in, so most existing experiences are unaffected until a developer enables it; Roblox does not give performance benchmarks in the announcement, only qualitative guidance on when Automatic mode engages.
