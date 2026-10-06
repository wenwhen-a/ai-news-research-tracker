## CreativeFlow: A One-to-Many Analogical Relation Transfer Method for 3D Asset Generation
- **arXiv:** 2610.05167 · https://arxiv.org/abs/2610.05167
- **Submitted:** 2026-10-04
- **Authors:** Xuechen Li, Shuai Zhang, Nanxuan Zhao, Qing Chen
- **Qualifying affiliation(s):** Adobe Research — Nanxuan Zhao
- **Categories:** cs.AI; cs.GR
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents CreativeFlow, an analogical generation framework inspired by cognitive science that explicitly models analogical divergent thinking to counter creative homogenization in text-to-3D pipelines. The method derives source-target asset pairs that are relationally similar but have distinct geometric configurations, via a three-stage pipeline: attribute inference, dual-path relational expansion through knowledge graphs/LLMs, and Structure Mapping Theory-based analogical mapping with multi-objective filtering. The resulting workflow and generated assets also form a dataset/benchmark for future relation-aware 3D model training.
**Purpose (≤3 sentences):** The authors state that current text-to-3D generation pipelines suffer from "creative homogenization" — a tendency to produce visually/structurally similar outputs — and aim to introduce controlled, analogy-driven diversity instead.
**Breakthrough (≤3 sentences):** The authors report that expert evaluations show the framework "substantially enhances creative novelty and visual fascination" compared to baselines, and that it yields a reusable dataset/benchmark for relation-aware 3D model training.
**Tools & method (≤3 sentences):** The method draws on Wikidata, the Getty Art & Architecture Thesaurus, and AskNature as knowledge sources for attribute and relation inference, combined with LLM-based reasoning and Structure Mapping Theory for analogical mapping; evaluation used custom expert assessments of 5–10 relations per source asset. No hardware specifications are mentioned.
**Limitation (≤3 sentences):** The paper does not include a dedicated limitations section; in the Future Work discussion the authors note a need "to establish robust evaluation metrics specifically designed to quantify generative creativity," implying current evaluation is preliminary rather than standardized.

## Lollypop: Camera-to-Motion-Capture Calibration Verification with a Reference Target
- **arXiv:** 2610.04785 · https://arxiv.org/abs/2610.04785
- **Submitted:** 2026-10-03
- **Authors:** Tianyi Liu, Kevin Harris, Mihika Dave, Kun He
- **Qualifying affiliation(s):** Meta — Tianyi Liu, Kevin Harris, Mihika Dave, Kun He (all four authors, Meta, Redmond, WA, USA)
- **Categories:** cs.CV
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces Lollypop, a fiducial-mocap reference target that independently verifies camera-to-motion-capture (mocap) calibration. The target couples an ArUco fiducial with a mocap marker constellation so that the visual center and tracked centroid represent the same physical point; verification projects the mocap point into the image and measures disagreement with the detected fiducial center. Experiments show sub-pixel nominal error, sensitivity to controlled extrinsic perturbations, and increasing error during an illustrative mixed-handling sequence.
**Purpose (≤3 sentences):** The authors state that camera-to-mocap calibration is essential for using mocap as ground truth in robotics, AR/VR, and other computer vision tasks, but that calibration can drift after deployment while existing residual checks and visual inspection provide only limited independent verification.
**Breakthrough (≤3 sentences):** The authors report that their target achieves sub-pixel nominal accuracy, demonstrates measurable sensitivity to controlled extrinsic perturbations, and detects increasing error during a representative handling/drift scenario — providing an independent check beyond standard calibration residuals.
**Tools & method (≤3 sentences):** The verification procedure compares ArUco-detected fiducial corners (via 2D homography-warped canonical center) against a mocap-derived centroid projected through the full mocap-pose/camera-extrinsic/intrinsic transformation chain, reporting both 2D pixel-space and 3D metric-space error. Hardware used includes a Meta Quest 3 headset (four fisheye cameras) and a 36-camera OptiTrack Prime 41 mocap system, with a carbon-fiber target plate carrying a printed ArUco marker and six retroreflective marker stickers (0.12 mm tape thickness); no public datasets were used, only in-house recordings.
**Limitation (≤3 sentences):** The paper has no dedicated limitations section, but the authors note in their conclusion that "future work includes multi-point or non-coplanar reference targets and stronger depth observability," implying the current single coplanar target has limited depth-error sensitivity.

