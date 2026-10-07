## FLEX-WAM: Flexible Block-Causal World-Action Models for Long-Horizon Imagination and Planning
- **arXiv:** 2610.05483 · https://arxiv.org/abs/2610.05483
- **Submitted:** 2026-10-04 (Sun, 4 Oct 2026 19:41:50 UTC)
- **Authors:** R. Khorrambakht, Joseph Amigo, Félix Lebel, Leon Seetoo, Jean Ponce, Zhenzhen Li, Ludovic Righetti
- **Qualifying affiliation(s):** NVIDIA — Zhenzhen Li (other authors: NYU CREO, NYU Courant/ENS-PSL, NYU/ANITI)
- **Categories:** cs.RO (primary); cs.AI (cross)
- **Open release:** none (authors state code and checkpoints are "omitted for anonymous review and will be released upon acceptance")
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** FLEX-WAM is a block-causal world-action model that jointly predicts action-conditioned video and generates actions from a shared architecture, supporting variable-length contexts and frame-by-frame or block-by-block autoregressive rollout.
**Purpose (≤3 sentences):** It addresses the problem that existing joint video-action models use fixed-horizon backbones poorly suited to streaming inference, aiming to unify simulation and policy inference within one flexible, deployable architecture.
**Breakthrough (≤3 sentences):** The authors report that, used as a joint action proposer and simulator inside MCTS, FLEX-WAM solves the long-horizon PushT task and all five OGBench Puzzle-4x4 tasks entirely in imagination, and that on a bimanual OpenArm-based robot a single checkpoint jointly serves as a play policy and an expected-outcome predictor.
**Tools & method (≤3 sentences):** The model combines axial attention with blockwise diffusion forcing in a KV-cacheable, block-causal architecture, and counters weak action responsiveness from naive joint training by balancing state/action flow-matching gradients via a "Forward-Dynamics (FD) elasticity" training-time proxy.
**Limitation (≤3 sentences):** The authors note joint training can still produce futures that only weakly respond to commanded actions without the FD-elasticity fix, that text conditioning was dropped because it competes with action information and impairs simulation, and that OGBench planning "success" is measured only in imagination, with closed-loop real-world execution left to future work.

---

## CleanMDM: Clean Motion Diffusion Model for Multimodal Motion Cleanup
- **arXiv:** 2610.05411 · https://arxiv.org/abs/2610.05411
- **Submitted:** 2026-10-04 (Sun, 4 Oct 2026 17:50:26 UTC)
- **Authors:** Zhe Li, Shicheng Wang, Bowen Cai, Huan Fu
- **Qualifying affiliation(s):** Alibaba — Bowen Cai, Huan Fu (other authors: Peking University, Light Origins)
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** CleanMDM is a motion diffusion model that treats mocap cleanup as masked conditional generation, accepting plug-and-play combinations of noisy 3D motion, sparse 2D/3D keyframes, and text to denoise and complete character motion.
**Purpose (≤3 sentences):** It targets cleaning up noisy or incomplete motion-capture data (jitter, foot skating, missing frames) with a single unified model instead of task-specific pipelines.
**Breakthrough (≤3 sentences):** The authors report that a Latent Motion Quality Discriminator and a Mesh-Aware Contact Projection step reduce artifacts such as skating and jitter, and that text and 2D-keyframe conditioning provide effective additional control, improving over prior cleanup/generation baselines (trained on AMASS/MotionLLaMA; validated on HAA500, IDEA400, Kungfu, HuMMan, AIST++).
**Tools & method (≤3 sentences):** The pipeline combines masked conditional diffusion with a learned motion-quality discriminator and a mesh-aware contact-projection optimization step applied over a simplified ground/terrain model.
**Limitation (≤3 sentences):** The authors state the evaluation relies on controlled, synthetically injected corruption (jittering, floating, foot sliding, drifting) and a simplified ground model for contact projection, and plan to incorporate more realistic video-mocap degradations, stronger learned contact priors, and additional control modalities in future work.

---

