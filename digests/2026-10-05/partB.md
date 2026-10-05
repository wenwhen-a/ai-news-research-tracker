# Part B — Research → Product
Window: last 90 days (2026-07-07 to 2026-10-05). Monday full sweep (Western big tech & publishers / NVIDIA-Adobe-engines / Chinese tech groups, each with direct primary-source checks; `github_releases.py` lead generator returned HTTP 403 Forbidden on every tracked org this run and contributed no leads) plus a 90-day re-check of every item already in `state/product_seen.json` for material changes. Products: 3 new, 3 updated.

---

## MagicDawn GI
- **Company:** Tencent (Tencent Games)
- **Status:** GA (free / non-commercial tier) · **Released:** date not stated on page (previously Announced-only as of 2026-09-28; observed changed 2026-10-05) · **Update**
- **Surface:** studio tool / cross-engine rendering plugin
- **Primary source:** https://magicdawn.tencent.com/?lang=en
- **Underlying research:** no traceable paper
- **Availability:** Free download, personal version restricted to "个人学习、研究和非商业用途" (personal learning, research and non-commercial use); commercial licensing by contacting magicdawn@tencent.com

**What shipped (≤3 sentences):** Update since 2026-09-28: MagicDawn, Tencent Games' rendering brand previously tracked as Announced-only in full, now states on its own page "MagicDawn GI 现已开放免费使用" (GI is now open for free use) with a "免费下载 GI 工具" (free-download GI tool) button — the GI (global illumination) component specifically has moved from announced to self-serve downloadable. The other named sub-tools remain earlier-stage: NDGI (neural dynamic global illumination) is in "Beta 试用" (beta trial), and SPATIAL, COMPRESS and REMASTER are still listed as "coming soon."
**What research it translates (≤3 sentences):** Tencent describes MagicDawn as its "前沿渲染品牌" (frontier rendering brand) for AI-driven graphics and cross-engine adaptation; the page cites no specific paper — "no traceable paper."
**Practical significance (≤3 sentences):** Tencent states the GI tool can be freely downloaded for personal, non-commercial use today, giving individual developers/engine integrators access to the global-illumination tool without an invitation or waitlist, while commercial use still requires contacting Tencent directly.
**Engineering details (≤3 sentences):** The page mentions an activation-key mechanism for engine integration but no engine compatibility list (e.g., Unreal/Unity) or version number was retrievable; the destination URL of the download button could not be resolved via automated fetch.
**Limitation / caveats (≤3 sentences):** The free tier is explicitly non-commercial-only, so this is not unrestricted GA; whether the download requires account registration could not be confirmed. NDGI and the other three sub-brands (SPATIAL, COMPRESS, REMASTER) remain gated/unreleased, so most of the MagicDawn brand is still effectively Announced-only.

## Roblox Studio — Expanding the Character Controller Library (Custom Abilities API, new default abilities)
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta) · **Released:** 2026-10-03 (expanded beta post; initial Studio Beta announced 2026-09-10) · **New**
- **Surface:** Roblox Studio / Character Controller Library (CCL)
- **Primary source:** https://devforum.roblox.com/t/studio-beta-expanding-the-character-controller-library-new-default-abilities-custom-abilities-api/4863739
- **Underlying research:** no traceable paper
- **Availability:** Opt-in Studio Beta, cross-platform (keyboard/mouse, gamepad, touch) with platform-specific default keybindings; free for all Roblox creators who opt into the beta.

**What shipped (≤3 sentences):** Roblox expanded its Character Controller Library (CCL) beta with a Custom Abilities API (lifecycle methods OnSetup/OnStart/OnStop/OnUpdate) plus two new default abilities, Sprint and Crouch, and a reworked Shift-Lock called "Configurable Turning." Creators can bind abilities to cross-platform action slots and either extend or fully replace the default ability set, with optional Server Authority for consistency.
**What research it translates (≤3 sentences):** This is an engine/architecture replacement for Roblox's legacy Humanoid movement system rather than a packaged research result; Roblox states upcoming work "includes incorporating animations into the CCL so that they can be driven by abilities directly," linking it to the still-Announced-only "New Default Movement" (motion matching + root motion) roadmap item. No underlying paper is cited.
**Practical significance (≤3 sentences):** Roblox states CCL characters run "10% to 25% faster" than legacy Humanoid during active gameplay and "up to 1.5x faster" during steady motion, and that walk animations driven by the new system are "already deployed on mobile and console platforms." Creators get a documented, cross-platform input/ability framework instead of hand-rolling movement scripts per platform.
**Engineering details (≤3 sentences):** The Custom Abilities API supports Press/Hold/Toggle/Repeat input bindings mapped automatically across keyboard, gamepad and touch; Server Authority can be enabled per-ability for networked consistency. Blended animations for locomotion are listed as planned future work, not yet shipped.
**Limitation / caveats (≤3 sentences):** This is still an opt-in Studio Beta, not a default-on system, and animation-driven abilities / blended locomotion are future work, not current functionality. (Borderline on-topic: primarily a movement/input-architecture change rather than animation content generation; included for its stated animation-system roadmap tie-in — observed, not stated, as a strict qualifier.)

