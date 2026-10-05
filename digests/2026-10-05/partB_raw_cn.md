# Part B — Research → Product (Chinese companies sweep)
Window: last 90 days (2026-07-07 to 2026-10-05). Companies: Tencent, ByteDance/TikTok, miHoYo/HoYoverse, NetEase, Alibaba, Baidu, Kuaishou.

**Retrieval note:** WebSearch quota for this session was exhausted early in the run (shared session-wide budget, reported as "200 of 200 used" before this task's own searches could run). All verification after that point used WebFetch and raw `curl` only. Several company primary pages (seed.bytedance.com/en/blog, 3d.hunyuan.tencent.com, hunyuan.tencent.com, hoyoverse.com/en-us/news, Baidu Qianfan console, Bailian console) are JS-rendered single-page apps that returned empty/skeleton content to both WebFetch and raw curl, so the "check for brand-new products" sweep for those surfaces is **incomplete** this run — treat the "0 new products found" result below as a lower bound, not a confirmed clean sweep. Direct re-checks of the specific tracked-item primary-source URLs supplied in the task worked normally.

New products (GA / Public beta·preview) verified this pass: 0
Updates to tracked items: 2 (3 item blocks: HappyOyster Directing, HappyOyster Acting, MagicDawn GI)
Announced-only (new): 2 lines
Near-misses: 0

---

## HappyOyster Directing (happyoyster-1.0-directing)
- **Company:** Alibaba (ATH Innovation Business Group / Bailian) — borderline unit, flagged
- **Status:** GA (inferred, see caveats) · **Released:** 2026-09-17 (catalog listing date) · **Update**
- **Surface:** cloud API (Alibaba Cloud Model Studio / Bailian Open API)
- **Primary source:** https://help.aliyun.com/zh/model-studio/newly-released-models#happyoyster-1.0-directing
- **Underlying research:** no traceable paper
- **Availability:** Singapore-hosted deployment, listed as "国际" (international) region; Open API

**What shipped (≤3 sentences):** Update since 2026-09-22: HappyOyster Directing, previously tracked as Announced-only on this same Model Studio page, now appears inside the "newly-released-models" table with the same formatting, date field (2026-09-17) and international/Singapore region tag as the already-GA happyoyster-1.0-adventure entry, with no "coming soon" or waitlist wording distinguishing it. The page's own text describes it as "实时交互、可沉浸演绎的开放式世界模型" (a real-time interactive, immersively-directable open-world model).
**What research it translates (≤3 sentences):** Same underlying real-time interactive world-model line as HappyOyster 1.0's "执导/Directing" mode on the consumer site happyoyster.cn; no arXiv paper is cited on the Model Studio page or found elsewhere — "no traceable paper."
**Practical significance (≤3 sentences):** If the tier change holds, this gives developers API access (not just the consumer happyoyster.cn product) to the Directing mode specifically, alongside the already-API-available Adventure mode.
**Engineering details (≤3 sentences):** Deployed via Alibaba Cloud Model Studio in the Singapore region; this pass could not retrieve a specific API call example or per-call/per-second price for Directing (Adventure's pricing, confirmed in a prior run, was ~$0.007067/World Creation call and ~$0.028267/sec of World Experience at 480p — not independently re-confirmed for Directing).
**Limitation / caveats (≤3 sentences):** The Model Studio page does not carry an explicit "GA"/"正式发布" vs "Beta"/"邀测" label for any entry on this page (including the confirmed-GA Adventure endpoint), so this status change is inferred from table placement and date matching, not stated text — moderate confidence only. Could not confirm an actual callable API example for Directing in this pass.

## HappyOyster Acting (happyoyster-1.0-acting)
- **Company:** Alibaba (ATH Innovation Business Group / Bailian) — borderline unit, flagged
- **Status:** GA (inferred, see caveats) · **Released:** 2026-09-17 (catalog listing date) · **Update**
- **Surface:** cloud API (Alibaba Cloud Model Studio / Bailian Open API)
- **Primary source:** https://help.aliyun.com/zh/model-studio/newly-released-models#happyoyster-1.0-acting
- **Underlying research:** no traceable paper
- **Availability:** Singapore-hosted deployment, listed as "国际" (international) region; Open API

**What shipped (≤3 sentences):** Update since 2026-09-22: HappyOyster Acting, previously tracked as Announced-only, now appears in the same "newly-released-models" table as the GA happyoyster-1.0-adventure entry, with identical formatting and the same 2026-09-17 international/Singapore date. The page describes it as "实时交互的角色演绎模型，基于多模态" (a real-time interactive, multimodal character role-play/performance model).
**What research it translates (≤3 sentences):** Same HappyOyster world-model/character-interaction line as the other HappyOyster endpoints; no arXiv paper found — "no traceable paper."
**Practical significance (≤3 sentences):** Exposes the "Acting"/character-interaction mode of HappyOyster as a standalone, developer-callable endpoint distinct from the consumer happyoyster.cn product, if the apparent tier change holds.
**Engineering details (≤3 sentences):** Deployed via Alibaba Cloud Model Studio, Singapore region; no API call example or pricing figure for Acting specifically could be retrieved this pass.
**Limitation / caveats (≤3 sentences):** Same caveat as Directing: the page uses no explicit GA/Beta label for any model row, so the Announced→available change is inferred from table placement, not an explicit status statement — moderate confidence. Treat as provisional until an explicit "立即调用"/pricing section for Acting is found.

## MagicDawn GI
- **Company:** Tencent (Tencent Games)
- **Status:** GA (free / non-commercial tier) · **Released:** date not stated on page (previously Announced-only as of 2026-09-28; observed changed 2026-10-05) · **Update**
- **Surface:** studio tool / cross-engine rendering plugin
- **Primary source:** https://magicdawn.tencent.com/?lang=en
- **Underlying research:** no traceable paper
- **Availability:** Free download, personal version restricted to "个人学习、研究和非商业用途" (personal learning, research and non-commercial use); commercial licensing by contacting magicdawn@tencent.com

**What shipped (≤3 sentences):** Update since 2026-09-28: MagicDawn, Tencent Games' rendering brand previously tracked as Announced-only in full, now states on its own page "MagicDawn GI 现已开放免费使用" (GI is now open for free use) with a "免费下载 GI 工具" (free-download GI tool) button — i.e., the GI (global illumination) component specifically has moved from announced to self-serve downloadable. The other named sub-tools remain earlier-stage: NDGI (neural dynamic global illumination) is in "Beta 试用" (beta trial), and SPATIAL, COMPRESS and REMASTER are still listed as "coming soon."
**What research it translates (≤3 sentences):** Tencent describes MagicDawn as its "前沿渲染品牌" (frontier rendering brand) for AI-driven graphics and cross-engine adaptation; the page cites no specific paper — "no traceable paper."
**Practical significance (≤3 sentences):** Tencent states the GI tool can be freely downloaded for personal, non-commercial use today, giving individual developers/engine integrators access to the global-illumination tool without (as far as stated) an invitation or waitlist, while commercial use still requires contacting Tencent directly.
**Engineering details (≤3 sentences):** The page mentions an activation-key mechanism for engine integration but no engine compatibility list (e.g., Unreal/Unity) or version number was retrievable this pass; the actual destination URL of the download button could not be resolved via automated fetch.
**Limitation / caveats (≤3 sentences):** The free tier is explicitly non-commercial-only, so this is not unrestricted GA; whether the download requires account registration could not be confirmed. NDGI and the other three sub-brands (SPATIAL, COMPRESS, REMASTER) remain gated/unreleased, so most of the MagicDawn brand is still effectively Announced-only.

### Announced only (not yet usable)
- MagicDawn NDGI (Neural Dynamic Global Illumination), beta trial, no visible public signup — Tencent · observed 2026-10-05 · https://magicdawn.tencent.com/?lang=en
- MagicDawn SPATIAL / COMPRESS / REMASTER (spatial audio, AI package compression, game-quality enhancement — all listed "coming soon") — Tencent · observed 2026-10-05 · https://magicdawn.tencent.com/?lang=en

Near-misses: 0
- (No on-topic candidates were found and excluded this pass; see the retrieval note above on reduced coverage for several company blog/news surfaces.)

## Items re-checked this pass with no material update (unchanged, not re-listed above)
- NetEase 《逆水寒：新世界》 character rendering upgrade (h.163.com/news/official/20260612/37231_1304115.html) — same content as first_seen, publish date 2026-06-12, release date 2026-06-26, no new version/date found.
- Alibaba HappyOyster 1.0 (happyoyster.cn) — no version number, changelog or status change visible.
- Alibaba HappyOyster 1.0 Adventure via Model Studio — unchanged.
- Alibaba Wan 3.0 (通义万相 3.0) — wan3.0-video appears in the Model Studio catalog (dated 2026-08-06, Beijing region) without an explicit beta/GA label either way; inconclusive, not reported as a confirmed tier change.
- ByteDance Seedance 2.5 — blog still states "API access coming soon via BytePlus ModelArk," no date given; API has not shipped.
- Tencent Motus — PR Newswire release is static; no follow-up/availability update found; still no stated external access terms.
- Tencent GIGA (news.qq.com) — not re-fetched (trade-press article unlikely to self-update); no update claimed.
- Kuaishou Kling 4.0 Flash (kling.ai) — site is a JS-rendered skeleton for its model carousel; could not confirm or deny a tier change beyond the tracked "Public beta/preview (early access)" status.
- Alibaba ABot-World — could not reach a usable primary source this pass (AMAP main site has no visible ABot-World content; Bailian console page did not render).

**Verification:** every item above with a 5-block entry was checked against the stated primary-source URL in this session (quoted text taken from that fetch). No item was fabricated; where evidence was inferential rather than an explicit stated label (the two HappyOyster entries), that is flagged in Limitation/caveats.
