**[B02] Roblox Studio — Expanding the Character Controller Library (Custom Abilities API, new default abilities)**
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta) · **Released:** 2026-10-03 (expanded beta post; initial Studio Beta announced 2026-09-10) · **New**
- **Surface:** Roblox Studio / Character Controller Library (CCL)
- **Primary source:** <https://devforum.roblox.com/t/studio-beta-expanding-the-character-controller-library-new-default-abilities-custom-abilities-api/4863739>
- **Underlying research:** no traceable paper
- **Availability:** Opt-in Studio Beta, cross-platform (keyboard/mouse, gamepad, touch) with platform-specific default keybindings; free for all Roblox creators who opt into the beta.

**What shipped:** Roblox expanded its Character Controller Library (CCL) beta with a Custom Abilities API (lifecycle methods OnSetup/OnStart/OnStop/OnUpdate) plus two new default abilities, Sprint and Crouch, and a reworked Shift-Lock called "Configurable Turning." Creators can bind abilities to cross-platform action slots and either extend or fully replace the default ability set, with optional Server Authority for consistency.
**What research it translates:** This is an engine/architecture replacement for Roblox's legacy Humanoid movement system rather than a packaged research result; Roblox states upcoming work "includes incorporating animations into the CCL so that they can be driven by abilities directly," linking it to the still-Announced-only "New Default Movement" (motion matching + root motion) roadmap item.
