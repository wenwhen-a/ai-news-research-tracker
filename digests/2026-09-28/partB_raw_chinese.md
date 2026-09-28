# Part B — Chinese Tech Sweep (Tencent, ByteDance/TikTok, miHoYo/HoYoverse, NetEase, Alibaba, Baidu, Kuaishou)
Window: 2026-06-30 to 2026-09-28. Compiled 2026-09-28.

Companies already carrying items in `state/product_seen.json` for this window (checked, not re-verified unless noted): Alibaba (HappyOyster 1.0 Adventure + consumer site, Wan 3.0 public beta, ABot-World / ABot-3DWorld, HappyOyster Directing/Acting announced-only), ByteDance (Seedance 2.5), NetEase (《逆水寒：新世界》 character rendering upgrade). No tier changes found for any of these on this pass (see notes under each company below).

---

## Motus (Tencent Games' end-to-end AI character-animation pipeline)
- **Company:** Tencent
- **Status:** GA (internal studio tool — used in production, not an external developer product) · **Released:** 2026-08-27 (Gamescom Cologne debut) · **New**
- **Surface:** Internal game-production tooling (animation pipeline used inside Tencent's own studios)
- **Primary source:** https://www.prnewswire.com/news-releases/bringing-digital-characters-to-life-tencent-games-motus-makes-gamescom-debut-with-end-to-end-ai-animation-pipeline-302861442.html (Tencent Games' own press release; corroborated by Tencent News coverage of the same Gamescom disclosure: https://news.qq.com/rain/a/20260829A0BD2J00)
- **Underlying research:** no traceable paper — the release names no paper and cites no arXiv ID; Tencent Hunyuan's separately-published "HY-Motion 1.0: Scaling Flow Matching Models for Text-to-Motion Generation" (arXiv:2512.23464, Tencent Hunyuan 3D Digital Human Team) covers a related text-to-motion model but is not cited by the Motus materials, so it is not recorded as Motus's underlying paper (per rule: no inference from topic similarity).
- **Availability:** Not offered as an external product, SDK or API; Tencent states the technology "has been applied across multiple titles" and, per the follow-up Tencent News coverage, is "currently integrated into over 90 projects," including named users Peace Elite (和平精英) and The Finals. No developer signup, pricing or licensing path is described for outside studios.

**What shipped (≤3 sentences):** Tencent Games' Central Tech group publicly unveiled Motus, an end-to-end generative-AI pipeline covering character rigging, skinning, text/video/keyframe-driven motion generation, automated animation-defect correction (jitter, mesh penetration, foot sliding), and real-time audio/text-driven facial and body animation for NPCs and digital humans. It made its public debut at Gamescom Devcom/Gamescom 2026 in Cologne on August 27, 2026, alongside sibling tools GIGA (game-playing AI agents), MagicDawn (rendering/global illumination) and WeTest (automated QA) under the new "Tencent Games Central Tech" brand.
**What research it translates (≤3 sentences):** Tencent describes Motus as built on "Tencent Games' proprietary family of generative animation foundation models," i.e. in-house motion-generation and rigging research rather than a single named academic paper. No arXiv paper or preprint is cited in the announcement.
**Practical significance (≤3 sentences):** Tencent states the pipeline is already integrated into more than 90 internal projects, including live titles PUBG Mobile/Peace Elite and The Finals, replacing manual rigging/skinning and hand-keyed animation-defect fixing with automated generation and QA passes. Tencent frames this explicitly as production infrastructure rather than a demo, saying AI's value lies "in integration into actual development workflows rather than standalone content generation."
**Engineering details (≤3 sentences):** The pipeline stages are: automatic skeleton generation from character topology, automatic skinning-weight prediction for muscle/cloth/part deformation, motion generation from text/video/keyframe inputs (including multi-character interactions for combat/social scenarios), an automated refinement stage that detects and corrects common animation artifacts, and a real-time layer that drives facial expression and body motion from audio or text for NPCs and virtual presenters.
**Limitation / caveats (≤3 sentences):** This is an internal Tencent-studio tool, not something external developers or customers can access, license, or try — there is no SDK, plugin, waitlist, or pricing page. Quality claims (defect detection, "production-ready" skeletons "within seconds") are Tencent's own and are not independently benchmarked in the release; no research paper is cited to check the underlying methods.

---

### Announced only (not yet usable)
- GIGA (general-purpose game-playing AI agent framework) · Tencent · 2026-08-27 · https://www.prnewswire.com/news-releases/bringing-digital-characters-to-life-tencent-games-motus-makes-gamescom-debut-with-end-to-end-ai-animation-pipeline-302861442.html and https://news.qq.com/rain/a/20260829A0BD2J00 (research-agenda framing — vision-based decision-making and instruction alignment for game agents; no product surface, access path, or ship date given)
- MagicDawn (cross-engine global-illumination/rendering brand) · Tencent · 2026-08-27 · https://magicdawn.tencent.com/?lang=en and https://news.qq.com/rain/a/20260829A0BD2J00 (described as addressing open-world lighting/performance; no external release, pricing or engine-plugin availability stated — flagged, not verified as usable by outside studios)

Near-misses: none for Tencent beyond the two announced-only items above.

---

## ByteDance / TikTok
No new GA or public-beta items found in the 90-day window beyond the already-tracked Seedance 2.5 (release_date 2026-07-31, already in `product_seen.json`). Checked Seed3D, DreamActor, PICO developer blog and Volcano Engine/BytePlus catalog changelogs — DreamActor M2.0 (arXiv, Jan 2026, academic co-authors) is a research paper outside the window, not a ByteDance product release, and is Part A territory in any case.

### Announced only (not yet usable)
- none verified with a primary source this run.

Near-misses:
- Jianying/CapCut (剪映) "AI New Creation" event, 2026-09-20 — showcased 剪映Hub (multi-track editor workspace), an AI creation agent "小映," and a first look at "ICG Studio," an AI interactive-movie/game creation platform ("从一份剧本出发，做出能够观看、选择和探索的互动故事"). Coverage (stdaily.com, 163.com, geekpark.net, news.qq.com) describes ICG Studio as "首次展示" (first shown) with no stated public access, pricing or launch date — sounds like a demo/preview, not confirmed usable today. No CapCut/Jianying-owned primary source (blog/release notes) was found to verify availability, and topic fit (interactive-fiction/video tool vs. our 4 tracked topics) is borderline. Recorded as near-miss/unverified rather than Announced-only.
- Jianying/CapCut digital-human (数字人) short-video narration feature — multiple trade-press reports (bianews.com, pai.com.cn) describe it as in internal beta (内测) with public launch "expected by end of September 2026," but no ByteDance/Douyin primary source confirms an actual ship date or GA status as of 2026-09-28. Near-miss/unverified.

---

## miHoYo / HoYoverse
No new qualifying items found in the 90-day window. Checked hoyoverse.com engine/tech posts and GDC/SIGGRAPH talk listings; found only general strategy statements (continued AI/cloud/industrialization R&D investment) and a reportedly UE5-built unannounced title ("Varsapura") with no documented shipped AI/engine feature. Coverage gap: miHoYo/HoYoverse publishes very little in English or Chinese about concrete engine/animation/3D-gen tooling on official channels; nothing met the primary-source bar this run.

### Announced only (not yet usable)
- none verified with a primary source this run.

Near-misses: none substantive enough to record (studio strategy commentary only, no named product).

---

## NetEase
No new qualifying items found in the 90-day window beyond the already-tracked 《逆水寒：新世界》 character-rendering upgrade (release_date 2026-06-26, already in `product_seen.json`). Checked fuxi.163.com and NetEase Games update pages for 逆水寒:新世界, 永劫无间 and other titles — August/September updates found were routine content patches (crossover events, new heroes/seasons), not documented AI/animation/engine feature releases.

### Announced only (not yet usable)
- none verified with a primary source this run.

Near-misses:
- NetEase Fuxi AI Lab GDC talk on speech-driven facial-expression-animation synthesis (reported 2026-07-21 via 游戏陀螺/TapTap coverage) — this is a technical conference talk about an animation-synthesis algorithm, not a shipped product with a customer-facing surface, so it does not meet the Part B bar (research disclosure, not a product). Excluded per product-criteria's "research demo" exclusion rather than listed as announced-only.

---

## Alibaba
No new items beyond what is already recorded in `state/product_seen.json` for the window (HappyOyster 1.0 / Adventure API / consumer site, Wan 3.0 public beta, ABot-World/ABot-3DWorld, HappyOyster Directing and Acting as announced-only/invite-only). Checked for tier changes:
- **Wan 3.0**: still described as invite-testing-turned-public-beta on Alibaba Cloud Bailian (pay-as-you-go pricing live, time-limited discount running through 2026-09-23); no evidence found of a move to unrestricted GA. No tier change.
- **HappyOyster Directing / Acting**: a 2026-09-20 follow-up piece (ai.codefather.cn, syndicating what appears to be Alibaba/Qianwen platform messaging) confirms Adventure mode needs no invite-testing application ("开发者无需申请邀测权限，可直接通过 API") — consistent with Adventure's existing GA record — but does not state that Directing or Acting have left invite-only testing (邀测); Directing is still described only as region-limited (Singapore, US-Virginia). No confirmed tier change for Directing/Acting this run.

### Announced only (not yet usable)
- (no new item; see Directing/Acting already in `product_seen.json`)

Near-misses:
- ABot-World / ABot-3DWorld — already tracked; no update found this run.

---

## Baidu
No qualifying products found in the 90-day window across any of the 4 tracked topics (3D generation, world models, character animation, game engines/tooling). Searched Baidu Qianfan model-marketplace update logs, research.baidu.com, and Baidu's digital-human/Apollo simulator coverage — Baidu's visible 2026 output in this space is limited to text/multimodal LLM and digital-human "broadcast avatar" commerce features with no dated primary-source release matching our topics in this window, and Baidu's Apollo "game engine simulator" is an autonomous-driving synthetic-data tool, not a games/character/3D-content product.

### Announced only (not yet usable)
- none.

Near-misses: none — genuine coverage gap. Baidu appears to have no active shipped or announced product in 3D generation, world models, character animation, or game engines this window.

---

## Kuaishou
No qualifying NEW items found in the 90-day window. Kling's most recent major releases (Kling 3.0, 2026-02-05; Kling 3.0 Turbo/Omni upgrade, 2026-06-17) both predate the window, and searches for klingai.com changelog entries in August–September 2026 surfaced only a model/template deprecation notice (retiring 10 models and an API on 2026-09-15) and continued video/image-generation iteration, none of it on our 4 tracked topics (3D generation, world models, character animation, game engines/tooling) with a dated, in-window, primary-sourced release.

### Announced only (not yet usable)
- none.

Near-misses: none substantive — Kling's activity this window is video/image generation quality iteration, outside Part B's 4 topics for this sweep.

---

## Overall near-misses (cross-company)
- Jianying/CapCut ICG Studio (ByteDance) — interactive-movie/game creation platform, first shown 2026-09-20, no primary source or confirmed availability.
- Jianying/CapCut digital-human narration feature (ByteDance) — reported in internal beta, expected end-of-September launch, unconfirmed by any ByteDance primary source as of 2026-09-28.
- NetEase Fuxi GDC talk on speech-driven facial animation (2026-07-21) — research disclosure, no product surface.
