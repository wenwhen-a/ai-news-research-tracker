**[B01] Studio MCP Server — Open Cloud Access & Asset Import (Roblox)**
- **Company:** Roblox
- **Status:** GA · **Released:** 2026-11-04 · **New**
- **Surface:** Studio dev tool / AI agent integration (external MCP clients, e.g. Claude Code)
- **Primary source:** <https://devforum.roblox.com/t/studio-mcp-server-updates-open-cloud-access-in-your-mcp-client-and-asset-import-workflows/4975849>
- **Underlying research:** no traceable paper
- **Availability:** Works with external MCP (Model Context Protocol) clients such as Claude Code; Roblox states it does not apply to Studio's own built-in Assistant. Free platform feature; permissions are configured per game and saved per account, with collaborators setting their own.

**What shipped:** Roblox expanded its Studio MCP server, which lets external AI-agent clients connect to Roblox Studio, with a new `open_cloud_invoke` tool that calls Open Cloud APIs (creating developer products/game passes, changing game/place settings, publishing, restarting servers, reading analytics, calling allowlisted external APIs) and a new asset-import workflow that lets an agent bring in a Blender/Maya model (GLB/FBX) and correct its scale, rotation, textures, colors, anchoring and placement.
**What research it translates:** This is an engineering/product update to Roblox's own AI-agent tooling, not a published research result; Roblox does not cite an underlying paper.
**Practical significance:** A Roblox developer can now let an AI coding agent (Roblox's example: Claude Code) not just edit code in Studio but also call Roblox's Open Cloud platform APIs and import ready-made 3D assets from external tools, within permissions the developer explicitly grants per game.
