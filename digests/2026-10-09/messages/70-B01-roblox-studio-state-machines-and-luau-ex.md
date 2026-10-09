**[B01] Roblox Studio — State Machines and Luau Expressions for Animation Graphs (beta)**
- **Company:** Roblox
- **Status:** Public beta/preview · **Released:** 2026-10-08 · **New**
- **Surface:** Studio tool (character-animation tooling, built into the game engine's Animation Graph Editor)
- **Primary source:** <https://devforum.roblox.com/t/studio-beta-introducing-state-machines-and-luau-expressions-for-animation-graphs/4921939>
- **Underlying research:** no traceable paper
- **Availability:** Opt-in via Studio → File → Beta Features → "Animation Graphs State Machines"; Roblox's FAQ states the features currently work only in Studio, not in live/published experiences.

**What shipped:** Roblox added two new node types to its Animation Graph Editor: State Machine nodes, which let creators define animation states and the transitions between them visually, and Luau Expression nodes, which let creators write parameter math (e.g., blend weights, transition conditions) as a line of Luau inside the graph.
**What research it translates:** No paper or research blog post is cited; this extends Roblox's existing node-based Animation Graph Editor (itself out of beta and fully released since 2026-07-15, per `product_seen.json`) rather than introducing a new ML model.
**Practical significance:** Roblox states scripts still call `SetParameter()` to drive the graph, but transition logic that previously had to live in script can now live in the graph itself, via Luau-expression conditions or "wait for state to finish" transitions with per-transition blend Length/Curve and unique Priority values.
**Engineering details:** Transitions from an (Any) state can fire regardless of current state, and conflicting transitions resolve by highest (unique) Priority; expressions are parsed once when the graph loads and are saved with the graph asset.
