# Part B — Research → Product
Window: last 90 days (2026-08-18 to 2026-11-16). Qualifying products: 1 (1 new, 0 previously reported, 0 flagged). Announced-only: 2. Open releases moved to Part A: 0.

---
## Kling 4.0 Flash API
- **Company:** Kuaishou (Kling)
- **Status:** GA · **Released:** 2026-11-04 · **New**
- **Surface:** Cloud API (Kling developer API)
- **Primary source:** https://kling.ai/document-api/updates/api.md
- **Underlying research:** arXiv:2512.16776, "Kling-Omni Technical Report" (Kling Team, Kuaishou Technology) — inferred from the product family; Kuaishou has not published a paper naming "Kling 4.0 Flash" specifically
- **Availability:** Self-serve via the Kling developer API, no invitation mentioned in the changelog; billing is based on total generated duration (no official per-second price published)

**What shipped (≤3 sentences):** Kuaishou's Kling developer-API changelog records a new, separate Kling 4.0 Flash API endpoint (dated 2026-11-04), generating 3–20 second videos at 720P. It supports text-to-video, image-to-video (single first-frame image), and omni reference-to-video accepting up to 15 reference inputs. This is distinct from the full Kling 4.0 model (up to 30s, 720P/1080P) that reached full global launch on 2026-10-15/10-28 and is already logged as a prior entry.

**What research it translates (≤3 sentences):** Kuaishou's most recent public technical report for the Kling line is the Kling-Omni Technical Report (arXiv:2512.16776, Dec 2025), describing a unified multimodal system combining generation, editing and reasoning with two-stage distillation for faster long-sequence inference. The Flash variant's smaller/faster profile is consistent with that report's stated efficiency work, but the link is inferred from the product family, not a direct citation.

**Practical significance (≤3 sentences):** Kuaishou states Flash is a faster, lower-latency tier of the same Kling 4.0 generation alongside the full model, giving API developers a cheaper/quicker option for shorter clips without waiting for full 1080p/30s generation. It is reachable today via the same developer-API account already used for Kling 4.0, with no separate signup described in the changelog.

**Engineering details (≤3 sentences):** Outputs are capped at 20 seconds versus 30 for the full model, and resolution is fixed at 720P (no 1080P option listed). Reference inputs (omni reference-to-video) accept up to 15 images, matching the ceiling Kuaishou already offers on full Kling 4.0.

**Limitation / caveats (≤3 sentences):** No official per-second price was found on Kuaishou's own pages during this check; only unverified third-party reseller estimates exist, so availability/pricing should be reconfirmed directly against klingai.com before relying on it. The "Flash" naming previously referred to an early-access build of Kling 4.0 Flash in September/October 2026, so this November API listing may represent a re-launch of that earlier preview rather than an entirely new model (moderate confidence).

### Announced only (not yet usable)
- Nodusfall (dark-fantasy co-op action RPG, reportedly built on Unreal Engine 5) · miHoYo/HoYoverse · revealed 2026-08-25 · https://nodusfall.hoyoverse.com
- Genie 4 (real-time world model with native spatial audio, built on Gemini Omni) · Google DeepMind · 2026-10-27 · https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/

Near-misses: 11 — Baidu Apollo World (autonomous-driving world model, out of topic scope); ByteDance Pico world model (Bloomberg leak, unconfirmed); ByteDance DreamActor-M2 (research/third-party host only, belongs in Part A); ByteDance Seedream 5.5 (image editing, out of topic scope); Tencent HY-Motion 1.0 (open-weights, out of window, belongs in Part A); Sony XYN Spatial Scan / Spatial Scan Navi v1.1.0→v1.2.0 (minor point-version bumps only, no disclosed feature list); Microsoft TRELLIS.2 (open-weights research artifact, no confirmed product integration); Adobe Firefly Graph beta (general AI-workflow tool, 3D support only "on the roadmap"); NVIDIA GR00T 2 / Isaac Lab 3.0 (robotics/physical-AI, out of scope); Epic UE/MetaHuman EULA change allowing AI training on projects (licensing term, not a shipped feature).

Verification: every listed item was re-checked against its stated primary source (release date, releasing company, status tier, and every claim in its five blocks) before inclusion; three dedicated sweeps covered Western big tech/publishers, NVIDIA/Adobe/engines, and Chinese tech companies respectively, plus a re-check of every `product_seen.json` entry in each group's company list for material updates.
