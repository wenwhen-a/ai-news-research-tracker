**[B01] Roblox Engine — Minimum Draw Distance Raised to 500 Studs + Auto-Quality Level Improvements**
- **Company:** Roblox
- **Status:** GA · **Released:** 2026-11-05 · **New**
- **Surface:** engine (client rendering)
- **Primary source:** <https://devforum.roblox.com/t/increasing-the-minimum-draw-distance-to-500-studs-and-other-auto-quality-level-improvements/4977292>
- **Underlying research:** no traceable paper
- **Availability:** Automatic rollout to every Roblox experience; no creator opt-in required.

**What shipped:** Roblox's Rendering team raised the minimum draw distance at the lowest automatic quality level from 200 to 500 studs, with faster ramp-up across the first few quality levels (first four auto levels move from 200/250/300/450 studs to 500/800/1200/1600 studs).
**What research it translates:** No paper or named model underlies this; it is an internal engineering optimization.
**Practical significance:** Players on the lowest auto-detected quality tier now see roughly 2.5x further by default, addressing a gap where low-end/mobile devices rendered a visibly smaller world than higher-tier devices.
**Engineering details:** Affects Roblox's internal auto quality-level (QL) system across both draw distance and terrain/beam rendering paths.
**Limitation / caveats:** Roblox's post frames several related items as future work, not yet shipped: particle emitter `Rate` still scales aggressively by quality level, and creators do not yet have a way to flag which parts of a scene matter most to the auto-quality system.
