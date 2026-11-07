**[B02] Roblox Studio — Generate R15 Animations From a Prompt (Prompt to Animation + R6 Motion Rebuilder)**
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta) · **Released:** 2026-11-05 · **New**
- **Surface:** Studio dev tool (Assistant / Studio MCP)
- **Primary source:** <https://devforum.roblox.com/t/studio-beta-generate-r15-animations-from-a-prompt-plus-optional-r6-motion-rebuilder/4977709>
- **Underlying research:** no traceable paper
- **Availability:** Opt-in Studio Beta (File > Beta Features > "Animation Generation in Assistant"); reachable via Assistant's `/generate_animation` command or Studio MCP's `generate_animation` tool; free during the beta; capped at four generations per account per minute, subject to change before full release.

**What shipped:** Roblox shipped a Studio Beta feature that generates an R15 animation clip from a written description of a movement ("Prompt to Animation"), plus an optional "Motion Rebuilder" that converts an existing R6 animation into an R15 version as a new asset, leaving the original R6 clip unchanged.
**What research it translates:** Roblox's devforum post names no underlying paper for either tool — "no traceable paper."
**Practical significance:** A creator can describe a motion in plain language inside Studio's Assistant — or have an external AI agent call it via Studio MCP's `generate_animation` tool — and get a usable R15 clip in about 20–30 seconds without hand-authoring keyframes or sourcing mocap, and separately upgrade older R6-rig animations to R15 automatically instead of re-animating them.
**Engineering details:** Works only with humanoid rigs and standard R15 output (Advanced R15 unsupported); via Studio MCP an agent can specify a rig and clip length up to 10 seconds, or an R6 animation asset ID to convert; Studio MCP can process lists of R6 clips (rate-limited) while Assistant converts one clip at a time.
