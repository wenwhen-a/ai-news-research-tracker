# Part B — Research → Product
Window: last 90 days (2026-08-02 to 2026-10-31). Light check (daily primary-surface check; next full sweep: Monday 2026-11-02). Qualifying products: 1 new, 1 updated. Announced-only: 0. Open releases moved to Part A: 0.

---

## Roblox Studio — Prompt-to-Avatar (Generate Game Characters)
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta, opt-in via File > Beta Features) · **Released:** 2026-10-29 · **New**
- **Surface:** studio tool (Avatar Setup panel in Roblox Studio; also exposed via Assistant and Studio MCP)
- **Primary source:** https://devforum.roblox.com/t/studio-beta-generate-game-characters-with-prompt-to-avatar/4964945
- **Underlying research:** arXiv 2503.15475, "Cube: A Roblox View of 3D Intelligence" (Roblox's own foundation-model paper for text-to-shape/text-to-scene 3D generation) — not explicitly cited in this post; Roblox's other text-to-3D tools (Cube 3D Generation, Procedural Models) are built on Cube, but this specific announcement names no underlying model
- **Availability:** Free, opt-in Studio Beta; staged rollout (staff noted full rollout took longer than a day); no stated region restriction

**What shipped (≤3 sentences):** Roblox shipped a beta Avatar Setup tool that generates a full Roblox-ready 3D character model from a text prompt: a creator describes a character, refines a generated 2D concept image, then builds the 3D model with a choice of built-in clothing or a bare body, static or dynamic head, and R15 or Advanced R15 rig.
**What research it translates (≤3 sentences):** Roblox's Cube foundation model (arXiv 2503.15475) describes a 3D shape tokenizer supporting text-to-shape and text-to-scene generation built to work with LLMs for 3D content creation; Prompt-to-Avatar is consistent with that text-to-3D generation lineage already used in Roblox's Cube 3D Generation and Scene Generation tools, though the devforum post does not name Cube directly.
**Practical significance (≤3 sentences):** Roblox states this lets a creator generate a usable, riggable in-game character from a written description instead of modeling or commissioning one, directly inside Studio; generation takes roughly 3-6 minutes (longer with a dynamic head).
**Engineering details (≤3 sentences):** Lives in the Avatar Setup tool, reachable once "Build Avatar (Beta)" is enabled under File > Beta Features; also callable through Assistant and Studio MCP; outputs are constrained to R15/Advanced R15 rigs (no custom rig support).
**Limitation / caveats (≤3 sentences):** Roblox states avatar accessories are not generated in this beta even when shown in the 2D concept, AI-driven animation ("Prompt-to-Animation") is not included and is future work, and quality is still being improved — forum reports cite weak hands/mouths/faces and occasional failed builds needing a retry.

---

## Roblox Scene Generation — Studio Beta launch (update to the RDC 2026 "Scene Generator" announcement)
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta) · **Released:** 2026-10-30 · **Update**
- **Surface:** studio tool (Assistant `/generate_scene` command, or right-click viewport > Generate > Scene, in Roblox Studio)
- **Primary source:** https://devforum.roblox.com/t/introducing-scene-generation-prototype-scenes-faster/4966611 (updates the previously logged key https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play, first_seen 2026-09-17, tier "Announced only")
- **Underlying research:** arXiv 2503.15475, "Cube: A Roblox View of 3D Intelligence" — the paper explicitly reports text-to-scene generation as an application of its shape tokenizer; not cited by name in this devforum post
- **Availability:** Free, Studio-only beta; no stated region restriction or waitlist

**Update since 2026-09-17: what changed.** Roblox's September 11 RDC 2026 announcement described Scene Generator only as something that "will power prompt-to-scene functionality across both Build and Studio" (tier: Announced only, no usable surface). On 2026-10-30, Roblox shipped it as a working Studio Beta feature — a genuine tier change from Announced-only to Public beta/preview, usable today by any opted-in developer with no waitlist.
**What research it translates (≤3 sentences):** Cube's shape tokenizer (arXiv 2503.15475) is described by its authors as supporting "text-to-scene generation" directly, working with existing LLMs for scene analysis; Scene Generation's text/image-to-scene pipeline lines up with that capability, though this post does not name Cube explicitly.
**Practical significance (≤3 sentences):** Roblox states a creator can generate an editable scene — including models, textures and terrain — from a source image, a text prompt, or both, with control over size, position, and whether to use procedural models or meshes, in about 2-3 minutes per generation.
**Engineering details (≤3 sentences):** Accessed via the `/generate_scene` Assistant command or a right-click "Generate > Scene" viewport menu entry in Studio; output is a fully editable scene (not a flattened asset), refinable like any other Studio content.
**Limitation / caveats (≤3 sentences):** This is a Studio-only beta (the original RDC announcement also named the mobile Build app as a future target, not mentioned in this post); no GA date, pricing, or Build-app availability is stated yet.

### Announced only (not yet usable)
(none this window)

Near-misses: 3 — (1) Roblox Studio Beta "Build 2D, Isometric, and Top-Down Games With Orthographic Camera" (2026-10-30) — a genuine new engine capability (`Camera.ProjectionType = Orthographic`) but no AI/research link and materially thin (a single camera-projection toggle), so kept as a near-miss rather than a full item. (2) NVIDIA GeForce News, "Phantom Blade Zero Launches Today For GeForce RTX & RTX Spark" (2026-10-28/29) — ships the already-logged DLSS 4.5 / path-tracing / Ray Reconstruction feature set in a newly launched game, which is "one more game adopting an existing feature," not a new capability. (3) NVIDIA GeForce News, "Experience Minecraft With Path Tracing and DLSS – RTX Remix 1.6 Available Now" (2026-10-28) — same URL/content already logged as an update in `product_seen.json` on 2026-10-26/28; unchanged, not re-listed.

Verification: each item above was checked on its own primary page for publication date, tier/access requirements, and stated company; the Scene Generation item was cross-checked against the existing `product_seen.json` entry it updates. arXiv citation (2503.15475) was verified via direct web search of the paper itself; it is flagged in both items as not explicitly named in the Roblox posts themselves, to avoid inferring a model link from topic similarity alone.
