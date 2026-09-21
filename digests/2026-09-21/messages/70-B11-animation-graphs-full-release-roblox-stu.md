**[B11] Animation Graphs — full release (Roblox Studio)**
- **Company:** Roblox
- **Status:** GA · **Released:** 2026-07-15 · **New**
- **Surface:** Studio tool/engine feature (Roblox Studio, Avatar tab)
- **Primary source:** <https://devforum.roblox.com/t/full-release-animation-graphs-create-complex-character-motion-visually/4739840>
- **Underlying research:** no traceable paper — a conventional node-based animation blend-graph/state-machine system (comparable to Unity Animator or Unreal AnimGraph), not a published ML technique
- **Availability:** Free, built into Roblox Studio for all creators; works with live, published games (not just Studio testing) as of this release. No waitlist.

**What shipped:** Roblox moved Animation Graphs out of beta into full release, letting creators build and blend complex character motion visually via a node graph (Clip, Blend1D/2D, Select, Mask, Over, Add, Subtract) instead of hand-writing Luau scripting pipelines for animation state transitions.
**What research it translates:** Not derived from a specific research paper; applies established game-engine animation-blending techniques inside Roblox's cross-platform engine, integrated with Roblox's "Adaptive Animation" retargeting system for custom humanoid rigs.
**Practical significance:** Roblox states the tool lets animators "work more independently" of engineers, and reports 280+ fixes/improvements shipped since the April 2026 beta — giving Roblox's creator base a professional-grade animation-blending workflow previously only available via bespoke scripting or third-party engines.
**Engineering details:** Accessible via the Avatar tab in Roblox Studio; exposes a runtime parameter system controllable via API for gameplay-driven transitions; supports custom humanoid rigs through Adaptive Animation integration; graphs now replicate over the network for multiplayer play.
