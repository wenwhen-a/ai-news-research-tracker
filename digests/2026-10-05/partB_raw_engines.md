# Part B — Research → Product: NVIDIA / Adobe / Unity / Epic / Roblox / AMD / Autodesk group
Window: 2026-07-07 to 2026-10-05 (today 2026-10-05 UTC)
Scope: NVIDIA, Adobe, Unity, Epic Games, Roblox, AMD, Autodesk (borderline, flagged)
Topics: 3D generation/reconstruction, world models, character animation/motion, game engines/rendering

## Summary of findings
This group already has extensive coverage in `state/product_seen.json` (through 2026-10-03/10-04 entries: Gears of War E-Day DLSS 4.5, Frustum Streaming, Kling 4.0, etc.). Re-checked all primary sources for this group through 2026-10-05. **Three new qualifying items** (1 AMD, 2 Roblox) — no tier changes or material updates were found on any already-tracked item for NVIDIA, Adobe, Unity, Epic Games, AMD or Autodesk. One new Announced-only item (Roblox Terrain Updates, invite-gated early access). Several leads could not be confirmed against a primary source and are logged as near-misses.

### Already-tracked items re-checked for updates (no material change found)
- NVIDIA — GeForce news latest entry remains the already-tracked Gears of War: E-Day DLSS 4.5 / RTX Mega Geometry post (2026-10-01); developer.nvidia.com/blog and docs.omniverse.nvidia.com/dev-guide (Kit release notes, "Last updated Oct 02 2026") show no Kit/Isaac/RTX Kit/ACE entry newer than the already-tracked Kit 110.3 / Isaac Sim 6.1 / RTX Kit 2026.3 items. No new NVIDIA item found after 2026-10-03.
- Adobe — blog.adobe.com/en/topics/3d's newest post is still "Adobe Substance 3D unveils new innovations... OpenPBR everywhere" (2026-07-21), the already-tracked item. Nothing newer found.
- Unity — unity.com/blog/unite-seoul-keynote-2026-recap (the already-tracked Unity 7 Announced-only source) now gives a specific timeline: "The Unity 7 Preview launches in December [2026]... with full release targeted for Q1 next year [2027]... and some features arriving earlier in beta." This is new detail but not a tier change — nothing has shipped yet, so it stays Announced-only; no update entry written.
- Epic Games — could not confirm or rule out a Fortnite/UEFN v43.x release; dev.epicgames.com documentation pages returned only empty table-of-contents shells to the fetcher and unrealengine.com/en-US and /news returned HTTP 403 on every attempt. No v43.x or UE 5.9 release was confirmed from a primary source (see near-misses for UE 5.9 lead).
- AMD — gpuopen.com homepage/blog checked for Jul–Oct 2026; FSR SDK 2.3 (already tracked) has no newer SDK version, but a related **new** item was found (AMD FSR plugin for Unreal Engine 5.8 — see below).
- Autodesk — could not reach area.autodesk.com, autodesk.com/products/maya pages (403) or find an Autodesk-owned page confirming the Maya MotionMaker "Bring Your Own Data" / ML Deformer features reported by trade press at SIGGRAPH 2026; logged as a near-miss (unverified). No update found to the already-tracked 3ds Max 2027.2 Gaussian Splat item.
- Roblox — devforum.roblox.com/c/updates/announcements walked in full for late Sept–early Oct 2026. The Scene Generator, NPC Dynamic Behavior / New Default Movement, and Creator Roadmap 2026 Fall Update roadmap items (all already tracked as Announced-only) have no devforum post indicating they shipped to beta or GA. Two new items qualified (see below) plus one new Announced-only item (Terrain Updates).

---

## AMD FSR plugin for Unreal Engine 5.8
- **Company:** AMD (FLAG: borderline per product-criteria.md)
- **Status:** GA · **Released:** 2026-08-27 · **New**
- **Surface:** Official Unreal Engine 5.8 plugin (FidelityFX integration)
- **Primary source:** https://gpuopen.com/learn/amd-fsr-plugin-updated-for-unreal-engine-58/
- **Underlying research:** no traceable paper
- **Availability:** Free, public Unreal Engine 5.8 plugin distributed via AMD's FidelityFX framework; bundles FSR Upscaling 4.1.1, FSR Frame Generation 4.0.1 and FSR Ray Regeneration 1.2. Supports AMD Radeon RX 9000 Series (RDNA 4) and, newly with this update, AMD Radeon RX 7000 Series (RDNA 3); older GPUs fall back to the non-ML FSR 3 analytical path. No waitlist; updates can also be pushed later via AMD Software: Adrenalin Edition without a game patch.

