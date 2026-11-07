# Part B — Research → Product
Window: last 90 days (2026-08-09 to 2026-11-07). Retrieval: light check (not the Monday full sweep) — ~10 primary surfaces checked for the last 7 days (NVIDIA developer blog & GeForce news, Unreal Engine news/forums, Unity blog & release notes, Roblox newsroom & devforum, Adobe blog, Tencent Hunyuan, ByteDance Volcano Engine/Seed, Alibaba Cloud blog/Model Studio, Kuaishou Kling, PlayStation Blog). Products: 2 new, 0 updated.

---
## Fortnite / UEFN v43.00 — Procedural Content Generation, IK Retargeter, Gaussian-splat import
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-11-01 · **New**
- **Surface:** shipped game / creator platform (Fortnite / Unreal Editor for Fortnite)
- **Primary source:** https://forums.unrealengine.com/t/fortnite-ecosystem-v43-00/2848257
- **Underlying research:** no traceable paper
- **Availability:** Live now for all UEFN creators, free. Gaussian-splat import and the Verse Health and Damage Pipeline are marked Experimental. PCG-graph creation/editing and the new animation/profiling toolsets are reachable by AI coding agents through UEFN's MCP server.

**What shipped (≤3 sentences):** Epic shipped Fortnite Ecosystem v43.00, adding Procedural Content Generation (PCG) to UEFN for automated large-world asset placement ("detailed worlds, like forests, cities, and custom points of interest"), an IK Retargeter that lets creators reuse existing animations — including on NPCs — on custom characters "with less manual setup," and Sequencer improvements for camera setup, character animation and cutscene editing. The release also adds an Experimental Gaussian-splat import path for photoreal real-world scenes and lets AI agents create and edit PCG graphs directly through UEFN's MCP server.
**What research it translates (≤3 sentences):** The forum release notes name no underlying research paper for PCG, IK Retargeter or Gaussian-splat import — "no traceable paper."
**Practical significance (≤3 sentences):** A UEFN creator can populate large worlds automatically instead of hand-placing assets, retarget existing animation libraries onto new custom or NPC characters without re-rigging, and — per Epic — have an AI agent generate or edit PCG graphs via MCP, extending the agent-tool-calling pattern Epic introduced for UEFN earlier in 2026 into world-building and animation workflows.
**Engineering details (≤3 sentences):** Gaussian-splat import and the Verse Health and Damage Pipeline ship as Experimental; PCG and IK Retargeter ship as standard tools. MCP gains new toolsets for profiling (Timing Insights, Verse Insights, Memory Snapshot, Spatial Profiler), MetaSound audio import, and the animation tools above; the release also adds USD file import and Chaos outfit/cloth asset creation in UEFN.
**Limitation / caveats (≤3 sentences):** Gaussian-splat import and the Health and Damage Pipeline are explicitly marked Experimental (not production-ready). The release notes do not quantify IK Retargeter's or PCG's output quality, failure modes, or performance cost.

---
## Roblox Studio — Generate R15 Animations From a Prompt (Prompt to Animation + R6 Motion Rebuilder)
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta) · **Released:** 2026-11-05 · **New**
- **Surface:** Studio dev tool (Assistant / Studio MCP)
- **Primary source:** https://devforum.roblox.com/t/studio-beta-generate-r15-animations-from-a-prompt-plus-optional-r6-motion-rebuilder/4977709
- **Underlying research:** no traceable paper
- **Availability:** Opt-in Studio Beta (File > Beta Features > "Animation Generation in Assistant"); reachable via Assistant's `/generate_animation` command or Studio MCP's `generate_animation` tool; free during the beta; capped at four generations per account per minute, subject to change before full release.

**What shipped (≤3 sentences):** Roblox shipped a Studio Beta feature that generates an R15 animation clip from a written description of a movement ("Prompt to Animation"), plus an optional "Motion Rebuilder" that converts an existing R6 animation into an R15 version as a new asset, leaving the original R6 clip unchanged.
**What research it translates (≤3 sentences):** Roblox's devforum post names no underlying paper for either tool — "no traceable paper."
**Practical significance (≤3 sentences):** A creator can describe a motion in plain language inside Studio's Assistant — or have an external AI agent call it via Studio MCP's `generate_animation` tool — and get a usable R15 clip in about 20–30 seconds without hand-authoring keyframes or sourcing mocap, and separately upgrade older R6-rig animations to R15 automatically instead of re-animating them.
**Engineering details (≤3 sentences):** Works only with humanoid rigs and standard R15 output (Advanced R15 unsupported); via Studio MCP an agent can specify a rig and clip length up to 10 seconds, or an R6 animation asset ID to convert; Studio MCP can process lists of R6 clips (rate-limited) while Assistant converts one clip at a time.
**Limitation / caveats (≤3 sentences):** Per Roblox: Prompt to Animation does not yet play correctly on R6 rigs; some R6-to-R15 conversions bend knees or elbows the wrong way or show stretching on skinned characters; key-pose editing on the Mannequin rig can be inconsistent and "Edit in Assistant" only works on clips these tools created; and complex moves (swimming, golf swings) remain difficult for the models.

### Announced only (not yet usable)
(none)

Near-misses: 7 (NVIDIA Nov-4 WoW/RTX Spark driver post — same DLSS 5 rollout already logged as a 2026-11-05 update on the existing NBA 2K27 entry, nothing new; PlayStation Blog's Assassin's Creed Valhalla PSSR post — another game adopting an already-tracked feature, not a reportable update; Unity 6000.6.8f1 — maintenance patch, no new AI/3D feature; Unreal Engine 5.9 — only third-party press, no Epic primary source found, dropped as unverifiable; NVIDIA's Nov-2 Cosmos blog — robotics/AV/surgical-simulation focus, not a game-industry product, same near-miss as the prior day's check; two Roblox DevForum engine/API posts (CreateSurfaceAppearance asset IDs; minimum draw distance) — no stated AI/research link; Fab bundle additions and Fortnite v43.00's non-topic items — off-topic for the four tracked areas).
Verification: both new items above were fetched and read in full from their primary sources (forums.unrealengine.com and devforum.roblox.com) before being written up; both primary-source URLs were confirmed absent from `state/product_seen.json` prior to inclusion. Surfaces also checked with no qualifying items: Adobe blog/research.adobe.com, Tencent Hunyuan, ByteDance Seed/Volcano Engine, Alibaba Cloud Model Studio, Kuaishou Kling.
