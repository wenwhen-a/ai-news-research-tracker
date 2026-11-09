# Part B — Research → Product (raw, partial)
Agent scope: NVIDIA, Adobe, Intel, Qualcomm, Unity, Epic Games (Unreal Engine/MetaHuman/Fab/UEFN), Roblox only.
Window: last 90 days (2026-08-11 to 2026-11-09). Qualifying products: 3 (3 new, 0 updates found, 0 flagged). Announced-only: 1.
Retrieval note: `scripts/github_releases.py` returned HTTP 403 for every org in this scope (NVIDIA, nv-tlabs, NVlabs, NVIDIA-Omniverse, Unity-Technologies, Roblox, EpicGames) — GitHub API path was blocked in this session, so GitHub Releases leads were not available; coverage relied on web search/fetch of product-sources.md surfaces instead.

---

## Unreal Engine 5.9 "MegaJam Preview" (Unreal Canvas, in-editor Unreal MCP, Unreal Assistant)
- **Company:** Epic Games
- **Status:** Public beta/preview · **Released:** 2026-11-09 · **New**
- **Surface:** engine (downloadable preview build)
- **Primary source:** https://forums.unrealengine.com/t/unreal-engine-5-9-megajam-preview/2852840
- **Underlying research:** no traceable paper (Unreal Canvas and the AI tooling wrap third-party/user-supplied API keys rather than a named Epic research model)
- **Availability:** Free download for anyone via Epic Games Launcher, GitHub, or a separate Linux build; no invitation or waitlist. Built ahead of the Nov 12–15, 2026 Epic AI MegaJam but explicitly not jam-limited.

**What shipped (≤3 sentences):** Epic released a public preview build of Unreal Engine 5.9, which it says was built "primarily with AI agents, with engineers directing and reviewing the work." The build ships an experimental Unreal MCP that now starts automatically with the editor (toolsets for rendering, profiling, audio, UI, level creation and more), an "Unreal Assistant" that connects external AI coding agents (Claude Code, Codex, Cursor, OpenCode) to the editor, and "Unreal Canvas," an experimental tool for generating concept art, images, 3D meshes and video from a creator's own API keys. It also expands Python scripting coverage (audio, physics, Niagara, materials, PCG) and adds an experimental WebAssembly/WebGPU in-browser runtime (source-build only).
**What research it translates (≤3 sentences):** Epic does not cite a specific paper; the release frames the tooling as agent-assisted engine development (AI agents used to build the preview itself) plus bring-your-own-model integration points (Unreal Canvas, Unreal Assistant) rather than a single in-house trained model being shipped.
**Practical significance (≤3 sentences):** Any Unreal developer can download this today and test MCP-driven editor automation or AI-assisted asset generation against a non-production copy of a project; Epic explicitly recommends against converting a main project given the build's instability. It previews workflow changes (AI-agent-built engine features, in-editor MCP tooling) ahead of a full 5.9 release whose date Epic has not fixed.
**Engineering details (≤3 sentences):** Distributed via Epic Games Launcher and GitHub, plus a separate Linux build; WebAssembly/WebGPU export requires a source build and a C++ project. Rendering and animation changes for the eventual full 5.9 release were explicitly held back from this preview.
**Limitation / caveats (≤3 sentences):** Epic's own post lists multiple known issues and calls the release "rushed" (started about a week before the jam). Unreal Canvas and Unreal Assistant require the developer's own third-party API keys, so capability depends on external model access, not a bundled Epic model.

---

