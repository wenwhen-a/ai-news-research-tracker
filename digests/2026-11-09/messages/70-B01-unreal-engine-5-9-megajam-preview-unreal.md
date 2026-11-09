**[B01] Unreal Engine 5.9 "MegaJam Preview" (Unreal Canvas, in-editor Unreal MCP, Unreal Assistant)**
- **Company:** Epic Games
- **Status:** Public beta/preview · **Released:** 2026-11-09 · **New**
- **Surface:** engine (downloadable preview build)
- **Primary source:** <https://forums.unrealengine.com/t/unreal-engine-5-9-megajam-preview/2852840>
- **Underlying research:** no traceable paper (Unreal Canvas and the AI tooling wrap third-party/user-supplied API keys rather than a named Epic research model)
- **Availability:** Free download for anyone via Epic Games Launcher, GitHub, or a separate Linux build; no invitation or waitlist. Built ahead of the Nov 12–15, 2026 Epic AI MegaJam but explicitly not jam-limited.

**What shipped:** Epic released a public preview build of Unreal Engine 5.9, which it says was built "primarily with AI agents, with engineers directing and reviewing the work." The build ships an experimental Unreal MCP that now starts automatically with the editor (toolsets for rendering, profiling, audio, UI, level creation and more), an "Unreal Assistant" that connects external AI coding agents (Claude Code, Codex, Cursor, OpenCode) to the editor, and "Unreal Canvas," an experimental tool for generating concept art, images, 3D meshes and video from a creator's own API keys.
**What research it translates:** Epic does not cite a specific paper; the release frames the tooling as agent-assisted engine development (AI agents used to build the preview itself) plus bring-your-own-model integration points (Unreal Canvas, Unreal Assistant) rather than a single in-house trained model being shipped.
**Practical significance:** Any Unreal developer can download this today and test MCP-driven editor automation or AI-assisted asset generation against a non-production copy of a project; Epic explicitly recommends against converting a main project given the build's instability.