## CreativeFlow: A One-to-Many Analogical Relation Transfer Method for 3D Asset Generation
- **arXiv:** 2610.05167 · https://arxiv.org/abs/2610.05167
- **Submitted:** 2026-10-04 (Sun, 4 Oct 2026 12:24:36 UTC)
- **Authors:** Xuechen Li, Shuai Zhang, Nanxuan Zhao, Qing Chen
- **Qualifying affiliation(s):** Adobe — Nanxuan Zhao (Adobe Research, San Jose; other authors: Tongji University)
- **Categories:** cs.AI; cs.GR
- **Open release:** none (3-page paper to appear at SIGGRAPH Asia 2026 Posters)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** CreativeFlow is an analogical-generation framework for text-to-3D asset pipelines that derives source-target asset pairs sharing a relation but differing in geometric configuration, aiming to counter sameness in generated outputs.
**Purpose (≤3 sentences):** It addresses "creative homogenization" in current text-to-3D generation pipelines by explicitly modeling analogical divergent thinking drawn from cognitive science.
**Breakthrough (≤3 sentences):** The authors report expert user-study scores of 3.66/5 for identity preservation, 3.86/5 for novelty, and 3.31/5 for visual fascination versus 2.84/5 for the strongest baseline (compared against Hunyuan3D-2, TRELLIS-2, and SF3D), with each source asset expanding into 5-10 generated relations.
**Tools & method (≤3 sentences):** The framework produces a workflow of relationally similar source-target 3D asset pairs and uses the resulting assets to establish a dataset/benchmark intended for future relation-aware 3D model training.
**Limitation (≤3 sentences):** The authors describe the work as "an initial step," noting they still lack a large-scale structured source-relation-target dataset for training/benchmarking, lack robust metrics specifically for generative creativity and analogical rationality, and leave interactive creative tooling to future work.

---

## Lollypop: Camera-to-Motion-Capture Calibration Verification with a Reference Target
- **arXiv:** 2610.04785 · https://arxiv.org/abs/2610.04785
- **Submitted:** 2026-10-03 (Sat, 3 Oct 2026 21:56:30 UTC)
- **Authors:** Tianyi Liu, Kevin Harris, Mihika Dave, Kun He
- **Qualifying affiliation(s):** Meta — all four authors (Meta, Redmond, WA)
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Lollypop is a fiducial-mocap reference target that lets practitioners independently verify camera-to-motion-capture calibration by coupling an ArUco fiducial with a mocap marker constellation sharing the same physical center point.
**Purpose (≤3 sentences):** It targets calibration drift in deployed camera-to-mocap systems used as ground truth for robotics, AR/VR, and computer-vision tasks, where existing calibration residuals and visual inspection give only limited independent verification.
**Breakthrough (≤3 sentences):** The authors report a combined nominal median reprojection error of 0.53 pixels (RMSE 0.80 px, 95th percentile 1.47 px; 0.84 mm median / 2.02 mm p95 in metric space) and demonstrate increasing error under controlled perturbations (RMSE rising to 5.63 px at 5 mm translation and 6.46 px at 1.0° rotation).
**Tools & method (≤3 sentences):** Verification projects the tracked mocap centroid into the camera image and measures its disagreement with the detected ArUco fiducial center under a candidate calibration.
**Limitation (≤3 sentences):** The authors note the target's depth observability is not fully independent (back-projection depth is derived from mocap itself), that the 0.12 mm thickness of the retroreflective tape is the primary source of manufacturing error, and that ArUco detection is inherently limited to moderate viewing angles; they propose multi-point/non-coplanar targets with stronger depth observability as future work.

---