## Roblox Studio — CreateSurfaceAppearance: Asset IDs and DataModel Content
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta, opt-in) · **Released:** 2026-11-05 · **New**
- **Surface:** engine / studio tool (3D material API)
- **Primary source:** https://devforum.roblox.com/t/studio-beta-createsurfaceappearance-now-with-asset-ids-and-datamodel-content/4977713
- **Underlying research:** no traceable paper
- **Availability:** Opt-in via Studio File > Beta Features ("Mixed Content for CreateSurfaceAppearanceAsync"); not yet live in published experiences (server-side EditableImage maps don't replicate yet).

**What shipped (≤3 sentences):** Roblox extended `AssetService:CreateSurfaceAppearanceAsync`, which previously accepted only `EditableImage` maps, so a single call can now mix `EditableImage`, DataModel Content, and published Asset IDs for the same material's color/emissive/metalness maps. A live-edited `EditableImage` map updates the surface immediately without re-calling the method.
**What research it translates (≤3 sentences):** This is an engine/runtime API extension, not a published research result; Roblox states no model or paper behind it.
**Practical significance (≤3 sentences):** Roblox states creators can now use published images directly in a `SurfaceAppearance` without first converting them to `EditableImage`, which it says lowers memory use because assets are transcoded to a more efficient format; creators can also convert a painted/generated image to DataModel Content and share it with every player on a server.
**Engineering details (≤3 sentences):** Mixing DataModel Content or Asset IDs for a new map combination costs a few seconds of baking the first time it's used in a session. Feature gated behind a Studio beta toggle, with Roblox stating plans to bring it to live games after feedback.
**Limitation / caveats (≤3 sentences):** Server-side `EditableImage` maps do not yet replicate to clients, which see a checkerboard placeholder instead. Not usable in published/live experiences during this beta.

---

## NVIDIA Cosmos — new simulation checkpoints (Transfer-Auto, Sim-Auto, Sim-Transfer, Sim-Bimanual, Cosmos3-H-Embodied-Nano, Cosmos3-H-Dreams) via Cosmos NIM
- **Company:** NVIDIA — flagged: use-case is robotics/autonomous-vehicle/surgical simulation, not games; included under the "world models" topic per the skill's tracked-topic list, not the games-specific product surfaces.
- **Status:** GA · **Released:** 2026-11-02 · **New**
- **Surface:** cloud API / SDK (Cosmos NIM microservice container; also runnable via build.nvidia.com trial and Hugging Face weights)
- **Primary source:** https://developer.nvidia.com/blog/build-world-models-for-interactive-simulation-with-nvidia-cosmos/
- **Underlying research:** arXiv:2503.14492, "Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control" (NVIDIA) — matches the "Transfer" family of checkpoints named in the post; NVIDIA also links its own technical report at research.nvidia.com/labs/cosmos-lab/cosmos-simulation/technical-report.pdf.
- **Availability:** Downloadable/runnable today via the `nvcr.io/nim/nvidia/cosmos3:2.0.0` NIM container (no invitation), trial on build.nvidia.com, and checkpoints/weights on Hugging Face; NVIDIA Open Model License for the models, separate NVIDIA software license for the NIM container.

**What shipped (≤3 sentences):** NVIDIA released new Cosmos 3 simulation recipes and checkpoints — Transfer-Auto and Sim-Auto for autonomous-vehicle simulation, Sim-Transfer and Sim-Bimanual for robotics, and Cosmos3-H-Embodied-Nano / Cosmos3-H-Dreams for surgical scenarios — alongside guidance for running them as containerized Cosmos NIM microservices. NVIDIA states roughly 2–3x inference speedups from speculative decoding on H200 GPUs for the NIM path.
**What research it translates (≤3 sentences):** NVIDIA's own technical report underlies the release; the "Transfer" checkpoints align with the previously published Cosmos-Transfer1 paper (arXiv:2503.14492) on conditional world generation with adaptive multimodal (segmentation/depth/edge) control for Sim2Real transfer.
**Practical significance (≤3 sentences):** NVIDIA states developers can now pull specific, pre-trained Cosmos checkpoints for a named simulation task (AV, robot manipulation, surgical) instead of fine-tuning the base Cosmos 3 model themselves, with a documented GPU-memory table per task and a runnable NIM container command.
**Engineering details (≤3 sentences):** Delivered as the `cosmos3:2.0.0` NIM container (containerized, GPU-accelerated inference) plus checkpoints on Hugging Face and the Cosmos GitHub repo; NVIDIA reports 2–3x speedups via speculative decoding on H200 GPUs for the NIM path.
**Limitation / caveats (≤3 sentences):** The post is framed as a developer/technical guide rather than a standalone product launch, and NVIDIA's own framing targets physical-AI/robotics/AV workflows, not game development — kept here per the skill's "world models" topic but flagged as borderline for a games-tracker reader.

### Announced only (not yet usable)
- Roblox Asset Versioning (Meshes, Images, Audio, Video) · Roblox · 2026-11-05 · https://devforum.roblox.com/t/asset-versioning-is-coming-to-meshes-images-audio-and-video/4977769 (roadmap: `GetLatestVersionUriAsync()` Nov 11, 2026; Meshes/Images Jan 19, 2027; Audio/Video Feb 17, 2027 — dates stated as subject to change, nothing live yet)

Near-misses: Unreal Engine 5.9's eventual full/Preview-proper release (distinct from the Nov 9 MegaJam Preview) was confirmed only via Epic social-media posts and trade press (e.g. runtimewire.com, pcgameshardware.de) at Unreal Fest with no forum/blog post found — dropped as unverifiable from a primary source beyond the MegaJam Preview thread itself. NVIDIA's Nov 6, 2026 developer-blog post on "FLUX 3 Image Klein" inference speedups on Blackwell GPUs is a third-party (Black Forest Labs) model optimization, not an NVIDIA product — dropped as off-company. Adobe's Oct 2, 2026 blog post on Sony Pictures Imageworks' use of Substance 3D/After Effects on "KPop Demon Hunters" is a customer case study, not a new product/feature — dropped as not a release. Unity 6000.6.8f1 (Nov 3, 2026) is a routine patch build with no material new 3D/animation/AI feature documented — dropped as a minor patch. Qualcomm's Snapdragon/Adreno news surfaces turned up nothing dated in-window beyond the already-tracked Adreno Neural Fusion (2026-09-22); Intel's most recent XeSS SDK update (3.0.2) traces to 2026-07-24, just outside the 90-day window — both companies otherwise empty this run. Unity Spark and Unity 7 remain unchanged from their last recorded tiers (Spark: closed-beta waitlist only; Unity 7: public Alpha only, beta still slated for December 2026) — no material update found despite re-checking.

Verification: every item above was checked against its stated primary source (Epic/Roblox/NVIDIA's own forum, devforum, or developer-blog page) for URL resolution, release/post date, releasing-company identity, and status tier (GA vs. public beta/preview vs. announced-only) before inclusion; NVIDIA DLSS 5, RTX Remix 1.6.1, Isaac Sim 6.2.0, Omniverse Kit 110.4, Unity 7, Unity Spark, and the in-window Roblox entries already in `state/product_seen.json` were each re-fetched/re-searched for a material change since their recorded `first_seen`/`last_update` and found unchanged (DLSS 5's Nov 3 press coverage only restates the War Thunder/Where Winds Meet rollout already logged on 2026-11-05).
