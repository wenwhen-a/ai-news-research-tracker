## Beyond Visual Fidelity: Comparing Categorical and Continuous World Models
- **arXiv:** 2611.27870 · https://arxiv.org/abs/2611.27870
- **Submitted:** 2026-11-20
- **Authors:** Sarah Parisot, Melanie Fernandez Pradier, David Bignell, Sergio Valcarcel Macua, Katja Hofmann
- **Qualifying affiliation(s):** Microsoft — Sergio Valcarcel Macua, Katja Hofmann
- **Categories:** cs.LG, cs.AI
- **Open release:** none

**Summary (≤3 sentences):** The paper compares categorical (next-token) and continuous (whole-frame/flow-matching) prediction schemes for learning the dynamics of visual world models, testing both in controlled 2D (Pixel Pac-Man) and 3D (maze) environments. It measures rollout validity, calibration, and visual quality rather than relying on visual realism alone.
**Purpose (≤3 sentences):** The authors aim to determine whether visual realism in world-model outputs predicts faithful dynamics, since autoregressive token models and whole-frame flow matching normally bundle categorical/continuous and next-token/iterative choices together without isolating them.
**Breakthrough (≤3 sentences):** The authors report that in 2D, categorical models reach higher rollout validity with less training compute — greedy decoding gives the highest validity (about 86% at step 64 after 2 PFLOPs) while sampling gives the best-calibrated stochastic predictions — and that in 3D, categorical models again show stronger long-horizon performance with less training compute, with lossy-tokenization models staying competitive on semantic accuracy and FVD despite lower RGB accuracy.
**Tools & method (≤3 sentences):** Controlled 2D (8×8-grid Pixel Pac-Man with 3 ghosts) and 3D (64×64 RGB maze with a 10,000-entry lossless lookup vocabulary and a 256-entry VQ-VAE codebook) environments, with compute-matched comparisons (2–30 PFLOPs) across greedy/sampled categorical and continuous next-token/iterative models.
**Limitation (≤3 sentences):** The authors note their explanations for the Pac-Man behavior asymmetry are speculative, that exact dynamics-validity analysis is "not feasible" in the 3D maze so they rely on proxy metrics, and that matching parameter counts across model types would introduce confounding architectural differences, so they match on training compute instead.

---

## Ego2Ego: Generative Visual Perspective Taking Across Collaborators
- **arXiv:** 2611.27459 · https://arxiv.org/abs/2611.27459
- **Submitted:** 2026-11-20
- **Authors:** Chuhan Jiao, John Gideon, Anshul Gupta, Guy Rosman, Andreas Bulling
- **Qualifying affiliation(s):** Toyota Research Institute — John Gideon, Anshul Gupta, Guy Rosman; FLAG: borderline (TRI is not on the tracked company list; kept as a comparable-standing corporate robotics/AI lab)
- **Categories:** cs.CV, cs.RO
- **Open release:** none (abstract/paper mentions a "supplementary webpage" with extra videos, but no URL is given)

**Summary (≤3 sentences):** Ego2Ego introduces generative visual perspective taking: given an ego person's egocentric video, a scene point cloud, and a collaborator's camera trajectory, it generates the continuous egocentric video from the collaborator's viewpoint. It is built as backbone-agnostic geometric modules added onto a pretrained video diffusion model.
**Purpose (≤3 sentences):** The authors aim to move beyond prior work that reduced perspective taking to state estimation, geometric reconstruction, or discrete QA, and beyond cross-view video generation methods that infer the target view from the input video alone or require an external camera on the target person.
**Breakthrough (≤3 sentences):** The authors report that across three video diffusion backbones (Wan2.2-5B, Wan2.1-14B, and an "AnyView" setup) on the CoMind dataset, Ego2Ego improves visual quality, Level-2 scene layout accuracy, and collaborator-motion fidelity, outperforming cross-view video generation baselines such as WorldWander and EgoX on every backbone; their dense geometric rendering module raised PSNR by 1.29–1.80 dB over removing scene geometry.
**Tools & method (≤3 sentences):** The method renders dense, temporally consistent scene coordinate maps into every view as a shared spatial reference, aligns cross-view tokens in 3D ray space via relative geometric attention, and recovers regions outside the ego person's current view from the ego person's visual memory, evaluated on the CoMind dataset.
**Limitation (≤3 sentences):** The authors report that transparent surfaces (e.g., windows) absent from the input point cloud appear as empty regions that get filled with a blind or wall, and that because the static point cloud omits moving people, generated people's hair, face, and (for two of three backbones) clothing can differ from ground truth.

