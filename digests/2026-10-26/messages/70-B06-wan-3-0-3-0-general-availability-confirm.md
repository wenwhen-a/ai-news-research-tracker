**[B06 · Update] Wan 3.0 (通义万相 3.0) — General Availability confirmed**
- **Company:** Alibaba
- **Status:** GA · **Released:** 2026-08-24 (GA announced; blog published 2026-08-27) · **Update**
- **Surface:** cloud API (Alibaba Cloud Model Studio) + consumer apps (Wanxiang website, Qianwen Creation PC client, Qianwen app)
- **Primary source:** <https://www.alibabacloud.com/blog/wan3-0-at-general-availability-capabilities-benchmarks-pricing-and-the-workflows-it-changes_603505>
- **Underlying research:** no traceable paper for Wan 3.0 specifically; the Wan line's earlier generations are documented in arXiv:2503.20314 ("Wan: Open and Advanced Large-Scale Video Generative Models"), not confirmed to cover 3.0.
- **Availability:** GA on Alibaba Cloud Model Studio and "supported international channels" (Alibaba states availability varies by region and may change). API pricing: $0.05/sec (480P), $0.10/sec (720P), $0.20/sec (1080P) — e.g. ~$1.50 for a 30-second 480P clip, ~$6.00 for a 30-second 1080P clip, before promotions.

**What shipped:** Update since 2026-09-21: Alibaba Cloud's own blog (published 2026-08-27, stating GA was announced 2026-08-24) confirms Wan 3.0 is now fully Generally Available with standard production pricing — a tier this tracker had recorded only as "Public beta/preview" (sourced from a news.qq.com article about the Aug 6 public-beta opening).
**What research it translates:** No Wan 3.0-specific paper is cited in the GA post; it is presented as a direct successor to Wan2.7, continuing Alibaba's Wan video-generation line previously documented at arXiv:2503.20314.
**Practical significance:** Alibaba states Wan 3.0 natively generates up to 30 continuous seconds of video (versus Wan2.7's 2–15 seconds), with smart duration recommendation, video extension, and inputs spanning text, image, audio, video, documents (PDF/PPT/spreadsheets) and webpages.
