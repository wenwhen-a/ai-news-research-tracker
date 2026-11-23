# Part A — Papers
Window: last 30 days (2026-10-24 to 2026-11-23). Categories: cs.GR, cs.CV, cs.LG, cs.AI, cs.RO. Retrieval: arXiv API succeeded (573 candidates, 30-day window). Affiliation pre-screen used an independent reimplementation of the lead-filter logic (see final report for a note on why). GitHub Releases API returned 403 for all orgs (lead-generator only, no impact on verified results).. Qualifying papers: 113 (31 new, 82 previously reported, 6 flagged).

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

---
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

---
## VideoRNG: Relightable Neural Gaussians from Generative Video Models
- **arXiv:** 2611.25338 · https://arxiv.org/abs/2611.25338
- **Submitted:** 2026-11-19
- **Authors:** Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Ravi Ramamoorthi, Zahra Montazeri, Miloš Hašan
- **Qualifying affiliation(s):** NVIDIA — Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Miloš Hašan. Ravi Ramamoorthi is also at University of California, San Diego; Zahra Montazeri is also at University of Manchester.
- **Categories:** cs.CV, cs.GR
- **Open release:** none

**Summary (≤3 sentences):** VideoRNG generates complete, relightable 3D assets from a text prompt or single image, without prescribing a mesh or analytic material model, using a video generator (fine-tuned from a pretrained video-diffusion backbone) that produces a structured RGBA turntable sequence, followed by a feed-forward reconstruction model mapping selected turntable frames to millions of anisotropic Gaussians with learned neural appearance features. A shared directional decoder and stochastic Gaussian ray tracer turn this "ray-traced Relightable Neural Gaussians" (rtRNG) representation into radiance under novel viewpoints and illumination.
**Purpose (≤3 sentences):** To overcome limits of classical 3D-asset representations (surface meshes, compact PBR materials) and existing Gaussian-splatting generators that bake fixed illumination into appearance, for objects whose look arises from fine geometry or complex light transport.
**Breakthrough (≤3 sentences):** The authors report that VideoRNG generates complex assets such as fur, feathers, and spider webs — appearance categories classical representations struggle to express — that can be interactively rendered, relit, and integrated into scenes.
**Tools & method (≤3 sentences):** Depth-anchored appearance training preserves high-frequency appearance while learning geometry; foreground token selection and cost-aware distributed sampling make million-Gaussian reconstruction practical; both stages initialize from a pretrained video-diffusion backbone.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not state explicit failure modes or acknowledged limitations.

---

