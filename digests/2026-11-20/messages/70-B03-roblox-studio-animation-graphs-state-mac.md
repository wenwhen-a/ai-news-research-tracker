**[B03 · Update] Roblox Studio — Animation Graphs: State Machines and Luau Expressions reach Full Release**
- **Company:** Roblox
- **Status:** GA · **Released:** 2026-11-19 · **Update**
- **Surface:** Engine / studio tool (Animation Graph Editor; usable in Studio and live games)
- **Primary source:** <https://devforum.roblox.com/t/full-release-state-machines-and-luau-expressions-in-animation-graphs/4997058>
- **Underlying research:** no traceable paper (internal engine/tooling feature)
- **Availability:** Free, built into Roblox Studio's Animation Graph Editor for all creators; now usable in published, live experiences, not just Studio.

**What shipped:** Update since 2026-10-09: Roblox moved State Machine and Luau Expression nodes in its Animation Graph Editor out of Studio Beta into full release, per a Nov 19 devforum post — a tier change from Public beta/preview to GA.
**What research it translates:** No external research paper; this is a visual node-graph tool for authoring character-animation state machines and inline Luau expressions, built on Roblox's existing Animation Graph system (full-released July 2026).
**Practical significance:** Roblox states creators can now ship these state-machine-driven animation graphs — e.g., combo systems where a swing can only follow another swing, not idle — in live, published games rather than only prototyping them in Studio.
**Engineering details:** Adds live preview that highlights the active state/transition during playtest, immediate application of expression/condition edits without reloading the graph, parameter-less graph wiring, and fixes to state renaming/duplicate-naming bugs.
**Limitation / caveats:** Luau Expressions still cannot use loops, functions, tables, `require()`, method calls, other libraries, or DataModel access — they can only read graph parameters, so gameplay logic must still set those parameters from scripts.