## Neuroll: Real-Time Neural Strand-Based Hair Simulation via Simulator-in-the-Loop Unrolling
- **arXiv:** 2610.04689 · https://arxiv.org/abs/2610.04689
- **Submitted:** 2026-10-03
- **Authors:** Gene Wei-Chin Lin, Jessica Jia-En Lee, Yu Ju (Edwin) Chen, Egor Larionov, Tuur Stuyck
- **Qualifying affiliation(s):** Meta — Gene Wei-Chin Lin, Jessica Jia-En Lee, Yu Ju (Edwin) Chen, Egor Larionov (Meta Reality Labs); NVIDIA — Tuur Stuyck
- **Categories:** cs.GR
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents Neuroll, a neural time integrator for strand-based hair simulation designed to mirror the input-output formulation of classical time integrators (previous hair states, material stiffness, collision geometry). It is trained via a self-supervised, simulator-in-the-loop method with randomized unrolling horizons, and by operating in each strand's local coordinate frame it generalizes across hairstyle, material property, body motion, and body type. The resulting strand-based neural simulator is density-independent, lightweight, memory-efficient, and real-time performant, suitable for gaming and virtual avatars.
**Purpose (≤3 sentences):** The authors state that optimized classical time integration can simulate thousands of hair strands in real time but is still too computationally demanding for commodity hardware, while existing learning-based alternatives tend to produce less physically plausible motion and often fail to generalize to out-of-distribution scenarios.
**Breakthrough (≤3 sentences):** The authors report stable long-horizon rollouts with linear per-strand scaling and real-time performance: total inference time for 3,000 strands is 0.460 ms (0.273 ms body-field autoencoder + 0.187 ms neural integrator) on an NVIDIA RTX 4080 Laptop GPU, and the method naturally extends to quasi-static simulation by resetting hair states.
**Tools & method (≤3 sentences):** Training used grooms from the CT2Hair dataset plus synthetic artist-created hairstyles; generalization testing used 4 selected grooms (straight to curly, including ponytails) and 6 motion sequences (13,161 frames) of indoor/outdoor activity. The network comprises a 2-layer MLP neural integrator (hidden dim 512, 1.63 MB) and a 2-layer MLP body autoencoder (hidden dim 256, 0.87 MB), run on an Intel Core i7 CPU with NVIDIA RTX 4080 Laptop GPU.
**Limitation (≤3 sentences):** The authors report the integrator "consistently under-predicts motion magnitude, reaching a motion ratio of 0.622 against the reference simulation," and that long hairstyles are harder to handle because training starts from a draped configuration and the body-field coverage is restricted to the head/shoulder region; self-collisions and friction are omitted, the former because modeling them would forfeit the per-strand independence underlying the method's linear scaling.

## Sparse-View 4D Gaussian Splatting via Spatiotemporal Priors and Generative Assistance
- **arXiv:** 2610.04606 · https://arxiv.org/abs/2610.04606
- **Submitted:** 2026-10-03
- **Authors:** Shengqi Wang, Zhengxian Yang, Kaiwen Tian, Yang Liu, Bowen Liu, Hua Du, Taicheng Huang, Jiamin Wu, Tao Yu
- **Qualifying affiliation(s):** JD.com — Yang Liu, Taicheng Huang (FLAG: borderline)
- **Categories:** cs.CV
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents a 4D Gaussian Splatting framework built for the Sparse-View Track of the SIGGRAPH Asia 2026 Volumetric Video Challenge, which requires dynamic scene reconstruction from only six wide-baseline cameras. The framework combines region-adaptive spatial priors (foreground masks, mask-voting densification, monocular-depth-regularized background), motion-consistent temporal priors (frame interpolation and optical-flow-constrained Gaussian motion), and generative assistance (diffusion-based restoration of virtual-camera renders used as pseudo-supervision).
**Purpose (≤3 sentences):** The authors state the goal is robust dynamic scene reconstruction under extremely sparse, wide-baseline camera setups (six cameras), where standard dense-view 4D Gaussian Splatting methods are not applicable.
**Breakthrough (≤3 sentences):** The authors report improving full-frame PSNR from a 25.60 dB baseline to 29.75 dB on the validation set, and achieving 30.04 dB full-frame PSNR / 27.88 dB foreground PSNR on the official test benchmark, ranking first overall in the Sparse-View Track of the SIGGRAPH Asia 2026 Volumetric Video Challenge.
**Tools & method (≤3 sentences):** The pipeline uses YOLO11 and SAM 2 for foreground masks, RoMa for point correspondences, Depth Anything V2 for monocular depth, RIFE for frame interpolation, VideoFlow for optical flow, and an "ArtiFixer" diffusion model for virtual-view restoration; training/evaluation used the official SIGGRAPH Asia 2026 Volumetric Video Challenge data (six training cameras, eight held-out test cameras) on a single NVIDIA RTX 3090 GPU.
**Limitation (≤3 sentences):** The paper states in its Conclusion and Future Work that "future work will focus on reducing reconstruction time and model size to support real-time applications on standalone VR headsets," implying the current method is not yet real-time or lightweight enough for standalone VR deployment.

