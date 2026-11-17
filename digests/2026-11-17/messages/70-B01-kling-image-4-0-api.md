**[B01] Kling Image 4.0 API**
- **Company:** Kuaishou
- **Status:** GA · **Released:** 2026-11-17 · **New**
- **Surface:** cloud API
- **Primary source:** <https://kling.ai/document-api/updates/api.md>
- **Underlying research:** no traceable paper
- **Availability:** Available now via the Kling API (`/image-generation/kling-4.0` for text-to-image/image-to-image/image sets, `/long-image-generation/kling-4.0` for long-image generation); billing now counts both input reference images and output images, rate varies by resolution; no specific pricing figures given in the changelog itself (points to a separate pricing page).

**What shipped:** Kuaishou shipped Kling Image 4.0, succeeding Kling Image 3.0, via new API endpoints for standard and long-image generation. The changelog states native 8K resolution (up from 3.0's native 4K), improved realism, text rendering and instruction-following, and up to 10 combined image/subject references.
**What research it translates:** No underlying paper is cited or traceable; this is a direct API version upgrade of Kuaishou's existing Kling Image line.
**Practical significance:** Per Kling's own API changelog, this is a full major-version jump (3.0→4.0) in image-generation resolution and reference handling, directly comparable to the already-tracked Kling 4.0 video-generation line. The long-image endpoint is aimed at e-commerce and web-design use cases.
**Engineering details:** Supports 2K/4K/8K output for single images and image sets (`settings.series_amount` 2–10 or auto), 1K/2K for long images, prompts up to 50,000 characters in English (21,000 for non-English), and asynchronous task status via `GET /tasks`.
**Limitation / caveats:** No pricing figures are given in the changelog itself; no independent third-party coverage was found yet confirming the stated quality improvements.
