**[B02] Orthographic Camera (Studio Beta)**
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta, opt-in; not usable in published games) · **Released:** 2026-10-30
- **Surface:** Studio / engine (camera / rendering system)
- **Primary source:** <https://devforum.roblox.com/t/studio-beta-build-2d-isometric-and-top-down-games-with-orthographic-camera/4966772>
- **Underlying research:** no traceable paper
- **Availability:** Studio-only beta today; Roblox states "Published games can't use orthographic cameras yet" and that the API may still change.

**What shipped:** Roblox added a new `Camera.ProjectionType` option, Orthographic, that renders the world without perspective so "objects keep the same size at any distance." It is aimed at 2D, isometric, top-down and minimap-style games; the existing Perspective mode remains the default, so current games are unaffected.
**What research it translates:** No traceable paper — this is a standard camera-projection feature (orthographic vs. perspective projection), not derived from a cited research result.
**Practical significance:** Roblox states creators can build side-scrollers, isometric and top-down games, puzzle games and minimaps using the new `OrthographicSize` (default 35 studs, the visible view height), `OrthographicMode` (Vertical/Horizontal/Diagonal/MaxAxis, controlling what `OrthographicSize` measures) and `ViewStretch` (0.5–2.0, shared with Perspective cameras) controls.
**Engineering details:** Exposed as a new value of the `Camera.ProjectionType` property, available now in Roblox Studio Beta; `ViewStretch` is shared across both Perspective and Orthographic camera types.
**Limitation / caveats:** Roblox states sun shadows render incorrectly under the new mode, `ViewportFrame` cameras still render in perspective, specular highlights and reflections "may look off," VR is unsupported, and the feature is Studio-only — published games cannot use it yet.
