# Part B — Light Check (2026-09-22 to 2026-09-29)

Surfaces checked (10): NVIDIA developer blog + GeForce news; Unreal Engine news + forum announcements; Unity news/blog + release notes; Roblox newsroom + devforum updates; Adobe blog + research.adobe.com/news; Tencent Hunyuan (hunyuan.tencent.com / 3d.hunyuan.tencent.com); ByteDance Volcano Engine / Seed (seed.bytedance.com); Alibaba Model Studio (Bailian) newly-released-models; Kuaishou Kling (klingai.com → kling.ai); PlayStation Blog.

Cross-checked against `state/product_seen.json` (loaded before this run) to separate New vs. Previously-reported vs. material Update.

---

## The Witcher 3: Wild Hunt — Remastered: Path Tracing & DLSS 4.5 Ray Reconstruction Update
- **Company:** NVIDIA (feature shipped in CD PROJEKT RED's The Witcher 3: Wild Hunt — Remastered)
- **Status:** GA · **Released:** 2026-09-29 · **New**
- **Surface:** Shipped game (free content/graphics update), via NVIDIA Game Ready Driver
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/witcher-3-wild-hunt-remastered-path-tracing-dlss-4-5-ray-reconstruction/
- **Underlying research:** no traceable paper (page does not cite a specific arXiv paper for the 2nd-gen Ray Reconstruction transformer model or the Linear-Swept Spheres hair technique)
- **Availability:** Free update, PC only, GeForce RTX 40/50 Series required for full feature set (SER, path-traced hair); available now for anyone who owns the game — no waitlist.

**What shipped (≤3 sentences):** NVIDIA and CD PROJEKT RED shipped a free update adding full path tracing to The Witcher 3: Wild Hunt — Remastered on PC, with DLSS 4.5 Ray Reconstruction using NVIDIA's "second-generation transformer" AI denoising model. RTX 50-series owners additionally get up to 6X DLSS Multi Frame Generation and a new Linear-Swept Spheres path-traced hair-rendering technique; RTX 40-series owners get Shader Execution Reorder (SER)-optimized path tracing.
**What research it translates (≤3 sentences):** This extends the same DLSS 4.5 Ray Reconstruction transformer model and RTX path-tracing/hair-rendering pipeline NVIDIA has been rolling out across other titles (e.g., Control: Resonant, 007 First Light) this cycle; no separate paper is cited on this page.
**Practical significance (≤3 sentences):** NVIDIA states performance reaches up to 385 FPS at 4K on RTX 5090 and 245 FPS at 4K on RTX 5080 in Ultra+ path tracing mode, making a 2015-era open-world game fully path-traced and AI-upscaled at high frame rates. It is a concrete example of NVIDIA's DLSS 4.5 stack being retrofitted into an existing shipped/remastered title rather than only new releases.
**Engineering details (≤3 sentences):** Ships alongside a new GeForce Game Ready Driver (released 2026-09-22, covering this title plus Control: Resonant, Gears of War: E-Day and AION 2). Uses DLSS 4.5 Ray Reconstruction (2nd-gen transformer denoiser), Multi Frame Generation (up to 6X on RTX 50), SER (RTX 40/50), and Linear-Swept Spheres hair rendering (RTX 50 only). PC-only; no console version mentioned.
**Limitation / caveats (≤3 sentences):** Highest-end features (6X Frame Generation, Linear-Swept Spheres hair) are gated to RTX 50-series GPUs; RTX 40-series gets a reduced feature set and older/non-RTX GPUs get no path tracing. No underlying research paper is cited by NVIDIA for this specific update.

---

### Announced only (not yet usable)
(none new in this window beyond items already tracked in product_seen.json)

---

Near-misses:
- Kling 4.0 / Kling 4.0 Flash (Kuaishou) — unverified (trade press and social media state Flash went live 2026-09-28 for Ultra Yearly subscribers, but klingai.com redirects to kling.ai and neither the homepage nor the pricing page could be made to confirm availability, tier-gating, or a waitlist; also borderline on-topic as a generic video-generation model rather than 3D/world-model/character-animation/engine feature)
- PS5 Pro "Enhance PSSR Image Quality" default-on system update — outside-window (trade press dates the update to 2026-09-16, before the 2026-09-22–09-29 window; no blog.playstation.com primary post was found)
- "Join The Hunt: Roblox 20" anniversary event (Roblox newsroom, running through 2026-09-28) — not-a-product (community/nostalgia event revisiting old games, not a new engine/creation-tool feature)
- Adobe Firefly "What's new — September 2026" (background removal for video, GPT Image 2 aspect ratios) — off-topic (generic image/video generation features, not 3D/world-model/character-animation/game-engine)
- Alibaba Bailian new listings (Qwen3.8-Max, Qwen3.8-Omni-Flash, Qwen-Audio-3.1-TTS-Flash, released 2026-09-01/09-18) — off-topic (general LLM/audio models, not on the four tracked topics)
- Unity 6000.6.3f1 (released 2026-09-24) — minor-patch (bug-fix/patch release per Unity's own release notes, no material new capability)
- Tencent Hunyuan 3D 3.1 — outside-window (released July 2026, day-zero third-party integration tweets found but no new primary-source activity in the 09-22–09-29 window)
- ByteDance real-time 3D world model (Bloomberg report) — outside-window/announced-only (reported 2026-09-08, "as early as October" unveiling; no product surface yet)
- NVIDIA developer-blog items dated in window (Sept 22–28: Open Agent Safety Platform, OpenShell, DSX MaxLPS, NodeWright, NV-Reason-CT, Isaac ROS agent post) — off-topic (general AI-infra/agent/robotics-perception posts, not 3D graphics/world-models/character-animation/game-engines)
- Unreal Engine forum items in window (Fortnite 42.30 known-issues thread; UEFN-source-assets-to-Fab thread, dated 09-21 just outside window) — not-material (known-issues notice / already-covered ecosystem note, no new shipped feature)

Verification: Every item above (both the reported item and each near-miss) was checked against its own primary-source page (NVIDIA GeForce news, klingai.com/kling.ai, PlayStation Blog, Roblox newsroom/devforum, Adobe blog, Alibaba Model Studio help.aliyun.com catalog, Unity release notes, Unreal Engine forums, Tencent/ByteDance official pages) rather than relying on trade-press summaries alone; where a primary source could not confirm a claim (Kling 4.0 Flash tier/availability), it is flagged "unverified" and excluded from the main list rather than forced in.