---
## ViDecide: Teaching Video Diffusion Models to Reason and Plan Step by Step
- **arXiv:** 2611.26389 · https://arxiv.org/abs/2611.26389
- **Submitted:** 2026-11-19
- **Authors:** Kaiwen Zhang, Yiming Gao, Zeqi Xiao, Xintao Wang, Pengfei Wan, Kun Gai, Xingang Pan
- **Qualifying affiliation(s):** Kuaishou — KlingAI Research (Yiming Gao, Pengfei Wan, Kun Gai). Remaining authors are at NTU S-Lab and CUHK.
- **Categories:** cs.CV
- **Open release:** none (project page only: https://kevin-thu.github.io/ViDecide)

**Summary (≤3 sentences):** ViDecide is a decision-centric framework that trains video diffusion models to predict state transitions causally and decide when to stop, using a decision-focused training schedule instead of treating a generation as one fixed-length clip. It adds Corrective Fine-tuning (CFT), which corrects failed decisions by mapping their noise to the model's own successful continuations.
**Purpose (≤3 sentences):** To address current video generation models' frequent violation of physical and logical constraints in multi-step reasoning and planning, which the authors say persists even after large-scale reasoning-data training or existing diffusion RL methods.
**Breakthrough (≤3 sentences):** The authors report an average strict success rate of 83.8% across abstract games, planning tasks, and a new multi-step robot-planning benchmark, versus 23.3% for standard fine-tuning and 67.8% for the strongest prior method, with generalization to larger puzzles and unseen layouts.
**Tools & method (≤3 sentences):** CFT achieves stable improvement without policy-gradient optimization by mapping noise from failed decisions to the model's own successful continuations; evaluated on abstract games, planning tasks, and a new multi-step robot-planning benchmark.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not state explicit failure modes beyond framing the work against prior fixed-length-clip training and RL baselines.

---

---
## Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency
- **arXiv:** 2611.26040 · https://arxiv.org/abs/2611.26040
- **Submitted:** 2026-11-19
- **Authors:** Zhihao Hu, Jianqi Ma, Jun Zhang, Jiayang Bai, Haifeng Shi, Yanxiang Zhuang, Zhongqian Sun, Weidong Zhang, Wei Yang
- **Qualifying affiliation(s):** Tencent — Tencent AIPD (listed as the affiliation for the full author group on the paper). Note: "NVIDIA" in the lead's company-match is a false positive — it refers only to the NVIDIA A800 GPUs used as hardware, not an author affiliation.
- **Categories:** cs.CV
- **Open release:** none

**Summary (≤3 sentences):** Streaming-AAA is a paradigm for controllable, infinite generation of AAA-quality game video, built on a redesigned VAE for efficient high-resolution decoding, diffusion-forcing pretraining with an extended temporal training horizon, and post-training distillation plus memory compression for inference efficiency. The authors report the system generates 1080p gameplay video at 43 FPS with 198 ms end-to-end interaction latency.
**Purpose (≤3 sentences):** To close the gap between existing controllable streaming video-generation methods and practical gameplay, which the authors say have failed to jointly achieve high visual fidelity, high frame rate, and low interaction latency.
**Breakthrough (≤3 sentences):** The authors report 1080p gameplay generation at 43 FPS with 198 ms end-to-end latency on NVIDIA A800 GPUs, supporting long-horizon play without severe temporal degradation or collapse, and substantial improvements in visual fidelity, frame rate, latency, and long-term stability over prior controllable video-generation approaches.
**Tools & method (≤3 sentences):** A redesigned VAE architecture enables real-time 1080p decoding; the diffusion model is pretrained with diffusion forcing over a significantly extended temporal horizon for long-term dependencies and persistent memory; post-training distillation and memory compression improve inference efficiency. Hardware: NVIDIA A800 GPUs.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not detail specific failure cases beyond the temporal-degradation/collapse risk in long-horizon play that the method is designed to mitigate.

---

---
## SpecWM: Turning Verification into Refinement for Streaming World Models
- **arXiv:** 2611.26211 · https://arxiv.org/abs/2611.26211
- **Submitted:** 2026-11-19
- **Authors:** Jiaming Li, Lingzhen Li, Xiaze Yang, Chenyu Zhu, Kaiqi Liu, Xiaotong Zhao, Songlian Li, Toyota Li, Alan Zhao, Haobin Zhong, Yue Ma, Zhiyuan Ma
- **Qualifying affiliation(s):** Tencent (Xiaotong Zhao, Songlian Li, Toyota Li, Alan Zhao, Haobin Zhong; Jiaming Li also lists Tencent alongside Huazhong University of Science and Technology). Other authors are at HUST, Peking University, and HKUST.
- **Categories:** cs.CV
- **Open release:** none

**Summary (≤3 sentences):** SpecWM (Speculative World Model) is a training-free inference framework for streaming world models that verifies draft chunks from a fast model against the target model's latent velocity field, then applies two thresholds to Accept, Refine, or Reject each draft. The verification signal is itself reused as a correction rather than requiring costly target regeneration.
**Purpose (≤3 sentences):** To overcome limits of existing speculative streaming-world-model methods, whose verification covers only an external scorer's evaluation dimensions, adds decoding/scoring cost, and provides no correction for rejected drafts.
**Breakthrough (≤3 sentences):** On WBench Navigation, the authors report SpecWM improves visual quality at a 1.63× speedup over the target model and raises NavScore from the draft's 75.99 to 85.63, achieving the best quality–speed–control trade-off they measured; a new LongSpecBench shows sustained quality and control over long, multi-turn rollouts.
**Tools & method (≤3 sentences):** One-step refinement reuses the verification signal to improve perceptual quality, while three-step refinement strengthens camera following and trajectory consistency; evaluated on WBench Navigation, the new LongSpecBench, and Hy-Nomas across backbones and denoising budgets.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not state explicit limitations beyond motivating transition-aware refinement as a response to prior methods' shortcomings.

---

---
## SceneAnything: Agentic Reconstruction of Large-Scale Mesh Scenes from a Single Video
- **arXiv:** 2611.25340 · https://arxiv.org/abs/2611.25340
- **Submitted:** 2026-11-19
- **Authors:** Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Zahra Montazeri, Ravi Ramamoorthi, Milos Hasan
- **Qualifying affiliation(s):** NVIDIA — Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Ravi Ramamoorthi (also University of California, San Diego), Milos Hasan. Zahra Montazeri is at University of Manchester.
- **Categories:** cs.CV, cs.GR
- **Open release:** code (the authors state: "We will release the harness, agent instructions, reusable libraries, and scenes.")

**Summary (≤3 sentences):** SceneAnything is an automated system that reconstructs editable mesh scenes from real and generated video, coordinating agents, pretrained vision models, and graphics tools through an explicit reconstruction protocol; a scene-owner agent plans the environment and briefs author agents who write parameterized Blender programs. Shared camera, depth, and segmentation estimates ground component construction, and a visibility/fit-based level-of-detail rule selects construction level while unseen regions are completed and marked as inferred.
**Purpose (≤3 sentences):** To reconstruct editable 3D scenes from video that both match visible structure and plausibly complete unseen surfaces — including text-to-scene construction when paired with video generation — addressing the layout, scale, and lighting errors the authors say direct agent-reconstruction attempts produce.
**Breakthrough (≤3 sentences):** The authors report, from an evaluation on 100 scenes, improved original-view fidelity over direct-agent reconstruction and higher novel-view content similarity than the compared video-to-3D methods.
**Tools & method (≤3 sentences):** A software harness coordinates agents that write parameterized Blender programs using shared camera/depth/segmentation estimates; assembled scenes use fitted lighting and supported motion, with revisions undergoing programmatic checks and independent visual comparisons, and accepted programs/lessons reused across scenes.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not state explicit failure modes beyond noting that unseen regions must be completed and are marked as inferred rather than observed.

---

---
## Plan4D: Generative Plannable 4D Worlds
- **arXiv:** 2611.26516 · https://arxiv.org/abs/2611.26516
- **Submitted:** 2026-11-19
- **Authors:** Hangwei Zhang, Rujing Dang, Ruimin Lin, Jiahong Wu, Xiangxiang Chu, Chuanxia Zheng
- **Qualifying affiliation(s):** Alibaba — AMAP, Alibaba Group (all six authors, per the paper's author block)
- **Categories:** cs.CV
- **Open release:** none (project page only: https://fogradio.github.io/plan4d-project)

**Summary (≤3 sentences):** Plan4D is a generative plannable 4D world model that predicts future RGB video together with dense 4D geometry (depth, cameras, point clouds, scene flow) from an observed scene and text-specified actions. It uses a model-stitching architecture that couples Depth Anything 3 with LongCat-Video and adds an auxiliary DPT head for scene-flow prediction.
**Purpose (≤3 sentences):** To add explicit 4D modeling to video-based world models, which the authors say otherwise offer weak physical grounding and limited geometric consistency, given that training data with paired actions and dense 4D annotations is scarce.
**Breakthrough (≤3 sentences):** The authors report state-of-the-art performance in generative 4D modeling of environmental reactions on both synthetic and real-world datasets, with improved visual fidelity and geometric accuracy for long-horizon, fine-grained action planning in dynamic 3D scenes.
**Tools & method (≤3 sentences):** Plan4D stitches a pretrained 3D reconstructor (Depth Anything 3) with a pretrained video generator (LongCat-Video) and augments it with an auxiliary DPT head for scene-flow prediction, leveraging each model's priors rather than training from scratch on scarce paired data.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not describe specific failure modes beyond motivating the data-scarcity problem that the model-stitching design addresses.

---

---
## PRIO: Pre-trained Representation for Interactive Objects in 4D Worlds
- **arXiv:** 2611.25500 · https://arxiv.org/abs/2611.25500
- **Submitted:** 2026-11-19
- **Authors:** Shixun Huang, Lifu Wei, Yue Chang, Chen Geng, Heng Zhang, Jinhyung Ahn, Caoliwen Wang, Siyuan Chen, Donglai Xiang, Jiajun Wu, Peter Yichen Chen
- **Qualifying affiliation(s):** NVIDIA — Donglai Xiang. Remaining authors are at University of British Columbia, University of Toronto, Stanford University, and Yonsei University.
- **Categories:** cs.CV
- **Open release:** none

**Summary (≤3 sentences):** PRIO is a pre-trained representation for interactive objects that, given static geometry, predicts an object-specific configuration space in a single forward pass, providing generalized coordinates for Lagrangian mechanics so physical laws and user actions govern motion. Because configurations are linear in these coordinates, the quantities needed for dynamics are precomputed and run at interactive rates without further network inference.
**Purpose (≤3 sentences):** To let objects in reconstructed or generated 3D/4D scenes move, deform, and respond physically to user actions in real time, which the authors say static captured or generated geometry currently cannot do.
**Breakthrough (≤3 sentences):** The authors report that, pre-trained on diverse 4D trajectories, PRIO generalizes to unseen shapes and, compared with existing 4D generation methods, generates dynamics faster and follows user actions more faithfully; they demonstrate its use in real-to-sim workflows and robot manipulation.
**Tools & method (≤3 sentences):** PRIO supports meshes, point clouds, and 3D Gaussians as input geometry; dynamics quantities are precomputed from the predicted linear configuration space and run at interactive rates without further network inference at runtime.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not state explicit failure modes or scope limits beyond its general generalization claim.

---

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

---
## Coda-DaVinci: Reimagining Video Generation with Code2Video
- **arXiv:** 2611.26595 · https://arxiv.org/abs/2611.26595
- **Submitted:** 2026-11-19
- **Authors:** Yiyan Ji, Qixun Wang, Yang Shi, Zhuoran Zhang, Yifan Xu, Tengfei Liu, Yuqi Tang, Xiaohan Zhang, Shujie Li, Jiafu Tang, Xuanyu Zhu, Xinyu Liu, Yan He, Yushuo Guan, Zihao Wang, Xianghua Ying, Shixuan Liu, Haotian Wang, Wenjing Yang, Zhaoxiang Zhang, Yuanxing Zhang, Pengfei Wan, Jiaheng Liu
- **Qualifying affiliation(s):** Kuaishou — KlingAI Research (Qixun Wang, Yang Shi, Yushuo Guan, Zihao Wang, Yuanxing Zhang, Pengfei Wan); KlingAI Research is Kuaishou's generative-video research group. Remaining authors are at Nanjing University, Peking University, HKUST, University of Hong Kong, Tsinghua University.
- **Categories:** cs.CV
- **Open release:** none

**Summary (≤3 sentences):** Code2Video uses agent-authored 3D proxies to guide video generation; this paper studies how proxy granularity, physics simulation, and prompting affect downstream quality via controlled experiments and blinded human evaluation, then introduces Coda-DaVinci, a task-adaptive agentic framework that selects between proxy-guided and direct generation. A multi-agent harness preserves scene assets and guides repairs through visual inspection and independent review.
**Purpose (≤3 sentences):** To understand how 3D-proxy construction and prompting choices affect downstream video-generation quality in the Code2Video paradigm, and to build a framework that adapts proxy granularity and generation strategy per entity.
**Breakthrough (≤3 sentences):** The authors report leading instruction-following on VTR and scene consistency on R2M, improved physical plausibility over direct generation, and higher visual realism than the compared Code2Video baselines; long-video evaluations show gains in event structure and consistency across successive interactions.
**Tools & method (≤3 sentences):** The framework selects between proxy-guided and direct generation, adapts modeling granularity per entity, and coordinates physics simulation with proxy-grounded prompting; a multi-agent harness handles repairs via visual inspection and independent review, evaluated on VTR, R2M, and long-video benchmarks.
**Limitation (≤3 sentences):** The authors state the long-video, multi-turn evaluations reveal limitations in transition stability and adherence to scene settings.

---

---
## WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation
- **arXiv:** 2611.25251 · https://arxiv.org/abs/2611.25251
- **Submitted:** 2026-11-18
- **Authors:** Qianzhong Chen, Muyuan Lin, Yuyin Sun, Mac Schwager, Cheng-Hao Kuo, Roberto Martín-Martín
- **Qualifying affiliation(s):** Amazon — listed in the paper's affiliation block alongside Stanford University and University of Texas at Austin; the HTML does not map individual authors to institutions, but a footnote confirms "work done during an internship at Amazon."
- **Categories:** cs.RO
- **Open release:** none (project website only: https://qianzhong-chen.github.io/wevo.github.io/)

**Summary (≤3 sentences):** WEVO is a teleoperation-free framework for post-training a whole-body humanoid VLA policy inside an action-conditioned video world model. Simulated manipulation/locomotion play data first improves the world model's contact-dynamics and viewpoint-change prediction; a VLA trained on synthetic demonstrations then collects 20 autonomous real-robot rollouts per task to align the world model with deployment observations, after which the VLA, a whole-body controller, and the video world model form a closed-loop RL environment with dense progress rewards.
**Purpose (≤3 sentences):** To improve humanoid VLA policies beyond imitation learning via reinforcement learning, without the safety risks of real-world humanoid exploration or the sim-to-real exploitation risk of simulator-only RL.
**Breakthrough (≤3 sentences):** Across three real robot tasks, the authors report that play data improves every evaluated world-model metric and downstream policy success, and that video-world-model RL raises mean success from 23.3% to 75.0%, compared with 48.3% for real-robot RL.
**Tools & method (≤3 sentences):** The closed-loop RL environment combines a VLA, a whole-body controller (WBC), and a video world model with dense progress rewards; the world model is aligned to deployment observations using 20 autonomous real-robot rollouts per task, collected by a VLA trained on synthetic demonstrations.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not state explicit limitations beyond motivating the approach against unsafe humanoid exploration and sim-to-real gaps.

---
## Recursive Self-Improvement of Video Evaluators for Judging Temporal Quality (EVA-RSI)
- **arXiv:** 2611.23890 · https://arxiv.org/abs/2611.23890
- **Submitted:** 2026-11-18 (v1)
- **Authors:** Yu Yuan, Ruizhou Ding, Shaoheng Fang, Stanley H. Chan, Zhuo Chen
- **Qualifying affiliation(s):** Roblox — Yu Yuan (Roblox internship + Purdue), Ruizhou Ding (Roblox), Shaoheng Fang (Roblox internship + UT Austin), Zhuo Chen (Roblox)
- **Categories:** cs.AI
- **Open release:** none stated

**Summary (≤3 sentences):** EVA-RSI is a multi-agent recursive self-improvement (RSI) framework for training video evaluators that judge the temporal quality (physics, smoothness, dynamics) of generated video. It builds a fixed proxy exam from construction-defined edits (e.g., temporal reversal, frame dropping) to supply supervision without human annotation, anchored by a small human-labeled real-video set.
**Purpose (≤3 sentences):** RSI has worked well in math/coding, where explicit verifiers give reliable single-goal feedback, but video evaluation has no such verifier and must balance multiple dimensions at once where a gain on one can cost another. The authors aim to adapt RSI to this harder, multi-dimensional, verifier-free setting.
**Breakthrough (≤3 sentences):** Starting from Qwen3-VL-8B, the authors report EVA-RSI improves motion evaluation (largest gain on smoothness) with gains that carry over to defect types never seen during the run, and achieves the highest observed scores among 21 tested models on the dynamics subsets of public benchmarks. Used as an RL reward, it increases generated motion and earns higher human preference; a data-selection pipeline using it also increases motion.
**Tools & method (≤3 sentences):** Each quality dimension has its own LLM proposer agent; a leader agent coordinates proposals and a Nash bargaining rule selects updates that balance progress across dimensions. Humans design the proxy exam, review candidate changes, and revise the curriculum between stages.
**Limitation (≤3 sentences):** The authors state video evaluation has no explicit verifier and must judge many dimensions simultaneously, where improving one can cost another — the core difficulty the method is built to manage rather than fully eliminate. The curriculum still requires human design and review between stages.

---

---
## Infer3D: Inverse Generative Modeling Enables Robust 3D Reconstruction
- **arXiv:** 2611.25061 · https://arxiv.org/abs/2611.25061
- **Submitted:** 2026-11-18 (v1)
- **Authors:** Amani Kiruga, Mark Hamilton, Joshua B. Tenenbaum, William T. Freeman, Vincent Sitzmann, Yilun Du, Ayush Tewari
- **Qualifying affiliation(s):** Google DeepMind — Mark Hamilton (other authors: Harvard, MIT, Cambridge)
- **Categories:** cs.CV, cs.LG, cs.RO
- **Open release:** demo (project page, no stated code/weights) — https://amanikiruga.github.io/infer3d-site/

**Summary (≤3 sentences):** Infer3D is an inverse generative modeling framework for monocular 3D reconstruction that recovers the latent variables of a generative model to best match a single input image, rather than using feedforward amortized inference. It couples a generative image prior with a frozen 3D lifting network to keep outputs on a valid, multi-view-consistent 3D manifold and avoid degenerate flat results.
**Purpose (≤3 sentences):** Feedforward 3D reconstruction networks degrade on out-of-distribution (OOD) viewpoints and scene conditions not seen during training. The authors aim to generalize better to unfamiliar viewpoints by mirroring the top-down generative inference strategy that cognitive science attributes to human 3D perception.
**Breakthrough (≤3 sentences):** The authors report Infer3D achieves superior OOD reconstruction accuracy compared to feedforward networks trained on equal or larger datasets, across controlled synthetic and real-world tasks. They also introduce an adaptive inference strategy that spends more test-time compute on ambiguous OOD examples while routing in-distribution inputs efficiently, which they liken to humans taking longer on confusing stimuli.
**Tools & method (≤3 sentences):** The method optimizes the latent variables of a generative image model against the monocular input, constrained by a frozen 3D lifting network that enforces multi-view consistency, with Gaussian-style decoders for novel views (per the project page). Compute is allocated adaptively at test time based on how ambiguous/OOD the input appears.
**Limitation (≤3 sentences):** The abstract does not state explicit limitations. The optimization-based (inverse) inference approach inherently trades off speed for robustness relative to feedforward networks (observed, not stated).

---

---
## EyeDiT: Anatomy-Grounded Multi-Modal Eye Generation and Simulation
- **arXiv:** 2611.23670 · https://arxiv.org/abs/2611.23670
- **Submitted:** 2026-11-18 (v1)
- **Authors:** Yonghan Lee, Zachary Willms, Kun Liu, Pushkar Anand, Ali Behrooz, Dmitri Model, Dinesh Manocha, Yatong An
- **Qualifying affiliation(s):** Meta Reality Labs — Zachary Willms, Kun Liu, Pushkar Anand, Ali Behrooz, Dmitri Model, Yatong An (corresponding author); other authors: University of Maryland, College Park
- **Categories:** cs.CV
- **Open release:** demo (project page, no stated code/weights) — https://lyhan12.github.io/eyedit

**Summary (≤3 sentences):** EyeDiT is an anatomy-grounded, multi-modal 3D eye generation and simulation model trained on optical coherence tomography (OCT), labeled anatomy point clouds, and near-eye images, for synthesizing eye-tracking (ET) data for AR/VR. A Multi-Modal Anatomy VAE first encodes an anatomy-aware latent from all input modalities, then an "Eye Latent DiT" generates latents conditioned on optical axis, pupil position/radius, and subject identity.
**Purpose (≤3 sentences):** Existing synthetic eye generators are largely image-centric and lack high-quality underlying 3D eye anatomy, limiting control mainly to gaze direction and providing no anatomical labels. EyeDiT targets richer, anatomically grounded control and labeling for ET development in AR/VR.
**Breakthrough (≤3 sentences):** The authors report EyeDiT outperforms previous eye-image synthesis models in novel-view synthesis (24.9 dB vs. 21.8 dB PSNR from a single view). A public ET neural network trained on EyeDiT's synthetic data shows a smaller sim-to-real gaze-error gap (3.5° vs. 8.4°) than when trained on other generators' data, approaches a network trained on real data, and improves further (2.3° vs. 2.6°) when combined with real data.
**Tools & method (≤3 sentences):** The pipeline trains a Multi-Modal Anatomy VAE encoding OCT, anatomy point-cloud, and near-eye-image inputs into an anatomy-aware latent, then trains an Eye Latent DiT to generate latent samples conditioned on optical axis, pupil position/radius, and subject identity, paired with Gaussian decoders for novel-view simulation.
**Limitation (≤3 sentences):** The abstract does not state explicit limitations. The approach depends on OCT, point-cloud, and near-eye-image training data, which are likely more costly to collect than ordinary images (observed, not stated).

---

---
## Efficient World-Model Planning via Physics-Guided Search Distillation (PGSD)
- **arXiv:** 2611.24171 · https://arxiv.org/abs/2611.24171
- **Submitted:** 2026-11-18 (v1; v2 on 2026-11-19)
- **Authors:** Hongyu Zhang, Xiaoshuai Hao, Heye Huang, Qingwen Meng, Wenjun Shi, Jianao Xu, Xin Hu, Xuanru Jin, Jingyi Zhang, Baicang Guo
- **Qualifying affiliation(s):** Xiaomi Corporation — Xiaoshuai Hao. **FLAG: borderline** — Xiaomi is not on the SKILL.md tracked-company list; kept per the "unsure, comparable-standing" rule since Xiaomi runs large in-house AI/robotics research comparable to other flagged companies (e.g. Huawei, Samsung). Other authors: Yanshan University, KAIST, Tsinghua University, Beijing Automotive Technology Center Co., Ltd.
- **Categories:** cs.RO, cs.CV
- **Open release:** none stated

**Summary (≤3 sentences):** PGSD is a single-view world-model planning framework for autonomous driving that combines future-scene representations with execution feedback to repair trajectories that would otherwise violate road boundaries. The pretrained planner and rewarder remain frozen, and no future scenes are generated online at inference.
**Purpose (≤3 sentences):** The authors note that accurate future prediction in driving world models does not guarantee road-compliant execution, and when every candidate trajectory violates road boundaries, simple re-ranking cannot select a feasible one. PGSD targets verified, beyond-pool trajectory repair for this failure case.
**Breakthrough (≤3 sentences):** The authors report single-view PGSD achieves 90.97 PDMS on NAVSIM v1, exceeding all compared single-view planners, while retaining 73.2% of the search teacher's PDMS gain over execution-aware selection alone. On NAVSIM v2 navhard it reaches 38.96 EPDMS, improving on WorldDrive by 11.24 points (40.5%), and the distilled student replaces up to ten search rollouts with a single verification rollout per repair trigger.
**Tools & method (≤3 sentences):** Three components: Execution-Aware Selection checks ego-vehicle road compliance under simulated execution; a Clearance-Aware Search Teacher generates beyond-pool corrections favoring larger minimum road-boundary clearance; and a Future-Conditioned Repair Student predicts a single correction from rewarder features and execution feedback. The authors also report qualitative zero-shot transfer evidence on HUGSIM Hard examples.
**Limitation (≤3 sentences):** The zero-shot transfer evidence on HUGSIM Hard is described as qualitative rather than quantitative (observed). The abstract does not state further limitations.

---

---
## Towards Data-Efficient, Real-Time World Models
- **arXiv:** 2611.22497 · https://arxiv.org/abs/2611.22497
- **Submitted:** 2026-11-17
- **Authors:** Raluca Stevenson, David Bignell, Jennifer C. White, Tabish Rashid, Emanuele Aiello, Mariya Hendriksen, Junha Hyung, Sadegh Aliakbarian, Abdelhak Lemkhenter, Marko Tot, Katja Hofmann, Sarah Parisot
- **Qualifying affiliation(s):** Microsoft (Sarah Parisot — Microsoft, Cambridge, UK; the paper's acknowledgments state "This work was carried out at Microsoft"; Katja Hofmann, the arXiv submitter, is also Microsoft Research Cambridge)
- **Categories:** cs.AI
- **Open release:** none mentioned in the abstract

**Summary (≤3 sentences):** This paper targets real-time, data-efficient gameplay world models by replacing next-token prediction with a two-stage discrete-diffusion approach built on top of an existing autoregressive world model (citing Kanervisto et al., 2025). A lightweight refinement transformer performs iterative masked predictions to produce the final frames. The authors show the resulting model can also be trained on a much smaller gameplay dataset than prior state-of-the-art models.
**Purpose (≤3 sentences):** Current state-of-the-art gameplay world models trade inference speed for consistent, high-quality generation, which the authors say makes real-time interactive play and ideation difficult. The large data requirements of these models also make custom training impractical for creative use cases, limiting their adoption.
**Breakthrough (≤3 sentences):** The authors report a 79x inference speed-up over the base autoregressive world model with, in their words, "a modest quality trade-off." They also report the model can be trained to reproduce high-quality, consistent gameplay using a dataset of approximately 28 hours (about one day) of gameplay data.
**Tools & method (≤3 sentences):** The approach builds on an existing autoregressive world model capable of generating consistent, complex sequences over minutes (Kanervisto et al., 2025), and introduces a two-stage discrete-diffusion scheme with a lightweight refinement transformer carrying out iterative masked predictions in place of next-token prediction.
**Limitation (≤3 sentences):** The authors explicitly acknowledge a "modest quality trade-off" that comes with the reported 79x speed-up; the abstract gives no further quantified detail on this trade-off.

---

---
## RFW-S: Everyday Deformable Objects with Independent Simulation Verification
- **arXiv:** 2611.23056 · https://arxiv.org/abs/2611.23056
- **Submitted:** 2026-11-17 (v1; v2 on 2026-11-18)
- **Authors:** Jiarui Guo, Saining Zhang, Jiaying Wan, Jiawei Weng, Junhao Chen, Rui Zhang, Yuanbo Lyu, Zhiheng Lee, Peishuo Li, Jingrun Du, Weiqing Xiao, Weiyi Lin, Zenan Meng, Hu Wei, Lin Qu, Zongzheng Zhang, Hao Zhao, Chaojian Li
- **Qualifying affiliation(s):** Alibaba Group — Zenan Meng (confirmed via corresponding author email at @alibaba-inc.com, matched to the paper's listed "Alibaba Group" affiliation); other listed affiliations: Tsinghua University, Nanyang Technological University, Nanjing University, HKUST
- **Categories:** cs.RO, cs.CV
- **Open release:** none stated

**Summary (≤3 sentences):** RFW-S is a large-scale dataset of 83,365 simulation-verified deformable-object assets spanning 485 everyday categories across five structural families (soft solids, cloth sheets, shells, garments, bags), built for robotic simulation. An automated pipeline combines reference-guided 3D generation, structure-aware physical modeling, and LLM-assisted parameter estimation/calibration.
**Purpose (≤3 sentences):** Existing 3D asset collections for robotic simulation emphasize visual diversity but leave scalable physical construction and verification of deformable objects largely unsolved. RFW-S targets assets with executable physical properties and realistic interaction behavior at scale.
**Breakthrough (≤3 sentences):** The authors introduce an independent simulation-verification framework that evaluates object behavior under interactions distinct from those used for parameter calibration, and report this characterizes deformable responses across different physical configurations. They further demonstrate sim-to-real replay of fragile-object manipulation and evaluate robotic grasping in terms of both task success and object integrity.
**Tools & method (≤3 sentences):** The pipeline integrates reference-guided 3D asset generation, structure-aware physical modeling, and LLM-assisted parameter estimation and calibration, followed by independent simulation verification on held-out interaction types. Evaluation covers robotic grasping success, object integrity, and sim-to-real replay for fragile objects.
**Limitation (≤3 sentences):** The abstract does not state explicit limitations.

---

---
## FastFrames: Video Generation at Interactive Latency
- **arXiv:** 2611.23226 · https://arxiv.org/abs/2611.23226
- **Submitted:** 2026-11-17 (v1)
- **Authors:** Gene Chou, Guandao Yang, Fujun Luan, Lars Mescheder, Wei Dong, Stephan R. Richter, Vladlen Koltun
- **Qualifying affiliation(s):** Apple — the paper's affiliation list names Apple and Cornell University, and a footnote states "This work was completed during Gene's internship at Apple"; the HTML extraction did not preserve which superscript ties each remaining author to which institution, so the full per-author mapping is unresolved beyond this.
- **Categories:** cs.CV
- **Open release:** none stated

**Summary (≤3 sentences):** FastFrames is a family of fast autoregressive video diffusion models aimed at interactive latency for applications such as camera-conditioned and physics-conditioned video generation. The authors profile state-of-the-art autoregressive video diffusion inference and replace components they find to dominate latency with lightweight alternatives.
**Purpose (≤3 sentences):** Existing autoregressive video diffusion models are, per the authors, orders of magnitude too slow for fluid interactive use, despite being a promising medium for interactive visual experiences.
**Breakthrough (≤3 sentences):** The authors report their 1.3B variant runs at 36 ms per frame (28 responses per second) on a single B200 GPU while matching the generation quality of a state-of-the-art model nearly 8x slower. Their 14B variant runs at 45 ms per frame (22 RPS) on an 8x B200 GPU node with, they state, significantly better visual quality and realism.
**Tools & method (≤3 sentences):** Profiling the inference pipeline, the authors find that VAE decoding and KV-cache updates — often treated as fixed implementation details — account for over half of end-to-end latency, and they replace these with lightweight alternatives. They demonstrate the resulting system on camera-conditioned and physics-conditioned video generation.
**Limitation (≤3 sentences):** The abstract does not state explicit limitations. Reported speeds rely on high-end B200 GPU hardware (observed, not stated).

---

---
## FailureGen: Scalable Robot Failure Data Generation with World Models
- **arXiv:** 2611.22367 · https://arxiv.org/abs/2611.22367
- **Submitted:** 2026-11-17
- **Authors:** Akul Santhosh, Chaitra Sathe, Aastha Jhunjhunwala
- **Qualifying affiliation(s):** NVIDIA (all three authors, per the paper's HTML author block)
- **Categories:** cs.RO, cs.AI
- **Open release:** none mentioned in the abstract

**Summary (≤3 sentences):** FailureGen generates synthetic robot failure videos with temporal event annotations by reusing action trajectories from previously recorded failures and transferring them into new, compatible contexts. It fine-tunes an action-conditioned NVIDIA Cosmos world model on both successful and failed real robot executions as the generative backbone. The method is intended to scale up the range of failure scenarios available for robot learning.
**Purpose (≤3 sentences):** Robot failures are difficult to collect at scale, which the authors say limits the diversity of failure scenarios represented in robot learning datasets. FailureGen aims to synthetically expand this failure data by reusing real recorded failures in new situations.
**Breakthrough (≤3 sentences):** The authors report that, in a preliminary comparison, a visual failure detector trained on real plus generated data reaches an average precision of 0.51 versus 0.41 using real data alone, and detects 33 of 36 failure intervals versus 28 of 36 for real-data-only training.
**Tools & method (≤3 sentences):** The four-stage pipeline: (1) fine-tunes an action-conditioned Cosmos world model on successful and failed real executions; (2) annotates source recordings to identify donor failure segments and compatible successful host recordings; (3) transfers donor motion into host contexts, with optional spatial offsets, to generate continuous video rollouts; (4) annotates and filters the generated samples by observed events and visual quality.
**Limitation (≤3 sentences):** The authors describe their validation as "a preliminary comparison" across two implementations with different tasks and robot configurations, indicating the detection-accuracy results are early-stage rather than a broad benchmark.

---

---
## Evolve in Panorama, Render in View: Panoramic World State Evolution for Video World Models
- **arXiv:** 2611.22733 · https://arxiv.org/abs/2611.22733
- **Submitted:** 2026-11-17
- **Authors:** Longtao Jiang, Mingfei Han, Jianmin Bao, Tingjun Dai, Jinjie Wei, Zhiran Zhang, Xin Tao, Zhihui Li, Salman Khan, Xiaojun Chang
- **Qualifying affiliation(s):** Kuaishou Technology (co-author(s); the HTML author block lists "Mohamed bin Zayed University of Artificial Intelligence" and "Kuaishou Technology" as the paper's two affiliations but does not map each name to a specific one)
- **Categories:** cs.CV
- **Open release:** none yet — abstract states "Code, models, and data will be released"

**Summary (≤3 sentences):** PanoEvo is a video world model that keeps content outside the camera's current view evolving by maintaining world state in the latent space of a panoramic video diffusion model, where every direction is represented at every time step. A Perspective Renderer then reads that panoramic latent state via latent-space projection and direction-restricted cross-attention to render sharp perspective views. The authors also built PanoEvo-Data, an event-centric dataset from real 360° videos, to train the model to evolve a scene from a single starting image.
**Purpose (≤3 sentences):** The paper targets a specific failure mode of current video world models: when the camera turns away and returns, unobserved parts of the scene freeze, lose objects, or change appearance because there is no representation for content outside the current view. It aims to give world models a persistent, always-evolving representation of the full surrounding scene.
**Breakthrough (≤3 sentences):** The authors report that PanoEvo achieves the best overall score among 23 publicly evaluated models on WRBench and the highest total score on STEVO-Bench.
**Tools & method (≤3 sentences):** A "Panoramic Evolver" is trained coarse-to-fine as an image-to-panoramic-video diffusion model on the newly built PanoEvo-Data. A separate "Perspective Renderer," built on a perspective video diffusion model, converts the low-resolution panoramic latent state into high-quality rendered views via latent-space projection and direction-restricted cross-attention.
**Limitation (≤3 sentences):** The authors note that directly projected views from the panorama are blurry and show low-quality details or structural errors because each perspective view covers only a small part of the low-resolution panorama — the stated motivation for adding the separate Perspective Renderer. Code, models, and data are announced but not yet released.

---

---
## DOOM-GS: Dynamic Out-of-core Optimization for Massive Gaussian Splatting
- **arXiv:** 2611.22805 · https://arxiv.org/abs/2611.22805
- **Submitted:** 2026-11-17 (v1)
- **Authors:** Doğa Yılmaz, Jialin Zhu, Binglun Wang, He Wang
- **Qualifying affiliation(s):** Baidu Research — Jialin Zhu; other authors: University College London
- **Categories:** cs.GR
- **Open release:** none stated (a new evaluation dataset is contributed but no link is given in the abstract)

**Summary (≤3 sentences):** DOOM-GS is, per the authors, the first out-of-core optimization method designed specifically for massive-scale dynamic 3D Gaussian Splatting, handling scenes whose primitives exceed GPU memory. It introduces memory-management strategies for caching spatio-temporal primitives and a fast learning method for large numbers of primitives.
**Purpose (≤3 sentences):** Prior out-of-core Gaussian Splatting training assumes static scenes; dynamic GS primitives that move in space and time break the memory-management assumptions those methods rely on, which DOOM-GS targets.
**Breakthrough (≤3 sentences):** The authors state DOOM-GS makes it possible to reconstruct city-scale dynamic scenes with high quality on moderate hardware. Because no directly comparable methods exist, they adapted several closely related methods for comparison and report improvements over these adapted baselines.
**Tools & method (≤3 sentences):** The method combines memory-management strategies that optimize caching for spatio-temporal Gaussian primitives with a fast learning method for large primitive counts. The authors also contribute a new dataset for evaluation, citing a lack of suitable existing datasets for large-scale dynamic GS.
**Limitation (≤3 sentences):** The authors note there are no directly comparable prior methods, requiring adaptation of related methods for comparison, and no suitable existing large-scale dynamic-GS dataset, requiring a new contributed one — both indicating limited external benchmarking for this problem setting.

---
## FaceRiff: Data-Efficient Unified Text-to-3D Face Asset Synthesis via Geometric Conditioning
- **arXiv:** 2611.21867 · https://arxiv.org/abs/2611.21867
- **Submitted:** 2026-11-16
- **Authors:** Elly Akhoundi, Mathieu Lamarre, Thibault Goyallon, Patrick Anderson, Étienne Danvoye
- **Qualifying affiliation(s):** Electronic Arts (all five authors, per the paper's HTML author block: EA Vancouver, EA Montréal, EA Toronto)
- **Categories:** cs.CV, cs.AI, cs.GR
- **Open release:** none mentioned in the abstract

**Summary (≤3 sentences):** FaceRiff generates complete 3D face assets — mesh, albedo, and displacement — directly from text prompts in a shared UV space, by adapting a pretrained SDXL image diffusion backbone with task-specific LoRA adapters. UV normal maps are used as geometric conditioning: per-instance normals guide albedo and displacement synthesis, while a dataset-mean normal anchors mesh generation. The method is trained on only 2,049 scans from about 350 identities on a single GPU.
**Purpose (≤3 sentences):** High-resolution facial datasets with consistent UV-mapped geometry, albedo, and physically based displacement are scarce, even though such assets are needed for photorealistic digital-human rendering. The authors aim to produce render-ready 3D face assets without large specialized datasets or per-instance optimization.
**Breakthrough (≤3 sentences):** The authors report FaceRiff updates less than 3% of the SDXL backbone's parameters per task, and that a blind study with 45 industry professionals found it achieves "substantially higher perceived realism" than the DreamFace baseline, approaching that of real captures. They also report greater per-prompt diversity than FaceG2E and DreamFace while preserving prompt alignment and fixed-topology UV consistency.
**Tools & method (≤3 sentences):** The method adapts a pretrained SDXL backbone with task-specific LoRA adapters, using UV normal maps as geometric conditioning for albedo, displacement, and mesh generation. It additionally produces lighting-independent albedo suitable for physically based (PBR) relighting and pore-scale displacement, which the authors say prior text-driven baselines lack.
**Limitation (≤3 sentences):** The authors frame the result as a demonstration that pretrained 2D diffusion priors can be adapted to this task "under limited data" — training used only 2,049 scans from roughly 350 identities, and the method is demonstrated specifically on faces (observed, not stated as a general limitation).

---

---
## DreamFAR: Real-Time and Long-Horizon Interaction with Diverse Objects
- **arXiv:** 2611.22001 · https://arxiv.org/abs/2611.22001
- **Submitted:** 2026-11-16
- **Authors:** Yiming Dou, Botao He, Antonio Loquercio, Andrew Owens, Jitendra Malik, Sumedh Anand Sontakke, Ruoshi Liu
- **Qualifying affiliation(s):** Amazon FAR (the paper's HTML author block lists "Amazon FAR" alongside Cornell University, University of Maryland College Park, and University of Pennsylvania as the paper's affiliations, without a stated author-to-institution mapping)
- **Categories:** cs.RO
- **Open release:** code and weights — authors' Reproducibility Statement says they release training/inference code and an interactive demo, plus weights for both the full DreamFAR and an ABC-trained DreamFAR, and their ABC data split with evaluation scripts; project page https://www.yimingdou.com/DreamFAR/

**Summary (≤3 sentences):** DreamFAR is a world model for robot manipulation whose dynamics model is trained from scratch on a large robot-native teleoperation dataset, with no internet-video pretraining. The authors present an architecture and training recipe designed specifically for robot-native data. They report it is significantly smaller than high-performance video generation world models while running at 10 FPS on a commercial GPU.
**Purpose (≤3 sentences):** Existing world models for robot manipulation are either fit to a single environment or cannot simulate long-horizon, contact-rich events, limiting their use as simulators for robot learning. DreamFAR aims to provide a world model that handles real-time, long-horizon interaction with diverse objects.
**Breakthrough (≤3 sentences):** The authors report DreamFAR "significantly outperforms existing models in predicting the long-horizon future" and shows better understanding of contact and causality than larger video generation models, despite its smaller size and 10 FPS runtime on a commercial GPU.
**Tools & method (≤3 sentences):** The dynamics model is trained from scratch on a large-scale robot-native teleoperation dataset (no internet-video pretraining), using an architecture and learning recipe the authors designed for this data regime. Demonstrated applications include policy evaluation and mixed-data co-training.
**Limitation (≤3 sentences):** The abstract does not state explicit residual limitations of DreamFAR itself beyond the gaps in prior models it is designed to address (observed, not stated).

---

### Previously reported papers (still in window)
- FVScore: Specification-Driven Neuro-Symbolic Video Evaluation · Google Cloud AI Research — Long T. Le, Yiwen Song, Tomas Pfister, Yale Song · 2026-11-17 · FVScore is a neuro-symbolic framework for evaluating specification-driven video generation. · https://arxiv.org/abs/2611.22673
- Decoding Without a Decoder: Direct Pixel Prediction from Diffusion Transformers · FLAG: borderline — Luma AI (Hansheng Chen and Xinchen Yan are listed with "Affiliation: Luma AI" in the HTML author block; other authors are listed with Stanford University / Caltech) · 2026-11-17 · Latent diffusion models normally need a separate decoder to turn denoised latents into pixels, adding complexity and inference cost. · https://arxiv.org/abs/2611.22287
- WinDEX: Metric 3D Hand Motion Reconstruction in the Wild for Dexterous Teleoperation and Policy Learning · FLAG: borderline — CyberOrigin (Xin You); other co-authors are at City University of Hong Kong · 2026-11-16 · Collecting large-scale, metrically accurate 3D hand-motion data in the wild is hard, limiting data for training dexterous robot hands. · https://arxiv.org/abs/2611.21143
- UNITE: Consolidating Embodied VLM Specialists via Shared-Anchor One-Bit Factorization · ACE Robotics, Shanghai — Tao Tao, Zhi Hou, Xiaogang Wang. FLAG: borderline — ACE Robotics (not on the explicit qualified-company list; standing unclear, kept per borderline rule). Other authors: Sichuan University, Nanyang Technological University, Sun Yat-sen University (Shenzhen). · 2026-11-16 · UNITE consolidates multiple fine-tuned vision-language-model (VLM) "specialists" — for visual grounding, spatial reasoning, navigation, and driving understanding — into a single compact mixture-of-experts model instead of deploying them separately or merging them into one conflict-prone dense model. · https://arxiv.org/abs/2611.20767
- Reference Forcing: Long Video Generation with Region-Guided Drift Correction · Adobe — Haitian Zheng (co-authors otherwise at University of Rochester) · 2026-11-16 · Long autoregressive video generators drift in subject/background appearance over time because they are distilled over short windows and KV-cache history can itself have drifted. · https://arxiv.org/abs/2611.21559
- MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos · Tencent Hunyuan (one of three affiliations listed on the paper, alongside Peking University and HKUST; exact per-author mapping was not extractable from the HTML, but a footnote notes some authors' work was "done during an internship at Tencent Hunyuan," indicating Tencent Hunyuan staff co-authorship) · 2026-11-16 · Streaming video generators must sustain quality beyond their training horizon while managing growing self-generated history and KV-cache costs. · https://arxiv.org/abs/2611.21339
- DuoFlow: Towards Synchronized Speech and Motion Generation with Fine-Grained Control · Tencent — Di Kang, Linchao Bao (other co-authors at Tsinghua University) · 2026-11-16 · Existing joint speech-motion generation models only implicitly condition on transcript semantics or speech features, giving little explicit control over motion hierarchy, body parts, or vocal style. · https://arxiv.org/abs/2611.21530
- Conflict-Aware Multi-Teacher On-Policy Distillation in Aligned Action Spaces for Cross-Game Generalization · FLAG: borderline — LIGHTSPEED (Jing Yi, Haitao Li; likely Tencent's Lightspeed Studios, not independently confirmed beyond the paper's own "LIGHTSPEED" affiliation label); other co-authors at HKUST(GZ)/HKUST · 2026-11-16 · The authors target zero-shot cross-game generalization: consolidating several single-game vision-language-model (VLM) experts into one model that can control unseen games from raw pixels with no target-game training. · https://arxiv.org/abs/2611.21094
- BlockAlign: Preference Optimization for Trajectory-Distilled Video Generation · Alibaba Group — all eight authors (contact emails on alibaba-inc.com domain). · 2026-11-16 · BlockAlign is a preference-optimization framework for aligning few-step, "trajectory-distilled" video generators (e.g., Parallel Decoding Distillation and Parametric Trajectory Distillation models) without teacher fine-tuning or re-distillation. · https://arxiv.org/abs/2611.20351
- The Flip Test: Video World Models Fail to Learn the World State · Google DeepMind — Lijun Yu, Adams Wei Yu, Ang Cao, Baochen Sun, Ming-Hsuan Yang, Nan Hua, Yuan Hao, Ya Xu, Ed H. Chi, Xuezhi Wang, Yinxiao Liu (Mi Luo: UT Austin, work done as a Google DeepMind intern; Alex Dimakis: UC Berkeley) · 2026-11-15 · The authors introduce FlipTest, a counterfactual benchmark that probes whether video world models actually track physical world state rather than just drawing plausible pixels. · https://arxiv.org/abs/2611.19822
- WA-JEPA: Goal-Aware Predictive Feedback Action Refinement for a World-Action Model · Hikvision Research Institute — Wenming Tan, Kai Zhang, Haibo Lei; FLAG: borderline — Hikvision (not on explicit company list; other co-authors are Harbin Institute of Technology and Anhui Polytechnic University) · 2026-11-14 · WA-JEPA is a JEPA-based "world-action" model that generates robot action proposals and then iteratively refines them using the model's own latent predictions of future scenes, instead of searching over candidate action sequences. · https://arxiv.org/abs/2611.19183
- ResWAM: Learning What Changes, Not What Stays, for World-Action Models · FLAG: borderline — Cisco and IBM Research are listed among the paper's affiliations (alongside Michigan State University and University of Michigan); exact per-author mapping to Cisco/IBM was not clearly resolvable from the rendered HTML, but both corporate affiliations appear on the author block. · 2026-11-14 · The paper addresses world-action models (WAMs) — vision-language-action policies augmented with future prediction — which the authors argue waste capacity supervising mostly-static full future observations instead of task-relevant motion. · https://arxiv.org/abs/2611.19559
- Prepare Lighter and Faster for Open-Vocabulary Queries: A Query-Wise 3D Segmenter for Gaussian Splatting · Qualcomm (Qualcomm AI Research) — Khoi Nguyen; Nhat-Quynh Le-Pham (work done while at Qualcomm) · 2026-11-14 · The paper presents a training-free, query-driven framework for open-vocabulary 3D instance segmentation directly on pretrained 3D Gaussian Splatting scenes, avoiding the expensive preprocessing and per-scene training of prior methods. · https://arxiv.org/abs/2611.19429
- GameWM: Toward Next-Generation Video Games with Interaction-Centric World Models · Tencent (Lightspeed Studios) — all authors · 2026-11-14 · The authors propose GameWM, a design for next-generation video games that splits responsibilities between a lightweight "engine" that keeps exact rules/state/camera/world-layout and a generative video model ("VM") that renders the look of the world and the detail of player interactions. · https://arxiv.org/abs/2611.19247
- TelePhysica: Agentic Reconstruction of Physically Interactive Scenes · China Telecom — Institute of Artificial Intelligence (TeleAI), all authors (Shu and Zhan completed the work as TeleAI interns; Li is corresponding author); FLAG: borderline · 2026-11-13 · TelePhysica is a closed-loop, agentic pipeline that reconstructs a physically simulatable 3D scene from a single photo and uses the resulting physics rollouts to condition video diffusion models. · https://arxiv.org/abs/2611.18078
- SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation · Tencent — Xingyi Li, Yiqin Zhu, Jingwen Ye, Yang Sun, Weidong Zhang (Jiahao Yang is affiliated with Fudan University) · 2026-11-13 · SceneAgent is a multi-agent framework for generating 3D game scenes that can be ported across different game-engine backends without rebuilding the generation pipeline from scratch. · https://arxiv.org/abs/2611.17821
- LongCat-Video-Avatar 1.6 Technical Report · Meituan — authorship credited directly to "Meituan LongCat Team" on the paper itself; FLAG: borderline — Meituan (not on the explicit company list; no arXiv HTML version exists to independently verify affiliations, so this relies on the author-field attribution rather than an HTML affiliation block) · 2026-11-13 · This is a technical report on LongCat-Video-Avatar 1.6, an audio-driven avatar video generation model that builds on the team's prior 1.5 version, aiming to improve lip-audio synchronization, natural head/body motion, and visual consistency over long generated sequences. · https://arxiv.org/abs/2611.18822
- Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agents · miHoYo (Honkai AI R&D Team) — all authors listed under this team affiliation · 2026-11-13 · Gamer is a generalist vision-language-action agent framework built by miHoYo's Honkai AI R&D Team for long-horizon, real-time play across both 2D interfaces and 3D open-world games, including miHoYo's own title Honkai: Star Rail (HSR). · https://arxiv.org/abs/2611.18397
- Découpage: Directorial Audio-Visual Control for Long Multi-Shot Video Generation · Ant Group (affiliation listed for the author group alongside HKUST and Zhejiang University; the HTML rendering lost the footnote markers linking individual names to institutions, so the specific Ant Group author(s) could not be individually confirmed); FLAG: borderline — Ant Group · 2026-11-13 · DECOUPAGE is a screenplay-driven framework for generating long, multi-shot, multi-character videos with synchronized but independently-timed audio and visual tracks, addressing cinematic effects like dialogue that bridges across cuts (J-/L-cuts) and deliberate silences. · https://arxiv.org/abs/2611.18866
- Split-and-scale Latent 3D Representations · Apple — all five authors; paper states all funding came from Apple · 2026-11-12 · Apple researchers propose "split-and-scale," a way to boost the effective capacity of latent 3D representations at inference time without retraining a larger tokenizer. · https://arxiv.org/abs/2611.16126
- Rethinking Actions: Continuity-Aware Priors for World-Model Planning · Alibaba Group — Qian Yang; (other authors are at Beijing University of Posts and Telecommunications; Bin Fang's affiliation is ambiguous in the HTML, with an Ant Group email domain visible — FLAG: borderline on that one author only, but Qian Yang/Alibaba alone satisfies the gate) · 2026-11-12 · The paper studies whether action proposals that better respect the temporal continuity of expert action sequences improve goal-directed planning with learned visual world models. · https://arxiv.org/abs/2611.16645
- PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models · ByteDance Seed (listed among the paper's affiliations; exact per-author mapping not recoverable from the HTML, affiliation fields were blank — other listed affiliations: Peking University, UC Santa Barbara, MIT, Universität Hamburg, Hangzhou Normal University) · 2026-11-12 · PhysLoop is a harness in which an LLM agent writes a physics task/scene program that Unreal Engine (with Taichi/Genesis support) simulates, a verifier checks the simulated result, and a video model (Seedance 2.5 by default) renders appearance on top — building a training/repair pipeline for physical · https://arxiv.org/abs/2611.16748
- Neural Render Proxies for Interactive and Differentiable Lighting · Disney Research|Studios — Sergio Sancho, Alexander Rath, Marco Manzi, Pascal Chang, Amit H. Bermano, Markus Gross, Marios Papas (all list affiliation 2); FLAG: borderline (Disney not on the explicit qualifying list but is a comparable top-tier entertainment/graphics industry lab) · 2026-11-12 · The paper introduces a method for interactive, differentiable relighting of static scenes (fixed camera, fixed materials) by decoupling path sampling from emission computation. · https://arxiv.org/abs/2611.17185
- Back to Pixels: Lifting Latent Video Diffusion into Pixel Space · Roblox (listed affiliation block; other listed affiliations are UC Merced, UPenn, UT Austin) · 2026-11-12 · The paper presents PixVid, which adapts a pretrained latent video diffusion model (Wan2.1-14B) to generate video directly in pixel space instead of a compressed VAE latent space. · https://arxiv.org/abs/2611.17336
- VibePrevisBench: Evaluating Agentic Coding for 4D Scene Generation in Blender · Kuaishou (Kling AI) — paper lists "Kling AI" as one of five author affiliations, with Yuzhe Chen's work explicitly "conducted during the author's internship at Kling AI." FLAG: borderline — the HTML extraction could not cleanly map every author to a numbered affiliation (no visible superscripts), so the full author↔institution mapping beyond Yuzhe Chen's internship footnote is inferred, not directly confirmed from the text. · 2026-11-11 · The paper introduces VibePrevisBench, a 242-task benchmark that asks coding agents to turn a text/photo/video brief into an executable 4D scene in Blender and render a proxy ("previs") video. · https://arxiv.org/abs/2611.15789
- Topology-Aware 4D Gaussian Splatting for Egocentric Videos · Google — Federico Tombari (listed as Technical University of Munich; Google) · 2026-11-11 · The paper introduces TopoEgo, a benchmark of egocentric video clips with topology-changing object interactions (cutting, assembly, opening, closing), and Topo-4DGS, a 4D Gaussian Splatting method built to handle those topology changes. · https://arxiv.org/abs/2611.16012
- MatrixSplat: Matrix-Parallel and Feature-Scalable 3D Gaussian Splatting Rendering on GPUs · Snap Inc. — Jian Wang. FLAG: borderline (Snap is not on the illustrative list but is a comparable industry research lab; other co-authors are from UT Arlington, UT Dallas, University of Georgia, and Argonne National Laboratory) · 2026-11-11 · MatrixSplat re-engineers 3D Gaussian Splatting (3DGS) rendering to better use GPU Tensor Cores, replacing the standard sequential depth-sorted alpha-compositing with an order-independent weighted accumulation expressible as matrix operations. · https://arxiv.org/abs/2611.15153
- RF3DGS: Reflection-Free 3D Gaussian Splatting with Self-Priors · Huawei Research — Chenyang Lei (other authors: Hong Kong University of Science and Technology); **FLAG: borderline** (Huawei is not on the core tracked list — per product-criteria.md, kept and flagged as a comparable top-tier lab) · 2026-11-10 · RF3DGS removes reflections from 3D Gaussian Splatting reconstructions by exploiting the fact that, across multiple views of the same 3D point, the darkest pixel is usually reflection-free. · https://arxiv.org/abs/2611.13772
- FlashMotion: Ultra-Fast Long-Term 3D Motion Generation · Tencent — Mingshuang Luo, Zijiao Zeng ("This work was conducted at Tencent IEG Motus Group") · 2026-11-10 · FlashMotion is a framework for generating long 3D human motion sequences — text-to-motion, music-to-dance, and speech-to-gesture — under a tight inference budget. · https://arxiv.org/abs/2611.13626
- Camera3R: Feed-Forward 3D Reconstruction from Heterogeneous Camera Models · Google — Yunwen Zhou, Erin Hong, Dongxu Zhao, Eric Turner, Federico Tombari (affiliation block lists "@google.com"; Ruxiao Duan and Alex Wong are dual-affiliated with Yale University) · 2026-11-10 · Camera3R is a low-rank adaptation (LoRA) framework that extends feed-forward 3D reconstruction networks pretrained on perspective images to other camera models (fisheye, panoramic) without full retraining. · https://arxiv.org/abs/2611.13453
- BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model · NVIDIA — Jaewoo Seo, Laura Leal-Taixé (project page hosted at research.nvidia.com/labs/sil); Seungryong Kim is listed with KAIST · 2026-11-10 · BirdDreams is an autoregressive driving world model that generates a perspective (camera-view) video and a schematic bird's-eye-view (BEV) video jointly, so scene layout is part of the prediction rather than inferred implicitly. · https://arxiv.org/abs/2611.14815
- Spaghetti Splatting: Differentiating Curvilinear Dirac Masses via Convolution · Wayve Labs — Shrisudhan Govindarajan, Daniel Rebain, Andrea Tagliasacchi (FLAG: borderline — Wayve is a well-funded autonomous-driving AI company, not on the main tracked list) · 2026-11-09 · The paper introduces "Spaghetti Splatting," a method for learning curve-like (curvilinear) 3D primitives directly from images via differentiable volume rendering, extending the convolution-based formulation used in EWA splatting and 3D Gaussian Splatting to one-dimensional, infinitely-thin geometry. · https://arxiv.org/abs/2611.12716
- PhysOPSD: Code as Privilege for Physically Plausible Video Generation · Alibaba — Zilong Dong et al. (affiliation block lists "HKUST & Alibaba Token Hub" and "Alibaba Group"; footnote states the work was done at ATH@Alibaba Group) · 2026-11-09 · PhysOPSD is a framework for making video-generation models physically plausible by using executable simulation code as a "privileged" physical context during on-policy distillation, rather than relying on supervised fine-tuning or sparse physics-based RL rewards. · https://arxiv.org/abs/2611.12411
- HIST3R: Decomposing and Rectifying State Updates with History for Streaming 3D Reconstruction · NVIDIA — Yu-Chiang Frank Wang (listed as National Taiwan University and NVIDIA) · 2026-11-09 · HIST3R is a training-free framework for streaming 3D reconstruction that decomposes CUT3R-style recurrent state updates into a magnitude (how strongly a new observation is written into the scene state) and a direction (where the update moves the state), then rectifies the direction using locally con · https://arxiv.org/abs/2611.12011
- Budget-aware Correspondence-driven View Selection for Real-time 3D Perception of Mobile Robots · Amazon — Sanjeev J. Koppal (FLAG: borderline — footnote states a concurrent appointment as "Associate Professor at ECE-UF and a Scholar at Amazon Robotics," not a primary industry affiliation) · 2026-11-09 · The paper introduces BCVS, a pose-free, correspondence-driven view-selection algorithm that runs at over 22 FPS on CPU to filter redundant frames from image sequences for real-time 3D perception on mobile robots. · https://arxiv.org/abs/2611.11809
- From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models · Roblox — Changran Liu, Qi Wu, Haomiao Jiang · 2026-11-08 · The paper presents a framework that uses an LLM-powered coding agent to automatically build game environments, tasks, and scripted expert players from natural-language skill descriptions, which then generate keyboard-and-mouse demonstrations without any human gameplay data. · https://arxiv.org/abs/2611.11136
- Tiresias: Towards Language-Conditioned World Models · Microsoft Research — Qi Dai · 2026-11-07 · The paper argues that language-conditioned world modeling is fragmented across domains with different action spaces, datasets, and evaluation protocols. · https://arxiv.org/abs/2611.10392
- Dynamics-Informed Action Learning for Goal-Conditioned Latent Planning · Tencent ARC Lab — Yiran Wang, Cheng Cheng, Ying Shan (Ying Shan is Tencent ARC Lab's well-known lead; author-to-footnote mapping was partly garbled in the HTML but the Tencent ARC Lab affiliation is clearly listed) · 2026-11-07 · The paper introduces Dynamics-Informed Action Learning (DIAL), a method for latent world models used in visual control planning. · https://arxiv.org/abs/2611.10660
- BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs · SenseTime Research — Yichen Liu, Yuxin Guo, Jingcheng Ni, Lewei Lu, Zehuan Wu (FLAG: borderline — SenseTime is not on the primary company list but is a comparable top-tier industrial AI lab) · 2026-11-07 · BlenderFORGE is a training framework for open-weight multimodal LLM agents that edit 3D scenes in Blender by generating Blender Python (bpy) code. · https://arxiv.org/abs/2611.10768
- Video-Coder: Reinforcing Agentic Coding for Video Generation · Microsoft — Junan Hu (Microsoft Research); other co-authors are University of Central Florida, University of Würzburg, Tsinghua University, UNC-Chapel Hill, UW–Madison · 2026-11-06 · The authors introduce Video-Coder, a video-generation agent that writes and executes code to construct a dynamic 3D scene ("Draft Video") providing structure and motion signals to downstream video generators, rather than generating pixels directly. · https://arxiv.org/abs/2611.09894
- Left-Right-Consistent Iterative Stereo Matching via Cross-Injection · Meta — all four authors listed under Meta Reality Labs · 2026-11-06 · The paper proposes cross-injection (CI), a lightweight add-on for iterative refinement-based stereo-matching models that produces mutually consistent left- and right-view disparity maps from a single pass, rather than two independent passes that often disagree. · https://arxiv.org/abs/2611.09458
- PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State · Tencent — Junyou Li, Deheng Ye (Jihai Zhang's internship was at Tencent; other authors: Chinese University of Hong Kong, Wellington College, Nanyang Technological University) · 2026-11-05 · PlayGen2 is a real-time interactive world model that separates learned 3D state evolution from neural rendering, keeping a persistent world memory (a volumetric occupancy grid for static geometry plus identity-indexed 3D states for the player and other entities) and a separate neural renderer that t · https://arxiv.org/abs/2611.07867
- Householder Motion Embedding: Noise Modulation for Motion-Controllable Video Generation · Amazon — Hongdong Li (Amazon Scholar, part-time; his full-time appointment is at the Australian National University); other authors are at ANU and Vertex Lab Technology Limited. **FLAG: borderline** — the Amazon affiliation is a part-time "Amazon Scholar" appointment, not the author's primary institution. · 2026-11-05 · The paper proposes Householder Motion Embedding (HME), a training-free way to encode motion control into the initial noise of a video diffusion model using a sequence of Householder reflections that form an orthogonal transform on each spatial location's channel vector. · https://arxiv.org/abs/2611.07294
- EgoGeneralist: Unifying Egocentric Action-Video Tasks through Video-Native Modeling · Ant Group (Ant Digital Technologies) — among Yanlin Jin / Bowen Yang / Cheng Zhang / Yifan Yang (other affiliations: Monash University, Institute of Automation, Chinese Academy of Sciences); **FLAG: borderline** — Ant Group is a separate entity from Alibaba Group and is treated here as a comparable top-tier industry lab per the tracker's borderline rule, not as "Alibaba" itself · 2026-11-05 · EgoGeneralist adapts pretrained video generators to jointly handle action-conditioned egocentric video generation, 3D hand/body pose estimation, and joint action-video generation, using a "role-adaptive action renderer" that represents metric 3D motion as both a controllable signal and a recoverable · https://arxiv.org/abs/2611.08477
- Dynamic GPU Voxel Grids and Voxel-sequential Processing in NanoVDB · NVIDIA — Francis Williams, Christopher Horvath, Rohan Sawhney, Mark Harris, Jonathan Swartz, Ken Museth (six of seven authors); Eftychios Sifakis is also affiliated with University of Wisconsin-Madison · 2026-11-05 · The paper extends NanoVDB, NVIDIA's GPU sparse-volume data structure, with dynamic topology operators (morphological dilation, grid merging, pruning, cross-resolution coarsening/refinement) that rebuild grids of hundreds of millions of voxels in milliseconds using bit-parallel algorithms, removing N · https://arxiv.org/abs/2611.08665
- Bri3D: Bridging the Object-Scene Gap in Single-Image 3D Generation via Scene-Anchor · Alibaba — one of Hongye Hou / Shuai Zhang / Hongjie Li at Taobao & Tmall Group of Alibaba (the paper lists Hong Kong University of Science and Technology (Guangzhou), Taobao & Tmall Group of Alibaba, and Hong Kong University of Science and Technology as the three affiliations but the author-to-affiliation mapping was lost in page extraction) · 2026-11-05 · Bri3D generates compositional 3D scenes from a single image by first predicting a color-coded scene scaffold of coarse object geometry and layout, extracting each object as a voxel "scene anchor," refining it into a pose-preserving support, and then using a frozen object generator to synthesize deta · https://arxiv.org/abs/2611.07961
- ReactWorld: Structuring Interaction Responses for Embodied Video Generation · Huawei Technologies Co., Ltd. — Hanwei Liu, Huijia Zhang, Hanzhang Wang, Linjie Hu, Bin Xiao, Xuan Zhou, Dong Zhang (remaining authors: Tongji University / Zhejiang University, per paper's author block) · 2026-11-04 · Embodied video world models can predict scene changes from robot actions, but the paper argues generated object responses may not match task intent or contact dynamics. · https://arxiv.org/abs/2611.06120
- RDT-3D: Resolution-Decoupled Training for High-Fidelity 3D Geometry Generation · JD.com, Beijing, China — all listed authors (single affiliation block for the whole author group) · 2026-11-04 · The paper targets high-fidelity 3D geometry generation, which needs both global structural coherence and fine surface detail. · https://arxiv.org/abs/2611.06141
- Motion-guided Contrastive Regularization For Latent World Models · Qualcomm AI Research — Qiqi Hou, Jisoo Jeong, Yinhao Zhu, Amir Said (Yiwen Chen and Huaizu Jiang are at Northeastern University; a footnote states the work was done during an internship at Qualcomm) · 2026-11-04 · The paper studies JEPA-style latent world models, which learn action-conditioned dynamics without reconstructing observations, and identifies a failure mode it calls "static collapse," where the encoder keeps episode-specific background content and drops manipulation-relevant state changes. · https://arxiv.org/abs/2611.06901
- Möbius: A Unified Motion-Language Model Bridging Understanding and Generation · Tencent Games Motus — Jinyi Wang (project lead), Ronghui Li, Yu Lu, Xinwei Jiang, Zijiao Zeng (corresponding author), and co-affiliation for Jiazhi Shu and Yubo Zhao (other co-authors are HKUST and MIT) · 2026-11-03 · Möbius is a unified motion-language model that understands, generates, and edits human motion within a single framework, rather than pairing a separate language model (for understanding) with a separate diffusion module (for generation). · https://arxiv.org/abs/2611.05279
- Isekai3D SDG: A Platform for Diverse Synthetic Gameplay Visual Data · NVIDIA — all 13 listed authors · 2026-11-02 · The paper presents Isekai3D SDG, a platform for simulating and capturing synthetic 3D gameplay data for vision and world-model research. · https://arxiv.org/abs/2611.03626
- History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models · Microsoft Research — Yuke Zhao, Zisu Huang, Yifan Yang (listed with a dual Zhejiang University / Microsoft Research affiliation). Other authors are affiliated with Zhejiang University, Monash University, and Adelaide University. (Note: a "Google" flag from the screening tool was checked and found to be a false positive — the term does not appear anywhere on the paper's page; the real qualifying affiliation is Microsoft Research.) · 2026-11-02 · The paper addresses weak historical conditioning in few-step autoregressive video diffusion world models, which causes drift and inconsistency over long video horizons. · https://arxiv.org/abs/2611.02782
- Gnomon4D: Learning Where and When to Focus for Geometric Motion-Grounded World-Action Modeling · Kuaishou/KlingAI Research — Lingwei Dang (work done during an internship at KlingAI Research), Yan Zhou (project lead), Guoxin Zhang, Pengfei Wan. Other authors list Nanjing University, Beijing Normal University, Shadow AI, Tsinghua University, and South China University of Technology (corresponding author: Qingyao Wu). · 2026-11-02 · The paper introduces Gnomon4D, a world-action model (WAM) that jointly generates future video, robot actions, and GeoDelta, an explicit 4D geometric motion field capturing how embodiment and object points move in the image plane and change in depth across frames. · https://arxiv.org/abs/2611.02474
- AgiWorld: An Agentic Video World Model for Building Persistent Worlds · Adobe Research — the paper lists two affiliations for the author group, "The University of Texas at Austin" and "Adobe Research" (the exact per-author split was not recoverable from the extracted text, but several co-authors, consistent with prior Adobe Research publications in this area, are Adobe-affiliated; Kalyan Sunkavalli is an established Adobe Research scientist) · 2026-11-02 · The paper presents AgiWorld, a system that builds a persistent, explorable video world from a single image and a free-form instruction, combining a planning agent (AgiWorld-Agent) that designs the world and directs exploration with a video world model (AgiWorld-WM) that generates video in chunks and · https://arxiv.org/abs/2611.02341
- Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence · Xiaomi (paper authored and titled by the Xiaomi Auto World Model Team; Xiaomi logo on title page; model feeds "Xiaomi's autonomous driving stack") — FLAG: borderline (Xiaomi) · 2026-11-01 · The paper presents Xiaomi Auto World Model 2.0, a unified streaming causal world model for "Physical AI" that models physical scene evolution and unifies heterogeneous conditioning inputs within a shared representation space for view-consistent generation. · https://arxiv.org/abs/2611.01677
- Reconstruction as Spatial Evaluation: Diagnosing Cross-View Spatial Intelligence in Large Vision-Language Models · Alibaba Group (Alibaba Token Hub) — Junfei Wu, Qiuyue Wang, Xuhong Huang, Qihang Peng, Mingsheng Li, Jian Guan, Shuai Bai · 2026-11-01 · The paper introduces ReconSpatial, a benchmark that diagnoses cross-view spatial intelligence in large vision-language models (LVLMs) by requiring multi-view 3D scene reconstruction in indoor, tabletop, and outdoor settings. · https://arxiv.org/abs/2611.02026
- Lie Routing Vision Language Models for View-Robust 3D Understanding · Tencent, China — Hao Zheng, Huimin Huang, Wei Ji, Yawen Huang, Xian Wu. Other authors list Westlake University (Jingjun Yi, Chen Hu, Yefeng Zheng) and University of Amsterdam (Qi Bi, Yongkang Li; Jingjun Yi is also now affiliated with University of Amsterdam). · 2026-11-01 · The paper studies "viewpoint-induced semantic drift," where vision-language models give inconsistent answers about the same object as the camera viewpoint changes. · https://arxiv.org/abs/2611.02306
- Learning-to-Memorize: Dynamic Context Management for Long-Horizon Autoregressive Video Generation · ByteDance Seed — Haowei Zhu (also Tsinghua University), Jia Li, Xing Wang, Tianyu Zhao, Jiexi Wang, Xurui Peng, Xinglong Wu · 2026-11-01 · The paper proposes Learning to Memorize (L2M), a learned framework that decides which historical frames to keep, evict, or update during long-horizon autoregressive video generation, operating under a fixed KV-cache budget. · https://arxiv.org/abs/2611.01858
- GSExplorer: Interactive World Generation with a Persistent 3D Gaussian World State · Horizon Robotics — Puxin Yan (also The University of Hong Kong; listed as Project Leader) — FLAG: borderline (Horizon Robotics) · 2026-11-01 · GSExplorer is a framework for interactive world generation that pairs a video generator with a persistent 3D Gaussian Splatting scene representation. · https://arxiv.org/abs/2611.01543
- UniCaMo: Unified Camera and Motion Control for Video Diffusion Models · Qualcomm AI Research — Long Vu, Tan Ngo, Animesh Karnewar, Amir Habibian, Hung Bui, Minh Hoai Nguyen, Phong Nguyen-Ha. Note: Binh-Son Hua is primarily affiliated with Trinity College Dublin; his contribution is noted as "work done under consultancy capacity" for Qualcomm. · 2026-10-31 · UniCaMo is a unified framework for jointly controlling camera motion and object motion in image-and-text-to-video diffusion models. · https://arxiv.org/abs/2611.00810
- ReelCache: An Efficient KV Cache Compression and Management System for Multi-Round Video Generation · Google — Jitian Zhang · 2026-10-31 · ReelCache is a system that compresses and manages the attention key-value (KV) caches of autoregressive video diffusion models during multi-round, interactive video generation. · https://arxiv.org/abs/2611.09973
- Hierarchical World Models with Implicit Dynamics · Meta-FAIR — Nicolas Ballas, Mido Assran (affiliation marker "2" = Meta-FAIR in the author block) · 2026-10-30 · The paper introduces ID-WM (Implicit Dynamics World Models), a hierarchical world model for embodied planning that separates state-space reachability from local control. · https://arxiv.org/abs/2610.42146
- Coarse3D: Controllable and Faithful Sparse Structure Generation for Image-to-3D · Alibaba Group (all listed authors) · 2026-10-30 · Coarse3D is a coarse-stage, sparse-structure generation model for image-to-3D pipelines that produces orientation-controllable, structurally faithful voxel geometry from arbitrary unposed images. · https://arxiv.org/abs/2610.41231
- Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation · FLAG: borderline — Huawei (Technology Planning Dept of the Computing Technology Research Institute, Huawei, Shanghai; and Huawei Noah's Ark Institute, Shenzhen); lead affiliation is Xidian University (academic). Huawei is on the tracker's "borderline, keep + flag" list, not the core tracked-company list. · 2026-10-30 · Any Forcing is a framework for autoregressive (streaming) video generation that supports both flexible sampling-step counts and stable one-step generation, addressing the quality/speed tradeoff and the content drift/collapse that one-step methods suffer over long sequences. · https://arxiv.org/abs/2610.42031
- LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation · NVIDIA — Oliver Hahn, Stefan Roth (also Sherwin Bahmani, work done while at NVIDIA) · 2026-10-29T17:18:51Z · LucidLyra is a feed-forward model that reconstructs a 3D scene as Gaussians while jointly predicting open-vocabulary semantics and class-agnostic instance groupings, all in a single pass from video-diffusion latents. · https://arxiv.org/abs/2610.40495
- Wizard: Manipulate Any World in Real Time via Agentic Control · Tencent — Yuzhe Wu, Zijun Lin, Yeying Jin · 2026-10-29T16:03:19Z · Wizard is an agentic game world model that gives real-time, precise control over character motion in generated game worlds. · https://arxiv.org/abs/2610.40339
- RFW-A: Agentic Procedural Generation of 400K Articulated Assets over 500 Categories · Alibaba Group — Yuanbo Lyu, Yi Yang, Jiawei Weng, Weiyi Lin, Lin Qu, Zenan Meng, Hu Wei (corresponding authors' contact emails use @alibaba-inc.com), plus Wenyi Li, Jiarui Guo, Rui Zhang, Jingrun Du (dual Alibaba/Tsinghua) · 2026-10-29T15:58:15Z · RFW-A combines agentic program synthesis with procedural generation: agents build reusable, category-level generator programs from existing articulated-asset code, test and refine them across sampled configurations, then produce assets procedurally without further model calls. · https://arxiv.org/abs/2610.40333
- PhysAg3D: Bridging 3D Generative and Agentic Models for High-Fidelity and Physically-Interactive Assets · Huawei — Fanpeng Meng, Jiemin Fang, Chen Yang, Qi Tian (also Guangdong Laboratory of Artificial Intelligence and Digital Economy); FLAG: borderline (Huawei is not on the core tracked list but is a comparable top-tier industry lab) · 2026-10-29T12:29:27Z · PhysAg3D couples 3D generative models with agentic reasoning and tool use to turn a single image into an interactive 3D asset. · https://arxiv.org/abs/2610.39924
- Aligning Misaligned Benchmarks for Single-View Novel View Synthesis · Google — Stephan Garbin, Hossam Isack · 2026-10-28T06:49:44Z · The authors argue that single-view novel-view-synthesis methods are hard to compare fairly because each method's output must first be pose-aligned to ground truth, and common test-time pose optimization is ill-posed, leaving methods evaluated at arbitrary local optima. · https://arxiv.org/abs/2610.38349
- ETA-Motion: Efficient Topology-Agnostic Motion Diffusion via Sparse Joint Learning · Samsung Electronics — Seoyoung Hwang (dual KAIST/Samsung Electronics); FLAG: borderline (Samsung is not on the core tracked list but is a comparable top-tier industry lab) · 2026-10-28T04:18:55Z · ETA-Motion generates motion for characters with arbitrary, varying skeletons by training a motion generator on only a compact subset of joints rather than all joints. · https://arxiv.org/abs/2610.38259
- METATRON: A Promptable Whole-Body Execution Layer for Humanoids · NVIDIA — Chen Tessler, Yifeng Jiang, Yi Shi, Umar Iqbal, Gal Chechik, Xue Bin Peng (Alec Otto, Dollhouse Robotics, interned at NVIDIA) · 2026-10-27T22:26:59Z · Metatron is a humanoid control system built on a frozen, generative whole-body base policy plus a programmable skill layer on top. · https://arxiv.org/abs/2610.38027
- GOFish: Full Field-of-View Gaussian Splatting and Mesh Extraction · Amazon — Allen Tu, Meher Gitika Karumuri, Shifan Zhu, Hailing Wang, Yen-Liang Lin, David Held (per PDF affiliation superscript "1 = Amazon"; most likely as an internship collaboration, since other authors hold University of Maryland/Northeastern/CMU affiliations) · 2026-10-27T18:32:45Z · GOFish is the first 3D Gaussian Splatting surface reconstruction method that trains directly on fisheye images, rasterizing fields of view beyond 180° and extracting an aligned mesh from the same scene. · https://arxiv.org/abs/2610.37818
- RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions · Alibaba — DAMO Academy, Alibaba Group / Hupan Lab: Minghao Zhu, Dongchi Huang, Xingyue Zhao, Kehan Li, Xin Li, Zhenyu Zeng, Mingxiu Chen, Deli Zhao · 2026-10-27T07:54:16Z · RynnWorld-Latent is a video world model that uses latent actions from RynnLAM as a shared conditioning interface, letting it train on human videos, robot demonstrations, and simulation rollouts without needing a common action space. · https://arxiv.org/abs/2610.36791
- GeoGSplat: Geometry-Grounded Non-Pixel-Aligned Gaussian Splatting · Horizon Robotics — at least one author (exact name-to-institution mapping not recoverable from the HTML author block, which lists "Xi'an Jiaotong University, EPFL, Horizon Robotics, University of the Chinese Academy of Sciences" as a group without clear per-author linkage); FLAG: borderline (Horizon Robotics is not on the illustrative company list) · 2026-10-27T07:15:03Z · GeoGSplat is a feed-forward Gaussian Splatting model for novel view synthesis that adds geometric priors to the non-pixel-aligned framework, which otherwise tends to place Gaussian centers poorly under large viewpoint changes. · https://arxiv.org/abs/2610.36760
- Hy-Nomas: Towards Free-form Interactive World Generation · Tencent — all listed authors (Tencent Hy Visual Generation Team) · 2026-10-27T06:48:59Z · Hy-Nomas is an 8B-parameter diffusion-based video world model that follows free-form text instructions and continuous camera control across multiple interaction turns, generating variable-length video segments from current inputs and cached history. · https://arxiv.org/abs/2610.36729
- SWIM: Learning What Matters from Behaviors for JEPA World Models · Unity Technologies — Yan Zheng, Tian Wang, Florian Dubost, Alejandro Mottini, Junze Liu, Arvind Srinivasan, Kai Zhong, Kun Qian, Sharon Gao, Vianne Gao, Houyu Zhang, Qingjun Cui; Jiaming Hu and Shi Bo are listed with dual affiliation (Boston University and Unity Technologies). Verified from the HTML author block ("Unity Technologies" stated explicitly, not the generic word "unity"). · 2026-10-27T05:28:28Z · SWIM is a method for training JEPA (joint-embedding predictive architecture) world models so that their learned state representation better reflects physical task progress rather than only visual similarity. · https://arxiv.org/abs/2610.36662
- BoxWorld: Let World Engines Control and Video Generators Render · Huawei Canada — Ahmed Hatem, Chintan Trivedi, Wallace Michel Pinto Lira, Xuebin Qin; FLAG: borderline (Huawei is a comparable top-tier industry lab not on the illustrative list, per tracker rules) · 2026-10-26T22:36:36Z · BoxWorld builds real-time interactive video worlds with user-defined rules by separating interaction logic from video rendering. · https://arxiv.org/abs/2610.36371
- PosePlaner: Denoising Any Feed-Forward Pose Predictor from Pairwise Planar Geometry · Ant Group (Robbyant) — Bin Tan (superscript 2, corresponding author), Yujun Shen (superscript 2), Nan Xue (superscript 2); Yihang Chen is dual-affiliated (HKUST + Ant Group, superscript 1,2). FLAG: borderline (Ant Group is explicitly named as a borderline example in the task brief). · 2026-10-26 · PosePlaner refines camera poses from any feed-forward multi-view 3D predictor (e.g., DUSt3R, VGGT) using flow matching conditioned on pairwise planar geometry, treating pose refinement as a conditional generation problem. · https://arxiv.org/abs/2610.34845
- Generative Structure from Motion with Native 3D Diffusion · Tencent — Zibo Zhao (the HTML page's per-author affiliation block tags Zibo Zhao solely with "Tencent"; the other six authors are tagged "The University of Hong Kong" and "Transengram"). · 2026-10-26 · The paper proposes GenSfM, which recovers 3D object structure and camera pose from a few uncalibrated views by integrating image-based 3D reconstruction with a native 3D diffusion model. · https://arxiv.org/abs/2610.35522
- FL4N: Feed-forward Latent Model for 4D Novel View Synthesis · Google DeepMind — the HTML author block lists two team affiliations, "KAIST AI" and "Google DeepMind," for the full author group; the page carries no per-author superscripts, so the exact author(s) tied to Google DeepMind cannot be isolated from the page itself. · 2026-10-26 · FL4N is presented as the first feed-forward latent model for 4D novel view synthesis (NVS), rendering dynamic scenes across new viewpoints and timestamps from monocular video without explicit 4D Gaussian primitives. · https://arxiv.org/abs/2610.35854
- DriveUniTok: A Unified Multimodal Tokenizer for Driving World-Action Models · Xiaomi EV — Hanchao Leng (project leader), JiaHui Huang, Hanbing Li, Jingwei Zhao, Kuiyuan Yang, Guang Chen, Hangjun Ye, and Jingbo Xu (dual-affiliated with Tsinghua University). FLAG: borderline (Xiaomi's EV/automaker division; not on the default illustrative company list, but matches the "automaker AI labs" borderline category named in the brief). · 2026-10-26 · DriveUniTok is a unified multimodal tokenizer for driving world-action models (WAMs) that encodes appearance, projected-LiDAR metric geometry, and ego motion into a single decodable continuous latent, rather than modeling them separately. · https://arxiv.org/abs/2610.35044
- TurboWAM: Learning What Matters for Fast World Action Models · Huawei (Noah's Ark Lab / Department of Foundation Model) — Guile Wu, Xingxin Chen, Chengjie Huang, Sam Hosseini, Tongtong Cao, Yingxue Zhang, Dongfeng Bai, and Shuangzhi Li (dual-affiliated with University of Alberta; footnote states the work was done during an internship at Huawei Canada). FLAG: borderline (Huawei is explicitly named as a borderline example in the task brief). · 2026-10-24 · TurboWAM is a fast world action model (WAM) for robot policy learning that reduces inference latency by adaptively aggregating world-model-layer representations according to their relevance to action prediction, rather than using every layer uniformly. · https://arxiv.org/abs/2610.33941

Near-misses (on-topic candidates excluded, with reason):
- 2611.27266 · PP-CFG: Polarity-Preserving Guidance for Controllable Few-Step Image and Video Generation · off-topic on closer read: a generic classifier-free-guidance/diffusion-distillation technique for image and video generation (tested on Wan2.1 and Qwen-Image), not 3D, world models, character animation, or game engines — dropped despite a verified Tencent YouTu Lab affiliation (Chengjie Wang and others).
- 2611.26629 · Posterior Matching Distillation · off-topic on closer read: a generic diffusion-distillation technique for image/video generation (tested on SDXL and FLUX.2), not 3D, world models, character animation, or game engines — dropped despite a verified NVIDIA affiliation (Julius Berner, Arash Vahdat).
- 2611.26493 · SGAR: Feed-Forward 3D Reconstruction via Sparse Geometry-Guided Attention · academic only (all five authors at CVLab, EPFL, Switzerland), no industry co-author despite the "NVIDIA" company-match lead.
- 2611.26334 · Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers · academic only (all three authors at the MIT Operations Research Center), no industry co-author despite the "Tencent" company-match lead (likely triggered because the paper benchmarks against Tencent-associated models such as HY-WorldPlay-8B, not by an author affiliation).
- 2611.25847 · TrajCal: Trajectory-Calibrated Time Schedules for Few-Step Flow Sampling · off-topic on closer read: a generic sampling-schedule calibration method for flow-matching image/video generation, with no 3D, world-model, character-animation, or game-engine content (Alibaba Group affiliation is confirmed for at least two authors, but the topic gate fails independent of the company gate).
- 2611.25134 · GEMS: Generation and Experience Memory for Subgoal-Guided Long-Horizon World Model Planning · academic (University of Minnesota, Twin Cities) plus Cisco, a non-qualifying industry co-author not comparable to the tracked 3D/graphics/gaming labs; "Meta" regex match traced to the "Meta-World" benchmark name, not an affiliation
- 2611.23825 · Learning Martial Arts Motion Skills for Animating Opponents in VR Sparring Games · academic only (Arizona State University, Rice University), no qualifying industry co-author; "Meta" regex match traced to the "Meta Quest" headset target hardware, not an affiliation
- 2611.23416 · OCLDA-GS: Object-Centric Local Deformation-Aware Gaussian Streaming · academic only (University of Southern Mississippi, University of Utah), no qualifying industry co-author; "Google" regex match traced to the "Google Immersive" dataset name used for evaluation, not an affiliation
- 2611.22880 · Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving (AgentWorld) · academic only (Shanghai Jiao Tong University, MoE Key Lab of AI), no qualifying industry co-author; "Meta" regex match not traceable to any stated affiliation
- 2611.22769 · ForceBody: Force-Paired Parametric Body Motion with Torque Uncertainty · academic only (Michigan State University, University of North Carolina at Chapel Hill) plus one independent researcher, no qualifying industry co-author
- 2611.22717 · PCRG: Training-Free Pruning and Caching of Reference Tokens for Video Generation · non-qualifying affiliation — the paper's only listed affiliation is "Anorak" (Anorak Games), a UK pre-seed AI startup that raised $5M in November 2026, not a top-tier industry lab comparable to the tracked companies; also arguably off-topic (reference-conditioned video generation/editing acceleration, not specifically 3D/world-models/character-animation/game-engines).
- 2611.22673 · FVScore: Specification-Driven Neuro-Symbolic Video Evaluation · off-topic on closer read — despite a strong Google Cloud AI Research affiliation (Tomas Pfister, Yale Song, Long T. Le, Yiwen Song) plus National University of Singapore (Min-Yen Kan), the paper is a generic video-generation evaluation/scoring framework, not specifically about 3D, world models, character animation, or game engines.
- 2611.22537 · Testing World Models on Actions They Have Never Seen: Held-Out Plans, Forecast Accuracy and Price Rules in Retail · academic only, no industry co-author — sole author Karthik Iyer, with no institutional affiliation stated anywhere on the arXiv page (only a personal email and ORCID).
- 2611.22483 · Manufacturing Differential Sparsity: Planner-Hardware Co-Design for Efficient World Model Planning · academic only, no industry co-author — all five authors are at University of Southern California and Columbia University, per the paper's HTML author block.
- 2611.22287 · Decoding Without a Decoder: Direct Pixel Prediction from Diffusion Transformers · off-topic on closer read — the paper is a general diffusion-model architecture improvement (removing the VAE decoder for direct pixel prediction) demonstrated on Wan video generation and ImageNet text-to-image, not specifically about 3D, world models, character animation, or game engines; affiliation is also borderline (Luma AI, per the HTML author block for Hansheng Chen, with Xinchen Yan noted as "work done while at Luma AI," alongside Caltech and Stanford).
Verification: every listed paper was checked twice against arXiv (v1 date and title on the abstract page; affiliations read from the paper's HTML or PDF author block; topic confirmed from the abstract) before inclusion. 6 papers list an open release (weights, code or demo).

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
