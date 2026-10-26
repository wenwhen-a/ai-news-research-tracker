# Part B — Research → Product: Tencent / ByteDance·TikTok / miHoYo·HoYoverse / NetEase / Alibaba / Baidu / Kuaishou
Window: 2026-07-28 to 2026-10-26 (new items) · Monday recheck: 12 recently-reported items

## Tencent Hunyuan 3D Cloud API — HY-3D 3.1 full pipeline (generation, rigging, retopology, texture, text-to-motion)
- **Company:** Tencent
- **Status:** GA · **Released:** on or before 2026-09-29 (doc "last updated" stamp; no explicit launch-announcement date found) · **New**
- **Surface:** cloud API (Tencent Cloud, under the Hunyuan product)
- **Primary source:** https://cloud.tencent.com/product/hunyuan (model catalog: https://cloud.tencent.com/document/product/1823/130082 ; HY-3D model doc: https://cloud.tencent.com/document/product/1823/137181 ; HY-3D-Motion doc: https://cloud.tencent.com/document/product/1823/137780)
- **Underlying research:** HY-3D-Motion corresponds to arXiv:2512.23464 "HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation" (comment links to the Tencent-Hunyuan GitHub org). The base hy-3d-3.0/3.1 generation line and the rigging/retopology/texture tools carry no cited paper on the product docs; "no traceable paper" for those specifically (a related Tencent paper, "Hunyuan3D-Buffalo 1.0," arXiv:2608.02711, covers similar scalable 3D generation/editing but is not cited by the product page, so it is not asserted as the basis here).
- **Availability:** Self-serve — any Tencent Cloud account can create an API key (sub-accounts need the `QcloudTokenhubFullAccess` policy); no invite or waitlist. No pricing is published on the docs pages or the general Hunyuan product page. Default concurrency: 3 simultaneous tasks for HY-3D-3.0/3.1 generation; 1 simultaneous task for HY-3D-Motion, HY-3D-Rigging, HY-3D-Retopology, HY-3D-Texture, HY-3D-UV, HY-3D-Component and HY-3D-Format.

**What shipped (≤3 sentences):** Tencent Cloud's Hunyuan product page now advertises "混元生3D 3.1模型" (model ID `hy-3d-3.1`), a higher-precision successor to `hy-3d-3.0`, alongside a full asset-pipeline suite of callable APIs: HY-3D-Motion (text-to-3D-character-motion, FBX output), HY-3D-Rigging (skeleton + skinning), HY-3D-Retopology, HY-3D-Texture, HY-3D-UV, HY-3D-Component (part splitting) and HY-3D-Format (format conversion). This is distinct from — and not previously tracked via — the consumer-facing 3d.hunyuan.tencent.com site, which separately advertises a "混元3D生成大模型2.5版本" creation platform.

**What research it translates (≤3 sentences):** HY-3D-Motion's text-to-motion capability lines up with Tencent's own "HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation" (arXiv:2512.23464), a flow-matching model for generating 3D human motion from text descriptions, tied to the Tencent-Hunyuan GitHub org. The base 3D-generation models continue Tencent's published Hunyuan3D 1.0/2.x line (e.g. arXiv:2411.02293) but no 3.0/3.1-specific paper is cited by the product.

**Practical significance (≤3 sentences):** Tencent's own docs describe an asynchronous submit/query job API (`/v1/api/3d/submit`, `/v1/api/3d/query`, task IDs valid 24 hours) that lets a developer go from a text or image prompt to a textured, rigged, retopologized, UV-unwrapped 3D asset — and now also generate skeletal character animation from a text prompt (1–12 seconds, default 5s) — entirely through Tencent Cloud rather than the Hunyuan 3D Studio web UI. HY-3D-Motion also supports retargeting generated motion onto an existing Hunyuan-generated model via a `retarget_file` parameter.

**Engineering details (≤3 sentences):** `hy-3d-3.1` drops the "LowPoly" generate_type option that `hy-3d-3.0` supports; both accept text (≤1024 UTF-8 chars), image, or up to ~6-angle multi-view input, with `face_count` tunable from 3,000 to 1,500,000 and output in obj/glb/stl/usdz/fbx. HY-3D-Motion's text prompt is capped at 128 characters, with optional `enable_mesh` (skinned FBX), `enable_rewrite` (prompt expansion) and `enable_duration_est` parameters. HY-3D-Retopology is documented as using "Polygon 1.5" internally; no corresponding paper was found.

**Limitation / caveats (≤3 sentences):** No press release or launch blog post was found for this suite — it was discovered via Tencent Cloud's own docs/model-catalog pages, so the exact public launch date is inferred from documentation "last updated" timestamps (2026-09-09 for Motion, 2026-09-29 for the base 3D doc) rather than a stated ship date. No pricing is published anywhere checked. Per-task concurrency is capped at 1 for every tool except base 3D generation (capped at 3), which limits throughput for production use.

---

## Wan 3.0 (通义万相 3.0) — General Availability confirmed
- **Company:** Alibaba
- **Status:** GA · **Released:** 2026-08-24 (GA announced; blog published 2026-08-27) · **Update**
- **Surface:** cloud API (Alibaba Cloud Model Studio) + consumer apps (Wanxiang website, Qianwen Creation PC client, Qianwen app)
- **Primary source:** https://www.alibabacloud.com/blog/wan3-0-at-general-availability-capabilities-benchmarks-pricing-and-the-workflows-it-changes_603505
- **Underlying research:** no traceable paper for Wan 3.0 specifically; the Wan line's earlier generations are documented in arXiv:2503.20314 ("Wan: Open and Advanced Large-Scale Video Generative Models"), not confirmed to cover 3.0.
- **Availability:** GA on Alibaba Cloud Model Studio and "supported international channels" (Alibaba states availability varies by region and may change). API pricing: $0.05/sec (480P), $0.10/sec (720P), $0.20/sec (1080P) — e.g. ~$1.50 for a 30-second 480P clip, ~$6.00 for a 30-second 1080P clip, before promotions.