**What shipped (≤3 sentences):** AMD updated its official FidelityFX Super Resolution plugin for Unreal Engine 5.8, extending the ML-based FSR Upscaling 4.1.1 and Frame Generation 4.0.1 pipeline — previously RDNA4-only in-engine — to also run on RDNA 3 (Radeon RX 7000 Series) cards inside UE5.8 projects. The update improves motion-vector input handling and adds FidelityFX API hooks so the bundled FSR components can be refreshed by a driver update rather than a new game build.

**What research it translates (≤3 sentences):** This packages AMD's existing FSR 4.1.1 ML upscaling and temporal frame-generation techniques (already shipped as the standalone FSR SDK 2.3, tracked separately, released 2026-06-24) directly into Epic's engine as a first-party plugin rather than requiring per-title custom integration. No specific arXiv paper underlies this engine-plugin packaging work.

**Practical significance (≤3 sentences):** Any Unreal Engine 5.8 developer can now enable ML-based FSR upscaling and frame generation for RDNA 3 GPU owners without writing custom FidelityFX integration code, lowering the bar for RDNA 3 (not just the newer RDNA 4) players to get AMD's AI upscaler in UE5.8 titles. AMD frames this as closing the gap between the SDK-level RDNA 3 support (June 2026) and actual in-engine availability for Unreal developers.

**Engineering details (≤3 sentences):** The plugin exposes FSR Upscaling 4.1.1, FSR Frame Generation 4.0.1 and FSR Ray Regeneration 1.2 through Unreal Engine's native plugin system; FidelityFX API hooks allow AMD Software: Adrenalin Edition to push future FSR component updates without a new game build. Supported hardware tiers are RDNA 4 (full ML path), RDNA 3 (newly added ML path), and older GPUs (FSR 3 analytical fallback).

**Limitation / caveats (≤3 sentences):** This is an engine-plugin release, not a new FSR algorithm version — the underlying FSR Upscaling 4.1.1 / Frame Generation 4.0.1 / Ray Regeneration 1.2 versions match the already-tracked June 2026 FSR SDK 2.3 release, just newly exposed inside UE5.8. No pricing or licensing terms were stated beyond "free plugin."

---

## Roblox Studio — Expanding the Character Controller Library (Custom Abilities API, new default abilities)
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta) · **Released:** 2026-10-03 (expanded beta post; initial Studio Beta announced 2026-09-10) · **New**
- **Surface:** Roblox Studio / Character Controller Library (CCL)
- **Primary source:** https://devforum.roblox.com/t/studio-beta-expanding-the-character-controller-library-new-default-abilities-custom-abilities-api/4863739
- **Underlying research:** no traceable paper
- **Availability:** Opt-in Studio Beta, cross-platform (keyboard/mouse, gamepad, touch) with platform-specific default keybindings; free for all Roblox creators who opt into the beta.

**What shipped (≤3 sentences):** Roblox expanded its Character Controller Library (CCL) beta with a Custom Abilities API (lifecycle methods OnSetup/OnStart/OnStop/OnUpdate) plus two new default abilities, Sprint and Crouch, and a reworked Shift-Lock called "Configurable Turning." Creators can bind abilities to cross-platform action slots and either extend or fully replace the default ability set, with optional Server Authority for consistency.

**What research it translates (≤3 sentences):** This is an engine/architecture replacement for Roblox's legacy Humanoid movement system rather than a packaged research result; Roblox states the team's "upcoming work includes incorporating animations into the CCL so that they can be driven by abilities directly," linking it to the still-Announced-only "New Default Movement" (motion matching + root motion) roadmap item. No underlying paper is cited.

**Practical significance (≤3 sentences):** Roblox states CCL characters run "10% to 25% faster" than legacy Humanoid during active gameplay and "up to 1.5x faster" during steady motion, and that walk animations driven by the new system are "already deployed on mobile and console platforms." Creators get a documented, cross-platform input/ability framework instead of hand-rolling movement scripts per platform.

**Engineering details (≤3 sentences):** The Custom Abilities API supports Press/Hold/Toggle/Repeat input bindings mapped automatically across keyboard, gamepad and touch; Server Authority can be enabled per-ability for networked consistency. Blended animations for locomotion are listed as planned future work, not yet shipped.

**Limitation / caveats (≤3 sentences):** This is still an opt-in Studio Beta, not a default-on system, and Roblox's own post frames animation-driven abilities and blended locomotion as future work, not current functionality. (Borderline on-topic: this item is primarily a movement/input-architecture change, not animation content generation; included here for its stated animation-system roadmap tie-in, observed not stated as a strict qualifier.)

---