---

## Beyond Future Views: Exploring Future-State World Models for Vision-Language Navigation
- **arXiv:** 2611.27418 · https://arxiv.org/abs/2611.27418
- **Submitted:** 2026-11-20
- **Authors:** Kangyi Wu, Pengna Li, Yucheng Wang, Yance Fang, Xihan Ma, Zhizhong Su, Yang Wu, Ye Deng, Jinjun Wang, Jianyi Liu
- **Qualifying affiliation(s):** Horizon Robotics — Yucheng Wang (Project Leader), Xihan Ma, Zhizhong Su; FLAG: borderline (Horizon Robotics is not on the tracked list; kept as a comparable-standing robotics/AI company)
- **Categories:** cs.RO
- **Open release:** none

**Summary (≤3 sentences):** FS-Nav proposes a future-state world modeling framework for Vision-Language Navigation that represents the navigation-relevant future as goal-directed spatial states rather than predicted pixel/latent future views. It predicts a short-horizon waypoint and a mid-horizon route corridor from spatial memory and language instructions and feeds them to a VLM navigator via top-down and first-person interfaces.
**Purpose (≤3 sentences):** The authors question whether predicting future views (pixels or latents), as existing navigation world models do, is the right way to represent the future for VLN, drawing on evidence that the human hippocampus prospectively represents goals and intervening locations rather than raw future observations.
**Breakthrough (≤3 sentences):** The authors report state-of-the-art validation-unseen performance — 60.7 SR / 55.9 SPL on R2R-CE and 55.1 SR / 46.5 SPL on RxR-CE; ablations show combining the waypoint and corridor interfaces raises R2R-CE SR from a 40.9 no-interface baseline to 44.4, and adding future-state guidance contributes 3.0 of those SR points beyond a 0.5-point gain from past spatial context alone.
**Tools & method (≤3 sentences):** The framework is built on Qwen2.5-VL-3B-Instruct and trained on R2R, RxR, and ScaleVLN data; future-state prediction runs in 66.7 ms on an RTX 4090, versus 2.36–2.94 s for VLM inference.
**Limitation (≤3 sentences):** The authors report that training on ground-truth states but testing on predicted ones drops SR to 11.1 (versus 72.3 with ground truth at both stages), and state that "future-state prediction quality remains a major bottleneck"; the paper has no dedicated limitations section beyond this.

---

## Zing-1.0: A Playable World System Built on Controllable Rendering
- **arXiv:** 2611.27336 · https://arxiv.org/abs/2611.27336
- **Submitted:** 2026-11-20
- **Authors:** Zing Team, SeedLeap.ai (individual authors are not named in the paper)
- **Qualifying affiliation(s):** SeedLeap.ai (Zing Team); FLAG: borderline — not on the tracked company list and its scale/standing could not be independently verified from the paper
- **Categories:** cs.CV
- **Open release:** none found (acknowledgments credit "Loopit" for help with launch demos/showcasing, but no link to code, weights, or a demo is given)

