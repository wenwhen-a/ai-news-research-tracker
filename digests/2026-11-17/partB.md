# Part B — Research → Product
Window: last 90 days (2026-08-19 to 2026-11-17). Retrieval: daily light check (10 primary surfaces; Unreal Engine's own news/forum pages returned 403/404, corroborated via web search instead). Products: 1 new, 0 updated.

---
## Kling Image 4.0 API
- **Company:** Kuaishou
- **Status:** GA · **Released:** 2026-11-17 · **New**
- **Surface:** cloud API
- **Primary source:** https://kling.ai/document-api/updates/api.md
- **Underlying research:** no traceable paper
- **Availability:** Available now via the Kling API (`/image-generation/kling-4.0` for text-to-image/image-to-image/image sets, `/long-image-generation/kling-4.0` for long-image generation); billing now counts both input reference images and output images, rate varies by resolution; no specific pricing figures given in the changelog itself (points to a separate pricing page).

**What shipped (≤3 sentences):** Kuaishou shipped Kling Image 4.0, succeeding Kling Image 3.0, via new API endpoints for standard and long-image generation. The changelog states native 8K resolution (up from 3.0's native 4K), improved realism, text rendering and instruction-following, and up to 10 combined image/subject references.
**What research it translates (≤3 sentences):** No underlying paper is cited or traceable; this is a direct API version upgrade of Kuaishou's existing Kling Image line.
**Practical significance (≤3 sentences):** Per Kling's own API changelog, this is a full major-version jump (3.0→4.0) in image-generation resolution and reference handling, directly comparable to the already-tracked Kling 4.0 video-generation line. The long-image endpoint is aimed at e-commerce and web-design use cases.
**Engineering details (≤3 sentences):** Supports 2K/4K/8K output for single images and image sets (`settings.series_amount` 2–10 or auto), 1K/2K for long images, prompts up to 50,000 characters in English (21,000 for non-English), and asynchronous task status via `GET /tasks`.
**Limitation / caveats (≤3 sentences):** No pricing figures are given in the changelog itself; no independent third-party coverage was found yet confirming the stated quality improvements.

### Announced only (not yet usable)
(none)

Near-misses: 9 (Sony QSSR rollout to more games — not a tier change; NVIDIA DLSS 5 in Where Winds Meet — still scheduled for Nov 23, not yet shipped; Unreal Engine 5.9 "MegaJam Preview" — shipped Nov 9, one day outside the window and already baseline; several Roblox Studio-beta devforum posts dated Nov 9–11 that duplicate already-reported items verbatim; Adobe Substance 3D/Firefly — no new in-window primary-source confirmation beyond the existing Nov 13 baseline entry; Tencent Motus/GIGA/MagicDawn — still announced-only, no beta/GA transition found; Unity Spark — still no confirmed beta transition; Alibaba Model Studio's only in-window additions (qwen4-max, qwen4-max-preview) are general LLMs outside the tracked topics; Unity 6000.6.9f1 — minor patch, excluded).
Verification: every item above was checked against its stated primary source before inclusion; the one new item (Kling Image 4.0 API) was confirmed directly on Kuaishou's own API changelog page.
