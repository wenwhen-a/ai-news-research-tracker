**[B02] Roblox Studio — CreateSurfaceAppearance: Asset IDs and DataModel Content**
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta, opt-in) · **Released:** 2026-11-05 · **New**
- **Surface:** engine / studio tool (3D material API)
- **Primary source:** <https://devforum.roblox.com/t/studio-beta-createsurfaceappearance-now-with-asset-ids-and-datamodel-content/4977713>
- **Underlying research:** no traceable paper
- **Availability:** Opt-in via Studio File > Beta Features ("Mixed Content for CreateSurfaceAppearanceAsync"); not yet live in published experiences (server-side EditableImage maps don't replicate yet).

**What shipped:** Roblox extended `AssetService:CreateSurfaceAppearanceAsync`, which previously accepted only `EditableImage` maps, so a single call can now mix `EditableImage`, DataModel Content, and published Asset IDs for the same material's color/emissive/metalness maps.
**What research it translates:** This is an engine/runtime API extension, not a published research result; Roblox states no model or paper behind it.
**Practical significance:** Roblox states creators can now use published images directly in a `SurfaceAppearance` without first converting them to `EditableImage`, which it says lowers memory use because assets are transcoded to a more efficient format; creators can also convert a painted/generated image to DataModel Content and share it with every player on a server.
**Engineering details:** Mixing DataModel Content or Asset IDs for a new map combination costs a few seconds of baking the first time it's used in a session.
**Limitation / caveats:** Server-side `EditableImage` maps do not yet replicate to clients, which see a checkerboard placeholder instead.