**Summary (≤3 sentences):** Zing-1.0 is presented as a "Playable World System built on Controllable Rendering," where an executable engine (WorldKit) resolves player actions and produces a proxy video from updated world state, and a streaming video model (adapted from MiniMax-H3) renders the player's actual view from that proxy in real time. The authors describe it as the first implementation-independent specification of a Playable World System, separating world construction, execution, observation synthesis, and the interaction runtime.
**Purpose (≤3 sentences):** The authors aim to formalize "Controllable Rendering" as a way to build AI-generated interactive worlds driven by explicit, coded game logic rather than purely learned dynamics, with WorldKit giving coding agents structured authoring tools to construct executable proxy worlds.
**Breakthrough (≤3 sentences):** The authors report the renderer leads compared streaming editors with scores of 3.90 on OpenVE and 3.44 on LongV2VBench, and that on their own StreamEval benchmark Zing-1.0 scores 57.86 on instruction editing and 54.06 on reference editing, exceeding published baselines on both tracks; the serving system reaches a steady-state throughput of 23.82 FPS at 832×480 using one H200 for the DiT plus one H100 each for encoding and decoding.
**Tools & method (≤3 sentences):** WorldKit provides reusable character, camera, and control components for an executable proxy engine; the streaming renderer adapts MiniMax-H3 for block-causal autoregressive generation with incremental decoding, distilled to a few denoising steps per block, with an Interaction Runtime that uses cross-block joint execution and sparse attention with compressed K/V to cut inference overhead.
**Limitation (≤3 sentences):** The authors acknowledge that conflicts between recently generated history and the current proxy can compound deviations over long rollouts, that it remains open how much of the player's view the engine versus renderer should prescribe (e.g., gait or body pose), and that richer conditioning interfaces (depth maps, entity IDs) and lower end-to-end interaction latency remain open problems.

---

## Where Structure Enters a World Model: From Predictive Fit to Physical Rollout
- **arXiv:** 2611.27149 · https://arxiv.org/abs/2611.27149
- **Submitted:** 2026-11-20
- **Authors:** Panayiotis Christou, Satyapragnya Kar, Flavjo Xhelollari, Parijat Dube, Rajarshi Das
- **Qualifying affiliation(s):** Oracle — Parijat Dube; FLAG: borderline — Oracle is a major tech company but not typically associated with 3D/world-model/graphics research, so its standing in this specific domain is unclear
- **Categories:** cs.AI
- **Open release:** none

**Summary (≤3 sentences):** This study examines how incorporating physical structure (conserved-quantity supervision, symmetry-aware representations, temporal consistency, learned structured dynamics) affects the accuracy and physical coherence of world models, using token-based models of planetary motion and JEPA-style visual models of mechanical systems. It evaluates generalization across initial conditions and physical-parameter shifts.
**Purpose (≤3 sentences):** The authors investigate whether accurate short-term predictions from world models translate into physically coherent long-horizon rollouts, and how different ways of injecting physical structure affect that translation.
**Breakthrough (≤3 sentences):** The authors report that angular-momentum supervision lowers normalized drift from 0.9196 to 0.4662 across three seeds, that adding their temporal-dynamics-variant (TDV) objective lowers position MSE from 1.0755 to 0.3851 AU² for plain next-token prediction, and that in visual models, supervised energy-based dynamics heads produce finite 400-step forecasts in 125 of 125 seed-system cases versus only 37–45 of 125 for a Lag-caVAE baseline.
**Tools & method (≤3 sentences):** Experiments use token-based autoregressive models on planetary-motion simulations (AU² and direction-cosine metrics) and JEPA-style visual models with energy-based dynamics heads on mechanical-system video, comparing plain next-token prediction against conserved-quantity, relative, and pairwise supervision variants.
**Limitation (≤3 sentences):** The authors state that conservation-based gains are not identified as the unique cause of improvement, that nominal physical consistency does not establish identification of an unseen physical law, that gravity and length are not separately identifiable in their coefficient-recovery experiment, and that reported confidence intervals are conditional on the trained checkpoints rather than replication across more seeds.

---

