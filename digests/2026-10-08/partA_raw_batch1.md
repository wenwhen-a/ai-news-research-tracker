## RoboJEPA: Scaling Robotic Latent World Models
- **arXiv:** 2610.10515 · https://arxiv.org/abs/2610.10515
- **Submitted:** 2026-10-07
- **Authors:** Artem Zholus, Nicolas Beltran-Velez, Jianhao Yuan, Sarath Chandar, Tushar Nagarajan, Daniel Severo, Koustuv Sinha, Michal Drozdzal, Adriana Romero Soriano, Jeannette Bohg, Nicolas Ballas, Mahmoud Assran
- **Qualifying affiliation(s):** Meta — 9 of 12 authors listed as "FAIR at Meta," including joint last authors Nicolas Ballas and Mahmoud Assran; three co-authors are from Chandar Research Lab/Mila/Polytechnique Montréal
- **Categories:** cs.AI (primary), cs.RO (cross-list)
- **Open release:** none (abstract states checkpoints and training/deployment code will be released, but no repository link is given anywhere on the arXiv page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** RoboJEPA is a Joint Embedding Predictive Architecture (JEPA) world model trained on 23 public manipulation datasets spanning 12 robot platforms, scaled from 22M to 8B parameters. The authors report that latent rollout error follows a second-order power law in compute, and that this error predicts downstream planning performance.
**Purpose (≤3 sentences):** The authors aim to establish compute-scaling laws for robotic world models and to find a training-time proxy (rollout error) that predicts real-robot planning performance without requiring costly on-hardware evaluation at every checkpoint.
**Breakthrough (≤3 sentences):** The authors report the 8B model is "the largest JEPA predictor model trained to date," fit with a second-order (not simple) power law whose extrapolation to held-out 4B/8B scales lands within 0.6×10⁻³ (DROID) and 1.4×10⁻³ (RoboCasa) of observed error. They report real-robot success rates of 67%/50%/27% (Grasp/Object Lift/Pick-and-Place) for the 8B model vs. 60%/30%/21% for the 4B model, and state object-interaction tasks only succeed in simulation once training exceeds roughly 10²² FLOPs.
**Tools & method (≤3 sentences):** Training data totals ~2.87M episodes (~15,022 hours of video, ~6,692 hours with synchronized actions) from datasets including DROID, RoboSet, RoboMIND, LeRobot (SO-101), RoboCasa365 (sim), 1X humanoid, AgiBot World, and nine Open-X Embodiment datasets; the predictor sits on a frozen V-JEPA 2.1 encoder. At inference, the model plans by sampling actions uniformly and ranking them with the learned world model (no learned policy), over more than 50,000 planning evaluation episodes across two robot platforms; reported training compute spans 2×10¹⁹ to 9.5×10²² FLOPs.
**Limitation (≤3 sentences):** The authors state the scaling laws describe only the predictor, since the V-JEPA 2.1 encoder is kept frozen rather than co-trained; they also note the fits sit close to data saturation on the fixed training corpus, implying further gains likely need more diverse interaction data rather than just scale. They state the model uses no language conditioning or learned action policy, planning is not real-time, and VLA baselines (π0-FAST, π0.5) are only contextual references since they differ in goal specification and training data.

---

## Position Forcing: Self-Conditioning 3D Generation
- **arXiv:** 2610.10342 · https://arxiv.org/abs/2610.10342
- **Submitted:** 2026-10-07
- **Authors:** Ziheng Ouyang, Zeqiang Lai, Jiarui Chen, Jiangshan Wang, Yuhao Wan, Jingbo Gong, Xiangyu Yue, Hengshuang Zhao, Qibin Hou, Chunchao Guo
- **Qualifying affiliation(s):** Tencent Hunyuan — one of the paper's four listed institutions (VCIP/Nankai University, Tencent Hunyuan, MMLab/CUHK, Fudan University, Shanghai Innovation Institute, HKU); corresponding author Chunchao Guo lists a tencent.com address
- **Categories:** cs.CV
- **Open release:** none found on the arXiv page
- **Shipped counterpart:** none found (compared against Tencent's own shipped Hunyuan3D-2.1 as a baseline, see below, but Position Forcing itself is not shipped)

**Summary (≤3 sentences):** The paper targets single-stage 3D generative models that represent shapes as unordered sets of latent tokens (VecSet representations), which must implicitly infer each token's position during denoising. The authors propose "Position Forcing," a self-conditioning scheme that recovers token positions from the current denoising estimate and feeds them back at progressively finer resolution.
**Purpose (≤3 sentences):** The goal is to improve single-stage VecSet 3D generation quality by giving the diffusion transformer explicit, coarse-to-fine positional guidance instead of leaving position purely implicit.
**Breakthrough (≤3 sentences):** On reconstruction (Chamfer Distance/F1), Position Forcing reports 5.39/95.38 at the largest tested latent size (64×20480) versus Tencent's own Hunyuan3D-2.1 at 7.62/92.06 on the same setting. On generation, it is best or tied-best on all four reported metrics (ULIP-T/I, Uni3D-T/I) against baselines including TRELLIS 2 and Hunyuan3D-2.1, though the authors' own numbers show the margins over the closest baselines are small (roughly 0.001–0.007).
**Tools & method (≤3 sentences):** The method quantizes recovered token positions at progressively finer resolutions across denoising stages and re-injects them as positional encodings into the diffusion transformer; inference runs in BF16 precision. Reconstruction is evaluated on an unnamed held-out set of meshes excluded from training; generation is scored with ULIP and Uni3D similarity metrics against an unnamed benchmark.
**Limitation (≤3 sentences):** The paper has no dedicated limitations section; the authors note as a design trade-off that training uses single-timestep sampling rather than unrolling the full inference trajectory, to avoid added computational overhead. They also state that position predictions are unreliable at high noise levels, which is why early denoising stages use only coarse position quantization.

---

## OmniCam: Omni-Camera Trajectory Generation via Geometry-Grounded Pose Token Learning
- **arXiv:** 2610.09513 · https://arxiv.org/abs/2610.09513
- **Submitted:** 2026-10-07
- **Authors:** Zhenyang Liu, Chenjie Cao, Yisu Zhang, Xuhui Zuo, Xiangyang Xue, Yanwei Fu, Tengfei Wang, Chunchao Guo
- **Qualifying affiliation(s):** Tencent Hunyuan — FLAG: the paper's affiliation block lists "Fudan University, Shanghai Innovation Institute, Tencent Hunyuan, Zhejiang University" without per-author footnote markers in the rendered HTML; Tencent affiliation is inferred from co-author Chunchao Guo, who is independently confirmed as Tencent Hunyuan (tencent.com email, corresponding author) on the companion submission 2610.10342 the same week
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** none found on the arXiv page
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** OmniCam is an autoregressive model that generates camera pose trajectories from a single panorama plus a text description of the desired camera motion, using a panoramic point-cloud encoder and a hybrid rotation/translation pose tokenization. The authors also introduce OmniCaT, a new dataset of 267,700 camera trajectories across 9,998 scenes and four camera-behavior types.
**Purpose (≤3 sentences):** The authors aim to produce geometry-grounded, text-controllable camera trajectories that generalize across trajectory styles, for downstream use in camera-controlled video generation and robotic active perception.
**Breakthrough (≤3 sentences):** The authors report 28–47% lower trajectory error and a 65.8% lower collision rate than GenDoP retrained on their own OmniCaT dataset. They also report results on the public DataDoP benchmark using OmniCam trained only on OmniCaT, without DataDoP-specific fine-tuning.
**Tools & method (≤3 sentences):** The model combines a panoramic point-cloud encoder with separate geometric and semantic conditioning and a 3D target anchor; training used 8×NVIDIA H20 GPUs for roughly 100 epochs on the OmniCaT dataset. Baselines Director3D and GenDoP were retrained on OmniCaT, while CCD and E.T. were evaluated from released checkpoints as out-of-domain references.
**Limitation (≤3 sentences):** The authors state that geometry is estimated and incomplete and that supervision comes from a heuristic planner, so the model can inherit reconstruction errors and planner bias; observations are also limited to static scenes. They flag the DataDoP zero-shot comparison and the robot success-rate aggregation as still needing independent verification, and list failure cases involving noisy depth near thin structures, ambiguous target phrases, and reflective/transparent surfaces.

---

## Hardware-aware Calibrated Clustered Attention for Efficient Visual Geometric Transformers
- **arXiv:** 2610.09274 · https://arxiv.org/abs/2610.09274
- **Submitted:** 2026-10-07
- **Authors:** Weitian Wang, Shubham Rai, Cecilia De La Parra, Akash Kumar
- **Qualifying affiliation(s):** Robert Bosch GmbH — FLAG: borderline (automotive/industrial hardware company, not on the core tracked list; three of four authors list Bosch, the fourth lists Ruhr University Bochum only); comparable in kind to other hardware-adjacent companies on the "keep and flag" list
- **Categories:** cs.CV (primary), cs.LG (cross-list)
- **Open release:** none found on the arXiv page
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper speeds up the global attention layers of the Visual Geometry Grounded Transformer (VGGT), a 3D scene-reconstruction model, with a hardware-friendly "blockwise clustered attention" (BC attention) that restricts clustering to hardware-aligned neighborhood blocks.
**Purpose (≤3 sentences):** The authors aim to reduce VGGT's attention latency and off-chip memory traffic on GPUs without materially degrading 3D reconstruction accuracy, adding a calibration method to control the accuracy/speed trade-off.
**Breakthrough (≤3 sentences):** On ETH3D, calibrated BC attention reaches about 1% accuracy loss (overall error 0.700→0.707) with 2.10–2.63× faster global attention and 1.77–2.35× faster full-backbone latency; a looser setting (under 5% loss) reaches 2.26–2.87× and 1.90–2.55× respectively. At 200 input frames, backbone latency drops from 25.11s to 9.84–10.67s; the method also transfers to a second model, MapAnything, with overall ETH3D error moving only from 0.120 to 0.121.
**Tools & method (≤3 sentences):** Evaluation used a single NVIDIA H200 GPU, PyTorch in bfloat16, and FlashAttention-2 as the attention kernel for both standard and BC attention; benchmarks were ETH3D (point-map estimation) and DTU (dense multi-view stereo), both scored by accuracy, completeness, and Chamfer-style overall error. The method adds a hashing hyperplane calibration and a threshold-based error-compensation step on top of blockwise clustering.
**Limitation (≤3 sentences):** The paper has no dedicated limitations section; in the conclusion the authors state the approach "focuses solely on local token similarities" and suggest future work could add framewise similarity across temporally related frames. They claim the method applies "across most types of NVIDIA architectures" but evaluate on only one GPU (H200); an ablation also shows that lowering error-compensation coverage from 10% to 5% raises ETH3D accuracy error from 0.891 to 1.320.

# Near-misses
- 2610.09514 · STRIKE: Learning Visual State Transitions for Physical World Modeling · all 8 authors affiliated with Applied Intuition, USC, or UC Berkeley — no qualifying industry affiliation; "NVIDIA" screen hit was a reference-list citation (Cosmos models), not an author affiliation
- 2610.09134 · World Models Dream of Success: Diagnosing and Repairing Failure Insensitivity in Robot World Models · all 6 authors are academic (Colorado School of Mines, Northeastern, USC-ICT, NC State) — no qualifying industry affiliation; "NVIDIA" screen hit was a reference-list citation
- 2610.09326 · VIS-Ground: Video Interactive Storytelling with Contextual Grounding · qualifying Google affiliation confirmed (8 of 13 authors), but topic is general interactive-video-generation/storytelling controllability, not squarely 3D, world models, character animation, or game engines — borderline topic, excluded
- 2610.09254 · RoboRender: Robot-Oriented Video Generation for Visual Sim-to-Real Transfer · no HTML version available (404); abstract page lists no author affiliations — affiliation unverifiable
- 2610.10524 · GRACE: Generation-aware latent compression for efficient video generation · screen hit was "borderline"-list company terms with no specific match surfaced; topic is generic video-generation compression efficiency, not 3D/world-models/character-animation/game-engines — off-topic, not further verified
- 2610.10457 · MORCA: Offline-to-Online RL for Adaptive Cache Reuse in Video Diffusion Acceleration · Alibaba screen hit; topic is generic video-diffusion inference acceleration, not on tracked topics — off-topic, not further verified
- 2610.10430 · Conditional Flow Matching for Generation of 3D Multi-variable Instantaneous Urban Microclimate Fields · "Google" screen hit (likely a Google Scholar citation-tool match, not an author affiliation); topic is environmental/urban climate science — off-topic, not further verified
- 2610.10400 · Self-correction Optimization for Interleaved Multimodal Generation · borderline-list screen hit; topic is general interleaved multimodal (text+image) generation — off-topic, not further verified
- 2610.10047 · AdSpark: A Large-Scale Dataset and Benchmark for Product-Centric Advertisement Video Generation · borderline-list screen hit; topic is advertising video generation — off-topic, not further verified
- 2610.09800 · Beyond Masks and Trajectories: Flow-Guided Latent Action Injection for Stable Surgical Video Generation · Tencent screen hit; topic is surgical/medical video generation — off-topic, not further verified
- 2610.09558 · DrugTargetWorld: A Synthetic Biobank for Training and Benchmarking AI Scientists · "Google" screen hit; topic is drug discovery/biology — off-topic, not further verified
- 2610.09376 · Unified Multi-plane Autoregressive Diffusion for 3D Multi-contrast MRI Synthesis · Microsoft screen hit; topic is medical MRI synthesis — off-topic, not further verified

Verification pass: all four qualifying papers above were double-checked against both the arXiv abstract page (submission date, author list, categories, withdrawal status, comments/links) and the arXiv HTML rendering (author affiliation block, experiments section, stated limitations) before inclusion; no PDF fallback was needed. The eight near-miss/dropped items above were screened from their abstract/HTML text only, consistent with the "leads only" nature of the affiliation pre-screen.
