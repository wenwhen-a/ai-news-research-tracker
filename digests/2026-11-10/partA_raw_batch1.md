## Spaghetti Splatting: Differentiating Curvilinear Dirac Masses via Convolution
- **arXiv:** 2611.12716 · https://arxiv.org/abs/2611.12716
- **Submitted:** 2026-11-09
- **Authors:** George Shramko, Shrisudhan Govindarajan, Rudy Lam, Yizheng Xie, Daniel Rebain, David B. Lindell, Andrea Tagliasacchi
- **Qualifying affiliation(s):** Wayve Labs — Shrisudhan Govindarajan, Daniel Rebain, Andrea Tagliasacchi (FLAG: borderline — Wayve is a well-funded autonomous-driving AI company, not on the main tracked list)
- **Categories:** cs.CV, cs.GR
- **Open release:** code (authors state they "commit to fully release code" and mention a project webpage, but no URL is given in the paper)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces "Spaghetti Splatting," a method for learning curve-like (curvilinear) 3D primitives directly from images via differentiable volume rendering, extending the convolution-based formulation used in EWA splatting and 3D Gaussian Splatting to one-dimensional, infinitely-thin geometry. Curves are approximated as polylines rendered segment-by-segment so that joints are not double-counted, with a linearized camera projection for fast training/inference.
**Purpose (≤3 sentences):** Existing splatting methods struggle to represent curve-like structures (hair, fur, thin strands) because such primitives are infinitely thin and poorly suited to Gaussian "blob" kernels. The authors aim for a unified, differentiable formulation that handles both point-like and curve-like geometry.
**Breakthrough (≤3 sentences):** The authors report their formulation is a strict superset of 3D Gaussian Splatting (points are zero-length curves), supports kernels beyond Gaussians (e.g., Beta kernels), and yields native anti-aliasing plus long connected strands suitable for physics simulation. They report results competitive with state-of-the-art general-scene methods and better than methods specialized for line-like geometry.
**Tools & method (≤3 sentences):** Evaluated on Mip-NeRF 360 (standard unbounded-scene benchmark), plus Shelly (synthetic fur/wool/leaves), Fuzzy (captured fibrous objects), and GeomHair (400 strand-level hairstyles from head scans); hair renders use a Yuksel curly-hair model with GeomHair scenes path-traced in Blender. Frame rate was measured on an RTX 4090 GPU.
**Limitation (≤3 sentences):** The authors state that reproducing fine texture currently requires many short segments, and real hair reconstruction remains challenging. They also note that broader claims about automatically recovered topology require further evaluation, and they have not yet tested interpolating the kernel between segment endpoints (which could extend primitives to cones, triangles, and trapezoids).

## PhysOPSD: Code as Privilege for Physically Plausible Video Generation
- **arXiv:** 2611.12411 · https://arxiv.org/abs/2611.12411
- **Submitted:** 2026-11-09
- **Authors:** Harold Haodong Chen, Rui Peng, Lingteng Qiu, Kejie Qiu, Chao Xu, Zilong Dong
- **Qualifying affiliation(s):** Alibaba — Zilong Dong et al. (affiliation block lists "HKUST & Alibaba Token Hub" and "Alibaba Group"; footnote states the work was done at ATH@Alibaba Group)
- **Categories:** cs.CV
- **Open release:** code — https://github.com/aigc3d/PhysOPSD; project page — https://haroldchen19.github.io/PhysOPSD-site
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PhysOPSD is a framework for making video-generation models physically plausible by using executable simulation code as a "privileged" physical context during on-policy distillation, rather than relying on supervised fine-tuning or sparse physics-based RL rewards. A "PhysOPSD-Engine" converts real-world physical scenarios into verifiable simulation programs that supervise training.
**Purpose (≤3 sentences):** The authors note that modern video generators achieve high visual fidelity but often fail at physically plausible motion and complex interactions; supervised fine-tuning suffers from state mismatch and RL struggles with sparse, poorly defined physics rewards. PhysOPSD aims to close this gap with simulator-grounded supervision.
**Breakthrough (≤3 sentences):** The authors report dual-level physical privilege via an intermediate bottleneck plus controlled physical variations under shared rollout noise, achieving better physical plausibility than SFT and RL baselines using only about 3K training samples (built from a 33K-instance PhysOPSD-3K dataset), while preserving general video quality across multiple backbones.
**Tools & method (≤3 sentences):** Applied to two unified video generators (OmniWeaving, 8.3B, and UniVideo, 13B); simulation/annotation tools include MuJoCo, Genesis, and Blender, with Qwen3-VL-32B for annotation and a coding agent (named GPT-6-Astra in the appendix) generating simulation programs. Evaluated on VideoPhy-2, PhyGround, and VBench, compared against SFT (80K samples from WISA) and PhysHPO (21K samples) baselines.
**Limitation (≤3 sentences):** The authors state the method covers only phenomena standard simulators can stably compute, explicitly excluding chaotic multi-physics and thermodynamic phase transitions (e.g., combustion) and turbulent gas diffusion due to solver instability. They also note the pipeline's effectiveness depends on the underlying coding agent and physics solvers, which will need to advance for more complex scenarios, and frame PhysOPSD as a general distillation framework rather than a single model.