## ReactDrive: Self-Reactive Driving World Model
- **arXiv:** 2611.27024 · https://arxiv.org/abs/2611.27024
- **Submitted:** 2026-11-20
- **Authors:** Yifan Wang, Xiaoqi Wang, Cho-Ying Wu, Wenbin He, Chenyu You, Liu Ren
- **Qualifying affiliation(s):** Bosch Research North America / Bosch Center for Artificial Intelligence (BCAI) — Xiaoqi Wang, Cho-Ying Wu, Wenbin He, Liu Ren; FLAG: borderline — Bosch is not on the tracked list but is a large multinational with a dedicated AI research arm
- **Categories:** cs.CV
- **Open release:** demo/project page (https://reactdrive.github.io/); no code or weights stated

**Summary (≤3 sentences):** ReactDrive is a driving world model that jointly learns agent dynamics and visual generation through a shared agent-state representation, aiming to model how other traffic agents react to a specified ego action rather than only generating plausible-looking future video. The authors define "self-reactivity" as the capability to model agent responses from observed history and a given ego action and generate visual futures reflecting those responses without being supplied future agent trajectories.
**Purpose (≤3 sentences):** The authors target a gap in driving world models where errors in modeling other agents' responses to an ego maneuver can misrepresent maneuver safety and undermine the reliability of generated videos used for policy evaluation and learning.
**Breakthrough (≤3 sentences):** The authors report a 96.0% human-rater preference for ReactDrive's agent reactivity over five baselines (Vista, GEM, Epona, DrivingWorld, Cosmos3), drawn from 34 raters, 50 cases, and 300 videos, and report improved downstream planning when NAVSIM/TransFuser planners are trained with video augmentation from ReactDrive versus the other generators.
**Tools & method (≤3 sentences):** Dynamics supervision grounds a reactive dynamics prior in observed agent states while a joint video objective optimizes self-reactivity and visual realism together; downstream evaluation trains TransFuser planners on NAVTRAIN/NAVTEST with real data plus 500 generated videos per compared generator.
**Limitation (≤3 sentences):** The fetched text of the paper contains no explicit limitations section; the only caveat stated is procedural — 57 of 680 human-evaluation comparisons were left incomplete due to unfinished rating sessions.

---

## ViewDreamer: A Robot World Model beyond Fixed Camera Setups
- **arXiv:** 2611.26981 · https://arxiv.org/abs/2611.26981
- **Submitted:** 2026-11-20
- **Authors:** Ye Mao, Jinhui Xiong, Egor Larionov, Shiyang Lu, Krystian Mikolajczyk, Wei Ye
- **Qualifying affiliation(s):** Meta AI — Jinhui Xiong, Egor Larionov, Shiyang Lu, Wei Ye (Ye Mao: work done at Meta, dual-affiliated with Imperial College London)
- **Categories:** cs.CV
- **Open release:** none

**Summary (≤3 sentences):** ViewDreamer is a single robot world model that handles variable sets of synchronized cameras (one to four) by disentangling per-view generation from cross-view interaction, instead of generating each view separately or tiling views in a fixed layout. Each view follows a pretrained single-view generation path, and views interact only through shared slot tokens produced by a Cross-View Slot Agreement mechanism.
**Purpose (≤3 sentences):** The authors address the mismatch between most video generation models, which assume a fixed camera layout, and real robot demonstrations, whose camera number, placement, and order vary across embodiments.
**Breakthrough (≤3 sentences):** The authors report ViewDreamer achieves the best generation quality on their RoboView-Bench (one to four cameras) among evaluated models and improves cross-view consistency over independent per-view generation; derived world-action and action-conditioned variants outperform a FastWAM-Joint baseline, e.g. 74.9% vs. 70.0% total success on LIBERO-Plus and 53.6% vs. 40.7% on its Camera subset.
**Tools & method (≤3 sentences):** Training uses a curriculum that gradually increases the number of views for stability, and the Cross-View Slot Agreement module uses visual foundation models to group geometrically/semantically similar regions across views into shared slot tokens; evaluation spans RoboView-Bench, LIBERO-Plus, RoboTwin 2.0, RoboDojo, and a real Franka robot.
**Limitation (≤3 sentences):** The authors reproduced the FastWAM-Joint baseline from its official third-party code, and one evaluation task ("Cup into box") was recorded only at 320×180 and upsampled for display; the fetched excerpt contains no dedicated limitations section.

---

## Looking Right Is Not Being Right: Evaluating the Geometry of Agent-Built 3D Scenes
- **arXiv:** 2611.26937 · https://arxiv.org/abs/2611.26937
- **Submitted:** 2026-11-20
- **Authors:** Ziyang Long, Yen-Liang Lin, Shifan Zhu, Allen Tu, Meher Gitika Karumuri, Chenqi Li, Srikumar Sastry, Sarosij Bose, Mellon M. Zhang, Hsin-Jung Yang
- **Qualifying affiliation(s):** Amazon — Yen-Liang Lin, Meher Gitika Karumuri
- **Categories:** cs.CV
- **Open release:** code (github.com/Albertlongzi/looking-right-being-right) and dataset (huggingface.co/datasets/Zylong/looking-right-being-right); no weights or demo stated

**Summary (≤3 sentences):** The paper introduces a scan-referenced evaluation for vision-language agents that reconstruct rooms from video as editable 3D scenes, scoring geometric accuracy (surface, depth, furniture placement) against laser scans of 30 real rooms on a 0–100 scale, rather than relying on render realism. It also studies how agents use and verify their geometric inputs during revision.
**Purpose (≤3 sentences):** The authors aim to show that convincing renders from agent-built 3D scenes do not establish geometric accuracy, and to test whether agents can verify and correct their own scene reconstructions.
**Breakthrough (≤3 sentences):** The authors report that their strongest tested agent, "GPT-6 Astra," scores 51.4 on the geometric metric from video alone versus 75.9 for a dense reconstruction from the same video, and that agents inherit input errors almost proportionally (scaling supplied geometry by 1.25 lowers the geometric score by 58.5 points); a newly introduced geometric error report raised revision gains by 3.9 and 5.5 points for two of three tested agents over concurrent controls.
**Tools & method (≤3 sentences):** Evaluation uses 30 ARKitScenes rooms with laser-scan ground truth plus over 2,000 public BVB reconstructions, comparing agent tool-call logs, render similarity, and a newly introduced geometric error report that flags discrepancies between a saved scene and the agent's input points.
**Limitation (≤3 sentences):** The authors state the study covers only 30 indoor rooms from one dataset and three main models from one developer, with one run per room/condition; the error report was designed and tested on the same rooms (so transfer is untested), and the metric covers visible geometry only, not object semantics or editability.

---

## Latent Space Planning with Sequential Monte Carlo
- **arXiv:** 2611.26706 · https://arxiv.org/abs/2611.26706
- **Submitted:** 2026-11-19
- **Authors:** Hrishikesh Viswanath, Anindita Ghosh, Uttaran Bhattacharya, Aniket Bera
- **Qualifying affiliation(s):** Adobe Systems — Uttaran Bhattacharya
- **Categories:** cs.RO
- **Open release:** none (the paper cites other groups' released baseline code — GRASP, GD, LeWM — but states no release of its own)

**Summary (≤3 sentences):** The paper formulates latent-space planning with learned world models as optimization guided by Sequential Monte Carlo (SMC), moving a population of action sequences while a gradient-based optimizer updates the plan, and introduces a PDE-derived "cost-to-go" that uses the structure of the latent state space to guide the evolving sample distribution. It targets the respective weaknesses of sampling-based planners (poor long-horizon performance) and gradient-based planners (local minima).
**Purpose (≤3 sentences):** The authors aim to replace MPPI's resampling-free, importance-weighted estimation of a goal-favoring target distribution with SMC's explicit importance-weighting-and-resampling mechanism over a sequence of intermediate distributions.
**Breakthrough (≤3 sentences):** The authors report their method outperforms gradient-based planners by 29 and 50 percentage points, sampling-based planners by 35 points, and MPPI by 7 points in average success rate across navigation and manipulation tasks with visual and proprioceptive world models, while needing fewer iterations than gradient-based planners and coming within 4% of MPPI's iteration count.
**Tools & method (≤3 sentences):** Evaluated on Reacher, Point maze, Wall, Push-T, and Cube environments at horizons of 5–15 steps, using 150 planner iterations with 12 particles each and comparisons against HMC and random-walk-Metropolis (RWM) kernels; the PDE cost-to-go is validated via Spearman correlation with steps-to-goal (about 0.55–0.83 depending on environment).
**Limitation (≤3 sentences):** The authors state that finite-sample guarantees for their particle-dependent target sequence are "left open," that the PDE cost is only informative where offline transitions cover the latent space and can misorder states, and that on 12 of 50 Cube goals the solver returns non-positive values at up to ~5% of vertices.

---

## One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning
- **arXiv:** 2611.26617 · https://arxiv.org/abs/2611.26617
- **Submitted:** 2026-11-19
- **Authors:** Yuxin Jiang, Wenqiang Sun, Jiaqi Li, Yuchao Gu, Lvmin Zhang, Ivor Tsang, Mike Zheng Shou
- **Qualifying affiliation(s):** Tencent — listed as one of the affiliations for the first-five-author group (alongside Show Lab/NUS, A*STAR, and Stanford); the paper's HTML does not expose the superscript mapping from each name to its specific affiliation, but Tencent is explicitly one of the stated affiliations
- **Categories:** cs.CV, cs.AI, cs.LG, cs.RO
- **Open release:** none

**Summary (≤3 sentences):** O²LaF ("one prior, two dynamics") repurposes a single pretrained video diffusion transformer to initialize both an inverse-dynamics model (a feed-forward transition encoder with learnable action queries) and a forward-dynamics model (a causal, action-conditioned video generator), training both end-to-end through a compact bottleneck to learn transferable latent actions from unlabeled video. It also extends the framework to predictive representation priors such as V-JEPA2.
**Purpose (≤3 sentences):** The authors address a limitation of prior latent action learning, which recovers action supervision from visual transitions but typically learns the underlying forward/inverse dynamics largely from scratch, asking whether a pretrained video generator can instead supply the prior for both.
**Breakthrough (≤3 sentences):** The authors report state-of-the-art few-shot action probing and stronger zero-shot action transfer across visual contexts and embodiments on navigation and robotic manipulation tasks; on CameraBench camera-motion classification, their O2LaF-DiT (5B, LoRA) averages 89.1 AP (a reported +9.2 gain from latent-action pretraining) and O2LaF-Scratch (270M, full fine-tuning) gains +44.9 AP over its baseline, against a 62.8 AP reference for Qwen2.5-VL-72B.
**Tools & method (≤3 sentences):** Both dynamics models are initialized from the same pretrained video DiT; training uses a 32-dimensional Gaussian latent action, 5k updates, and a global batch size of 256 on 16 GPUs (peak 65.49 GiB memory for end-to-end training), evaluated with a MIND exact-match benchmark and 1,114 labeled CameraBench clips across 15 camera-motion categories.
**Limitation (≤3 sentences):** The authors acknowledge that the internal structure of learned latent actions is poorly understood (interpretation mostly requires inspecting reference videos), that the learned dynamics are optimized for visual prediction rather than decision-making, and that a simulator/forward-dynamics-model disagreement in their verifier case study could not be resolved without actually executing the trajectory.

---

# Near-misses
- 2611.27266 · PP-CFG: Polarity-Preserving Guidance for Controllable Few-Step Image and Video Generation · off-topic on closer read: a generic classifier-free-guidance/diffusion-distillation technique for image and video generation (tested on Wan2.1 and Qwen-Image), not 3D, world models, character animation, or game engines — dropped despite a verified Tencent YouTu Lab affiliation (Chengjie Wang and others).
- 2611.26629 · Posterior Matching Distillation · off-topic on closer read: a generic diffusion-distillation technique for image/video generation (tested on SDXL and FLUX.2), not 3D, world models, character animation, or game engines — dropped despite a verified NVIDIA affiliation (Julius Berner, Arash Vahdat).