## Neuroll: Real-Time Neural Strand-Based Hair Simulation via Simulator-in-the-Loop Unrolling
- **arXiv:** 2610.04689 · https://arxiv.org/abs/2610.04689
- **Submitted:** 2026-10-03 (Sat, 3 Oct 2026 18:05:34 UTC)
- **Authors:** Gene Wei-Chin Lin, Jessica Jia-En Lee, Yu Ju (Edwin) Chen, Egor Larionov, Tuur Stuyck
- **Qualifying affiliation(s):** Meta / Meta Reality Labs — Gene Wei-Chin Lin, Jessica Jia-En Lee, Yu Ju (Edwin) Chen, Egor Larionov; NVIDIA — Tuur Stuyck
- **Categories:** cs.GR
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Neuroll is a neural, strand-based real-time hair simulator that replaces classical time integration with a network trained via self-supervised, simulator-in-the-loop unrolling, formulated in each strand's local coordinate frame.
**Purpose (≤3 sentences):** It aims to bring physically plausible, real-time hair simulation for thousands of strands to commodity hardware for applications such as gaming and virtual avatars, where classical optimized integrators remain too costly and prior neural methods are less physically plausible and generalize poorly out-of-distribution.
**Breakthrough (≤3 sentences):** The authors report an inference time of 0.460 ms for 3,000 strands, a 7.7× speedup over Quaffure (comparable to Neuralocks at 0.203 ms) and roughly 200× faster than their ground-truth simulator (89.517 ms), stable rollouts for 2,000 consecutive frames versus 131 for Neuralocks, and generalization to up to 120,000 strands at 6.503 ms per frame.
**Tools & method (≤3 sentences):** The neural time integrator takes previous hair states, material stiffness, and collision geometry as input (mirroring classical integrators' formulation) and is trained with randomized unrolling horizons via self-supervised simulator-in-the-loop training, in each strand's local frame for generalization across hairstyle, material, and body type.
**Limitation (≤3 sentences):** The authors state the method generalizes well to short/mid-length hair but struggles on long hairstyles, under-predicts motion magnitude (a motion ratio of 0.622 versus the reference simulation), does not model strand self-collisions (which would break the per-strand independence the method relies on), and restricts body-collision signal to the head/shoulder region for performance reasons.

---

## DistScene: Object-to-Scene Distillation for 3D Scene Generation
- **arXiv:** 2610.06960 · https://arxiv.org/abs/2610.06960
- **Submitted:** 2026-10-03 (Sat, 3 Oct 2026 16:21:52 UTC)
- **Authors:** Kunming Luo, Hongyu Yan, Ken Deng, Chengcheng Zhou, Tianyu Liu, Haipeng Li, Haibin Huang, Xuelong Li, Ping Tan
- **Qualifying affiliation(s):** TeleAI / China Telecom — Chengcheng Zhou, Haibin Huang, Xuelong Li (Kunming Luo via internship); other authors: HKUST. **FLAG: borderline** — TeleAI/China Telecom is not on the tracker's explicit company list and its standing relative to tracked gaming/3D industry labs is unclear, so this is kept per the tracker's guidance for unsure industry labs rather than dropped.
- **Categories:** cs.CV
- **Open release:** none (project page lists code/checkpoint/dataset as "coming soon"; a HuggingFace preview-assets page exists: https://huggingface.co/coolbeam/DistScene-preview-assets)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** DistScene generates compositional 3D scenes from a single image by jointly producing separate environment and object components in a unified coordinate system, then refining objects and distilling object-level generative priors into the scene.
**Purpose (≤3 sentences):** It targets single-image 3D scene generation that preserves spatial coherence between objects and their environment alongside the fidelity of individual objects, which the authors say existing scene-level methods have not addressed well.
**Breakthrough (≤3 sentences):** The authors report improved spatial coherence over existing approaches on indoor (MIDI-test, Gen3DSR-test) and outdoor (UrbanScene3D) benchmarks, with additional qualitative evaluation on ScanNet.
**Tools & method (≤3 sentences):** Scene-Frame Generation jointly produces environment and object components, Object-Centric Refinement locally enhances each object with scene awareness, and Object-to-Scene Distillation transfers knowledge from pretrained object-generation models into the scene pipeline.
**Limitation (≤3 sentences):** The authors note indoor training assets generally omit ceilings (since reliable fully-enclosed empty rooms are hard to obtain from pretrained 3D object generators), which can yield open-top reconstructions of closed interiors, and that outdoor scenes lose fine geometric detail and may contain holes because a limited number of scene-frame voxels must cover a wide area, compounded by a smaller outdoor training set due to compute constraints.

---

## Sparse-View 4D Gaussian Splatting via Spatiotemporal Priors and Generative Assistance
- **arXiv:** 2610.04606 · https://arxiv.org/abs/2610.04606
- **Submitted:** 2026-10-03 (Sat, 3 Oct 2026 15:48:50 UTC)
- **Authors:** Shengqi Wang, Zhengxian Yang, Kaiwen Tian, Yang Liu, Bowen Liu, Hua Du, Taicheng Huang, Jiamin Wu, Tao Yu
- **Qualifying affiliation(s):** JD.com — Yang Liu, Taicheng Huang (other authors: Tsinghua University, Beijing MEET YUAN Co., Ltd.). **FLAG: borderline** — JD.com is named explicitly in the tracker's own criteria as a company to flag rather than silently include or exclude.
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The authors present a 4D Gaussian Splatting system built for the Sparse-View Track of the SIGGRAPH Asia 2026 Volumetric Video Challenge, reconstructing dynamic scenes from only six wide-baseline cameras.
**Purpose (≤3 sentences):** It addresses dynamic scene reconstruction under extremely sparse, wide-baseline camera coverage, a setting standard dense multi-view 4DGS pipelines are not designed for.
**Breakthrough (≤3 sentences):** The authors report their system achieved 30.04 dB full-frame PSNR and 27.88 dB foreground PSNR on the challenge test set, ranking first overall in the Sparse-View Track (improving a 25.60 dB baseline to 29.75 dB full-frame PSNR on their own validation set).
**Tools & method (≤3 sentences):** The framework combines region-adaptive spatial priors (foreground-mask-guided densification and metric-scale-aligned monocular depth for the background), motion-consistent temporal priors (frame interpolation and optical-flow-constrained Gaussian motion), and generative assistance that restores images from virtual cameras placed in the widest angular gaps using a pose-conditioned diffusion model.
**Limitation (≤3 sentences):** The authors note a slight SSIM decrease from diffusion-completion artifacts despite improved overall visual fidelity, and that the weakly-observed background (lacking direct geometric anchoring from the added priors) is more susceptible to geometric drift; they state future work will target reducing reconstruction time and model size for real-time use on standalone VR headsets.

---

## CurveCodec 2: Skeleton-agnostic animation compression with a learned entropy model
- **arXiv:** 2610.04211 · https://arxiv.org/abs/2610.04211
- **Submitted:** 2026-10-03 (Sat, 3 Oct 2026 01:54:18 UTC)
- **Authors:** Mingyi Shi, Huancheng Lin, Xuelin Chen, Taku Komura
- **Qualifying affiliation(s):** Adobe — Xuelin Chen (Adobe Research, London; other authors: University of Hong Kong)
- **Categories:** cs.GR (primary); cs.AI, cs.RO (cross)
- **Open release:** code — https://github.com/AIGAnimation/AnimationCodec; demo — https://playground.rubbly.cn/codec/ (project page: https://rubbly.cn/publications/curvecodec/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** CurveCodec 2 is a skeleton-agnostic skeletal-motion compression codec that encodes each sub-track as a quantized curve with rate-distortion-selected keys, entropy-coding the residuals under a small, bit-exact learned model.
**Purpose (≤3 sentences):** It aims to reduce skeletal-animation storage beyond what the body alone implies, improving on the authors' earlier CurveCodec and on ACL, the production animation-compression library used in modern game engines, under a stated per-clip error bound.
**Breakthrough (≤3 sentences):** The authors report that on a held-out set of 4,472 clips from 33 datasets, CurveCodec 2 needs 0.37x of ACL's bytes at ACL's default 0.01 cm precision under a worst-case-per-joint contract, and 0.22x at 0.1 cm under a mean-error contract, decoding on a single CPU core and transferring without retraining to a species absent from training.
**Tools & method (≤3 sentences):** The codec predicts each quantized curve from its own closed-loop-quantized past in the log map, selects which joints to sample via closed-loop hierarchy traversal, and entropy-codes residuals with a small learned model; the authors also report that a nearest-neighbour oracle over millions of samples and the learned in-betweeners they tried do not beat linear interpolation for filling coding gaps.
**Limitation (≤3 sentences):** The authors state the codec decodes whole clips and cannot retrieve individual poses in constant time like ACL (an inherent design property, not an optimization gap), that it was tested only as a codec without evaluation on a generative or recognition task, and that it degrades on short, low-rate clips of small skeletons (e.g., 0.676x ACL on HumanAct12, 0.628x on Edinburgh, 0.609x on BFA).

---

## SUAVE: Unified Video-Action Models via Masked Diffusion
- **arXiv:** 2610.04009 · https://arxiv.org/abs/2610.04009
- **Submitted:** 2026-10-02 (Fri, 2 Oct 2026 20:11:13 UTC)
- **Authors:** Rhythm Syed, Jean Mercat, Sedrick Keh, Kushal Arora, Paarth Shah, Aykut Onol, Mengchao Zhang, Tony Dear
- **Qualifying affiliation(s):** Toyota Research Institute — Jean Mercat, Sedrick Keh, Kushal Arora, Paarth Shah, Aykut Onol, Mengchao Zhang (Rhythm Syed also dual-affiliated TRI/Columbia; Tony Dear: Columbia only). **FLAG: borderline** — Toyota Research Institute is not on the tracker's explicit company list; flagged per guidance for unsure industry labs.
- **Categories:** cs.RO (primary); cs.CV, cs.LG (cross)
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SUAVE is a single masked-diffusion transformer that represents video, language, and robot actions as discrete tokens in one shared sequence, so that choosing which tokens to mask at inference turns the same network into a world model, a policy, or a joint video-action model.
**Purpose (≤3 sentences):** It aims to unify vision-language-action models (which act but don't imagine future observations) with video-based world-action models (which imagine but treat language as frozen conditioning) within a single architecture, rather than separate decoders or auxiliary action heads.
**Breakthrough (≤3 sentences):** The authors report that a single SUAVE model predicts long-horizon video and acts as a policy competitively with dedicated world models and specialized action policies on static/dynamic manipulation benchmarks (LIBERO, LIBERO-Plus, DOMINO), and that on a real robot it generates a subgoal image plus a one-second action chunk in 1,030 ms on an RTX 5090 GPU, sustaining closed-loop control at 2.5 actions/second; they also report pretraining on robot video plus co-training on human video substantially improves policy performance and zero-shot robustness to distribution shift.
**Tools & method (≤3 sentences):** Masking different token positions at inference lets one masked-diffusion transformer serve as world model, policy, or video-action model; for action-free co-training on unlabeled human video, action-token positions are filled with mask tokens and excluded from the loss.
**Limitation (≤3 sentences):** The authors state that co-training's improvement over pretraining alone, while positive, "is not statistically separable" at their scale; that a frozen MAGViT-v2 tokenizer bounds predicted-frame reconstruction quality and fixed-length token sequences prevent horizon adaptation; and that they evaluate only a single 7-DoF arm with an end-effector action space, without generating or evaluating language despite using a language-model backbone.

---

## SCCM: Spherically Consistent Coarse Matching for ERP Dense Feature Correspondence
- **arXiv:** 2609.36545 · https://arxiv.org/abs/2609.36545
- **Submitted:** 2026-09-29 (Tue, 29 Sep 2026 02:32:30 UTC)
- **Authors:** Gyeonggwan Lee, Eunsoo Im, Seunghwan Hong, Junghun Suh
- **Qualifying affiliation(s):** Kakao Mobility Corp. — all four authors (Gyeonggwan Lee also Korea University). **FLAG: borderline** — Kakao Mobility is a mobility/mapping company, not on the tracker's explicit list; flagged per guidance for unsure industry labs.
- **Categories:** cs.CV
- **Open release:** code — https://github.com/gandanlee/sccm (project page: https://gandanlee.github.io/sccm/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SCCM is a coarse-matching method for dense feature correspondence between 360° equirectangular (ERP) panoramas that explicitly corrects for the seam, latitude-dependent stretch, and non-uniform pixel area the ERP projection introduces.
**Purpose (≤3 sentences):** It targets the systematic degradation of perspective-trained dense matchers on ERP panoramas — which underlie omnidirectional pose estimation, 3D reconstruction, and SLAM — by fixing the three geometric distortions at the coarse-matching stage rather than at the refiner.
**Breakthrough (≤3 sentences):** The authors report SCCM improves PCK@1° from 0.230 to 0.275 on Matterport3D over a fixed, chart-naive coarse scaffold (refiner architecture unchanged), and outperforms the ERP-native EDM (0.163) and an ERP-retrained RoMa V1 (0.198) under a unified ERP dense-matching protocol, with zero-shot transfer to Stanford2D3D and leading results on outdoor Holo360D.
**Tools & method (≤3 sentences):** Built on the RoMa V1 framework with a frozen DINOv2-Large encoder, SCCM adds Spherical Positional Attention (a yaw-periodic RoPE paired with a tangent-plane bias) and Area-Aware Covisibility (a pre-sigmoid log-area correction applied to covisibility gating).
**Limitation (≤3 sentences):** The authors state SCCM assumes gravity-aligned ERP and does not explicitly handle camera tilt, with PCK@1° dropping to 0.142 at 10° synthetic pitch and 0.034 at 30° pitch for all tested ERP matchers; it inherits the frozen encoder's limitations in texture-less, photometrically ambiguous, or low-overlap regions; and it was trained only on Matterport3D (indoor) and Holo360D (outdoor), leaving the refiner stage "sphere-naïve."

---

# Near-misses
- 2610.05484 · Universal Test-Time Training · off-topic despite Adobe co-author (Hao Tan): the core contribution is a general shared-memory test-time-training architecture evaluated mainly on language modeling, with novel-view synthesis only one secondary evaluation task — not fundamentally a 3D/world-model/animation/game-engine research contribution.
- 2610.05289 · Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting · no qualifying affiliation: all six authors are academic (University of Technology Sydney, Yale, City University of Macau, Australian National University, Adelaide University); the "Google"/"NVIDIA" regex hits are grant-program acknowledgments (Google Research Scholar Program, NVIDIA academic grant program), not author affiliations.
- 2610.04351 · LoCoSplat: Real-Time Feed-Forward 3D Gaussian Splatting with Minimal 3D Reasoning · no qualifying affiliation: all authors are at Georgia Institute of Technology; no author affiliation matching the "NVIDIA" regex hit was found in the paper.
- 2610.04336 · A differentiable Lagrangian-coupled 3D Gaussian Splatting-SPH model for forward simulation and inverse analysis in solid mechanics · no qualifying affiliation (all three authors are HKUST Civil and Environmental Engineering; no author affiliation matching the "Google" regex hit was found) and off-topic (the paper applies 3DGS-SPH to solid-mechanics/civil-engineering inverse analysis, not 3D graphics, world models, animation, or game engines).
- 2610.06910 · GAMEGO: Training Game-Dev Agents with Synthetic Trajectories Anchored in Real-World Assets · off-topic despite a genuine Baidu affiliation (Jingyao Li, Zhengfan Wu, Jing Liu): this is a generic LLM coding-agent training/benchmark paper (synthetic-trajectory data generation and PRD construction for browser-game code synthesis), not a research contribution to 3D, world models, character animation, or game-engine technology itself.

**Verification statement:** All 15 leads were checked against their arXiv abstract page (title, authors, v1 date, categories, withdrawal status) and, where available, the arXiv HTML full text (author affiliation block, acknowledgments, and limitations/results sections) rather than relying on the batch's regex company_matches. No HTML-unavailable cases were encountered. Every included paper's v1 submission date falls within 2026-09-29 to 2026-10-04, inside the 2026-09-07–2026-10-07 window. A second read-through of each qualifying block against the fetched source text was performed before writing this file.
