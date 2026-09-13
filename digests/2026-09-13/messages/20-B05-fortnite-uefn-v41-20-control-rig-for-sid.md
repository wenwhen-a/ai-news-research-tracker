**[B05] Fortnite / UEFN v41.20 — Control Rig for Sidekicks, in-world UMG widgets, LLM-powered NPCs**
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-07-16 (LLM NPC publishing exits Experimental 2026-07-30) · **New**
- **Surface:** shipped game / creator tool (UEFN)
- **Primary source:** https://dev.epicgames.com/documentation/fortnite/41-20-fortnite-ecosystem-updates-and-release-notes-in-fortnite
- **Underlying research:** no traceable paper
- **Availability:** Live for all UEFN creators; LLM-powered NPC islands publishable from 2026-07-30.

**What shipped:** Epic's release notes state Control Rig support for Sidekicks arrives with "three archetypes — Dog Large, Dog Small, and Cat Small" built on Epic's internal rig structures; creators can "drag your UMG User Widget from the content browser into the viewport to display your UI in the level"; and on July 30 LLM conversations "exit Experimental and you'll be able to publish islands with LLM-powered NPCs and characters."
**What research it translates:** Epic's internal animation-rig tooling exposed to creators, and an LLM dialogue system for NPCs moving from experimental to publishable status.
**Practical significance:** Epic states it provides "consistent voices and personas to 36 Fortnite characters when used as NPCs," so creators can ship voiced, LLM-driven NPCs without engine code.
**Engineering details:** Control Rig limited to the three archetypes at launch; in-world widgets keep existing UMG functionality including Verse fields and UI animations.
**Limitation / caveats:** Epic states 36 characters get voices "with more coming over time," so coverage is partial at launch.
