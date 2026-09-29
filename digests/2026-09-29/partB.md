# Part B — Research → Product
Window: last 90 days (2026-07-01 to 2026-09-29). Retrieval: light check (10 primary surfaces; Monday full sweep resumes next). Products: 1 new, 0 updated.

---

## The Witcher 3: Wild Hunt — Remastered: Path Tracing & DLSS 4.5 Ray Reconstruction
- **Company:** NVIDIA (feature shipped in CD PROJEKT RED's The Witcher 3: Wild Hunt — Remastered)
- **Status:** GA · **Released:** 2026-09-29 · **New**
- **Surface:** Shipped game (free content/graphics update), via NVIDIA Game Ready Driver
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/witcher-3-wild-hunt-remastered-path-tracing-dlss-4-5-ray-reconstruction/
- **Underlying research:** no traceable paper (page does not cite a specific arXiv paper for the 2nd-generation Ray Reconstruction transformer model or the Linear-Swept Spheres hair technique)
- **Availability:** Free update, PC only, GeForce RTX 40/50 Series required for the full feature set (SER, path-traced hair); available now for anyone who owns the game, no waitlist.

**What shipped (≤3 sentences):** NVIDIA and CD PROJEKT RED shipped a free update adding full path tracing to The Witcher 3: Wild Hunt — Remastered on PC, with DLSS 4.5 Ray Reconstruction using NVIDIA's "second-generation transformer" AI denoising model. RTX 50-series owners additionally get up to 6X DLSS Multi Frame Generation and a new Linear-Swept Spheres path-traced hair-rendering technique; RTX 40-series owners get Shader Execution Reorder (SER)-optimized path tracing.
**What research it translates (≤3 sentences):** This extends the same DLSS 4.5 Ray Reconstruction transformer model and RTX path-tracing/hair-rendering pipeline NVIDIA has been rolling out across other titles this cycle (e.g. Control: Resonant, 007 First Light); no separate paper is cited on this page.
**Practical significance (≤3 sentences):** NVIDIA states performance reaches up to 385 FPS at 4K on RTX 5090 and 245 FPS at 4K on RTX 5080 in Ultra+ path tracing mode, making a 2015-era open-world game fully path-traced and AI-upscaled at high frame rates. It is a concrete example of NVIDIA's DLSS 4.5 stack being retrofitted into an existing shipped/remastered title rather than only new releases.
**Engineering details (≤3 sentences):** Ships alongside a new GeForce Game Ready Driver (released 2026-09-22, covering this title plus Control: Resonant, Gears of War: E-Day and AION 2). Uses DLSS 4.5 Ray Reconstruction (2nd-gen transformer denoiser), Multi Frame Generation (up to 6X on RTX 50), SER (RTX 40/50), and Linear-Swept Spheres hair rendering (RTX 50 only). PC-only; no console version mentioned.
**Limitation / caveats (≤3 sentences):** Highest-end features (6X Frame Generation, Linear-Swept Spheres hair) are gated to RTX 50-series GPUs; RTX 40-series gets a reduced feature set and older/non-RTX GPUs get no path tracing. No underlying research paper is cited by NVIDIA for this specific update.

### Announced only (not yet usable)
(none new in this window)

Near-misses: Kling 4.0 Flash (Kuaishou) — unverified availability/tier; PS5 Pro PSSR default-on update — outside window (dated 09-16); Roblox 20th-anniversary event — not a product; Adobe Firefly September updates — off-topic (generic image/video features); Alibaba Bailian Qwen3.8 listings — off-topic (general LLM/audio, not on tracked topics); Unity 6000.6.3f1 — minor patch; Tencent Hunyuan 3D 3.1 — outside window (July release); ByteDance real-time 3D world model report — outside window/announced-only; NVIDIA dev-blog AI-infra/agent/robotics posts — off-topic; Unreal Engine forum threads — not material.
Verification: every listed item and near-miss was checked against its own primary-source page (NVIDIA GeForce news, klingai.com/kling.ai, PlayStation Blog, Roblox newsroom/devforum, Adobe blog, Alibaba Model Studio catalog, Unity release notes, Unreal Engine forums, Tencent/ByteDance official pages) rather than trade-press summaries alone.