## CurveCodec 2: Skeleton-agnostic animation compression with a learned entropy model
- **arXiv:** 2610.04211 · https://arxiv.org/abs/2610.04211
- **Submitted:** 2026-10-03
- **Authors:** Mingyi Shi, Huancheng Lin, Xuelin Chen, Taku Komura
- **Qualifying affiliation(s):** Adobe Research — Xuelin Chen
- **Categories:** cs.GR; cs.AI; cs.RO
- **Open release:** demo/project page (https://rubbly.cn/publications/curvecodec/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents CurveCodec 2, a skeleton-agnostic skeletal-motion compression codec that asks which part of a production codec a learned model should take over, building on the authors' earlier CurveCodec. It codes every sub-track as a quantized curve in the log map (thinned to rate-distortion-selected keyframes via closed-loop per-joint sampling) and entropy-codes residuals under a small learned model with bit-exact integer inference across platforms. Two verified contracts are enforced on every decoded clip: ACL's own worst-case-per-joint tolerance, or ACL's mean-error-per-clip tolerance.
**Purpose (≤3 sentences):** The authors state that skeletal animation is stored as every joint's transform at every frame even though most of it is implied by the body, and that a production codec must guarantee a stated error bound for any skeleton; their earlier CurveCodec matched ACL's mean error but not its worst case, and measured payload in floats rather than bits, motivating this follow-up that targets bit-rate and worst-case guarantees.
**Breakthrough (≤3 sentences):** On a held-out test set of 4,472 clips from 33 datasets, the authors report CurveCodec 2 needs 0.37x of ACL's bytes at ACL's default precision of 0.01 cm under the worst-case contract, and 0.22x at 0.1 cm under the mean contract, while decoding on a single CPU core and transferring without retraining to a species absent from training data.
**Tools & method (≤3 sentences):** The method predicts each quantized curve from its own past, selects per-joint sampling in closed loop through the skeletal hierarchy, and uses a small learned entropy model for residual coding (with bit-exact integer inference); the authors found a nearest-neighbour oracle over millions of training samples performed no better than linear interpolation and that none of the learned in-betweeners tried "paid for itself." Evaluation used 4,472 held-out clips across 33 motion datasets, benchmarked against ACL, the production animation-compression library used in modern game engines.
**Limitation (≤3 sentences):** The paper does not present a dedicated limitations section in the portion reviewed; the authors do note that learned in-betweening approaches they tried failed to outperform simple interpolation baselines on the gaps their encoder leaves, implying the gains come specifically from residual/curve prediction and per-joint sampling rather than from generative in-betweening.

## SUAVE: Unified Video-Action Models via Masked Diffusion
- **arXiv:** 2610.04009 · https://arxiv.org/abs/2610.04009
- **Submitted:** 2026-10-02
- **Authors:** Rhythm Syed, Jean Mercat, Sedrick Keh, Kushal Arora, Paarth Shah, Aykut Onol, Mengchao Zhang, Tony Dear
- **Qualifying affiliation(s):** Toyota Research Institute — Jean Mercat, Sedrick Keh, Kushal Arora, Paarth Shah, Aykut Onol, Mengchao Zhang (and Rhythm Syed, dual-affiliated with Columbia University and Toyota Research Institute) (FLAG: borderline)
- **Categories:** cs.RO; cs.CV; cs.LG
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents SUAVE, a unified video-action model in which a masked diffusion transformer generates video and robot actions conditioned on language, with all three modalities represented as discrete tokens in one shared sequence. Choosing which tokens to mask at inference lets the same network act as a world model, a robot policy, or a video-action model, and unlabeled video can be co-trained by masking and excluding action positions from the loss. The authors report the approach is competitive with dedicated world models and specialized action policies on manipulation tasks, including real-robot deployment.
**Purpose (≤3 sentences):** The authors state that vision-language-action models are typically optimized to predict actions without imagining future observations, while world-action models built on video diffusion can imagine the future but treat language as frozen conditioning, and unified approaches so far either decode autoregressively token-by-token or bolt an auxiliary action head onto continuous video — motivating a single shared-token architecture for both.
**Breakthrough (≤3 sentences):** The authors report that a single SUAVE model predicts long-horizon video and acts as a policy competitively with dedicated world models/specialized policies on static and dynamic manipulation tasks, and that on a real robot it generates subgoal images plus a one-second action chunk in 1,030 ms on an RTX 5090 GPU, sustaining closed-loop control at 2.5 actions per second; pretraining on robot video plus co-training on human video substantially improves policy performance and zero-shot robustness to distribution shift.
**Tools & method (≤3 sentences):** The 32-layer transformer is initialized from MMaDA-8B with block-causal attention, using LLaDA for text tokens, MAGViT-v2 for video tokens (256 tokens per 256×256 frame), and uniform binning (256 bins/dimension) for action tokens, trained with masked diffusion (independent mask rates per modality, cosine corruption schedule) and 4-step denoising inference with prefix KV caching. Data includes DROID and embodiment-specific robot video, Something-Something v2 for action-free human video co-training, and evaluation on LIBERO, LIBERO-Plus, DOMINO plus three custom real-robot tasks using an xArm7 manipulator with wrist and over-shoulder RealSense cameras.
**Limitation (≤3 sentences):** The authors state that co-training yields higher task scores than pretraining alone but the difference "is not statistically separable" at their scale, that the frozen MAGViT-v2 tokenizer bounds reconstruction quality of predicted frames, and that fixed-length token sequences prevent the model from adapting its horizon to the task; evaluation also covers only a single 7-DoF arm embodiment, and the model does not generate or evaluate language despite its text-based backbone.

## SCCM: Spherically Consistent Coarse Matching for ERP Dense Feature Correspondence
- **arXiv:** 2609.36545 · https://arxiv.org/abs/2609.36545
- **Submitted:** 2026-09-29
- **Authors:** Gyeonggwan Lee, Eunsoo Im, Seunghwan Hong, Junghun Suh
- **Qualifying affiliation(s):** Kakao Mobility Corp. — Gyeonggwan Lee, Eunsoo Im, Seunghwan Hong, Junghun Suh (FLAG: borderline)
- **Categories:** cs.CV
- **Open release:** code (https://github.com/gandanlee/sccm) | demo/project page (https://gandanlee.github.io/sccm/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses dense feature matching between 360° panoramas stored in equirectangular projection (ERP), which introduces three distortions — a longitudinal seam (topology), latitude-dependent stretch (metric), and non-uniform pixel area (area) — not modeled by perspective-trained dense matchers. SCCM (Spherically Consistent Coarse Matching) augments a chart-naive cross-attention/dual-softmax coarse matcher with two sphere-derived priors: Spherical Positional Attention (yaw-periodic RoPE plus tangent-plane bias) and Area-Aware Covisibility (pre-sigmoid log-area correction), leaving the refiner architecture unchanged.
**Purpose (≤3 sentences):** The authors state that dense feature matching between 360° panoramas underpins omnidirectional pose estimation, 3D reconstruction, and SLAM, but that the coarse stage of perspective-trained dense matchers does not model ERP-specific distortions, causing systematic degradation on panoramic imagery.
**Breakthrough (≤3 sentences):** The authors report that correcting the three distortions at the coarse-stage interfaces improves PCK@1° from 0.230 to 0.275 on Matterport3D under a fixed coarse scaffold with the refiner architecture unchanged, and that instantiated in the RoMa V1 framework, SCCM also outperforms the ERP-native EDM (0.163) and an ERP-retrained RoMa V1 (0.198), while transferring zero-shot to Stanford2D3D and leading on outdoor Holo360D when trained there.
**Tools & method (≤3 sentences):** The method uses a frozen DINOv2-Large encoder with a RoMa V1 ConvRefiner, adding Spherical Positional Attention and Area-Aware Covisibility at the coarse-matching stage; evaluation covers Matterport3D (primary), Stanford2D3D (zero-shot transfer), Holo360D (outdoor LiDAR-captured trajectories), and Mapillary Metropolis (street-level transfer), with inference latency measured on an RTX 4090 GPU at 448×896 resolution (~5% overhead with caching, ~1.2% FLOP increase).
**Limitation (≤3 sentences):** The authors report the method assumes upright ERP alignment and is "not tilt-equivariant" — accuracy drops sharply under synthetic off-gravity pitch rotations (PCK@1° falls to 0.034 at a 30° tilt versus 0.273 upright) — and state a natively tilt-equivariant matcher remains future work; it also shares perspective matchers' generic failure modes in texture-less, reflective/HDR, low-overlap, and depth-discontinuity regions, which the authors say require upstream changes such as a stronger encoder or occlusion handling.

# Near-misses
- 2610.05289 · Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting · no industry author (all affiliations academic: University of Technology Sydney, Yale University, City University of Macau, Australian National University, Adelaide University)
- 2610.04351 · LoCoSplat: Real-Time Feed-Forward 3D Gaussian Splatting with Minimal 3D Reasoning · no industry author (all affiliations academic: Georgia Institute of Technology)
- 2610.04336 · A differentiable Lagrangian-coupled 3D Gaussian Splatting-SPH model for forward simulation and inverse analysis in solid mechanics · no industry author (all affiliations academic: Hong Kong University of Science and Technology); also borderline off-topic (solid-mechanics inverse analysis rather than core 3D/animation/world-model/engine focus)
