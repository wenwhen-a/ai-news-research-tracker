# Part B — Research → Product: China group (Tencent, ByteDance/TikTok, miHoYo/HoYoverse, NetEase, Alibaba, Baidu, Kuaishou)

Window: 2026-08-18 to 2026-11-16. Re-checked all product_seen.json entries for these companies against their primary sources; searched for new qualifying releases across the listed company surfaces.

## New products this window

### Kling 4.0 Flash API
- **Company:** Kuaishou (Kling)
- **Status:** GA · **Released:** 2026-11-04 · **New**
- **Surface:** Cloud API (Kling developer API)
- **Primary source:** https://kling.ai/document-api/updates/api.md
- **Underlying research:** arXiv:2512.16776, "Kling-Omni Technical Report" (Kling Team, Kuaishou Technology) — the closest technical disclosure Kuaishou has published for the Kling model family; the API changelog does not itself name a paper for the Flash variant specifically.
- **Availability:** Self-serve via the Kling developer API, no invitation mentioned in the changelog entry. Billing stated as based on total generated duration; the changelog does not give a per-second price (third-party resellers quote ~$0.09/sec at 720p, but that figure is unverified against Kuaishou's own pricing page, so it is omitted from the facts above).

**What shipped (≤3 sentences):** Kuaishou's Kling developer-API changelog records a new, separate Kling 4.0 Flash API endpoint (dated 2026-11-04), generating 3–20 second videos at 720P. It supports text-to-video, image-to-video (single first-frame image), and omni reference-to-video, with omni tasks accepting up to 15 reference inputs. This is distinct from the full Kling 4.0 model (up to 30s, 720P/1080P) that reached full global launch on 2026-10-15/10-28 and is already logged in product_seen.json.

**What research it translates (≤3 sentences):** Kuaishou's most recent public technical report for the Kling line is the Kling-Omni Technical Report (arXiv:2512.16776, Dec 2025), describing a unified multimodal-visual-language system combining generation, editing and reasoning with two-stage distillation for faster long-sequence inference. The Flash variant's smaller/faster profile is consistent with that report's stated efficiency work, but Kuaishou has not published a paper naming "Kling 4.0 Flash" specifically, so the link is inferred from the product family, not a direct citation.

**Practical significance (≤3 sentences):** Kuaishou states Flash is a faster, lower-latency tier of the same Kling 4.0 generation alongside the full model, giving API developers a cheaper/quicker option for shorter clips without waiting for full 1080p/30s generation. It is reachable today via the same developer-API account used for Kling 4.0, with no separate signup described in the changelog.

**Engineering details (≤3 sentences):** Outputs are capped at 20 seconds versus 30 for the full model, and resolution is fixed at 720P (no 1080P option listed). Reference inputs (omni reference-to-video) accept up to 15 images, matching the ceiling Kuaishou already offers on full Kling 4.0. The changelog gives no SDK, engine-plugin or file-format details beyond the API parameters themselves.

**Limitation / caveats (≤3 sentences):** No official per-second price was found on Kuaishou's own pages during this check; only third-party reseller estimates exist, and at least one aggregator claimed Kuaishou's own API did not yet serve this model, so availability should be reconfirmed directly against klingai.com before relying on it. The "Flash" naming has briefly referred to an early-access build of Kling 4.0 Flash in September/October 2026 (per product_seen.json's existing Kling 4.0 entry), so this November API listing could represent a re-launch of that earlier preview rather than an entirely new model — treat the distinction as moderate-confidence.

## Updates to previously-tracked products

None found this window. Re-checked primary sources for every China-group entry in product_seen.json (Tencent: Motus, MagicDawn, GIGA, Hunyuan 3D Cloud API hy-3d-3.1; ByteDance: Seedance 2.5; Alibaba: HappyOyster 1.0 + Adventure/Directing/Acting API endpoints, Wan 3.0, ABot-World, Tripo pipeline tools; Kuaishou: Kling 4.0; NetEase: Justice Online: New World) — none showed a tier change, new major version, new-platform availability, or pricing/licensing change dated within the last 7 days (2026-11-09 to 2026-11-16). MagicDawn's product page is unchanged since the 2026-10-05 update already on file; Tencent Cloud's Hunyuan product page still lists hy-3d-3.1 as current with no newer version; Alibaba Cloud Model Studio's "newly released models" table shows no new 3D/world-model entries after 2026-10-27 (only unrelated LLM releases such as qwen4-max); Kling's own API changelog shows only a minor aspect-ratio parameter addition (2026-11-14) on top of already-logged Kling 4.0, which is not material enough to count as an update.

### Announced only (not yet usable)
- Nodusfall (dark-fantasy co-op action RPG built on Unreal Engine 5, a departure from HoYoverse's Unity-based titles) · miHoYo/HoYoverse · revealed 2026-08-25 at Gamescom Opening Night Live · https://nodusfall.hoyoverse.com — pre-registration only, no release date or confirmed platform list beyond "PC" stated by some outlets; engine detail not confirmed on the official site itself at time of check.

Near-misses: 5 — Baidu Apollo World (world model, but for autonomous-driving/robotics simulation, not 3D/gaming — out of this tracker's topic scope); ByteDance real-time 3D "world model" for Pico headsets (Bloomberg-reported, no ByteDance primary-source confirmation — unverified); ByteDance DreamActor-M2 (SIGGRAPH 2026 character-animation paper hosted only via arXiv and third-party Replicate, no official ByteDance product page — tracked in Part A); ByteDance Seedream 5.5 (image-editing model, outside the 3D/world-model/animation/engine scope); Tencent HY-Motion 1.0 (open-weights text-to-3D-motion release on GitHub/Hugging Face, and released Dec 2025 — out of window and belongs in Part A, not Part B).
