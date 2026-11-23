# Part B — Chinese companies (Tencent, ByteDance/TikTok, miHoYo/HoYoverse, NetEase, Alibaba, Baidu, Kuaishou)

Window: 2026-08-25 to 2026-11-23. Discovery covered each company's primary product/changelog/blog pages per `product-sources.md`. Recheck covered the "Announced only" and versioned entries in `recent_products_cn.json` most likely to have moved.

## New

### Seedream 5.5
- **Company:** ByteDance
- **Status:** GA · **Released:** 2026-11-09 · **New**
- **Surface:** Consumer apps (Dreamina/即梦, Doubao) + cloud API (Volcano Engine Ark / BytePlus)
- **Primary source:** https://seed.bytedance.com/blog/more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5
- **Underlying research:** no traceable paper (prior generations have arXiv technical reports — e.g. Seedream 3.0, "Seedream 4.0: Toward Next-generation Multimodal Image Generation" — but no 5.5-specific report or citation was found on the launch page)
- **Availability:** ByteDance's own Seed blog/product page (seed.bytedance.com/seedream5_5) offers access via the "Dola" chat app and the BytePlus Playground, plus a "Get API" and an "Enterprise" path; no resolution tiers or pricing are stated on the primary page itself. Trade press (not verified against a primary page) additionally describes rollout across Jimeng/即梦, Doubao, Doubao Work and Volcano Ark in China, with CapCut/BytePlus named as the international surfaces and a Pro variant "to come later."

**What shipped (≤3 sentences):** ByteDance's Seed team shipped Seedream 5.5, a new image generation/editing model, on 2026-11-09, reachable today through ByteDance's own Dola app, the BytePlus Playground, and a developer API/enterprise path. It is positioned as the successor to Seedream 5.0 Pro, targeting professional image-creation workflows rather than a research preview.

**What research it translates (≤3 sentences):** ByteDance states the model improves multi-turn edit stability and adds native transparent (RGBA) output, extending the Seedream image-generation line whose earlier generations (3.0, 4.0) were documented in ByteDance's own arXiv technical reports. No Seedream-5.5-specific paper or citation was found on the launch page, so the exact research lineage for this version is not independently traceable.

**Practical significance (≤3 sentences):** ByteDance states that unedited regions of an image stay pixel-level stable across up to 100 successive edit rounds, aimed at iterative production work (e.g., e-commerce, marketing, game-asset, and fashion imagery) where earlier models would drift after a few edits. ByteDance also states the model generates native semi-transparent/transparent layers (e.g., stickers, cutouts) without a separate background-removal step. These are ByteDance's own claims; no independent benchmark was available.

**Engineering details (≤3 sentences):** The primary page highlights three capability pillars — multi-turn editing with pixel-level preservation of non-edited regions, native RGBA transparent-background generation, and more naturalistic lighting/material/skin rendering — but gives no architecture, parameter-count, or resolution-ceiling details. Access is exposed through a hosted chat surface (Dola), a web playground (BytePlus), and an API/enterprise tier, rather than open weights.

**Limitation / caveats (≤3 sentences):** The primary product page states no pricing, resolution limits, or regional availability, so terms for each surface (Dola vs. Playground vs. API) are unconfirmed from ByteDance's own page. Benchmark comparisons against competing models (reported in trade press, not on the primary page) are ByteDance's own self-reported figures and were not independently verified.

## Updated

### Kling 4.0 (video API — 4K + HDR added)
- **Company:** Kuaishou (Kling)
- **Status:** GA · **Changed:** 2026-11-19 · **Update**
- **Surface:** Cloud API (text-to-video / image-to-video / omni-video) + Kling app
- **Primary source:** https://kling.ai/document-api/updates/api.md
- **Underlying research:** no traceable paper confirmed for Kling 4.0 specifically. A related (but distinct) "Kling-Omni Technical Report" (arXiv:2512.16776, submitted 2025-12-18, Kuaishou Kling Team) describes a unified video generation/editing/reasoning system that may underlie Kling's Omni-video endpoints, but it is not cited by Kling's own changelog as the basis for this specific update, so it is not recorded as a confirmed match.
- **Availability:** Kling's own API changelog (kling.ai/document-api) shows the text-to-video, image-to-video, and omni-video endpoints for Kling 4.0 now accept `4k` for `settings.resolution`, plus a new `settings.dynamic_range` parameter enabling HDR output at 1080p or 4K (billed with an extra per-second HDR fee). This closes a gap the tracker flagged at the Kling 4.0 global launch (2026-10-15), when 4K/1080p output was still listed as "coming soon."

**What shipped (≤3 sentences):** Update since first_seen 2026-10-04: Kling's own API documentation shows that on 2026-11-19, Kling 4.0's text-to-video, image-to-video and omni-video endpoints gained native 4K resolution output and a new HDR dynamic-range option (1080p or 4K), both billed with an added per-second fee. At the 2026-10-15 global launch, 4K and HDR output were explicitly listed as still future-tense; this changelog entry converts that from "coming soon" to shipped and callable today.

