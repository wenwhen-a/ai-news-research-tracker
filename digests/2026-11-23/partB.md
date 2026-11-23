# Part B — Research → Product
Window: last 90 days (2026-08-25 to 2026-11-23). Monday full sweep across Western big tech/publishers, NVIDIA/Adobe/engines, and Chinese tech groups, plus a recheck of recently-tracked products for material changes. Qualifying products: 5 (2 new, 3 updated). Announced-only: 2. (The Part B sweep also re-surfaced Kling 4.0's Nov 19 4K/HDR API update, but that change was already recorded in product_seen.json from the 2026-11-20 run, so it is not re-listed here.)

---
## Roblox Studio — Automatic In-Game Image Text Translation (Beta)
- **Company:** Roblox
- **Status:** Public beta/preview · **Released:** 2026-11-10 · **New**
- **Surface:** Studio / Creator Hub localization tool (engine feature)
- **Primary source:** https://create.roblox.com/docs/production/localization/image-translations
- **Underlying research:** no traceable paper
- **Availability:** Beta ("functionality and availability are subject to change," per Roblox's own docs). Opt-in per target language via the Languages tab plus a new "Automatic Image Capture" setting; developers then enable translated-content on a per-image basis. Supported languages at launch: French, German, Indonesian, Italian, Korean, Portuguese, Spanish. Free, included in Roblox Studio/Creator Hub; no separate pricing. Translations are not instant — Roblox states capture and generation can take "up to a few days."

**What shipped (≤3 sentences):** Roblox shipped a beta that automatically detects and translates text baked into in-game images (signs, UI graphics, textures) rather than only text rendered through TextLabel/TextButton objects, which earlier automatic-translation tooling covered. The system regenerates the image with translated text while trying to match the original's font size, style and color, leaving non-text elements unchanged. Developers review source vs. translated images side by side and can disable a translation per image via the AutoLocalize property.
**What research it translates (≤3 sentences):** Roblox's docs give no model name or citation, and no matching paper was found via arXiv search on "image text translation," "scene text editing," or "visual text localization" tied to Roblox. The capability (OCR + style-preserving text replacement + translation) maps to the general "scene text editing" research area, but Roblox does not name a source, so per the no-inference rule this is recorded as no traceable paper.
**Practical significance (≤3 sentences):** This extends Roblox's existing automatic-translation system (previously text-only, then speech-to-speech via Automatic Translation for Text-to-Speech shipped Oct 8, 2026) to in-game visual assets, closing a localization gap that previously required artists to manually re-author translated textures per locale. Roblox states the feature is meant to let any creator reach non-English-speaking players without manual localization work on image assets.
**Engineering details (≤3 sentences):** The pipeline runs asynchronously: Studio/the client captures images containing text as players encounter them, queues them for translation, and populates a per-image localization table once generation completes (hence the multi-day lag). Generated translated images are visible only to the creator first, and developers get a feedback control to flag bad translations.
**Limitation / caveats (≤3 sentences):** Coverage is limited to seven languages at beta launch and excludes non-text visual elements by design. Generation latency (up to several days) makes it unsuitable for dynamically generated or frequently-changing in-game images. Roblox has not stated a GA timeline or published accuracy/fidelity benchmarks for the style-matching claim.

---
## Seedream 5.5
- **Company:** ByteDance
- **Status:** GA · **Released:** 2026-11-09 · **New**
- **Surface:** Consumer apps (Dreamina/即梦, Doubao) + cloud API (Volcano Engine Ark / BytePlus)
- **Primary source:** https://seed.bytedance.com/blog/more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5
- **Underlying research:** no traceable paper (prior generations have arXiv technical reports — e.g. "Seedream 4.0: Toward Next-generation Multimodal Image Generation" — but no 5.5-specific report was found on the launch page)
- **Availability:** ByteDance's own Seed blog/product page offers access via the "Dola" chat app and the BytePlus Playground, plus a "Get API" and an "Enterprise" path; no resolution tiers or pricing are stated on the primary page itself.

**What shipped (≤3 sentences):** ByteDance's Seed team shipped Seedream 5.5, a new image generation/editing model, on 2026-11-09, reachable today through ByteDance's own Dola app, the BytePlus Playground, and a developer API/enterprise path. It is positioned as the successor to Seedream 5.0 Pro, targeting professional image-creation workflows rather than a research preview.
**What research it translates (≤3 sentences):** ByteDance states the model improves multi-turn edit stability and adds native transparent (RGBA) output, extending the Seedream image-generation line whose earlier generations (3.0, 4.0) were documented in ByteDance's own arXiv technical reports. No Seedream-5.5-specific paper was found, so the exact research lineage for this version is not independently traceable.
**Practical significance (≤3 sentences):** ByteDance states that unedited regions of an image stay pixel-level stable across up to 100 successive edit rounds, aimed at iterative production work (e.g., e-commerce, marketing, game-asset, and fashion imagery) where earlier models would drift after a few edits. ByteDance also states the model generates native semi-transparent/transparent layers without a separate background-removal step. These are ByteDance's own claims, not independently verified.
**Engineering details (≤3 sentences):** The primary page highlights three capability pillars — multi-turn editing with pixel-level preservation, native RGBA transparent-background generation, and more naturalistic lighting/material/skin rendering — but gives no architecture, parameter-count, or resolution-ceiling details.
**Limitation / caveats (≤3 sentences):** The primary product page states no pricing, resolution limits, or regional availability. Benchmark comparisons against competing models (reported in trade press, not on the primary page) are ByteDance's own self-reported figures and were not independently verified.

---
## NVIDIA DLSS 5 with 3D-Guided Neural Rendering (Where Winds Meet rollout)
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-11-23 (Where Winds Meet rollout) · **Update**
- **Surface:** Shipped games (PC/GeForce NOW, in-game "Neural Rendering" toggle)
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/hogwarts-legacy-war-thunder-dlss-5-3d-guided-neural-rendering/
- **Underlying research:** NVIDIA Research project page, "DLSS 5: Generative Neural Rendering" — describes a real-time, one-step pixel-space diffusion model; no arXiv preprint found.
- **Availability:** GeForce RTX 50 Series desktop/laptop GPUs, RTX Spark systems, and GeForce NOW Ultimate; free, no waitlist, via a Game Ready Driver.

**What shipped (≤3 sentences):** Update since 2026-09-13: NVIDIA and developer Everstone Studio/publisher NetEase added DLSS 5 with 3D-Guided Neural Rendering to the wuxia open-world game Where Winds Meet, available November 23 in North America (November 24 elsewhere), following the same feature's earlier November rollouts to Hogwarts Legacy (Nov 5) and War Thunder (Nov 12). This completes the three-game rollout NVIDIA had announced as "pending" in its November 12 update.
**What research it translates (≤3 sentences):** DLSS 5 is built on a generative, diffusion-based neural renderer that treats the game engine's finished frame — geometry, textures, lighting buffers and motion vectors — as a conditioning signal for AI-generated final pixels, per NVIDIA's own research description. No peer-reviewed arXiv paper describes this specific technique.
**Practical significance (≤3 sentences):** NVIDIA states the feature now covers four shipped titles (NBA 2K27, Hogwarts Legacy, War Thunder, Where Winds Meet) plus RTX Remix, giving RTX 50-series/RTX Spark/GeForce NOW Ultimate owners a toggleable, no-cost visual upgrade.
**Engineering details (≤3 sentences):** Delivered via a Game Ready Driver update tied to each game's own patch, rather than a separate downloadable model; NVIDIA iterated the underlying model several times this quarter ahead of this rollout.
**Limitation / caveats (≤3 sentences):** Still restricted to RTX 50-series/RTX Spark/GeForce NOW Ultimate hardware, excluding RTX 40-series and older owners entirely. NVIDIA has not published independent third-party image-quality benchmarks for the Where Winds Meet implementation specifically.

---
## Unreal Engine 5.9 Preview (Unreal Canvas, AnimGen AI animation, MCP/agent tooling)
- **Company:** Epic Games
- **Status:** Public beta/preview · **Released:** 2026-11-19 (Preview 2) · **Update**
- **Surface:** Engine / editor (Preview build)
- **Primary source:** https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-9-release-notes
- **Underlying research:** "Control Operators for Interactive Character Animation," Ruiyu Gou (Epic Games), ACM Transactions on Graphics, Dec. 2025 — describes a controller-agnostic framework shown on a flow-matching-based autoregressive motion model. No arXiv preprint found.
- **Availability:** Free public Preview download via Epic Games Launcher/source; Epic states it "should be considered unstable until the final release."

**What shipped (≤3 sentences):** Update since 2026-11-09: the UE5.9 Preview build was revised (Preview 2, last updated 2026-11-19) adding the experimental UAF AnimGen plugin — a trained, flow-matching neural character controller that drives an AnimNode frame-by-frame — alongside the already-announced experimental Unreal Canvas collaborative workspace and expanded Python/Unreal MCP agent tooling. Epic says the Preview was built largely by AI agents under engineer direction.
**What research it translates (≤3 sentences):** AnimGen's controller uses flow matching and a neural network to synthesize character poses in real time, matching the approach Epic's own Ruiyu Gou published in ACM TOG (Control Operators). Unreal Canvas and the expanded MCP tooling reflect Epic's broader push toward agent-assisted content creation inside the editor itself.
**Practical significance (≤3 sentences):** Epic states this gives developers an experimental path to AI-driven procedural character animation (AnimGen) and agent-operable editing (Canvas, MCP) directly in a Preview build anyone can download today. It is explicitly not production-ready.
**Engineering details (≤3 sentences):** AnimGen is built on Epic's Universal Animation Framework (UAF) and includes an AutoEncoder plus multiple behavior classes driving the pose-generation AnimNode. The Preview also ships an experimental WebAssembly/WebGPU export target.
**Limitation / caveats (≤3 sentences):** Epic flags AnimGen, Unreal Canvas and the WebAssembly target as experimental/prototype features that may be refactored or removed before the full 5.9 release ships. The release notes do not fix a GA date for Unreal Engine 5.9.

---
## AMD FSR SDK 2.4 (FSR Upscaling 4.1.2 on RDNA 2, Vulkan parity, driver-assisted frame pacing)
- **Company:** AMD
- **Status:** GA · **Released:** 2026-10-28 · **Update**
- **Surface:** SDK / engine plugin (cross-engine, cross-API)
- **Primary source:** https://gpuopen.com/manuals/fsr_sdk/whats-new/
- **Underlying research:** No traceable paper.
- **Availability:** Free, available now via GitHub (precompiled binaries plus limited source) and GPUOpen; DirectX 12 and (new) Vulkan.

**What shipped (≤3 sentences):** Update since 2026-09-13: AMD's FSR SDK moved from 2.3 to 2.4, extending full-INT8 AI model support for FSR Upscaling 4.1.2 down to Radeon RX 6000 (RDNA 2) discrete GPUs, and bringing several FSR effects to feature parity on Vulkan alongside DirectX 12. It also adds Driver-Assisted Frame Pacing, limited to RX 9000-series GPUs and newer.
**What research it translates (≤3 sentences):** AMD has not published the underlying model architecture as a paper; GPUOpen's own documentation describes the SDK as a packaging of AMD's existing "Redstone" ML upscaling and frame-generation models.
**Practical significance (≤3 sentences):** AMD states this gives RX 6000-series owners access to the full-quality INT8 model, and gives Vulkan-based titles the same FSR 4 feature set as DirectX 12 games. Ray Regeneration and Radiance Caching remain DirectX-12-only and RDNA 4+-only.
**Engineering details (≤3 sentences):** The SDK ships as precompiled binaries plus limited source code on AMD's GitHub repository.
**Limitation / caveats (≤3 sentences):** Driver-Assisted Frame Pacing is gated to RX 9000-series-and-newer hardware only. No independent benchmarks of the RX 6000 full-INT8 model's performance impact were found.

### Announced only (not yet usable)
- Genie 4 (world model: real-time interactive simulation with native audio, steerable via natural language) · Google/DeepMind · 2026-10-27 · https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/ — rollout started only to a limited group of trusted testers; no customer or developer can use it today without an invitation.
- Adobe Dimension (rebuilt, Beta) · Adobe · 2026-11-09 (tied to Adobe MAX, Nov 10) · https://helpx.adobe.com/dimension/desktop/about-the-new-dimension.html — private prerelease signup for existing Dimension/Stager subscribers only; Adobe states GA is planned for 2027.

Near-misses: 11 — Amazon GameLift Streams "Instant Play Demos" (used by Pearl Abyss's Crimson Desert demo since ~Aug 31, 2026) could not be pinned to a primary-sourced GA date/tier (AWS gametech blog pages would not render). Square Enix's Gemini-powered internal QA tool and Capcom's "RE Engine → AI-generation engine" roadmap statement are trade-press-only with no primary source or ship date. Krafton/NVIDIA's PUBG Ally beta ended before this window with no GA found; Ubisoft's "Teammates" project and NCSoft's VARCO 3D both predate the 90-day window. Meta's Hologram remains announced-only with no confirmed Early Access rollout. Unity Production Pipeline is still invitation-only closed beta despite a stated "November 2026" public-availability target (first announced outside this window). Adobe Firefly 3D Digital Twin and Firefly Graph lack a clear GA/beta tier or are general creative-workflow tools rather than 3D/animation-specific. Baidu's 文心一镜 micro-expression model + 百度一镜 短漫剧Studio (announced at Baidu World, Nov 12) and Tencent Hunyuan 3D Studio 1.2 could not be confirmed via a primary source or in-window date. NetEase's AI short film "倩影" is a marketing case study, not a product surface. ByteDance's reported Nov 16 "full opening" of Seedance 2.5 4K API lacks a primary Volcano Engine/BytePlus page confirming that date. No qualifying new or updated product was found for Microsoft/Xbox, Google (consumer side beyond Genie 4), Meta (beyond Hologram), Apple, EA, Sony, Nintendo, Valve, Take-Two/Rockstar, Activision Blizzard, Krafton, Nexon, NCSoft, Square Enix, Sega, Capcom, Bandai Namco, Konami, Embracer, CD Projekt, Intel, Qualcomm, Tencent (beyond near-misses), Alibaba, Baidu (beyond near-miss), miHoYo or NetEase (beyond near-misses) in this window.
Verification: every item above was checked against its own primary source (company blog/newsroom/docs/release notes/API changelog, fetched directly) for release/change date, company, on-topic fit and status tier; `product_seen.json`'s existing entries across all three groups were spot-checked (prioritizing "Announced only" and versioned entries) for GA/version/availability changes dated within the last 7 days, and no other material changes beyond the six above were found.