## Roblox Marketplace — Create and Sell Animation Packs
- **Company:** Roblox
- **Status:** GA (Full Release) · **Released:** 2026-10-02 (pilot access since 2026-09-09) · **New**
- **Surface:** Roblox Studio / Marketplace (Creator Store)
- **Primary source:** https://devforum.roblox.com/t/full-release-create-and-sell-animation-packs-on-marketplace/4861803
- **Underlying research:** no traceable paper
- **Availability:** Open to verified creators with a Roblox Plus membership; one pack upload per day at launch; marketplace minimum price 300 Robux plus an 80-Robux upload fee; supports Limited editions and group uploads.

**What shipped (≤3 sentences):** Roblox moved "Animation Packs" on its creator Marketplace to full release, letting creators author and sell bundles of custom locomotion animations — covering Idle, Walk, Run, Jump, Fall, Climb and Swim states — for use across any compatible Roblox experience. Animations must be authored/converted to Roblox's CurveAnimation format in Studio, and the platform runs automated validation of movement constraints and runtime limits before publishing.
**What research it translates (≤3 sentences):** This is a creator-economy/marketplace feature for hand-authored or externally-created animation content, not a generative-AI or research-derived capability; Roblox's post describes no AI/ML component. No underlying paper applies.
**Practical significance (≤3 sentences):** Creators can now monetize reusable character-locomotion animation sets across the Roblox catalog rather than building bespoke animations per experience, with ID verification and Roblox Plus required to publish. Roblox states the feature began with a pilot program (access from 2026-09-09) before this full release.
**Engineering details (≤3 sentences):** Animations are stored/uploaded in Roblox's CurveAnimation format; Roblox Studio runs automated checks on movement constraints and runtime limits at upload time. The marketplace enforces a 300-Robux minimum price, an 80-Robux upload fee, and a one-upload-per-day cap at launch.
**Limitation / caveats (≤3 sentences):** No generative or AI component — this is a packaging/distribution feature for existing animation-authoring workflows, a weaker fit for the tracker's "character animation/motion" research-to-product bar than, e.g., Roblox's AI-driven Cube/Scene Generator work (observed, not stated). Upload is capped at one pack per day and gated behind ID verification plus a paid membership tier.

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
**Engineering details (≤3 sentences):** Deployed via Alibaba Cloud Model Studio in the Singapore region; a specific API call example or per-call/per-second price for Directing could not be retrieved this pass (Adventure's pricing, confirmed in a prior run, was ~$0.007067/World Creation call and ~$0.028267/sec of World Experience at 480p — not independently re-confirmed for Directing).
**Limitation / caveats (≤3 sentences):** The Model Studio page carries no explicit "GA"/"正式发布" vs "Beta"/"邀测" label for any entry on this page (including the confirmed-GA Adventure endpoint), so this status change is inferred from table placement and date matching, not stated text — moderate confidence only. Could not confirm an actual callable API example for Directing in this pass.

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

## AMD FSR plugin for Unreal Engine 5.8
- **Company:** AMD (FLAG: borderline per product-criteria.md)
- **Status:** GA · **Released:** 2026-08-27 · **New**
- **Surface:** Official Unreal Engine 5.8 plugin (FidelityFX integration)
- **Primary source:** https://gpuopen.com/learn/amd-fsr-plugin-updated-for-unreal-engine-58/
- **Underlying research:** no traceable paper
- **Availability:** Free, public Unreal Engine 5.8 plugin distributed via AMD's FidelityFX framework; bundles FSR Upscaling 4.1.1, FSR Frame Generation 4.0.1 and FSR Ray Regeneration 1.2. Supports AMD Radeon RX 9000 Series (RDNA 4) and, newly with this update, AMD Radeon RX 7000 Series (RDNA 3); older GPUs fall back to the non-ML FSR 3 analytical path. No waitlist; updates can also be pushed later via AMD Software: Adrenalin Edition without a game patch.

**What shipped (≤3 sentences):** AMD updated its official FidelityFX Super Resolution plugin for Unreal Engine 5.8, extending the ML-based FSR Upscaling 4.1.1 and Frame Generation 4.0.1 pipeline — previously RDNA4-only in-engine — to also run on RDNA 3 (Radeon RX 7000 Series) cards inside UE5.8 projects. The update improves motion-vector input handling and adds FidelityFX API hooks so the bundled FSR components can be refreshed by a driver update rather than a new game build.
**What research it translates (≤3 sentences):** This packages AMD's existing FSR 4.1.1 ML upscaling and temporal frame-generation techniques (already shipped as the standalone FSR SDK 2.3, tracked separately, released 2026-06-24) directly into Epic's engine as a first-party plugin rather than requiring per-title custom integration. No specific arXiv paper underlies this engine-plugin packaging work.
**Practical significance (≤3 sentences):** Any Unreal Engine 5.8 developer can now enable ML-based FSR upscaling and frame generation for RDNA 3 GPU owners without writing custom FidelityFX integration code, lowering the bar for RDNA 3 (not just the newer RDNA 4) players to get AMD's AI upscaler in UE5.8 titles. AMD frames this as closing the gap between the SDK-level RDNA 3 support (June 2026) and actual in-engine availability for Unreal developers.
**Engineering details (≤3 sentences):** The plugin exposes FSR Upscaling 4.1.1, FSR Frame Generation 4.0.1 and FSR Ray Regeneration 1.2 through Unreal Engine's native plugin system; FidelityFX API hooks allow AMD Software: Adrenalin Edition to push future FSR component updates without a new game build. Supported hardware tiers are RDNA 4 (full ML path), RDNA 3 (newly added ML path), and older GPUs (FSR 3 analytical fallback).
**Limitation / caveats (≤3 sentences):** This is an engine-plugin release, not a new FSR algorithm version — the underlying FSR Upscaling 4.1.1 / Frame Generation 4.0.1 / Ray Regeneration 1.2 versions match the already-tracked June 2026 FSR SDK 2.3 release, just newly exposed inside UE5.8. No pricing or licensing terms were stated beyond "free plugin."

### Announced only (not yet usable)
- Roblox Terrain Updates (Terrain Scattering, Path Splines, Projected Decals, Virtual Texturing, Signed Distance Fields) · Roblox · 2026-09-30 · https://devforum.roblox.com/t/terrain-updates-object-scattering-path-splines-projected-terrain-decals-and-more/4865617 (invitation-gated early-access signup, fails "usable today without asking for access")
- MagicDawn NDGI (Neural Dynamic Global Illumination), beta trial, no visible public signup · Tencent · observed 2026-10-05 · https://magicdawn.tencent.com/?lang=en
- MagicDawn SPATIAL / COMPRESS / REMASTER (spatial audio, AI package compression, game-quality enhancement — all listed "coming soon") · Tencent · observed 2026-10-05 · https://magicdawn.tencent.com/?lang=en

Near-misses: 10
- Ubisoft NEO NPC (Ubisoft × NVIDIA × Inworld AI) · still a research prototype; no evidence of a new announcement or status change inside the window.
- AWS WorldForge (Amazon/AWS RoboMaker 3D world generation) · robotics-simulation tool dated 2020 in available material, not an in-window release; also robotics- rather than game/creator-oriented.
- Odyssey world-simulation model (AWS-backed) · Amazon is an investor/cloud partner, not the operator; Odyssey is a world-model-native startup not tracked by default.
- Intel XeSS 3 (Multi Frame Generation, Panther Lake/Xe3) · on-topic but no verifiable primary-source (intel.com) release date inside the 90-day window; trade press points to a January 2026 CES announcement.
- Unreal Engine 5.9 (AI features: Developer Assistant, Semantic Search, MCP) · announced at Unreal Fest Seoul per trade press; unrealengine.com/dev.epicgames.com returned HTTP 403 or empty content on every fetch attempt — unverified.
- Autodesk Maya MotionMaker "Bring Your Own Data" + Maya ML Deformer · reported at SIGGRAPH 2026 by trade press; no reachable Autodesk-owned page to confirm release/availability status.
- AMD GPUOpen "Lightweight attention-based indirect illumination" (2026-08-20) · research/technique blog post with sample code, not a shipped product feature.
- AMD GPUOpen "Temporally stable generative illumination with a one-step diffusion model" (2026-09-09) · same pattern — research blog post, not a shipped product.
- AMD GPUOpen "How tetrahedral cages significantly reduce BVH memory usage" (2026-09-17) · ray-tracing technique/sample blog post, not a shipped product feature.
- Roblox "Expanding WorldModel Simulation Capabilities: Support for Collision Groups" (2026-09-20) · minor API extension to Roblox's `WorldModel` instance type, not an AI/world-model product in the tracker's sense.

Verification: every item above with a full 5-block entry was checked against its stated primary-source URL in this session; AMD, Roblox, Tencent and Alibaba are the releasing/operating organizations confirmed from those same pages. AMD and the Alibaba ATH Innovation Business Group / Bailian unit are flagged borderline per `references/product-sources.md`; the two HappyOyster status changes are flagged as inferred (moderate confidence) rather than explicitly stated. `github_releases.py` returned HTTP 403 Forbidden on all 27 tracked GitHub orgs this run and contributed no leads — coverage gap noted, not treated as evidence of absence. No item was fabricated.
