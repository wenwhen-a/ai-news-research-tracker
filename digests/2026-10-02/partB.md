# Part B — Research → Product
Window: last 7 days (2026-09-25 to 2026-10-02, light check). Products: 1 new, 0 updated.

---
## QSSR (Quick Spectral Super Resolution) on PS5
- **Company:** Sony Interactive Entertainment (post authored by Daniel Craig, Principal Engineer, Graphics R&D, SIE)
- **Status:** GA · **Released:** 2026-10-01 · **New**
- **Surface:** Platform feature (console-level AI upscaler), shipped day-one in patches for two games
- **Primary source:** https://blog.playstation.com/2026/10/01/ai-upscaling-is-coming-to-ps5/
- **Underlying research:** no traceable paper
- **Availability:** Live now on base PS5 (not PS5 Pro) as an in-game graphics option; patched into Marvel's Wolverine and Ghost of Yōtei on 2026-10-01; free, no waitlist. Sony states it "will be offered broadly to all PlayStation developers" for future titles.

**What shipped (≤3 sentences):** Sony shipped QSSR, a new AI upscaler for the base (non-Pro) PS5, distinct from PSSR which remains the standard on PS5 Pro. It launched with same-day patches adding a QSSR option to Marvel's Wolverine and Ghost of Yōtei.
**What research it translates (≤3 sentences):** Sony states QSSR came out of Project Amethyst, SIE's ongoing machine-learning graphics research collaboration with AMD, using "a streamlined neural network architecture" and a "hand-tuned implementation" built for PS5's more limited compute budget relative to PS5 Pro. No paper or technical report is cited.
**Practical significance (≤3 sentences):** Sony states QSSR brings "notable improvements to both image detail and image stability on PS5," and developers quoted in the post say it "adds more pixel-level clarity and stability" with temporal stability "that hasn't been possible on the PS5 console until now." It extends PSSR-class ML upscaling, previously PS5-Pro-exclusive, down to the much larger base-PS5 install base at no cost to players.
**Engineering details (≤3 sentences):** Delivered as a per-game, per-title integration (not an OS-level automatic toggle) via day-one patches to Marvel's Wolverine and Ghost of Yōtei; Sony did not disclose model size, inference cost, or hardware-level details beyond "streamlined" versus PSSR. Built under the same Project Amethyst SIE/AMD graphics-research partnership that produced PSSR.
**Limitation / caveats (≤3 sentences):** Available only in the two patched titles at launch; Sony gives no committed list or timeline for further titles beyond saying it will roll out "broadly." No benchmark numbers (frame-time cost, resolution tiers) are given in the announcement, only qualitative developer quotes.

### Announced only (not yet usable)
(none)

Near-misses: NVIDIA/IO Interactive "Gears of War: E-Day" GeForce news post (2026-10-01, https://www.nvidia.com/en-us/geforce/news/gears-of-war-e-day-dlss-4-5-ray-tracing-rtx-mega-geometry/) — DLSS 4.5 Ray Reconstruction and RTX Mega Geometry are already-tracked features (both logged in product_seen.json from earlier runs); this is one more game adopting existing features, not a new or materially changed product, so it is excluded per the task's rule.
Verification: every listed item was checked against its primary source (release date, releasing company, status tier, and every claim) before inclusion. Surfaces checked for this window: NVIDIA developer blog and GeForce news, Unreal Engine news/forum (unrealengine.com/news, forums.unrealengine.com — both returned errors on direct fetch; no in-window items surfaced via search either), Unity blog/editor release notes, Roblox newsroom and devforum announcements, Adobe blog, Tencent Hunyuan (hunyuan.tencent.com), ByteDance Seed (seed.bytedance.com), Alibaba Cloud Model Studio release-notes page (latest dated entries end 2026-09-24, just outside window), Kuaishou Kling (klingai.com redirects to kling.ai), and PlayStation Blog. All items already in state/product_seen.json with first_seen dates in this window (Roblox Texture Generation Tools, Roblox Quad Support for EditableMesh, Roblox Frustum Streaming, Meta Hologram, Tencent Motus/MagicDawn/GIGA, Qualcomm Adreno Neural Fusion, Unity 7 preview, The Witcher 3 Remastered path tracing, Control: Resonant DLSS 4.5) were confirmed unchanged and not re-listed.
