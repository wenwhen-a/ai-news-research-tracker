**[B01] Roblox Web Play — WebGPU rendering backend (Creator Beta)**
- **Company:** Roblox
- **Status:** Public beta/preview (Creator Beta) · **Released:** 2026-11-19 · **New**
- **Surface:** Engine / client (browser-based play)
- **Primary source:** <https://devforum.roblox.com/t/sharper-web-play-rendering-with-webgpu/4996719>
- **Underlying research:** no traceable paper (adoption of the public WebGPU browser-graphics standard; no company research paper tied to it)
- **Availability:** Opt-in Creator Beta only (Web Play itself launched 2026-10-29); requires a WebGPU-capable browser/device; not yet open to regular players; ships weekly alongside the desktop client.

**What shipped:** Roblox switched the renderer for its browser-based "Web Play" Creator Beta from WebGL to WebGPU.
**What research it translates:** This is engineering adoption of the WebGPU browser graphics API (the successor to WebGL across major browsers), not a result from a specific Roblox research paper.
**Practical significance:** Roblox states this is a rendering-quality and performance upgrade for creators testing their games in-browser during the Web Play Creator Beta, ahead of a planned wider release to players.
**Engineering details:** WebGPU support is now required; Roblox says it will run a device probe before opening Web Play to players and block unsupported devices with an explanatory message.
**Limitation / caveats:** Still Creator Beta only — not available to regular players yet, and some devices that worked under WebGL beta no longer qualify.