## Roblox Marketplace — Create and Sell Animation Packs
- **Company:** Roblox
- **Status:** GA (Full Release) · **Released:** 2026-10-02 (pilot access since 2026-09-09) · **New**
- **Surface:** Roblox Studio / Marketplace (Creator Store)
- **Primary source:** https://devforum.roblox.com/t/full-release-create-and-sell-animation-packs-on-marketplace/4861803
- **Underlying research:** no traceable paper
- **Availability:** Open to verified creators with a Roblox Plus membership; one pack upload per day at launch; marketplace minimum price 300 Robux plus an 80-Robux upload fee; supports Limited editions and group uploads.

**What shipped (≤3 sentences):** Roblox moved "Animation Packs" on its creator Marketplace to full release, letting creators author and sell bundles of custom locomotion animations — covering Idle, Walk, Run, Jump, Fall, Climb and Swim states — for use across any compatible Roblox experience. Animations must be authored/converted to Roblox's CurveAnimation format in Studio, and the platform runs automated validation of movement constraints and runtime limits before publishing.

**What research it translates (≤3 sentences):** This is a creator-economy/marketplace feature for hand-authored or externally-created animation content, not a generative-AI or research-derived capability; Roblox's post describes no AI/ML component. No underlying paper applies.

**Practical significance (≤3 sentences):** Creators can now monetize reusable character-locomotion animation sets across the Roblox catalog rather than building bespoke animations per experience, with ID verification and Roblox Plus required to publish. Roblox states the feature began with a pilot program (access from 2026-09-09) before this full release.

**Engineering details (≤3 sentences):** Animations are stored/uploaded in Roblox's CurveAnimation format; Roblox Studio runs automated checks on movement constraints and runtime limits at upload time. The marketplace enforces a 300-Robux minimum price, an 80-Robux upload fee, and a one-upload-per-day cap at launch.

**Limitation / caveats (≤3 sentences):** No generative or AI component — this is a packaging/distribution feature for existing animation-authoring workflows, which is a weaker fit for the tracker's "character animation/motion" research-to-product bar than, e.g., Roblox's AI-driven Cube/Scene Generator work (observed, not stated). Upload is capped at one pack per day and gated behind ID verification plus a paid membership tier.

---

### Announced only (not yet usable)
- Roblox Terrain Updates (Terrain Scattering, Path Splines, Projected Decals, Virtual Texturing, Signed Distance Fields) · Roblox · 2026-09-30 · https://devforum.roblox.com/t/terrain-updates-object-scattering-path-splines-projected-terrain-decals-and-more/4865617 — currently an early-access **signup** program ("developers can apply to test features as they're added throughout the end of 2026"), invitation-gated, so it fails the "usable today without asking for access" test.

Near-misses: 6
- Unreal Engine 5.9 · announced at Unreal Fest Seoul / State of Unreal 2026 with an AI-features focus (Developer Assistant, Semantic Search, MCP) and improved handheld support, per trade press (pcgameshardware.de, wnhub.io) — could not verify against a primary Epic source (unrealengine.com and dev.epicgames.com returned HTTP 403 or empty content to the fetcher on every attempt this run); excluded as unverified rather than fabricated.
- Autodesk Maya MotionMaker "Bring Your Own Data" + Maya ML Deformer · reported at SIGGRAPH 2026 (~2026-07-23) by trade press (etvbharat.com, creativebloq.com) as letting teams train custom motion-generation models on their own rig/animation data · no Autodesk-owned page could be reached to confirm release/availability status (area.autodesk.com, autodesk.com/products/maya returned 403); excluded as unverified.
- AMD GPUOpen — "Lightweight attention-based indirect illumination" (2026-08-20) — a neural global-illumination technique posted as a GPUOpen technical blog/sample, not a documented shipped product feature; open-source-sample territory (Part A-style), not Part B.
- AMD GPUOpen — "Temporally stable generative illumination with a one-step diffusion model" (2026-09-09) — same pattern: a research/technique blog post with sample code, not a shipped product.
- AMD GPUOpen — "How tetrahedral cages significantly reduce BVH memory usage" (2026-09-17) — ray-tracing technique/sample blog post (demoed on animated plants), not a shipped product feature.
- Roblox — "Expanding WorldModel Simulation Capabilities: Support for Collision Groups" (2026-09-20) — a minor API extension to Roblox's `WorldModel` instance type (a Studio simulation-container object), not an AI/world-model product in the tracker's sense; below the bar for inclusion.

Verification: every item above with a full 5-block entry was checked against the primary source URL listed; AMD and Roblox are the releasing/operating organizations confirmed from those same pages. AMD is a flagged borderline company per `references/product-sources.md`. No item was fabricated; unconfirmable leads were moved to near-misses rather than included.