**What shipped (≤3 sentences):** Update: Alibaba Cloud's own blog (published 2026-08-27, stating GA was announced 2026-08-24) confirms Wan 3.0 is now fully Generally Available with standard production pricing — a tier that the Sept 21 tracking entry (sourced from a 36Kr-style news.qq.com article about the Aug 6 public-beta opening) had recorded only as "Public beta/preview." This GA transition actually predates the tracker's first_seen date for this item, so it is reported here as a correction/confirmation rather than a change occurring this week. The tier in `state/product_seen.json` should be updated from "Public beta/preview" to "GA."

**What research it translates (≤3 sentences):** No Wan 3.0-specific paper is cited in the GA post; it is presented as a direct successor to Wan2.7, continuing Alibaba's Wan video-generation line previously documented at arXiv:2503.20314.

**Practical significance (≤3 sentences):** Alibaba states Wan 3.0 natively generates up to 30 continuous seconds of video (versus Wan2.7's 2–15 seconds), with smart duration recommendation, video extension, and inputs spanning text, image, audio, video, documents (PDF/PPT/spreadsheets) and webpages. Alibaba also claims omni-reference and consistency for identity, voice and lip-sync, and carries forward Wan2.7's video-editing capability (altering visuals, plot or dialogue without full regeneration).

**Engineering details (≤3 sentences):** The post gives per-second resolution-tiered pricing (480P/720P/1080P) rather than a flat per-clip rate, with a time-limited launch discount mentioned but not quantified. Alibaba names no specific model ID or API endpoint in the post itself (check the Model Studio catalog directly for the callable identifier, e.g. `wan3.0-video` / `wan3.0-video-prime`, both listed in Model Studio since 2026-08-06/08-20).

**Limitation / caveats (≤3 sentences):** Alibaba states audio texture and on-screen text rendering are "still maturing." No specific region list is given beyond "Model Studio and supported international channels." The GA announcement was found only via Alibaba Cloud's own blog, not the original news.qq.com tracking source, which had not been updated to reflect GA.

---

### Previously reported — no material change found
- https://h.163.com/news/official/20260612/37231_1304115.html | NetEase | 《逆水寒：新世界》 character rendering upgrade — page unchanged, no new version/platform/pricing details.
- https://www.happyoyster.cn | Alibaba | HappyOyster 1.0 — site still shows only Directing/Wandering modes, no version number, platform, or pricing stated; no change detected.
- https://help.aliyun.com/zh/model-studio/newly-released-models(#happyoyster-1.0-adventure/-directing/-acting) | Alibaba | HappyOyster Adventure/Directing/Acting — all three still listed with 上架时间 2026-09-17; Adventure deploys to 华北2(北京) + 新加坡, Directing/Acting to 新加坡 only; no tier (GA/邀测) explicitly stated on the page beyond the 2026-10-05 update already recorded; no further change this week.
- https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5 | ByteDance | Seedance 2.5 — blog post itself unchanged (static snapshot); the API-live update already recorded on 2026-10-17 stands, no further change found.
- https://finance.yahoo.com/technology/ai/articles/alibabas-amap-unveils-abot-world-072100723.html | Alibaba (AMAP) | ABot-World — could not locate a better AMAP-owned primary source this week (web-search budget for this session was exhausted before a targeted search could run); Yahoo link retained; no material change confirmed either way.
- https://www.prnewswire.com/news-releases/bringing-digital-characters-to-life-tencent-games-motus-makes-gamescom-debut-with-end-to-end-ai-animation-pipeline-302861442.html | Tencent | Motus — press release unchanged; still framed as an internal studio pipeline "applied across multiple titles" with no public SDK/API, pricing, or licensing stated.
- https://magicdawn.tencent.com/?lang=en | Tencent | MagicDawn — consistent with the 2026-10-05 update already recorded (Dawn personal/non-commercial edition downloadable via license key); sub-tools NDGI/SPATIAL/COMPRESS/REMASTER still have no working "learn more" links or stated status; no further change.
- https://news.qq.com/rain/a/20260829A0BD2J00 | Tencent | GIGA — same static article; still reads as a research/technical disclosure (general game-playing agent framework, FPS decision-making) with no named product, access path, or ship date; no material change.
- https://kling.ai/ | Kuaishou | Kling 4.0 full global launch — still the advertised flagship; no Kling 4.5/5.0 or further change found beyond the 2026-10-15 update already recorded.

### Announced only (not yet usable)
(none found this week for these 7 companies)

Near-misses: 4 — (1) Tencent-Hunyuan GitHub org shows several new open-weight research drops in the window (HY-World-2.0, Hunyuan3D-WorldClaw, Hunyuan3D-Buffalo 1.0, R-DMesh) — Part A territory, no product surface, excluded here; (2) ByteDance Volcano Engine/Ark docs, the Seed blog index, HoYoverse news, NetEase Fuxi, Baidu Research, Kuaishou's klingai.com changelog and Jianying/CapCut pages are all JS-rendered client apps that returned no readable content to WebFetch — no verifiable new items could be confirmed or ruled out there this week; (3) AMAP's own primary page for ABot-World was not located (search budget exhausted); (4) miHoYo/HoYoverse and Baidu together yielded zero confirmable candidates this week (Baidu's research.baidu.com was under maintenance).
Verification: primary-source double-check done for all listed items.