## HIST3R: Decomposing and Rectifying State Updates with History for Streaming 3D Reconstruction
- **arXiv:** 2611.12011 · https://arxiv.org/abs/2611.12011
- **Submitted:** 2026-11-09
- **Authors:** Kenneth Yang, Yu-Chiang Frank Wang
- **Qualifying affiliation(s):** NVIDIA — Yu-Chiang Frank Wang (listed as National Taiwan University and NVIDIA)
- **Categories:** cs.CV
- **Open release:** none confirmed (project page given: https://kennethyangg.github.io/HIST3R; no explicit code/weights link found in the fetched text)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** HIST3R is a training-free framework for streaming 3D reconstruction that decomposes CUT3R-style recurrent state updates into a magnitude (how strongly a new observation is written into the scene state) and a direction (where the update moves the state), then rectifies the direction using locally consistent historical states. Update magnitude is additionally scaled by the visual discrepancy between the new observation and history.
**Purpose (≤3 sentences):** The authors observe that streaming 3D reconstruction with recurrent scene states can drift over long videos because unreliable updates overwrite historical context, and argue existing training-free extensions only control update magnitude, not direction.
**Breakthrough (≤3 sentences):** Built on top of CUT3R without retraining, the authors report improved long-horizon performance on camera pose estimation, 3D reconstruction, and video depth estimation, including ATE reductions on ScanNet and TUM-Dynamics at 1000 frames and accuracy gains on 7-Scenes and NRGBD at 500 frames, while preserving CUT3R's memory footprint and inference speed.
**Tools & method (≤3 sentences):** Backbone is CUT3R, with HIST3R applied as a training-free, inference-time extension. Evaluated on TUM-Dynamics, ScanNet, 7-Scenes, and NRGBD for long-sequence reconstruction/pose, plus KITTI, Sintel, and Bonn for video depth and short-sequence tests; experiments run on a single NVIDIA H100 GPU (80GB).
**Limitation (≤3 sentences):** The authors state that, as a training-free method, HIST3R is bounded by the pretrained CUT3R model and cannot recover geometric information the underlying model does not encode, nor fully correct severely inaccurate candidate predictions. They also note it slightly underperforms CUT3R under sparse-view inputs, where the local temporal structure it relies on is weaker.

## Budget-aware Correspondence-driven View Selection for Real-time 3D Perception of Mobile Robots
- **arXiv:** 2611.11809 · https://arxiv.org/abs/2611.11809
- **Submitted:** 2026-11-09
- **Authors:** Vaishnav Ramesh, Jacob Carter, Shivali J. Patel, Sanjeev J. Koppal, Md Jahidul Islam
- **Qualifying affiliation(s):** Amazon — Sanjeev J. Koppal (FLAG: borderline — footnote states a concurrent appointment as "Associate Professor at ECE-UF and a Scholar at Amazon Robotics," not a primary industry affiliation)
- **Categories:** cs.RO, cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces BCVS, a pose-free, correspondence-driven view-selection algorithm that runs at over 22 FPS on CPU to filter redundant frames from image sequences for real-time 3D perception on mobile robots. Rather than full structure-from-motion or pose estimation, it scores frames by correspondence to favor novel views while retaining enough overlap for geometric stability, under a user-specified selection budget.
**Purpose (≤3 sentences):** The authors target efficient, on-the-fly reduction of redundant imagery for downstream 3D reconstruction on resource-constrained mobile robots (aerial, marine), where full SfM/pose pipelines are too costly to run online.
**Breakthrough (≤3 sentences):** The authors report BCVS outperforms CPU-friendly baselines at tight view budgets and stays competitive as budgets grow, with aerial and marine field trials showing up to 16% redundancy reduction while maintaining SfM registration and reconstruction quality.
**Tools & method (≤3 sentences):** Evaluation combines field trials (aerial drone and marine/underwater sequences) with COLMAP-based SfM registration and reconstruction quality checks against CPU-friendly baseline view-selection methods under varying view budgets.
**Limitation (≤3 sentences):** The authors state BCVS is sensitive to the balance between connectivity and parallax weighting — overweighting connectivity can retain rotation-only redundancy, while prioritizing parallax can fragment overlap. They also note feature-matching quality degrades in low-texture, dynamic, or heavily blurred scenes, weakening the selection signal; in the aerial sequence, a 600-view budget performed worse than 300 because extra selections were near-duplicates, and bicycle/stump scenes were excluded from low-budget evaluations because COLMAP registration frequently failed.

# Near-misses
- 2611.12319 · Mitigating SM-Level Load Imbalance in 3D Gaussian Splatting on GPUs · academic-only authors (both at KAIST; "Google" screening lead was a false match)
- 2611.12136 · LHNav: Long-Horizon Humanoid Navigation via Multirate Coordination and Physics-Grounded Action Data · off-topic: low-level humanoid navigation/robot-control system (Brain/Cerebellum/Brainstem coordination), not a general world-model/3D/animation/engine contribution, despite industry co-authors at Robbyant
- 2611.12087 · Compass 1: Towards Open-World and Persistent Embodied Navigation from Monocular RGB Videos · affiliation unverifiable: no HTML version available (404 on arxiv.org/html)
- 2611.11912 · LO-World: Unified BEV Latent Modeling for Joint 4D Occupancy and LiDAR Forecasting · academic-only authors (all at Xi'an Jiaotong University)
- 2611.11869 · Action Representation for Spatial Generalization in Robot World Models · off-topic: low-level robot manipulation study (surgical/peeling action-frame benchmark), not a general world-model technique; also affiliation unverifiable (no HTML version, sole academic-sounding author)
- 2611.11780 · Planners Exploit Deterministic Error: Dithered Low-Bit World Models · academic-only authors (both at Chungbuk National University)
- 2611.11605 · ScanDreamer: A Map-Grounded World Model for Quadrotor Navigation · academic-only authors (Xiamen University Malaysia, VinUniversity, Nanyang Technological University); also largely low-level robot-navigation control rather than a general world-model contribution
- 2611.11586 · FastGRT: Accelerating Training of 3D Gaussian Ray Tracing · academic-only authors (all at New York University; "Google" screening lead was a false match)
