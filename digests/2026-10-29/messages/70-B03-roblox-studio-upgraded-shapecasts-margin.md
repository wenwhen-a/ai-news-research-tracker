**[B03] Roblox Studio — Upgraded Shapecasts (Margins, Size Gradients, CFrame/size overrides)**
- **Company:** Roblox
- **Status:** GA · **Released:** 2026-10-28 · **New**
- **Surface:** engine/physics API (Roblox Studio + live games)
- **Primary source:** <https://devforum.roblox.com/t/upgrading-shapecasts-margins-size-gradients-optimizations-and-more/4963119>
- **Underlying research:** no traceable paper
- **Availability:** Live now in Studio and published games automatically for existing Blockcast/Spherecast/Shapecast calls (no opt-in needed); new `RaycastParams.Margin`, `RaycastParams.SizeGradient`, and `cframeOverride`/`sizeOverride` parameters on `WorldRoot:Shapecast` available now; in-Studio cast visualization via Visualization Modes or `settings().Physics.DrawShapecast`

**What shipped:** Roblox shipped a rewritten shapecast implementation (Blockcast, Spherecast, Shapecast) adding a `Margin` parameter that "inflates the cast shape by a constant distance in every direction," a `SizeGradient` parameter, CFrame/size override parameters, and new in-Studio visualization of cast shapes.
**What research it translates:** Not research-derived; this is an internal physics-engine optimization, so "no traceable paper" applies.
**Practical significance:** Roblox states existing calls automatically "run on a new implementation that is faster and more accurate, with no changes needed on your end," with casts running "up to 4.1× quicker," letting developers use more shapecasts per frame (e.g. melee hit detection, ground checks) without a performance penalty.
**Engineering details:** Ships as changes to `BasePart`/`WorldRoot` shapecast APIs and new `RaycastParams` fields; visualization is Studio-only, toggled under Visualization Modes > Physics Simulation > Shapecasts or via a plugin/Command Bar property.
