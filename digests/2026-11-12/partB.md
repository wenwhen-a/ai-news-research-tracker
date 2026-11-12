# Part B — Research → Product

Window: last 7 days (2026-11-05 to 2026-11-12). Daily light check of primary sources (not the Monday full 90-day sweep). Products: 1 new, 1 updated.

---

## Roblox Engine — Minimum Draw Distance Raised to 500 Studs + Auto-Quality Level Improvements

- **Company:** Roblox
- **Status:** GA · **Released:** 2026-11-05 · **New**
- **Surface:** engine (client rendering)
- **Primary source:** https://devforum.roblox.com/t/increasing-the-minimum-draw-distance-to-500-studs-and-other-auto-quality-level-improvements/4977292
- **Underlying research:** no traceable paper
- **Availability:** Automatic rollout to every Roblox experience; no creator opt-in required.

**What shipped (≤3 sentences):** Roblox's Rendering team raised the minimum draw distance at the lowest automatic quality level from 200 to 500 studs, with faster ramp-up across the first few quality levels (first four auto levels move from 200/250/300/450 studs to 500/800/1200/1600 studs). The update also makes terrain water transparent at all quality levels (previously opaque at low settings) and stops beams from aggressively cutting segment counts at low quality. Roblox states the change "roll[s] out automatically for every game" with nothing creators need to enable.

**What research it translates (≤3 sentences):** No paper or named model underlies this; it is an internal engineering optimization. Roblox states the team "profiled shaders and other rendering features at low quality levels" and optimized the most frame-time-heavy ones, which is what allowed draw distance to scale up without cost to performance on low-end devices.

**Practical significance (≤3 sentences):** Players on the lowest auto-detected quality tier now see roughly 2.5x further by default, addressing a gap where low-end/mobile devices rendered a visibly smaller world than higher-tier devices. Roblox tells creators to re-test visuals at each quality level (Studio Settings > Rendering > Editor Quality Level) and verify their StreamingTargetRadius, since content may now need to stream in further out than before.

**Engineering details (≤3 sentences):** Affects Roblox's internal auto quality-level (QL) system across both draw distance and terrain/beam rendering paths. Roblox warns the exact per-level numbers may still change and that reading `UserGameSettings.SavedQualityLevel` to gate visual effects will break, since that API is slated for deprecation.

**Limitation / caveats (≤3 sentences):** Roblox's post frames several related items as future work, not yet shipped: particle emitter `Rate` still scales aggressively by quality level, and creators do not yet have a way to flag which parts of a scene matter most to the auto-quality system.

---

## NVIDIA DLSS 5 with 3D-Guided Neural Rendering — War Thunder rollout · **Update**

- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-11-12 · **Update**
- **Surface:** shipped game (feature rollout)
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/war-thunder-dlss-5-3d-guided-neural-rendering-out-now/ (update to the tracked item first logged at https://www.nvidia.com/en-us/geforce/news/nba-2k27-dlss-5-3d-guided-neural-rendering-geforce-game-ready-driver/)
- **Underlying research:** no traceable paper (same DLSS 5 "3D-Guided Neural Rendering" model tracked under this entry since first_seen 2026-09-13)
- **Availability:** GeForce RTX 50 Series and RTX Spark systems; ships with War Thunder's "Eagle's Shadow" major update.

**What shipped (≤3 sentences):** Update since 2026-09-13: NVIDIA states DLSS 5 with 3D-Guided Neural Rendering is now live in War Thunder as part of the game's Eagle's Shadow update, moving War Thunder from the "confirmed for mid/late November rollout" status recorded on 2026-10-13 to an actually-shipped integration. The update arrives alongside new planes, ships, tanks, cluster bombs and other visual-effect work in War Thunder, unrelated to DLSS.

**What research it translates (≤3 sentences):** Same underlying DLSS 5 model already tracked under this entry (the "October 2026 Neural Rendering model," ~118M parameters). NVIDIA states developer Gaijin used it to improve highlights, refine shadows and add microcontrast in War Thunder.

**Practical significance (≤3 sentences):** NVIDIA states up to 400 fps at 4K and up to 550 fps at 1440p (Ultra preset, path tracing) in Gaijin's ground-battle benchmark, using Ray Reconstruction and up to 6X Multi Frame Generation. Independent outlet GameGPU reported a drop from 91 to 52 fps on an RTX 5090 at 4K with path tracing enabled in its own testing, illustrating that NVIDIA's headline figures are setting- and scenario-dependent.

**Engineering details (≤3 sentences):** Feature requires GeForce RTX 50 Series or RTX Spark hardware; NVIDIA's article does not state a specific required driver version for this update (a GeForce RTX/RTX Spark Game Ready Driver 621.24 WHQL was issued the same week for other titles).

**Limitation / caveats (≤3 sentences):** Where Winds Meet's DLSS 5 update, part of the same rollout plan, remains pending (NVIDIA states November 23) and has not shipped as of this check; it is not counted as a further update until it ships.

### Announced only (not yet usable)
- None newly qualifying this week.

**Near-misses (checked, not included):**
- MetaHuman Creator web application discontinuation (Epic Games, forums.unrealengine.com, 2026-11-05) — a retirement of a creation tool, not a new product/feature ship; MetaHuman creation itself continues inside the Unreal Engine editor.
- Where Winds Meet DLSS 5 update and Warhammer 40,000: Dawn of War IV driver optimizations (NVIDIA, nvidia.com/geforce/news) — both still pending (Nov 23 and Dec 3 respectively), not yet shipped.
- Roblox DevForum items reviewed but excluded as out of scope or unverifiable from a primary source in this pass: "[Beta] Translate Text in Your In-Game Images Automatically" (2026-11-11, localization feature, not clearly one of the four tracked topics), "Test Graphics and Memory on Lower-End Devices With the Performance Simulator" (2026-11-12, dev-testing tool, scope unclear), "Asset Versioning Is Coming to Meshes, Images, Audio, and Video" (2026-11-10, phrased as forthcoming, could not confirm tier from a primary post).
- Unity Hub 4.0 Beta and Unity CLI 1.0.0-beta.17 (discussions.unity.com, ~2026-11-06/07) — general engine tooling (project/package management, CLI), not clearly within the 3D/world-model/animation/game-engine-graphics scope; flagged borderline and not included.
- Alibaba Cloud Model Studio "newly-released-models" additions in the window (qwen4-max-preview, kimi-k3.1-pro, 2026-11-05/11) — general LLMs, not on the four tracked topics.
- Tencent Hunyuan (hunyuan.tencent.com, 3d.hunyuan.tencent.com), ByteDance Seed/Volcano Engine (seed.bytedance.com, volcengine.com), Kuaishou Kling (klingai.com/kling.ai), and PlayStation Blog (blog.playstation.com) — checked directly; no new product or material tier/version/availability change found dated in the 2026-11-05–2026-11-12 window.

**Verification:** Each primary source cited above was fetched directly in this session (NVIDIA GeForce news pages, the Roblox DevForum thread and its updates-category listing, create.roblox.com release notes, NVIDIA's developer blog listing, Alibaba Cloud Model Studio's "newly-released-models" page, and klingai.com/kling.ai) and checked for date, status tier, and the specific claims stated above; Unreal Engine, Unity, Adobe, Tencent Hunyuan, ByteDance Seed, and PlayStation Blog were searched and spot-fetched for the window with no additional qualifying items found.
