# Part B — Research → Product
Window: last 90 days (2026-08-23 to 2026-11-21). Light check of ~10 primary surfaces for items dated 2026-11-14 to 2026-11-21 (today is not a Monday, so no full sweep). Qualifying products: 1 (1 new, 0 updated). Announced-only: 0.

---
## UEFN Semantic Search — AI-powered Content Browser search
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-11-18 · **New**
- **Surface:** Engine / studio tool (UEFN Content Browser)
- **Primary source:** https://forums.unrealengine.com/t/semantic-search-is-now-live-in-uefn-v43-12
- **Underlying research:** no traceable paper

**What shipped (≤3 sentences):** Epic's UEFN v43.12 update adds an AI search mode to the Content Browser: toggling an "AI" button next to any search bar lets a creator type a natural-language description (e.g. "rusted metal barrel") and get matching assets by visual appearance/type rather than literal filename match (Epic's own example: that query surfaces an asset named `M_OldOilDrum`).
**What research it translates (≤3 sentences):** No external research paper is cited; Epic's forum post frames it as an embedding/semantic-matching search layer over the existing asset library's appearance and type metadata.
**Practical significance (≤3 sentences):** Epic states the feature is "now live" for all UEFN creators as of the v43.12 update, letting creators find assets by describing them instead of knowing their exact names.
**Engineering details (≤3 sentences):** Surfaced as an opt-in toggle inside the existing Content Browser search bar; matches on visual appearance and asset type rather than name strings.
**Limitation / caveats (≤3 sentences):** Epic's own post states the feature "currently works best with English queries," with no stated support for other languages yet; Epic does not label a separate beta/GA rollout tier beyond "now live."

### Announced only (not yet usable)
- none found in this window

Near-misses: 4 — Roblox Studio MCP Server (already GA, first_seen 2026-11-05) gained three new agent tool capabilities on 2026-11-20 (video capture in screen_capture, save_place, submit_feedback; devforum.roblox.com) — a real feature expansion but not a tier change, new major version, new platform, or pricing change, so not logged as an update. NVIDIA developer-blog tutorial "Build Training-Ready Physical AI Datasets with Two Prompts in NVIDIA Cosmos" (2026-11-18) mentions Cosmos Curator gaining multicamera/IMU/GPS/lidar input and Cosmos Dataset Search going open-source with an early-access agentic reranking feature, but it is framed as a how-to post with ambiguous GA/beta status, not a clean product announcement. NVIDIA RTX Spark compact-desktop hardware launch (blogs.nvidia.com, 2026-11-18) is a hardware SKU tied to the RTX Spark/neural-rendering ecosystem, not itself a 3D/world-model/character-animation/game-engine software feature. Two Roblox devforum items dated in-window ("[Studio Beta] UI Particles", 2026-11-19; "Create Avatar Moments to Showcase and Sell Your Items", 2026-11-20) are off-topic for the four tracked areas (no generative/ML component).
Verification: the new item was checked against Epic's own forum announcement (forums.unrealengine.com, fetched directly, independently re-verified) for date, company, and claims; product_seen.json was checked to confirm it is not already recorded. All ten primary surfaces (NVIDIA dev blog/GeForce news/blogs.nvidia.com, Unreal Engine news/forums, Unity blog, Roblox newsroom/devforum, Adobe blog, Tencent Hunyuan, ByteDance Volcano Engine/Seed, Alibaba Model Studio release notes, Kuaishou Kling release notes, PlayStation Blog) were checked for the 2026-11-14 to 2026-11-21 window; unrealengine.com/en-US/news returned HTTP 403 to automated fetch and hunyuan.tencent.com/3d.hunyuan.tencent.com are JS-only SPAs with no fetchable content, so those two were covered via the Unreal forums and Tencent Cloud's Hunyuan doc/catalog pages respectively.