**What research it translates (≤3 sentences):** Kling 4.0 continues Kuaishou's Kling video-generation line; a Kuaishou Kling-Team arXiv report on a unified "Kling-Omni" system (video generation, editing and reasoning in one model, arXiv:2512.16776) exists but is not cited by this changelog entry as its basis, so no confirmed paper link is recorded for the 4K/HDR capability itself.

**Practical significance (≤3 sentences):** Developers calling Kling's `/text-to-video/kling-4.0`, `/image-to-video/kling-4.0` and `/omni-video/kling-4.0` endpoints can now request 4K output and HDR dynamic range directly via API parameters, without needing a separate upscaling step, for workflows (e.g., film/trailer production) that were previously capped at 1080p. This is a self-serve API change (no new signup or invite required beyond existing Kling 4.0 access), per Kling's own documentation.

**Engineering details (≤3 sentences):** The change is exposed as two parameters: `settings.resolution` now accepts `4k` in addition to prior 720p/1080p values, and a new `settings.dynamic_range` parameter accepts `hdr` to enable HDR output at 1080p or 4K. Kling's changelog states billing is adjusted with "an extra per-second HDR fee" when the HDR flag is used, but does not give the fee amount or a resolution-vs-price table.

**Limitation / caveats (≤3 sentences):** Kling's own changelog gives no exact HDR surcharge figure, and does not state whether 4K/HDR is available uniformly across all three endpoints' sub-modes (e.g., Omni's reference-image/video inputs) or only standard generation. No independent (non-Kuaishou) confirmation of visual quality at the new tiers was located.

### Announced only (not yet usable)
- None newly identified this run for the assigned companies (checked Tencent/GIGA, Tencent/Hunyuan 3D Studio, Alibaba/HappyOyster variants, Baidu — see Near-misses for items that could not be confirmed via a primary source).

### Near-misses
- 文心一镜 ("ERNIE Yijing") micro-expression video model + 百度一镜 "短漫剧Studio" (Baidu) · announced 2026-11-12 at Baidu World 2026, reported live on the Qianfan (千帆) platform with API access "for enterprise customers and partners" (0.2 RMB/sec video-generation cost, AU-level micro-expression control, per multiple Chinese outlets) · sources: 科技日报 (stdaily.com), 新华网, 品玩 — all trade/state press; no primary Baidu page, newsroom post, or Qianfan model-card URL was found despite several searches, so this is excluded from the main list as unverified.
- Tencent Hunyuan 3D Studio 1.2 (brush-interaction PartGen 1.5, base model upgraded to Hunyuan 3D 3.1, no-application public beta) · trade press (AIBase, 品玩/Pingwest) describes this as a recent release, but the one source giving a specific date puts it at "1月16日" (January 16), which falls before this run's window (2026-08-25 to 2026-11-23); not included as not confirmed in-window, and the official 3d.hunyuan.tencent.com/studio page is JS-rendered with no retrievable changelog text to confirm either way.
- NetEase《天下》AI short film "倩影" (produced by NetEase's internal virtual-production team, ~2026-07, reported ~95% TVC cost reduction) — a marketing case study/short film, not a self-serve product surface with public availability; near-miss, not a Part B product.
- ByteDance Seedance 2.5 4K API "full opening" dated 2026-11-16 (reported by IT之家/ifeng.com and AIBase) — BytePlus's own blog (byteplus.com, dated 2026-10-27) confirms Seedance 2.5 4K exists and describes its capabilities, but gives no API-access date, pricing, or GA/preview label; no Volcano Engine or seed.bytedance.com primary page was found confirming the specific Nov 16 "fully opened" transition, so this is not recorded as a verified update this run.
- World Labs, Decart, Odyssey, Runway — not checked (out of scope: not assigned companies for this run).

**Verification:** All new/updated items above were checked against a primary company source (seed.bytedance.com's own Seed blog post for Seedream 5.5; Kling's own kling.ai/document-api changelog for the 4K/HDR update) rather than trade press. Recheck of existing `recent_products_cn.json` entries covered: Tencent (GIGA — no change since 2026-08-27 reveal, stays Announced-only, not re-listed per "skip silently" rule; MagicDawn/NDGI — no material change found beyond the already-recorded 2026-05-27 open-source release; Hunyuan 3D Cloud API — no hy-3d-3.2 or newer version found), Alibaba (Model Studio "newly-released-models" catalog fetched in full for Oct–Nov 2026 — no new Wan, HappyOyster, or world-model entries beyond the already-tracked Tripo pipeline), Kuaishou (Kling API changelog fetched in full — surfaced the 4K/HDR update above; Nov 14 aspect-ratio addition and Kling Image 4.0 itself were judged minor/already-tracked and skipped), ByteDance (Seedance 2.5 4K API claim investigated, left as near-miss for lack of primary source), Baidu/NetEase/miHoYo (official blogs/newsrooms checked directly; no in-window qualifying product found for miHoYo or NetEase despite multiple searches of hoyoverse.com and fuxi.163.com, whose content is JS-rendered with no retrievable dated posts).
