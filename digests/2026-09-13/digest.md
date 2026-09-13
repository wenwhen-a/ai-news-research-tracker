# Part A — Papers
Window: last 30 days (2026-08-14 to 2026-09-13). Categories: cs.GR, cs.CV, cs.LG, cs.AI, cs.RO. Retrieval: website fallback (arXiv API returned HTTP 429 on every query; exact-phrase searches on arxiv.org across 42 topic phrases, 895 candidates, affiliation pre-screen on arxiv.org/html, then per-paper verification). Qualifying papers: 68 (22 flagged).

---
## Decoupled Self-Forcing Distillation for Streaming Talking Head Generation
- **arXiv:** 2609.10317 · https://arxiv.org/abs/2609.10317
- **Submitted:** 2026-09-09
- **Authors:** Yanru An, Ruiyan Wang, Wenwu Wei, Rui Bu, Qi Wang, Hongwei Hu, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang
- **Qualifying affiliation(s):** Ant Group — Rui Bu (others: Shanghai Jiao Tong University); FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A streaming talking-head generator that fuses audio in a low-dimensional, identity-disentangled motion space rather than at the pixel level; a small causal autoregressive transformer produces motion latents that a pretrained diffusion renderer turns into video.
**Purpose (≤3 sentences):** Real-time, low-latency audio-driven talking-head video without quality loss, and mitigation of exposure bias in autoregressive streaming.
**Breakthrough (≤3 sentences):** The authors report 15.4 FPS at 1.3 s latency "with no quality degradation," with a motion generator of only 77M parameters.
**Tools & method (≤3 sentences):** "Decoupled self-forcing distillation" from a frozen bidirectional teacher into a block-causal renderer; MEAD and Hallo3 data; X-NeMo, umT5-base, wav2vec2-base and Qwen2.5-VL-7B components; trained on 4 A100 GPUs, evaluated on one H200.
**Limitation (≤3 sentences):** The authors note slightly higher first-frame latency than AvatarForcing and that visual quality is capped by the renderer backbone.

---
## DUET-DINO: Simultaneous Cross-View World Modeling for Latent Planning in Robot Manipulation
- **arXiv:** 2609.10506 · https://arxiv.org/abs/2609.10506
- **Submitted:** 2026-09-09
- **Authors:** Nisarga Nilavadi, Ralf Römer, Moritz Reuss, Michael Krawez, Tobias Jülg, Angela P. Schoellig, Rudolf Lioutikov, Wolfram Burgard
- **Qualifying affiliation(s):** NVIDIA — Moritz Reuss (also Intuitive Robots Lab, KIT)
- **Categories:** cs.RO, cs.CV
- **Open release:** code planned (the paper states "the code and model checkpoints will be open-sourced"; project page https://utn-air.github.io/DUET-DINO)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A dual-view latent world model for robot manipulation that fuses side-view and wrist-camera observations through cross-view attention and extends latent planning to a full 7-DoF end-effector action space.
**Purpose (≤3 sentences):** Single-view latent world models struggle to predict the fine translational, rotational and gripper-state changes needed for 7-DoF control.
**Breakthrough (≤3 sentences):** The authors report that DINOv3 captures action-conditioned visual dynamics better than V-JEPA 2, and that their normalised dual-view cost optimisation reaches 92% reach success, 72.5% angled-reach success and 60% lift-to-home success.
**Tools & method (≤3 sentences):** Cross-view conditioned latent prediction with CEM planning; trained on DROID (62,877 trajectories) and RoboArena (5,856 trajectories); evaluated in the RoboLab simulator and on a Franka Research 3 with two ZED cameras.
**Limitation (≤3 sentences):** The authors state CEM planning "limits real-time control" because of its computational cost and suggest vision-language-action models to accelerate planning.

---
## OmniPoint: Universal Monocular Metric Pointcloud from Any Camera
- **arXiv:** 2609.09394 · https://arxiv.org/abs/2609.09394
- **Submitted:** 2026-09-08
- **Authors:** Botao Ye, Marc Pollefeys, Ming-Hsuan Yang, Abhijit Kundu
- **Qualifying affiliation(s):** Google DeepMind — Botao Ye (intern), Ming-Hsuan Yang, Abhijit Kundu
- **Categories:** cs.CV
- **Open release:** none (project page lists paper and poster only)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** OmniPoint predicts metric 3D point clouds from a single image for pinhole, fisheye or panoramic cameras, using a representation that decouples projection geometry from scene structure.
**Purpose (≤3 sentences):** Existing monocular metric-depth methods are tied to a fixed camera model; the work aims to generalise metric point-cloud estimation across camera types without per-camera retraining.
**Breakthrough (≤3 sentences):** The authors report a "ray direction and radial distance" representation that lets one distance predictor serve pinhole, fisheye and panoramic inputs, trained on 29 labelled datasets plus 2 unlabelled panoramic datasets with a bidirectional augmentation that converts between pinhole and wide-angle views.
**Tools & method (≤3 sentences):** DINOv2 ViT-Large backbone; trained on 72 A100 GPUs; labelled and unlabelled panoramic data with synthetic camera-conversion augmentation.
**Limitation (≤3 sentences):** No code, weights or demo are released, limiting independent verification of the reported cross-camera generalisation (observed, not stated).

---
## GSComplete: Gaussian Splat Completion with 2D Diffusion Priors
- **arXiv:** 2609.08449 · https://arxiv.org/abs/2609.08449
- **Submitted:** 2026-09-08
- **Authors:** Elias Brugger, Philipp Erler, Stefan Ohrhallinger, Paul Guerrero
- **Qualifying affiliation(s):** Adobe — Paul Guerrero (Adobe Research, United Kingdom)
- **Categories:** cs.CV
- **Open release:** none (paper states code/dataset "will be made available upon acceptance")
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GSComplete completes partial 3D Gaussian-splat objects and scenes by adding new Gaussians in missing regions, guided by 2D diffusion priors through score distillation sampling (SDS) and a text prompt.
**Purpose (≤3 sentences):** It targets incomplete Gaussian-splat reconstructions (limited viewpoints, occlusions, single-view captures, LiDAR) that leave geometric holes, aiming for a complete representation while keeping the originally observed content unchanged.
**Breakthrough (≤3 sentences):** The authors report an "input preservation loss" that keeps original splats visible from designated viewpoints while about 5,000 new splats fill gaps, and report better input preservation than MVDream, Trellis, InstantMesh and TripoSG with competitive CLIP-based plausibility scores. They introduce the SplatComplete benchmark of 39 partial Gaussian-splat objects.
**Tools & method (≤3 sentences):** SDS with 2D diffusion priors over 6,000 optimisation steps; 5,000 new splats initialised spherically around the bounding box with a warm-up phase; evaluated on SplatComplete (multi-view captures, single-view reconstructions, LiDAR scans, synthetic meshes).
**Limitation (≤3 sentences):** Code and dataset are not yet public (observed, not stated); the paper's own limitations section was not captured by the fetch.

---
## Flow3D-OPD: Multi-Teacher On-Policy Distillation for 3D Geometry Generation with Flow-Matching Diffusion Transformer
- **arXiv:** 2609.07137 · https://arxiv.org/abs/2609.07137
- **Submitted:** 2026-09-07
- **Authors:** Zhiwei Ning, Zhen Zhou, Puhua Jiang, Xintong Han, Gengming Zhang, Jie Yang, Zhonglong Zheng, Yuanjie Zheng, Wei Liu, Chunchao Guo
- **Qualifying affiliation(s):** Tencent (Tencent Hunyuan3D) — Zhiwei Ning, Zhen Zhou, Puhua Jiang, Xintong Han, Chunchao Guo
- **Categories:** cs.CV, cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A two-stage post-training framework for image-to-3D flow-matching diffusion transformers that applies multi-teacher on-policy distillation to improve mesh geometry quality after pretraining.
**Purpose (≤3 sentences):** It addresses the difficulty of defining reinforcement-learning rewards for 3D geometric quality and the gradient interference that arises when optimising several heterogeneous quality objectives jointly.
**Breakthrough (≤3 sentences):** The authors first train domain-specialised teachers via direct preference optimisation guided by an agentic verifier, then consolidate them into one student by on-policy distillation with hard task-routing and gradient accumulation; they report the student surpasses every teacher on the average metric (win ratios: Teacher1 47.8%, Teacher2 53.0%, Teacher3 56.9%, Ours 61.0%).
**Tools & method (≤3 sentences):** Flow-matching DiT image-to-3D pipeline with VAE decoding and isosurface extraction; ULIP/Uni3D-based teachers; an agentic verifier as reward model; DPO for teacher training.
**Limitation (≤3 sentences):** No code or weight release is mentioned (observed, not stated); the paper's stated limitations were not captured by the fetch.

---
## Flexible Motion Generation from Language and Style References
- **arXiv:** 2609.08032 · https://arxiv.org/abs/2609.08032
- **Submitted:** 2026-09-07
- **Authors:** Kai Weixian Lan, Bodie Criswell, Briana Fedkiw, Zhan Zhang, Joseph Teran, Daniel Holden
- **Qualifying affiliation(s):** Epic Games — Zhan Zhang, Joseph Teran, Daniel Holden (the first three authors' contributions were made during Epic Games internships)
- **Categories:** cs.CV, cs.GR, cs.LG
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** FlexMoGen generates human motion conditioned jointly on a text prompt (content) and a style-reference motion clip (timing, limb articulation, dynamics), learning a variational style encoder without style labels.
**Purpose (≤3 sentences):** To give users control over both content and style, including long, time-varying multi-style synthesis that label-based methods could not generalise to.
**Breakthrough (≤3 sentences):** The authors report FlexMoGen "achieves the best balance between content fidelity and style reflection" relative to prior methods; accepted at Pacific Graphics 2026.
**Tools & method (≤3 sentences):** Joint pretraining of the style encoder and a text-to-motion latent diffusion model, a lightweight adaptation module and a relative positional encoding; trained on 100STYLE (100 styles, 8 gaits) and an internal MoCap set of 3,089 clips (about 6.4 hours).
**Limitation (≤3 sentences):** The authors report transfer is "hit or miss" for styles outside 100STYLE and that outputs tend to be over-smoothed, suppressing rapid limb movement.

---
## PASTEL: Panoramic Alignment for Monocular 4D Scene Reconstruction
- **arXiv:** 2609.06099 · https://arxiv.org/abs/2609.06099
- **Submitted:** 2026-09-05
- **Authors:** Yuankun Yang, Yi Wei, Bo Bai, Wenyang Zhou, Li Zhang
- **Qualifying affiliation(s):** Huawei (Central Media Technology Institute) — Yi Wei, Bo Bai, Wenyang Zhou; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PASTEL reconstructs 4D scenes from casually captured monocular video by reconstructing visible regions and generatively completing regions outside the camera's view. Its "panoramic scene alignment" reformulates exploration of invisible regions as a 2D directional trajectory problem instead of a 3D search.
**Purpose (≤3 sentences):** Monocular 4D reconstruction leaves large unseen regions unfilled, which limits VR and embodied-AI uses that need full scene coverage.
**Breakthrough (≤3 sentences):** The authors report reducing the search from 6-DoF to a 2D problem with explicit visibility boundaries, and a 0.9 dB PSNR improvement over the prior state of the art on the DyCheck iPhone dataset.
**Tools & method (≤3 sentences):** Monocular depth, pose and flow estimation combined with camera-controlled video-generation priors; evaluated on DyCheck iPhone.
**Limitation (≤3 sentences):** The authors state the method depends on accurate depth/pose/flow estimates and stable video-generation priors, degrades under very large camera motion, and that generated content is sometimes blurrier than covisible regions.

---
## WorldSculpt: Generating Compositional Worlds from Grounded Videos
- **arXiv:** 2609.05416 · https://arxiv.org/abs/2609.05416
- **Submitted:** 2026-09-04
- **Authors:** Muyao Niu, Jixuan He, Ruihan Yu, Lian Fu, Yonghao Yu, Zheng-Hui Huang, Yifan Zhan, Fengbo Lan, Yongtao Ge, Yinqiang Zheng, Kaipeng Zhang, Zhixiang Wang
- **Qualifying affiliation(s):** Alaya Lab (Shanda Group) — Muyao Niu and ten co-authors; FLAG: borderline (an "AI x Gaming" industry lab under Shanda Group, not on the core list)
- **Categories:** cs.CV
- **Open release:** code and weights (https://github.com/AlayaLab/WorldSculpt; Hugging Face checkpoints "AlayaLab/WorldSculpt" and "TencentARC/Pixal3D")
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** WorldSculpt generates compositional 3D scenes made of hundreds of individually separable object meshes from posed multi-view video, by extending the single-object generative prior Pixal3D with a multi-view conditioning pathway.
**Purpose (≤3 sentences):** Prior world-model and scene-reconstruction methods output one fused mesh or Gaussian set that cannot be decomposed into movable objects, which the authors say mismatches needs in gaming, AR/VR, simulation and robotics.
**Breakthrough (≤3 sentences):** The authors report generalisation to large, heavily occluded scenes with hundreds of objects despite fine-tuning only on single canonical objects, and that the method outperforms prior approaches on single-object, controlled multi-object and their new UE-MeshyScene benchmark, with larger gains as scene complexity grows. They also show converting generated 3DGS worlds (Marble, HY-World 2.0) into compositional mesh scenes.
**Tools & method (≤3 sentences):** Pixal3D base model plus multi-view conditioning; UE-MeshyScene benchmark of photorealistic cluttered scenes with per-object annotations and ground-truth meshes.
**Limitation (≤3 sentences):** Generation quality is bounded by the Pixal3D prior (observed, not stated); the paper's stated limitations were not captured by the fetch.

---
## RenderFormer-V2: Neural Rendering with Heterogeneous Scene Primitives
- **arXiv:** 2609.05738 · https://arxiv.org/abs/2609.05738
- **Submitted:** 2026-09-04
- **Authors:** Chong Zeng, Yue Dong, Pieter Peers, Lvmin Zhang, Maneesh Agrawala
- **Qualifying affiliation(s):** Microsoft Research — Yue Dong
- **Categories:** cs.CV, cs.GR, cs.LG
- **Open release:** code and weights (the paper states "The trained RenderFormer-V2 model and code can be found at: https://renderformer.github.io/v2")
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** RenderFormer-V2 is a transformer that renders images from heterogeneous scene primitives (triangles with textures or displacement, voxels, triangular lights, environment maps), handling caustics, volumetric scattering, environment lighting and out-of-distribution materials "without per-scene training or specialized code."
**Purpose (≤3 sentences):** A single learned model covering diverse light-transport effects and primitive types as a complement to physics-based renderers, scaling beyond the 44k-primitive limit of the original RenderFormer.
**Breakthrough (≤3 sentences):** The authors report handling more than 100k primitives; at 64K triangles they report LPIPS 0.0873 versus 0.3070 for RenderFormer, and 0.0999 versus 0.4772 at 128K, with average test-scene PSNR 28.25 / SSIM 0.8982 / LPIPS 0.0997 and about 2 to 3 seconds per frame at 64K primitives on an A100.
**Tools & method (≤3 sentences):** A 207M-parameter two-stage transformer: a 12-layer view-independent stage with sliding-window attention and rendering-informed attention sinks, and a 6-layer view-dependent stage with cross-attention and SWIN windowed attention; BRDF-agnostic neural material embeddings; trained 19 days on 32 A100 GPUs on about 10M sampled scenes (about 70 TB) at 256² to 2048².
**Limitation (≤3 sentences):** The authors state limits of 88 light sources per scene and a fixed 32x32 texture resolution per triangle, no explicit temporal coherence, and that adding a new primitive type "typically requires significant retraining."

---
## Learning 3D Editing without Paired Supervision via Generative Prior Distillation
- **arXiv:** 2609.04942 · https://arxiv.org/abs/2609.04942
- **Submitted:** 2026-09-04
- **Authors:** Hao Wen, Weibin Yun, Hongxing Fan, Haotian Lu, Rui Chen, Zehuan Huang, Lu Sheng
- **Qualifying affiliation(s):** VAST — Zehuan Huang; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** code (https://github.com/thiamine128/PriorEdit3D)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PriorEdit3D is a feed-forward instruction-guided 3D editing framework built on the UniLat3D geometry-appearance latent that learns without paired 3D before/after data, distilling visual priors from 2D image-editing models and semantic priors from vision-language models, with a 3D-aware distribution-matching regulariser.
**Purpose (≤3 sentences):** It addresses the scarcity of paired 3D editing training data.
**Breakthrough (≤3 sentences):** The authors report the best scores among compared methods (EditP23, Instant3DiT, 3DEditFormer, VoxHammer, Nano3D): PSNR 24.37, SSIM 0.94, FID 71.96, LLM-Identity 93.13%, LLM-Instruction 86.92%, at a reported 7-second runtime.
**Tools & method (≤3 sentences):** UniLat3D prior with differentiable rendering; Qwen3-VL-4B for semantic feedback; Qwen-Image-Edit-2511-Lightning for 2D edits; Gemini3-Flash for instruction generation; trained on Objaverse (73,451 objects); evaluated on a 130-sample set plus Amazon Berkeley Objects and Google Scanned Objects.
**Limitation (≤3 sentences):** The authors state it struggles with fine-grained edits such as text and small dense instances, non-edited regions may drift, and the UniLat3D prior makes large pose or topology changes difficult.

---
## GradRig: Differentiable Weights for Skinned Gaussian Splat Deformation
- **arXiv:** 2609.05127 · https://arxiv.org/abs/2609.05127
- **Submitted:** 2026-09-04
- **Authors:** Nina Vesseron, Élie Michel
- **Qualifying affiliation(s):** Adobe — Nina Vesseron (also ENSAE-CREST), Élie Michel
- **Categories:** cs.GR
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GradRig deforms 3D Gaussian splats with skinning by using spatial gradients of skinning weights, since splats lack mesh connectivity and rigid per-splat transforms open holes when shapes stretch; an optional adaptive resampling splits problematic splats.
**Purpose (≤3 sentences):** Mesh-free rigged deformation of Gaussian-splat representations at real-time rates.
**Breakthrough (≤3 sentences):** The authors report more accurate stretching than rigid-only transformation while keeping real-time rendering, compared against RigAnything (Liu et al., 2025).
**Tools & method (≤3 sentences):** Skinning-weight gradients plus adaptive resampling; scenes from 85K to 850K splats; benchmarked on an Apple M1 Max (32 GB) in a WebGL viewer.
**Limitation (≤3 sentences):** The authors state that storing weight gradients adds memory overhead, that linear interpolation does not improve their dictionary lookup, and that resampling applies to the rest shape rather than the deformed shape.

---
## WorldReward: Reward Modeling for Camera-Conditioned World Models
- **arXiv:** 2609.03952 · https://arxiv.org/abs/2609.03952
- **Submitted:** 2026-09-03
- **Authors:** Yibin Wang, Zehan Wang, Junshu Tang, Zhimin Li, Yujie Zhou, Jiazi Bu, Pengyang Ling, Feng Han, Zhixiong Zhang, Long Xing, Shengyuan Ding, Ziang Li, Cheng Jin, Yuhang Zang, Jiaqi Wang, Tianyu Pang
- **Qualifying affiliation(s):** Tencent Hunyuan — Zehan Wang, Junshu Tang, Zhimin Li, Tianyu Pang
- **Categories:** cs.CV
- **Open release:** none stated (project page https://codegoat24.github.io/WorldReward)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** WorldReward is a VLM-based pairwise reward model for camera-conditioned world models that splits videos into action-aligned chunks, scores each with structured visual evidence, and aggregates separate action-consistency and visual-quality scores.
**Purpose (≤3 sentences):** To supply a reward signal for reinforcement-learning post-training of camera-conditioned video world models that covers action fidelity and visual quality in one evaluator.
**Breakthrough (≤3 sentences):** The authors describe it as the "first VLM-based pairwise reward model that unifies action-consistency and visual-quality evaluation," report that it improves RL post-training of Tencent's HY-WorldPlay 1.5, and release WorldReward-Bench with 760 human-annotated video pairs.
**Tools & method (≤3 sentences):** Trained on 50,000 reasoning-augmented video pairs from eight world models across 224 trajectories, built through frontier-VLM distillation, agent-assisted auditing and human calibration.
**Limitation (≤3 sentences):** The paper discusses trade-offs between action and visual rewards but states no formal limitations in the retrieved content (observed, not stated).

---
## TileGS: Tile-Local Depth Binning for Gaussian Splatting Rasterization
- **arXiv:** 2609.03613 · https://arxiv.org/abs/2609.03613
- **Submitted:** 2026-09-03
- **Authors:** Wei Tan, Matias Turkulainen, Lauri Ilola, Hamed Rezazadegan Tavakoli, Juho Kannala
- **Qualifying affiliation(s):** Nokia Technologies — Lauri Ilola, Hamed Rezazadegan Tavakoli; FLAG: borderline
- **Categories:** cs.GR
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** TileGS reorganises 3DGS rasterisation into tile-local depth bins rasterised front to back, with selective repair where coarse ordering is insufficient, replacing long globally sorted tile ranges.
**Purpose (≤3 sentences):** Standard 3DGS rasterisation traverses a globally sorted stream that creates long per-tile ranges and heavy geometry-attribute memory traffic, limiting real-time performance.
**Breakthrough (≤3 sentences):** The authors report, across a 9-scene benchmark, a mean 1.44x raster-kernel speedup on an RTX 4090 and end-to-end frame speedups of 1.069x (RTX 4090) and 1.094x (RTX 1000 Ada) over gsplat while matching its output (|ΔPSNR|, |ΔSSIM|, |ΔLPIPS| all below 0.001). Nsight Compute profiling attributes the gain to reduced raster traversal work, with geometry attributes still 85.8% of raster traffic.
**Tools & method (≤3 sentences):** Tile-local depth-binned rasteriser with a "No-GW" default variant; benchmarked against gsplat on RTX 4090 and RTX 1000 Ada with Nsight Compute.
**Limitation (≤3 sentences):** Gains are reported only relative to gsplat on Ada-generation NVIDIA GPUs (observed, not stated).

---
## Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction
- **arXiv:** 2609.04201 · https://arxiv.org/abs/2609.04201
- **Submitted:** 2026-09-03
- **Authors:** Chin-Yang Lin, Yang-Che Sun, Cheng Sun, Fu-En Yang, Min-Hung Chen, Yen-Yu Lin, Wei-Chen Chiu, Yu-Lun Liu
- **Qualifying affiliation(s):** NVIDIA — Cheng Sun, Fu-En Yang, Min-Hung Chen (Chin-Yang Lin dual-affiliated NVIDIA / NYCU)
- **Categories:** cs.CV
- **Open release:** none stated (project page https://linjohnss.github.io/scal3r/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Scal3R reformulates online 3D reconstruction as multi-reference relative pose querying: lightweight learnable tokens (about 1% of parameters) are injected into a frozen CUT3R or STream3R backbone via asymmetric attention to query poses relative to several past keyframes, with an online pose-graph optimiser and loop closure.
**Purpose (≤3 sentences):** The authors observe that online reconstruction models collapse on long videos because regressing poses against a fixed first-frame anchor extrapolates beyond the training distribution, while per-frame depth stays stable.
**Breakthrough (≤3 sentences):** The authors report over 60% lower average ATE on KITTI than the online baseline, state-of-the-art results across Virtual KITTI, Sintel, TUM-Dynamic, ScanNet and 7-Scenes, low drift on kilometre-scale sequences, and convergence in 8 hours on a single NVIDIA A100 using only 4-view training samples. Accepted to ECCV 2026.
**Tools & method (≤3 sentences):** Frozen 24-layer CUT3R/STream3R backbones with DINOv2 encoders; visual-prompt tokens; iSAM2 pose-graph optimisation with loop closure; trained on TartanAir (K=3 references in training, 12 at inference; 40 epochs, AdamW, lr 1e-4).
**Limitation (≤3 sentences):** The authors state performance is bounded by the frozen backbone under occlusion or textureless regions, appearance-based loop closure can miss revisits under extreme viewpoint or illumination change, and keyframe selection and loop detection rely on hand-set thresholds.

---
## SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving
- **arXiv:** 2609.03602 · https://arxiv.org/abs/2609.03602
- **Submitted:** 2026-09-03
- **Authors:** Jinyang Wang, Shiwei Li, Junjian Wang, Zhiqiang Deng, Jianbin Gao, Yihang Zhao, Liu Liu, Yongjia Zhao, Jinlong Chen, Huirui Xu, Yifeng Pan, Kangwei Liu, Fan Ren, Ji Tao, Minghao Yang
- **Qualifying affiliation(s):** Chongqing Changan Technology Co., Ltd. — Junjian Wang, Zhiqiang Deng, Jianbin Gao, Yifeng Pan, Kangwei Liu, Fan Ren, Ji Tao; FLAG: borderline (automaker R&D, comparable to Toyota Research / Wayve)
- **Categories:** cs.CV, cs.RO
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SV-WAM is a surround-view world-action model for end-to-end driving that keeps six-camera context through an action-centred causal mask, co-trains with future-video prediction, and drops the video branch at inference.
**Purpose (≤3 sentences):** Low-latency closed-loop planning that retains the full surround context that front-view-only planners lack.
**Breakthrough (≤3 sentences):** The authors report 91.0 EPDMS on NAVSIMv2 at 342 ms latency, aided by a differentiable drivable-area compliance regulariser.
**Tools & method (≤3 sentences):** Trained on the NAVSIM trainval split on 16 NVIDIA H800 GPUs (about 24 h per stage); evaluated closed-loop on NAVSIMv2 and zero-shot open-loop on nuScenes; inference on one NVIDIA H20 (341.6 ± 2.1 ms).
**Limitation (≤3 sentences):** The authors state the roughly 5B-parameter backbone "remains relatively large for deployment on resource-constrained on-board platforms" and plan distillation, pruning, quantisation and real-vehicle closed-loop tests.

---
## Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations
- **arXiv:** 2609.03657 · https://arxiv.org/abs/2609.03657
- **Submitted:** 2026-09-03
- **Authors:** Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu
- **Qualifying affiliation(s):** Huawei Heisenberg Research Center — Onat Şahin, Mohammad Altillawi, Carlos Carbone, Ziyuan Liu; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Proposes "3D Morphological Perturbations," an optimisation-free regulariser that perturbs each Gaussian's scale, rotation and pruning in 3DGS scenes to create view-consistent corrupted training data, used to inject 3D-aware priors into video diffusion models.
**Purpose (≤3 sentences):** Sparse-view NeRF/3DGS artefacts need generative "fixers" trained on paired corrupted/clean renders, which previously required costly per-scene re-optimisation.
**Breakthrough (≤3 sentences):** The authors report removing per-scene 3DGS optimisation from data curation, and, scaled to a 14B-parameter video model via ControlNet, a 12.5% reduction in mean depth error versus image-to-image 3D artefact refiners and up to 8.0% higher robotics manipulation success on 3 of 4 tasks.
**Tools & method (≤3 sentences):** Per-Gaussian morphological perturbation; a lightweight video-diffusion sandbox plus a 14B video model with ControlNet; downstream robotics manipulation evaluation.
**Limitation (≤3 sentences):** Gains apply to 3 of 4 manipulation tasks (observed, not stated); the paper's stated limitations were not captured by the fetch.

---
## PointGT: Simultaneous Geometry and Texture Editing for Point-Based Representations
- **arXiv:** 2609.03341 · https://arxiv.org/abs/2609.03341
- **Submitted:** 2026-09-03
- **Authors:** Yanshu Zhang, George Shramko, Pratul P. Srinivasan, Ke Li
- **Qualifying affiliation(s):** Google DeepMind — Pratul P. Srinivasan
- **Categories:** cs.CV, cs.GR
- **Open release:** none stated (project page https://zvict.github.io/pointgt/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PointGT is a point-based 3D representation that supports simultaneous editing of geometry and appearance: it extends PAPR with a learned UV mapping from 3D points to a 2D texture atlas, so textures are edited in 2D while non-rigid geometry edits displace points.
**Purpose (≤3 sentences):** The authors state that recent texture-editing methods for 3D Gaussian Splatting "are not compatible with geometry edits and deformations."
**Breakthrough (≤3 sentences):** The authors report novel-view PSNR 33.48 (DTU) and 33.57 (Blender) at 30k points, and on VBench editing metrics subject consistency 0.844 versus 0.827 for GSTex and imaging quality 0.585 (a reported 12.48% improvement over GSTex). Accepted to ECCV 2026.
**Tools & method (≤3 sentences):** Unstructured point cloud with learned features rendered by cross-attention (PAPR); two geometry regularisers (close-to-ray, close-to-surface); deformation-aware correspondence via attention-weighted displacement fusion; evaluated on DTU, Blender synthetic and Mip-NeRF 360 with Objaverse assets.
**Limitation (≤3 sentences):** The authors state the method relies on an optimisation-based UV parameterisation that "can struggle to produce clean and low-distortion charts for objects with complex topology."

---
## Building Pretraining Data for World Models: An Unreal Engine-Based Pipeline for Action-Conditioned Video Generation
- **arXiv:** 2609.03557 · https://arxiv.org/abs/2609.03557
- **Submitted:** 2026-09-03
- **Authors:** Haoyu Wang, Songchun Zhang, Haoran Li, Haoyang Huang, Zeyue Xue, Nan Duan
- **Qualifying affiliation(s):** JD (Joy Future Academy) — Haoyu Wang, Songchun Zhang, Haoyang Huang, Nan Duan; FLAG: borderline (JD.com)
- **Categories:** cs.CV, cs.GR
- **Open release:** none stated (project page https://echo-team-joy-future-academy-jd.github.io/Echo-1.5-Page/wm/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A production pipeline on Unreal Engine that generates synthetic, action-conditioned, multi-view video for training interactive world models, combining physics simulation of character trajectories with offline cinematic rendering.
**Purpose (≤3 sentences):** Large-scale, precisely action-aligned pretraining data for action-conditioned video models, given the scarcity of controllable real-world video.
**Breakthrough (≤3 sentences):** The authors report about 2,691 hours of 1080p and 6,076 hours of 720p five-camera video from 429 curated Unreal Engine levels and 40 characters on a 200-GPU farm (25 nodes of 8 NVIDIA RTX 5090), with non-forward actions making up 46.6% of trajectories.
**Tools & method (≤3 sentences):** Stage I physics simulation for trajectories; Stage II offline rendering through Unreal Engine's Movie Render Queue; asset curation and cache-aware scheduling across 2,384 Fab asset packs.
**Limitation (≤3 sentences):** The authors state the system prioritises controllability and scale over cinematic quality, that actions are limited to locomotion (no jumping, climbing or complex interaction), and that it is infrastructure rather than a new world-model architecture.

---
## VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement
- **arXiv:** 2609.03153 · https://arxiv.org/abs/2609.03153
- **Submitted:** 2026-09-02
- **Authors:** Wenzhuo Xu, Yuchen Zhu, Chongjian Ge, Xuan Shen, Jing Shi, Jason Kuen, Yongxin Chen, Molei Tao, Christopher McComb, Noelia Grande Gutiérrez, Jiuxiang Gu
- **Qualifying affiliation(s):** Adobe Research — Jason Kuen, Jiuxiang Gu
- **Categories:** cs.CV
- **Open release:** none stated (project page https://veriphy-ai.github.io)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** VeriPhy is an agentic physical-verification system that checks generated video against a natural-language prompt: a text-only planner compiles the prompt into typed physical obligations and a statically validated execution plan before any frame is observed.
**Purpose (≤3 sentences):** To evaluate and refine world models by verifying whether generated physics matches what was requested, beyond plausibility scoring.
**Breakthrough (≤3 sentences):** On a 149-clip core with 304 annotated flaws, the authors report VeriPhy identified 228 defects versus 164 for a published question-decomposition evaluator on identical clips and models.
**Tools & method (≤3 sentences):** Qwen3-VL-30B-A3B-Instruct as planner and verifier, SAM 3 for segmentation, TAPNext++ for tracking, FlexSED for audio, Wan 2.2-VACE for generation and MuJoCo for simulation rendered as depth controls; a 1,500-clip benchmark with 2,582 human-annotated flaw records.
**Limitation (≤3 sentences):** The authors state the corpus was labelled by a single annotator without inter-rater metrics, that multi-object interactions such as billiard collisions do not reliably reproduce simulated physics, and that closed-loop refinement is not yet implemented.

---
## SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models
- **arXiv:** 2609.02886 · https://arxiv.org/abs/2609.02886
- **Submitted:** 2026-09-02
- **Authors:** Junchao Huang, Guian Fang, Shengju Qian, Xianghao Kong, Zhuoran Zhao, Wei Huang, Yihua Du, Zixin Zhang, Justin Cui, Yuchao Gu, Yukang Chen, Xinting Hu, Tianyu He, Shaoshuai Shi, Zhuotao Tian, Xin Wang, Mike Zheng Shou, Li Jiang
- **Qualifying affiliation(s):** NVIDIA — Wei Huang, Yuchao Gu, Yukang Chen; Microsoft Research Asia — Tianyu He
- **Categories:** cs.CV
- **Open release:** weights, code and data (https://github.com/Junchao-cs/SolarWM; https://huggingface.co/datasets/junchaoh-cs/SolarWM-Data)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SolarWM is an open foundation for interactive video world models: a reconfigurable data engine (1.43M clips from 10 datasets, about 25.85 TB) plus a backbone-native adaptation framework instantiated as four 5B to 33B models built on Wan2.2, LTX-2.5 and MiniMax-H3.
**Purpose (≤3 sentences):** A reproducible open foundation (data, recipe, weights) for long-horizon interactive world models, addressing inconsistent supervision from naive multi-source mixing.
**Breakthrough (≤3 sentences):** The authors report causal models that sustain real-time interaction over rollouts from minutes to hours despite training on 5-second sequences, via bidirectional adaptation, teacher-forced autoregressive initialisation and distribution-matching distillation.
**Tools & method (≤3 sentences):** A frame-aligned data contract covering observations, metric camera geometry, captions and quality metadata; sources include ABOT-World, DL3DV, MiraData, RealCam-Vid, SpatialVID, Sekai-Game, Sekai-Walking, MIND, MultiCamVideo and OmniWorld.
**Limitation (≤3 sentences):** No explicit limitations section was found in the retrieved content (observed, not stated).

---
## RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation
- **arXiv:** 2609.02847 · https://arxiv.org/abs/2609.02847
- **Submitted:** 2026-09-02
- **Authors:** Xiaolei Lang, Ze Kang, Zehao Huang, Naiyan Wang
- **Qualifying affiliation(s):** Xiaomi EV — Xiaolei Lang, Zehao Huang, Naiyan Wang; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none (project page https://jerry-locker.github.io/roge/, no code stated)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** RoGe fuses implicit 3D reconstruction and video-diffusion generation end to end for novel view synthesis: from a few posed images and a camera trajectory it produces a temporally coherent fly-through video without an explicit 3D intermediate.
**Purpose (≤3 sentences):** Hybrid reconstruction-plus-generation methods pass lossy rendered images or explicit 3D through to generation and give reconstruction no corrective signal back; RoGe removes that bridge.
**Breakthrough (≤3 sentences):** The authors report that on DL3DV, RoGe outperforms reconstruction-based, generation-based and hybrid baselines on image metrics and video temporal consistency, with ablations showing ray-queried implicit features beat raw reconstruction tokens and rendered RGB as conditioning.
**Tools & method (≤3 sentences):** A feed-forward reconstruction model builds an implicit scene representation; target camera rays query it for per-view features injected into a video diffusion model; both are trained jointly on DL3DV.
**Limitation (≤3 sentences):** Evaluation is restricted to DL3DV and the compute cost of joint training is not discussed (observed, not stated).

---
## H3-World: Turning Language Understanding into World Control
- **arXiv:** 2609.01560 · https://arxiv.org/abs/2609.01560
- **Submitted:** 2026-09-01
- **Authors:** Danze Chen, Zeqing Wang, Ziyue Lin, Xingyi Yang, Yeying Jin
- **Qualifying affiliation(s):** Tencent — Danze Chen, Zeqing Wang, Yeying Jin (also National University of Singapore)
- **Categories:** cs.CV, cs.AI
- **Open release:** weights and code (https://github.com/Danzer1xxxxChan/H3-World; https://huggingface.co/DANNY621/H3-World)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** H3-World turns the MiniMax-H3 video generator into an interactive world model by using natural language as the control interface for character and camera actions, aligning instructions to video latent intervals with temporal attention routing.
**Purpose (≤3 sentences):** To show that a large pretrained video generator can become a controllable interactive world model without a dedicated action module.
**Breakthrough (≤3 sentences):** The authors report effective character and camera control with only 0.199% trainable parameters (rank-32 LoRA, 10,000 steps).
**Tools & method (≤3 sentences):** 7,872 gameplay clips from ABot-World-Explorer-500h (128 held out), 124 frames per clip at 24 fps and 832x480; LoRA fine-tuning at learning rate 1e-4.
**Limitation (≤3 sentences):** The authors state the work is limited to short-horizon generation, lacks systematic evaluation across action combinations, and does not yet support persistent world state, real-time interaction, planning or policy learning.

---
## ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training
- **arXiv:** 2609.00188 · https://arxiv.org/abs/2609.00188
- **Submitted:** 2026-08-31
- **Authors:** Xionghao Wu, Yijun Yang, Shiyang Zhou, Haoze Sun, Jianhui Liu, Songsong Yu, Jiyao Zhang, Wenbo Li, Bo Wang, Guoqing Ma, Lin Song, Renjie Liao, Shenghe Zheng, Wei Tang, Xiaojuan Qi, Yanwei Li, Yuan Zhang, Zhuotao Tian, Haoyang Huang, Nan Duan
- **Qualifying affiliation(s):** JD (Joy Future Academy, collective byline) — FLAG: borderline (JD.com)
- **Categories:** cs.CV
- **Open release:** code (https://github.com/ZimaBlue-WAM/ZimaBlue; project https://zimablue-wam.github.io/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ZimaBlue trains World Action Models through a three-stage curriculum: causal video pretraining on egocentric video without action labels, multi-embodiment video-action mid-training with a unified action representation, then target-robot post-training with a Slow-Fast dual-system architecture.
**Purpose (≤3 sentences):** To scale world-action-model pretraining on abundant action-free egocentric video for cross-embodiment manipulation.
**Breakthrough (≤3 sentences):** The authors report that scaling pretraining video from 300 to more than 120,000 hours raises zero-shot task success from 36.1% to 77.8%, and that the Slow-Fast design predicts actions at 30 Hz on an RTX 4090.
**Tools & method (≤3 sentences):** A unified 100-dimensional state-action representation; pretraining data including EPIC-KITCHENS, Egocentric-100K, EgoDex, DROID and RoboCOIN; evaluation on real Franka robots and the LIBERO-Plus, RoboTwin 2.0 and RoboCasa365 simulators.
**Limitation (≤3 sentences):** The authors state remaining failures include difficulty advancing from correct intermediate states and local interaction errors such as target displacement or lost contact.

---
## FaceSnap: Real-Time Personalized Lightstage Facial Performance Capture
- **arXiv:** 2608.31033 · https://arxiv.org/abs/2608.31033
- **Submitted:** 2026-08-31
- **Authors:** Rukhshanda Hussain, Noé Artru, Emeline Got, Luiz Gustavo Hafemann, Alexandre Messier, Brandon Dearlove, Rafael M. O. Cruz, Abdallah Dib, Eric Granger
- **Qualifying affiliation(s):** Ubisoft (La Forge) — Emeline Got, Luiz Gustavo Hafemann, Alexandre Messier, Brandon Dearlove, Abdallah Dib
- **Categories:** cs.CV
- **Open release:** none (the Multi4D benchmark is announced)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A two-stage framework that amortises expensive lightstage multi-camera sessions into a reusable personalised model, then tracks facial performance in real time from a single camera at 83 fps, with a personalised residual upscaler recovering subject-specific detail. The authors also introduce Multi4D, a benchmark for topology-invariant 4D facial reconstruction.
**Purpose (≤3 sentences):** Lightstage capture for production digital humans needs costly camera arrays, hours of compute and large storage; the aim is to keep that fidelity while enabling monocular real-time capture after one personalisation step.
**Breakthrough (≤3 sentences):** The authors report 0.92 mm average point-to-surface error at about 12 ms per frame on an NVIDIA RTX A6000 versus 1.24 mm for Topo4D, LPIPS 0.0497 versus 0.0503 (Topo4D) and 0.0698 (fine-tuned ESRGAN), and roughly 5,000x speedup over Topo4D and 25,000x over production pipelines.
**Tools & method (≤3 sentences):** A personalised geometry-and-appearance model optimised once from multi-view capture, then a real-time single-camera tracker and upscaler; data from a 24-camera, 60 fps, 4K lightstage (3 subjects) and Multi4D (6 Multiface subjects, about 7,600 frames, 38 views).
**Limitation (≤3 sentences):** The authors state the dynamic appearance model runs at 512x512 and "may lose fine details such as micro-wrinkles" that offline methods capture.

---
## Can Video World Models Track Unobserved World States?
- **arXiv:** 2608.30692 · https://arxiv.org/abs/2608.30692
- **Submitted:** 2026-08-31
- **Authors:** Joonghyuk Shin, Yicong Hong, Jaesik Park, Xun Huang
- **Qualifying affiliation(s):** Roblox — Yicong Hong, Xun Huang (co-authors at Seoul National University)
- **Categories:** cs.CV
- **Open release:** demo (project page https://joonghyuk.com/stateful-vwm-web/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Studies whether video world models maintain a hidden, unobserved world state rather than only producing plausible frames, using an action-conditioned "Shell Game" task, a visual analogue of S5 permutation-group state tracking that decouples rendering from tracking the underlying state.
**Purpose (≤3 sentences):** To determine which architectures can track unobserved state over long horizons and isolate the mechanism behind success or failure.
**Breakthrough (≤3 sentences):** The authors report that plain Transformers and Mamba fail to extrapolate state tracking beyond training length, while linear attention with negative eigenvalues and test-time training with nonlinear fast weights succeed; they also report the negative-eigenvalue mechanism does not transfer to Memory Maze and Block World, where state must be corrected from observations.
**Tools & method (≤3 sentences):** The Shell Game benchmark plus Memory Maze and Block World, comparing Transformer, Mamba, linear-attention and test-time-training video architectures.
**Limitation (≤3 sentences):** The authors state a real world model "has to correct its state from observations, keep it fixed when an action fails, and keep it evolving even when no action arrives," and that some prediction problems "plausibly require NC¹-hard state tracking," which none of the tested architectures capture.

---
## CAER: Causal Action Effect Reweighting for World Model Training
- **arXiv:** 2608.30897 · https://arxiv.org/abs/2608.30897
- **Submitted:** 2026-08-31
- **Authors:** Jianjie Fang, Xvyuan Liu, Ziyou Wang, Rongze Tang, Zhaolu Wang, Zhuohang Li, Xin Zhang, Haisheng Su, Chen Gao, Wei Wu, Xinlei Chen, Yong Li
- **Qualifying affiliation(s):** Manifold AI — Xin Zhang, Haisheng Su, Wei Wu; FLAG: borderline (company tier unclear)
- **Categories:** cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** CAER reweights the training loss of action-conditioned video world models toward action-responsive tokens, since a uniform space-time MSE lets static background dominate gradients while sparse interaction dynamics stay under-optimised.
**Purpose (≤3 sentences):** To focus supervision on tokens causally affected by actions.
**Breakthrough (≤3 sentences):** The authors report consistent improvements across heterogeneous action-conditioned tasks, an online method to identify action-responsive tokens without external annotation, and a theoretical analysis of when focused reweighting beats uniform averaging.
**Tools & method (≤3 sentences):** Wan 2.2 5B backbone trained on eight NVIDIA H20 GPUs; evaluated on LIBERO, RoboTwin 2.0, RealEstate10K and PoseAnything.
**Limitation (≤3 sentences):** The authors note sensitivity to hyperparameters (about 10% action dropout, fixed noise level 0.50) and open questions about scaling to longer horizons and larger models.

---
## BLARM: Animating 3D Objects from Video via Blending Latent Rigid Motion Primitives
- **arXiv:** 2608.31113 · https://arxiv.org/abs/2608.31113
- **Submitted:** 2026-08-31
- **Authors:** Pradyumn Goyal, Yizhak Ben-Shabat, Hsueh-Ti Derek Liu, Haomiao Jiang, Snehasish Mukherjee, Kyle Spence, Mark Stauber, Evangelos Kalogerakis, Yunze Zeng
- **Qualifying affiliation(s):** Roblox — Yizhak Ben-Shabat, Hsueh-Ti Derek Liu, Haomiao Jiang, Snehasish Mukherjee, Kyle Spence, Mark Stauber, Yunze Zeng (Pradyumn Goyal as a Roblox intern)
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A feed-forward method that animates a static 3D mesh from monocular video, predicting a temporally coherent animated mesh without skeletons, cages or manual rigs, by representing motion as a compact set of learned time-varying rigid primitives blended with time-invariant per-vertex skinning weights.
**Purpose (≤3 sentences):** Automatic animation of arbitrary 3D objects from a single video, replacing manual rigging or dense per-vertex prediction.
**Breakthrough (≤3 sentences):** The authors report the best results on ActionBench (CD-3D 1.71, CD-4D 3.07, CD-Motion 7.15, FVD 426.72 versus baseline ranges 2.49 to 3.30 / 5.01 to 5.61 / 9.24 to 11.12 / 787 to 1270) and Motion80, with the fastest inference among compared methods (3.13 s per 16-frame video).
**Tools & method (≤3 sentences):** A transformer combining geometry-conditioned deformation latents with video features via factorised spatial-temporal attention; trajectory reconstruction loss, entropy regularisation for sparse skinning and motion-aware contrastive learning; about 10,000 Objaverse shapes rendered at 512x512, trained on 8 NVIDIA H200 GPUs for about 1.5 days.
**Limitation (≤3 sentences):** The authors acknowledge incorrect vertex-to-component assignment and "part entanglement" when nearby regions look alike but should move independently, and that the mesh topology must suit the target motion.

---
## ECHO: Dyadic 3D Facial Motion Generation with Asymmetric Deterministic Articulation and Stochastic Reaction
- **arXiv:** 2609.05506 · https://arxiv.org/abs/2609.05506
- **Submitted:** 2026-08-29
- **Authors:** Zhuoqiang Cai, Yujie Sun, Chaoyue Niu, Hongyun Yu, Zhiwen Chen, Chengfei Lv, Fan Wu
- **Qualifying affiliation(s):** Alibaba Group — Hongyun Yu, Zhiwen Chen, Chengfei Lv
- **Categories:** cs.GR, cs.CV, cs.SD
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ECHO generates 3D facial motion for both roles in a two-person conversation from audio alone, treating the speaker's mouth motion as deterministic and the listener's reaction as stochastic, decomposing motion into a stable anchor trajectory plus a stochastic residual with "Motion Memory" regularisation.
**Purpose (≤3 sentences):** Audio-only conversational digital humans that need plausible facial behaviour for both talking and listening.
**Breakthrough (≤3 sentences):** Versus ProbTalk3D the authors report Fréchet distance improving from 7.51 to 2.80 and paired Fréchet distance from 1.61 to 0.59; a user study scored ECHO above UniTalker for lip-sync (3.71 vs 3.03), interaction realism (3.77 vs 2.59) and naturalness (3.82 vs 2.34).
**Tools & method (≤3 sentences):** About 120 hours of speaker-disjoint dyadic video derived from Seamless-Interaction (30 FPS, 54-dim FLAME coefficients); base training about 10 hours on one NVIDIA RTX 4090.
**Limitation (≤3 sentences):** No explicit limitations section was found in the extracted text (observed, not stated).

---
## Non-Uniform Quantisation for 3DGS Compression
- **arXiv:** 2608.28272 · https://arxiv.org/abs/2608.28272
- **Submitted:** 2026-08-28
- **Authors:** Bert Van hauwermeiren, Patrice Rondao Alface, Adrian Munteanu
- **Qualifying affiliation(s):** Nokia — Patrice Rondao Alface; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** An importance-weighted, non-uniform quantisation scheme for 3D Gaussian Splatting compression with weighted merging to remove post-voxelisation redundancy, designed for the standard point-cloud codecs V-PCC and G-PCC.
**Purpose (≤3 sentences):** To cut 3DGS storage while minimising weighted reconstruction error, targeting MPEG standardisation.
**Breakthrough (≤3 sentences):** The authors report BD-Rate gains of -28.27% (MPEG Scenes, V-PCC), -48.08% (MPEG Scenes, G-PCC), -44.17% (MPEG Objects, V-PCC) and -32.95% (MPEG Objects, G-PCC) over PSNR, SSIM, IVSSIM and LPIPS, and state their weighted-merging strategy has been adopted into V-PCC Amendment 1.
**Tools & method (≤3 sentences):** Evaluated on the official MPEG 3DGS common-test-condition datasets on an Intel Core i9-13900 with an NVIDIA RTX 4090.
**Limitation (≤3 sentences):** The authors state preprocessing adds 112 to 116 seconds for large scenes and that the method underperforms FlexGaussian in some G-PCC configurations.

---
## NBS: No Bias Stereo
- **arXiv:** 2608.28933 · https://arxiv.org/abs/2608.28933
- **Submitted:** 2026-08-28
- **Authors:** Vage Taamazyan, Zhuowen Shen, Stefan Hinterstoisser, Alberto Dall'Olio, Agastya Kalra, Aarrushi Shandilya, Xin Li, Wenping Wang, Kartik Venkataraman
- **Qualifying affiliation(s):** Intrinsic (Google) — Vage Taamazyan, Zhuowen Shen, Stefan Hinterstoisser, Alberto Dall'Olio, Agastya Kalra, Aarrushi Shandilya, Kartik Venkataraman (affiliation printed as "Intrinsic (Google)")
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** NBS is a stereo-matching model built as a plain Vision Transformer with no stereo-specific architectural bias (no cost volumes or geometry modules), trained on large-scale synthetic data, framed by the authors as a 3D reconstruction task.
**Purpose (≤3 sentences):** It challenges the assumption that stereo 3D reconstruction needs heavy architectural inductive biases for accuracy and efficiency.
**Breakthrough (≤3 sentences):** The authors report state-of-the-art ETH3D results (EPE 0.09, bad@0.5 of 0.65 on non-occluded pixels) and, on their SimpleProc-S benchmark, about 4x faster runtime (0.060 s vs 0.240 s) and 2.8x lower peak memory (1.23 GB vs 3.52 GB) than S2M2 while roughly halving its bad@4.0 error.
**Tools & method (≤3 sentences):** Standard ViT backbone; trained on 128 A100 GPUs and a final stage on 64 H100 GPUs; an internal ~2.4M-scene synthetic dataset plus 13 public datasets; evaluated on ETH3D, SimpleProc and XYZ-IBD.
**Limitation (≤3 sentences):** The authors state the model predicts only positive disparities, requires fixed input dimensions, and its quadratic-memory ViT prevented native-resolution evaluation on Middlebury and Booster.

---
## SpatialCrafter: Single Image World Modeling with Generative 3D Proxies
- **arXiv:** 2608.27073 · https://arxiv.org/abs/2608.27073
- **Submitted:** 2026-08-27
- **Authors:** Chuan Fang, Lingteng Qiu, Yixun Liang, Rui Chen, Kunming Luo, Zhaohua Zheng, Tongyuan Bai, Feipeng Tian, Zilong Dong, Zihan Zhou, Ping Tan
- **Qualifying affiliation(s):** Alibaba Group (Tongyi Lab) — Lingteng Qiu, Zilong Dong
- **Categories:** cs.CV, cs.RO
- **Open release:** demo (project page https://fangchuan.github.io/SpatialCrafter/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SpatialCrafter turns one image into an explorable 3D scene by generating a global 3D proxy and refining its appearance with a video diffusion model, to reduce hallucination and drift compared with video-diffusion-only methods; the authors also build a 115K-scene dataset with geometric annotations.
**Purpose (≤3 sentences):** Image-to-scene generation for gaming, robotics and VR where video-diffusion methods lack global 3D consistency under large camera motion.
**Breakthrough (≤3 sentences):** At 81-frame generation the authors report FVD 193.54 on SpatialGen-Video (versus 339.04 for ViewCrafter and 525.23 for GEN3C), and on RealEstate10K FVD 148.71 / PSNR 17.185 / SSIM 0.659.
**Tools & method (≤3 sentences):** A Point-anchored Sparse Structure Flow module builds the proxy and a Generative Deferred Refiner handles appearance; 115,295 training pairs from SpatialGen, RealEstate10K and DL3DV; 16 then 32 NVIDIA H20 GPUs.
**Limitation (≤3 sentences):** No explicit limitations section was extracted (observed, not stated).

---
## Revisiting Local Context for Long-Horizon Streaming 3D Reconstruction
- **arXiv:** 2608.27529 · https://arxiv.org/abs/2608.27529
- **Submitted:** 2026-08-27
- **Authors:** Jiarong Han, Jincheng Xiong, Yuzhou Liu, Linzhe Shi, Changjie Wu, Ning Guo, Mu Xu, Hang Zhang, Ming Qian
- **Qualifying affiliation(s):** Alibaba Group (AMAP CV Lab) — all authors
- **Categories:** cs.CV
- **Open release:** code (https://github.com/amap-cvlab/ABot-Recon; project page https://amap-cvlab.github.io/ABot-Recon-html)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ABot-Recon is a streaming 3D reconstruction method that keeps only a 12-frame local temporal window, predicts point maps in the current camera frame plus adjacent-frame relative poses, and recovers global geometry and trajectory by sequential composition.
**Purpose (≤3 sentences):** Camera-motion and geometry estimation from very long video streams under bounded memory and compute, without persistent learned long-range memory.
**Breakthrough (≤3 sentences):** The authors report a 40% reduction in RPE-R and 4.35 m ATE on Oxford Spires (4.02 m with loop closure), the lowest average ATE among streaming methods on KITTI, and dense-reconstruction results of 1.37 m Chamfer / 91.81% F1 on Oxford Spires, 0.06 m / 94.88% on 7Scenes and 0.11 m / 92.19% on TUM-Dynamic, at 24.45 FPS with 6.71 GB GPU memory on an H100.
**Tools & method (≤3 sentences):** A lightweight rotation refiner and composition-aware pose loss; trained on 30 synthetic and real datasets (BlendedMVS, TartanAir, OmniWorld-Game, DL3DV, HyperSim, ScanNet++, ARKitScenes and others) on NVIDIA H20 and AMD MI308 GPUs.
**Limitation (≤3 sentences):** The authors state gains are "less pronounced" on compact indoor benchmarks where persistent context from frequent revisits helps, and leave dynamic scenes and external memory to future work.

---
## R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models
- **arXiv:** 2608.27328 · https://arxiv.org/abs/2608.27328
- **Submitted:** 2026-08-27
- **Authors:** Qiwen Gu, Bingjie Gao, Rui Chen, Geng Li, Jifan Li, Qishuai Wen, Li Niu, Jing Tang, Xiangxiang Chu, Junqiao Zhao
- **Qualifying affiliation(s):** Alibaba Group (DreamX Team) — Rui Chen, Geng Li, Jifan Li, Qishuai Wen, Jing Tang, Xiangxiang Chu
- **Categories:** cs.CV
- **Open release:** code (https://github.com/AMAP-ML/R2MBench)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** R2M-Bench tests whether video world models genuinely remember previously seen scenes rather than merely changing little, by comparing a revisit pair against two same-rollout controls (a gap-matched non-revisit pair and a short-range pair).
**Purpose (≤3 sentences):** The authors note that "high similarity between first-visit and return frames does not necessarily show that a video world model remembered the scene."
**Breakthrough (≤3 sentences):** The authors report their Normalised Memory Ratio correlates with human judgments at Spearman 0.547 and is far less correlated with generated motion (0.072) than raw revisit similarity (0.207); across seven models, DreamX-World-Memo scores highest (0.706), ahead of HY-WorldPlay (0.485), Matrix-Game 3.0 (0.403) and Lyra-2 (0.310).
**Tools & method (≤3 sentences):** 100 reference scenes and three leave-and-return trajectory templates form 300 instances, scoring appearance fidelity, identity, local geometry and persistent state.
**Limitation (≤3 sentences):** The authors state the benchmark "evaluates observable revisit-selective consistency rather than identifying an internal memory mechanism," that automatic metrics "inherit backbone, viewpoint, and prompt biases," and that object interaction and deliberately evolving state are out of scope.

---
## PAWBench: How Far Are We from Probabilistically Aligned World Modeling?
- **arXiv:** 2608.27345 · https://arxiv.org/abs/2608.27345
- **Submitted:** 2026-08-27
- **Authors:** Yuandong Pu, Le Zhuo, Sayak Paul, Gabriel Jorge Menezes, Avram Đorđević, Shiyang Li, Yifan Zhou, Bin Fu, Wenlong Zhang, Junjun He, Yu Qiao, Yihao Liu, Jinbo Xing, Xi Chen
- **Qualifying affiliation(s):** Alibaba (Tongyi Lab) — Yihao Liu
- **Categories:** cs.CV, cs.AI
- **Open release:** none stated (project page https://pawbench.github.io)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PAWBench tests whether video generators behave as probabilistically aligned world models: whether repeated rollouts from identical initial conditions and actions recover the correct distribution over futures rather than one plausible video.
**Purpose (≤3 sentences):** To formalise and measure probabilistic alignment as a distributional criterion for world models.
**Breakthrough (≤3 sentences):** The authors report benchmarking 11 video generation systems, including Veo 3.1 Fast, Kling 3 and Seedance 2, and find that none consistently matches reference probabilities while also covering valid futures.
**Tools & method (≤3 sentences):** 50 scenarios in two tracks, PAW-Calibration (analytically specified distributions) and PAW-Coverage (recovery of valid outcomes), with a PAWEval protocol built on Gemini 3.5 Flash to map videos to terminal outcomes.
**Limitation (≤3 sentences):** The authors state the benchmark scores only terminal outcomes rather than full trajectories, that finite rollout budgets limit distribution estimates, and that it covers controlled, visually parseable scenarios rather than interactive settings.

---
## CoGeo-GS: Concept-Driven and Geometry-Aware Multi-Object Removal in 3D Scenes
- **arXiv:** 2608.26656 · https://arxiv.org/abs/2608.26656
- **Submitted:** 2026-08-27
- **Authors:** Yuanxiang Ni, Xianliang Huang, Chenhang Ma, Chen Xiao, Yuewen Ma, Ruxin Wang, Hao Zhang
- **Qualifying affiliation(s):** ByteDance (PICO) — Xianliang Huang, Yuewen Ma
- **Categories:** cs.CV, cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A framework for removing several objects from a 3D Gaussian Splatting scene in one optimisation stage, using concept-aware semantic tagging of Gaussians and a depth-guided completion pipeline that combines monocular depth priors with diffusion-based refinement.
**Purpose (≤3 sentences):** Geometrically consistent, multi-view coherent removal of multiple objects, addressing occlusion and semantic-entanglement failures of single-object methods.
**Breakthrough (≤3 sentences):** For multi-object removal the authors report PSNR 28.9 versus 25.6 for the best baseline, SSIM 0.882 versus 0.821, LPIPS 0.086 (a 56.6% improvement) and FID 11.4 (a 50% improvement); single-object removal reaches PSNR 30.7 / SSIM 0.903 / LPIPS 0.072 / FID 9.8.
**Tools & method (≤3 sentences):** Evaluated on Mip-NeRF 360 and SPIn-NeRF with 30k iterations on one NVIDIA RTX 4090; accepted at ICME 2026.
**Limitation (≤3 sentences):** The authors state that reliable multi-object removal remains challenging under occlusion and semantic entanglement; specific failure cases are not detailed.

---
## 4DSynth: Controllable Procedural World Synthesis for Dynamic Embodied Simulation
- **arXiv:** 2608.26947 · https://arxiv.org/abs/2608.26947
- **Submitted:** 2026-08-27
- **Authors:** Zehao Qi, Haochen Luo, Jia-Wang Bian, Zeyu Ma, Shuyang Sun
- **Qualifying affiliation(s):** Google DeepMind — Shuyang Sun (co-authors at NTU, Oxford, Princeton)
- **Categories:** cs.RO, cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** 4DSynth converts a text description, a blueprint mask or a single photograph into an editable 4D environment with explicit geometry, animated actors, collision-free trajectories and physics-ready state for embodied agents.
**Purpose (≤3 sentences):** A procedurally generated, controllable 4D world-synthesis pipeline instead of static or hand-authored scenes.
**Breakthrough (≤3 sentences):** The authors introduce 4DSynth-Nav, 333 navigation and pick-and-place tasks, and report that Qwen3-VL-30B (13.2% success) and Gemini 3.1 Pro (33.3%) "both fail the majority of tasks," with Gemini ranging from 57.5% on the easiest tier to 18.2% on the hardest.
**Tools & method (≤3 sentences):** Procedural generation with explicit geometry, animated actors and physics-ready state; evaluation on 4DSynth-Nav.
**Limitation (≤3 sentences):** The authors state animated characters act as kinematic obstacles rather than responsive humans and plan to add responsive humans and articulated objects.

---
## InteractGesture: Progressive Chunk Guidance for Continuous Streaming Co-Speech Gesture Control
- **arXiv:** 2608.25734 · https://arxiv.org/abs/2608.25734
- **Submitted:** 2026-08-26
- **Authors:** Ekkasit Pinyoanuntapong, Ajinkya Deogade, Paul Streli, Wenjing Zhang, Joanna Materzynska, Pu Wang, Vittorio Ferrari, Jie Shen
- **Qualifying affiliation(s):** Meta — Ajinkya Deogade, Paul Streli, Wenjing Zhang, Joanna Materzynska, Vittorio Ferrari, Jie Shen
- **Categories:** cs.CV
- **Open release:** demo (project page https://exitudio.github.io/interactgesture-page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Adds inference-time per-joint spatial control to pretrained co-speech gesture generators through a diffusion sampler and differentiable decoder, with "Progressive Chunk Guidance" that keeps editable staggered chunk latents so constraints propagate across streaming chunk boundaries.
**Purpose (≤3 sentences):** Co-speech gesture generators lack per-joint spatial control (for example pointing at a target) in a streaming setting.
**Breakthrough (≤3 sentences):** On BEAT2 with GestureLSM the authors report FGD 0.431 with Progressive Chunk Guidance versus 0.442 synchronous, and average control error 6.335 cm streaming versus 11.701 cm for a Sequential Chunk Guidance baseline.
**Tools & method (≤3 sentences):** BEAT2 dataset, GestureLSM backbone, 30 FPS in 128-frame chunks with fixed-step DDIM sampling; hardware not disclosed.
**Limitation (≤3 sentences):** The authors state excessive post-sampling optimisation "can diminish naturalness."

---
## GLOSS: Geometric Local Self-Similarity Learning for Faithful Reference-Guided Texture Fill
- **arXiv:** 2608.25461 · https://arxiv.org/abs/2608.25461
- **Submitted:** 2026-08-26
- **Authors:** Chenyue Cai, Anita Hu, James Lucas, Szymon Rusinkiewicz, Masha Shugrina
- **Qualifying affiliation(s):** NVIDIA — Anita Hu, James Lucas, Masha Shugrina
- **Categories:** cs.GR, cs.CV, cs.LG
- **Open release:** code, weights and a Blender add-on announced (the authors state they "will release the code, the model checkpoint and Blender add-on" at https://chenyuecai.github.io/gloss-page/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A shape-specific local texture generation model trained on single-view renderings of one object that exploits geometry-texture self-similarity to perform reference-guided texture inpainting on a mesh without large 3D texture datasets.
**Purpose (≤3 sentences):** Interactive, geometry-consistent texture fill and editing on a single 3D shape in a small-data, per-shape regime.
**Breakthrough (≤3 sentences):** The authors report LPIPS 0.282 (per-mesh) / 0.302 (fine-tuned) and DreamSim 0.352 (fine-tuned), better than TEXGen (LPIPS 0.436) and competitive with Hunyuan2.1 and MV-Adapter, which train on much larger data.
**Tools & method (≤3 sentences):** Batch multi-attention learning over self-similarity within one object; an automated data pipeline built on off-the-shelf image generators; a Blender add-on prototype pilot-tested with 5 professional 3D artists.
**Limitation (≤3 sentences):** The authors state the small-data regime limits generalisation and raises per-shape cost, that the method assumes strong geometry-texture correlation, and that PBR generation is preliminary.

---
## 4DStreamCtrl: Interactive Video Generation with Online 4D Control
- **arXiv:** 2608.25479 · https://arxiv.org/abs/2608.25479
- **Submitted:** 2026-08-26
- **Authors:** Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu
- **Qualifying affiliation(s):** Tencent Hunyuan — Shiqian Li (also Peking University), Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen
- **Categories:** cs.CV, cs.AI
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A unified 3D point-track representation for joint camera and object control, depth editing and motion transfer in streaming video generation, integrated into a pretrained diffusion model through a "Geometric Motion Head."
**Purpose (≤3 sentences):** Real-time streaming 4D-controllable video generation rather than offline or single-signal control.
**Breakthrough (≤3 sentences):** The authors report 480p video at 20.6 FPS from a causal student distilled from 50 to 4 sampling steps, coherent over 350 frames with constant memory, and on DAVIS an EPE of 5.48 (student) versus 11.18 for MotionStream causal on the same backbone.
**Tools & method (≤3 sentences):** The OpenVidHD-Motion3D dataset mined from video; a 32x32 grid of 3D point tracks as the control interface; SpatialTrackerV2 for monocular geometry and camera recovery.
**Limitation (≤3 sentences):** The authors state monocular 3D estimation "can fail on challenging footage with extreme motion blur or occlusions," that the causal student shows a streaming-versus-offline quality gap, and that "small faces and background objects blur progressively" over long sequences.

---
## SceneReGen: Generative Reconstruction of 3D Scenes from a Single Image
- **arXiv:** 2608.23930 · https://arxiv.org/abs/2608.23930
- **Submitted:** 2026-08-25
- **Authors:** Zefan Tian, Yuteng Ye, Yiheng Zhang, Yuhang Yang, Xueqiang Lv, Shizhou Zhang, Le Liu, Di Xu
- **Qualifying affiliation(s):** Huawei — corresponding author Di Xu and co-authors (with Northwestern Polytechnical University); FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SceneReGen reconstructs a full 3D scene from one image by treating generated object assets as reconstruction primitives, with "selective pose factorization" that encodes observed orientation in the generated meshes while estimating translation and scale from scene evidence.
**Purpose (≤3 sentences):** To complete partially observed objects and place them coherently in a shared observation-aligned frame, bridging single-object generation and scene reconstruction.
**Breakthrough (≤3 sentences):** On 3D-FUTURE the authors report the best scene-level Chamfer distance (89.50), scene-level F-score (0.031) and 3D box IoU (0.009) among evaluated methods, with object-level Chamfer tied for best (68.95).
**Tools & method (≤3 sentences):** Trained on 3D-FUTURE (14,761 scenes) plus Objaverse and MeshFleet (about 25K objects) on 96 Ascend 910B NPUs for 500k iterations.
**Limitation (≤3 sentences):** The authors state texture synthesis lacks occlusion awareness, that performance degrades on low-resolution or blurry inputs, and that position estimation lacks collision regularisation, causing interpenetration.

---
## NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics
- **arXiv:** 2608.24199 · https://arxiv.org/abs/2608.24199
- **Submitted:** 2026-08-25
- **Authors:** Javier Gamazo Tejero, Lukas Zbinden, Keyur Sheth, Raghavendra K M, Nadim Daher, Diego Granero Maraña, Filip Binkiewicz, Patrick Thornycroft, Mahdi Azizian, Sean D. Huver
- **Qualifying affiliation(s):** NVIDIA — Javier Gamazo Tejero, Lukas Zbinden, Keyur Sheth, Raghavendra K M, Nadim Daher, Mahdi Azizian, Sean D. Huver (co-authors at CMR Surgical)
- **Categories:** cs.RO
- **Open release:** weights and code (https://github.com/isaac-for-healthcare/Cosmos-H-Dreams; https://huggingface.co/nvidia/Cosmos-H-Dreams; https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A real-time surgical world-model system combining an action-conditioned generative model, a teacher-to-student distillation recipe and a deployment stack on the NVIDIA FlashDreams streaming-inference library, built on Cosmos-H-Surgical-Simulator fine-tuned on the Open-H-Embodiment corpus.
**Purpose (≤3 sentences):** An interactive generative simulator for surgical robotics, since animal and cadaver labs are costly and classical simulators struggle with photorealism and deformable tissue.
**Breakthrough (≤3 sentences):** The authors report the distilled student streams at roughly 160 inference FPS on one NVIDIA RTX PRO 6000 Blackwell GPU and call it "the first interactive surgical world model supporting live human and policy control"; distillation raises FVD from 170.1 to 265.4 and LPIPS from 0.086 to 0.121 relative to the teacher.
**Tools & method (≤3 sentences):** Control via browser keyboard over WebRTC, a Meta Quest over WebXR, CMR Surgical's Versius console and learned policies; Self Forcing distillation to a causal few-step student.
**Limitation (≤3 sentences):** The authors state the real-time regime "carries a measurable fidelity cost," that "scenes with thin, self-interacting structures degrade most," and that the student sometimes hallucinates suture thread geometry where it folds or crosses.

---
## Luce: Relightable Gaussians for 3D Asset Generation
- **arXiv:** 2608.23943 · https://arxiv.org/abs/2608.23943
- **Submitted:** 2026-08-25
- **Authors:** Mayank Singh, Michele Stoppa, Alvise Memo, Rui Yu, Harsha Kalli, Srimanth Gunturi, Muhammad Ahmed Riaz, Behrooz Shahsavari, Waleed Abdulla, David E. Jacobs
- **Qualifying affiliation(s):** Apple — all authors
- **Categories:** cs.CV, cs.AI, cs.GR
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Luce introduces a PBR Gaussian representation that unifies geometry with albedo, metallic-roughness and tangent-space normals in voxelised Gaussian clouds, compresses it with a VAE into a diffusible latent, and generates assets from a single image with a rectified-flow transformer.
**Purpose (≤3 sentences):** Relightable, PBR-shaded 3D assets (Gaussians or textured meshes) from one image, so downstream renderers can relight them under arbitrary lighting.
**Breakthrough (≤3 sentences):** On Toys4K (N=412) the authors report FID 20.99 versus 29.22 for TRELLIS 2 and 29.76 for LiTo, and CLIP alignment 0.9062 versus 0.8898 for TRELLIS GS; on a PBR reconstruction subset (N=338) they report colour PSNR 36.1 dB and normal PSNR 34.6 dB.
**Tools & method (≤3 sentences):** Multi-layer DINOv2 conditioning; about 500K PBR-filtered assets from Objaverse and Objaverse-XL plus a 158K-asset TexVerse subset; 64 H100 GPUs for about 14 days each for the VAE and the flow model; inference on one H100.
**Limitation (≤3 sentences):** The authors state the voxelised representation may under-resolve fine detail, that the Cook-Torrance model omits subsurface scattering, anisotropy and thin-film effects, and that the pipeline targets object-centric assets rather than scenes.

---
## GameWAM: A World Action Model for Video Games
- **arXiv:** 2608.26200 · https://arxiv.org/abs/2608.26200
- **Submitted:** 2026-08-25
- **Authors:** Yuncheng Guo, Zhanqiu Zhang, Yiwen Guo, Weijia Li
- **Qualifying affiliation(s):** LIGHTSPEED — Zhanqiu Zhang (the paper's affiliation footnote reads only "LIGHTSPEED"; not identified in the paper as Tencent's Lightspeed Studios); FLAG: borderline
- **Categories:** cs.AI, cs.CV, cs.LG
- **Open release:** none stated (project page https://yunncheng.github.io/GameWAM/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GameWAM is presented as the first World Action Model for native closed-loop video-game play and GUI control, jointly generating future observations and executable keyboard-mouse action trajectories through parallel visual and action generative processes with block-causal conditioning and flow matching.
**Purpose (≤3 sentences):** To unify game-playing control policies with world-model-style visual prediction, since prior agents map perception to actions without modelling dynamics while interactive world models predict visuals without acting.
**Breakthrough (≤3 sentences):** The authors report competitive task success with fewer executed native actions than compared agents, and identify a failure mode they call "Low-Frequency Action Source Imprinting," where low-frequency components of the sampled action source steer coarse camera motion.
**Tools & method (≤3 sentences):** Block-cycle control coordinating prediction, execution and replanning; mode-specific prediction distributions and continuous-action normalisation; trained on synchronised gameplay and GUI trajectory data the authors constructed.
**Limitation (≤3 sentences):** The authors state GameWAM "is designed as a low-level closed-loop controller rather than a standalone high-level planner," with no symbolic task graph or long-horizon search.

---
## ExMesh++: From Multi-View Images to Relightable UV-PBR Mesh Assets via Topology-Adaptive Reconstruction and Decomposition
- **arXiv:** 2608.24109 · https://arxiv.org/abs/2608.24109
- **Submitted:** 2026-08-25
- **Authors:** Chuanjin Fan, Lifan Wu, Wenjie Chang, Hanzhi Chang, Wenfei Yang, Tianzhu Zhang
- **Qualifying affiliation(s):** Alibaba Group (Amap) — Wenjie Chang
- **Categories:** cs.GR, cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A staged multi-view reconstruction pipeline that yields editable, relightable UV-PBR mesh assets: geometry and topology are refined with consistent UV updates, then PBR maps and environment lighting are optimised on the fixed mesh with one-bounce indirect illumination.
**Purpose (≤3 sentences):** To close the gap between surface-only multi-view reconstruction and production-ready assets for standard DCC workflows.
**Breakthrough (≤3 sentences):** The authors report average Chamfer distance 0.58 on DTU (102K-vertex meshes, 13-minute runtime); on Synthetic4Relight, relighting PSNR 34.19 dB, albedo PSNR 30.16 dB and roughness MSE 0.005; on Stanford-ORB, novel-view PSNR-H 31.27 dB, relighting PSNR-H 26.60 dB and Chamfer 0.30.
**Tools & method (≤3 sentences):** Topology-adaptive vertex splitting and merging with UV consistency; two-stage inverse rendering; one-bounce diffuse indirect illumination via secondary ray tracing; about 30 minutes per scene on one NVIDIA RTX A6000.
**Limitation (≤3 sentences):** The authors state the method is limited to opaque isotropic metallic-roughness BRDFs, that the one-bounce model excludes multi-bounce transport and indirect specular reflection, and that CPU-based UV regeneration bottlenecks high-resolution meshes.

---
## ReWorld: An Interactive World Model with Long-Horizon Memory
- **arXiv:** 2608.23565 · https://arxiv.org/abs/2608.23565
- **Submitted:** 2026-08-24
- **Authors:** Zhifei Chen, Luozhou Wang, Guibao Shen, Dongyu Yan, Shuai Yang, Tianshuo Xu, Yihua Du, Wei Wang, Tianyi Gui, Lianghua Huang, Yingcong Chen
- **Qualifying affiliation(s):** Alibaba (ATH) — Zhifei Chen (also HKUST(GZ)), Guibao Shen, Wei Wang, Tianyi Gui, Lianghua Huang
- **Categories:** cs.AI
- **Open release:** demo (project page https://zhifeichen097.github.io/ReWorld/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ReWorld separates short-horizon control from long-horizon memory during training and bounds both at inference: most attention heads use short windows while a few global heads attend over full history, with a fixed 12-chunk pose-indexed landmark cache to regenerate starting views in minute-long sequences.
**Purpose (≤3 sentences):** To resolve the tension the authors describe as "control wants a short horizon, memory wants an unbounded one," while streaming in real time.
**Breakthrough (≤3 sentences):** The authors report the best rotation error (11.95 degrees) among seven compared methods and the highest mean VBench score (0.850) across seven video-quality dimensions.
**Tools & method (≤3 sentences):** A metric-scale-aligned data engine of 220,724 clips from eight sources (Unreal-rendered fly-throughs, roaming across 79 games, RealEstate10K, DL3DV and others); distribution-matching distillation confined to a LoRA adapter for four-step sampling at 704x1280.
**Limitation (≤3 sentences):** The authors state "memory is still keyed on camera pose alone; extending consolidation to dynamic scenes and richer, non-navigational interaction is the natural next step."

---
## Photorealistic Novel View Synthesis of Human Faces using Next-Scale Transformers
- **arXiv:** 2608.23410 · https://arxiv.org/abs/2608.23410
- **Submitted:** 2026-08-24
- **Authors:** Federico Stella, Fei Jiang, Zhongshi Jiang, Zohar Barzelay, Emanuel Garbin, Amin Jourabloo, Liuhao Ge
- **Qualifying affiliation(s):** Meta (Reality Labs) — Fei Jiang, Zhongshi Jiang, Zohar Barzelay, Emanuel Garbin, Amin Jourabloo, Liuhao Ge (Federico Stella, EPFL, as a Meta Reality Labs intern)
- **Categories:** cs.CV, cs.LG
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Adapts next-scale autoregressive transformers to synthesise multi-view-consistent novel views of human faces at 512x512 from synthetic training data, coupled with a pixel-aligned 3D Gaussian lifting model for face reconstruction.
**Purpose (≤3 sentences):** Higher-resolution, cross-view-consistent face renderings without large 2D pretraining sets, usable to drive 3D Gaussian face reconstruction.
**Breakthrough (≤3 sentences):** On the PSGS dataset (6 canonical views) the authors report their best variant reaching PSNR 23.13, SSIM 0.8816, LPIPS 0.1762 and DreamSim 0.01379, versus PSNR 16.75 / SSIM 0.79 for FaceLift-NVS.
**Tools & method (≤3 sentences):** Three-stage training for high-resolution convergence; the proprietary SS3D dataset (about 2M textured objects), PSGS (3.2K subjects) and the public Ava-256 dataset (256 subjects, 80 dome cameras); 64 to 128 NVIDIA A100 GPUs.
**Limitation (≤3 sentences):** The authors state the method struggles with unseen expressions and accessories such as hats because training data is limited to neutral expressions, and that background colour bleeding remains an issue.

---
## Object-Uni: A Unified Model for Object-Centric Spatial Understanding and Controllable Generation
- **arXiv:** 2608.22757 · https://arxiv.org/abs/2608.22757
- **Submitted:** 2026-08-24
- **Authors:** Mining Tan, Yinuo Wang, Ziqi Zhou, Weize Quan, Sifei Li, Jingdong Chen, DanDan Zheng, Libin Wang, Weiming Dong
- **Qualifying affiliation(s):** Ant Group — Weiming Dong (corresponding author); FLAG: borderline
- **Categories:** cs.CV, cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Object-Uni unifies object pose perception, spatial reasoning, pose-conditioned generation and object-centric novel-view synthesis by treating object pose as an explicit geometric variable, with a viewpoint-based orientation abstraction so multimodal LLMs can reason about 3D orientation in natural language.
**Purpose (≤3 sentences):** To move unified vision-language models from describing objects to manipulating their spatial state.
**Breakthrough (≤3 sentences):** The authors report azimuth error 22.87 degrees (74.44% AUC@30) versus 29.94 degrees (55.40%) for Orient Anything V2 on KITTI-Cityscapes, and on ImageNet3D generation 74.31 mIoU / 83.40% success versus 66.45 / 68.81% for SceneDesigner.
**Tools & method (≤3 sentences):** The UniSpatial-80K dataset (83,252 images, 91,392 annotated objects, 122 categories) and an "Object-Token-Grounded Pose Anchor"; about 18 hours on 8 NVIDIA H20 GPUs.
**Limitation (≤3 sentences):** The authors state the model "still has limitations in generating fine-grained text and human details," attributed partly to the generative backbone.

---
## AquaFlow: A Monocular Gaussian Splatting SLAM for Underwater Streaming Reconstruction
- **arXiv:** 2608.22906 · https://arxiv.org/abs/2608.22906
- **Submitted:** 2026-08-24
- **Authors:** Yingxiang Xu, Kerui Ren, Wenqi Guo, Changjian Jiang, Tao Lu, Linning Xu, Mulin Yu
- **Qualifying affiliation(s):** Shanghai AI Laboratory — Yingxiang Xu, Kerui Ren, Wenqi Guo, Tao Lu, Mulin Yu; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A monocular 3DGS SLAM system for underwater streaming reconstruction that pairs a subsea-finetuned 3D vision foundation model with a hybrid representation of distance-aware neural Gaussians and a physics-inspired light attenuation and scattering model.
**Purpose (≤3 sentences):** To extend streaming 3DGS reconstruction to underwater scenes where attenuation and scattering degrade pose tracking and geometry.
**Breakthrough (≤3 sentences):** The authors report PSNR 34.53 dB (Canyons), 26.77 dB (RedSea) and 36.31 dB (UW-Stereo-VI), a 4.74 dB gain and 13.2% lower localisation error than WaterSplat-SLAM, and ATE RMSE of 0.422 m / 0.958 m / 0.157 m on the three benchmarks.
**Tools & method (≤3 sentences):** Fine-tuned on 224,273 underwater image pairs (TartanAir-Ocean, MIMIR-UW, UWStereo, FLSea-stereo, sweet-corals); a new 62-sequence benchmark; 1.08 FPS (Canyons) on an Intel i9-14900K with one RTX 4090.
**Limitation (≤3 sentences):** The authors state a need for better zero-shot generalisation of the underwater foundation model and leave dynamic underwater environments to future work.

---
## Towards Alias-Free 4D Gaussian Representations with Motion-Aware Filtering
- **arXiv:** 2608.21828 · https://arxiv.org/abs/2608.21828
- **Submitted:** 2026-08-22
- **Authors:** Ankit Dhiman, Kunal A Kathare, Pranav Vignesh, Lokesh R Boregowda, Venkatesh Babu Radhakrishnan
- **Qualifying affiliation(s):** Samsung R&D Institute India, Bangalore — Ankit Dhiman, Lokesh R Boregowda; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Addresses aliasing in 4D Gaussian Splatting of dynamic scenes with a motion-aware 3D smoothing filter whose strength adapts to local motion instead of a static filter.
**Purpose (≤3 sentences):** Static anti-aliasing filters such as Mip-Splatting ignore motion, causing artefacts under zoom or resolution changes in dynamic scenes.
**Breakthrough (≤3 sentences):** The authors report 29.79 dB PSNR at 4x resolution on Plenoptic Video versus 27.40 dB for SARO-GS, and 32.36 dB versus 28.54 dB (Grid4D) on D-NeRF at 4x, a 5.21 dB gain over base SARO-GS.
**Tools & method (≤3 sentences):** Joint density of time and focal-length-to-depth ratio estimated by kernel density estimation drives the filter; evaluated on Plenoptic Video, D-NeRF and HyperNeRF; described as representation-agnostic across 4DGS frameworks.
**Limitation (≤3 sentences):** The authors state memory scales as O(N x D x T) (Gaussians x depth bins x time bins) and flag rapid complex-motion scenes for future optimisation.

---
## GameXpert-Bench: How Far Are Coding Agents from Expert Game Development?
- **arXiv:** 2608.21833 · https://arxiv.org/abs/2608.21833
- **Submitted:** 2026-08-22
- **Authors:** Kun Chen, Haorong Hong, Peizhong Gao, Jianfeng Lin, Tongxu Luo, Yuxuan Xie, Chenxu Liu, Jieling He, Zhongyuan Liu, Zeno Zeng
- **Qualifying affiliation(s):** Tencent — Yuxuan Xie, Jieling He, Zhongyuan Liu (Lightspeed Studios); Zeno Zeng (Hunyuan Team)
- **Categories:** cs.AI, cs.CL
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GameXpert-Bench evaluates LLM coding agents on end-to-end game development in three stages: generating a game from a request (97 tasks, 11 genres), diagnosing and fixing injected bugs (100 human-verified tasks) and iterative multi-turn improvement (17 chains), tested by live game interaction and behavioural checks.
**Purpose (≤3 sentences):** To measure how far coding agents are from expert game development, since prior benchmarks neglect bug-fixing and iterative refinement.
**Breakthrough (≤3 sentences):** The authors report Claude-Opus-5 leading GameGen with 79.7/100 (15 models, 1,455 runs; richness averages only 46.1), scoring 39.0/100 on GameFix under strict scoring, and 93.96/100 on GameOpt.
**Tools & method (≤3 sentences):** 50 confidential human-verified game levels with 19 to 27 injected bugs each; 701 acceptance criteria for optimisation; Playwright and headless Chromium runtime verification plus annotation by game-design specialists.
**Limitation (≤3 sentences):** The authors conclude "initial generation quality alone is insufficient to characterize an agent's game development capability," citing gaps in self-discovery, verification, regression control and long-horizon task management.

---
## Sparse Light Field Sampling Improves Casual 3D and 4D Reconstruction
- **arXiv:** 2608.20602 · https://arxiv.org/abs/2608.20602
- **Submitted:** 2026-08-20
- **Authors:** Shamus Li, Ruiming Cao, Laura Waller, Kristina Monakhova, Sara Fridovich-Keil
- **Qualifying affiliation(s):** Adobe — Ruiming Cao
- **Categories:** eess.IV, cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Studies why novel-view-synthesis pipelines use monocular input even though consumer devices carry several synchronised cameras, analysing sensor-limited and exposure-limited multi-camera capture for 3D and 4D reconstruction.
**Purpose (≤3 sentences):** To show that existing multi-camera hardware (phones, headsets, plenoptic cameras) improves single-shot, few-shot and casual-video reconstruction without new sensors.
**Breakthrough (≤3 sentences):** On synthetic NeRF-Blender data at one exposure the authors report 24.78 PSNR for light-field capture and 26.39 for a multiplexed setup versus 16.25 monocular; on dynamic real scenes, multi-view reaches 31.71 PSNR (iPhone) and 34.48 (stereo) versus 24.51 and 29.17 monocular.
**Tools & method (≤3 sentences):** Custom datasets from an iPhone 15 Pro (3 cameras), Apple Vision Pro (stereo) and a Lytro Illum (81 sub-views), plus a physical multiplexed light-field prototype; evaluated with 3DGS and 4DGS.
**Limitation (≤3 sentences):** The authors state benefits "diminish for distant content in large, unbounded scenes where disparity is minimal at more distant depths."

---
## MultiCube: Compositional 3D Generation With Part-Level Semantic and Spatial Control
- **arXiv:** 2608.20448 · https://arxiv.org/abs/2608.20448
- **Submitted:** 2026-08-20
- **Authors:** Ava Pun, Kangle Deng, Yiheng Zhu, Jun-Yan Zhu, Maneesh Agrawala, Tinghui Zhou
- **Qualifying affiliation(s):** Roblox — Ava Pun, Kangle Deng, Yiheng Zhu, Maneesh Agrawala, Tinghui Zhou
- **Categories:** cs.GR, cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** MultiCube generates 3D objects composed of semantically meaningful parts, with explicit control over part semantics (a schema) and spatial layout (bounding boxes) from a text prompt.
**Purpose (≤3 sentences):** Professional asset workflows need controllable, editable, part-decomposed objects rather than monolithic text-to-3D outputs.
**Breakthrough (≤3 sentences):** The authors report part-level Chamfer distance 0.040 versus 0.183 for CubePart, F-score 0.948 versus 0.787 and box IoU 0.847 versus 0.580, plus win rates of 82.9% over FullPart on semantic alignment and 82.2% over OmniPart on geometric quality.
**Tools & method (≤3 sentences):** A two-stage diffusion pipeline generates a monolithic mesh aligned to the layout, then decomposes it via a Part Layout Adapter; 510k assets (2.96M parts) for training; a 1.9B-parameter DiT plus a 22M-parameter adapter on 24 NVIDIA H200 GPUs; evaluated on PartObjaverse-Tiny.
**Limitation (≤3 sentences):** The authors acknowledge failures with badly mis-specified bounding boxes, occasional colliding parts, and no per-part iterative editing without full regeneration.

---
## 4DAnyone: Create Anyone in 4D from a Casual Monocular Video
- **arXiv:** 2608.20335 · https://arxiv.org/abs/2608.20335
- **Submitted:** 2026-08-20
- **Authors:** Yudong Jin, Tao Xie, Qihang Zhang, Zehong Shen, Zhen Xu, Yujun Shen, Hujun Bao, Xiaowei Zhou, Yinghao Xu
- **Qualifying affiliation(s):** Ant Group — Zehong Shen; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** code (project page https://4danyone.github.io)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Reconstructs 4D humans from uncalibrated casual monocular video by generating multi-view-consistent videos and lifting them into 4D Gaussian Splatting.
**Purpose (≤3 sentences):** Reconstruction-grade 4D human capture from a single handheld camera, addressing context-length and viewpoint-count limits of prior multi-view generation.
**Breakthrough (≤3 sentences):** The authors report PSNR 24.15 on DNA-Rendering (versus 20.55 for ReCamMaster and 20.38 for MV-Performer), SSIM 0.863, LPIPS 0.159, and PSNR 23.28 / SSIM 0.846 / LPIPS 0.117 on DyMVHumans.
**Tools & method (≤3 sentences):** Reference Context Packing compresses context from O(N) to O(1) and Target Context Routing shares context across groups during denoising; trained on MVGameHuman (38k videos, 24 cameras, 318 actors), DNA-Rendering (51k videos) and monocular data on 128 H20-3E GPUs.
**Limitation (≤3 sentences):** The authors state the model struggles with loose garments far from the body and inherits skeleton-estimation errors.

---
## Generalized Audio-Driven Synthesis of Precise Drummer Motion
- **arXiv:** 2608.19055 · https://arxiv.org/abs/2608.19055
- **Submitted:** 2026-08-19
- **Authors:** Álvaro G. Iñesta, Mattia Ryffel, Amit H. Bermano, Robert W. Sumner, Martin Guay
- **Qualifying affiliation(s):** Disney Research|Studios — Álvaro G. Iñesta, Mattia Ryffel, Robert W. Sumner, Martin Guay; FLAG: borderline (not on the tracked list)
- **Categories:** cs.CV, cs.GR, cs.SD
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A diffusion framework that synthesises drumming motion from audio with a dual-objective loss separating body-movement accuracy from stick-tip precision, plus two new metrics, Impact Point Deviation and Percussive Alignment Score; the paper won the Best Paper Award at SCA 2026.
**Purpose (≤3 sentences):** Music-driven character animation where high-acceleration drumming must stay precisely synchronised with audio.
**Breakthrough (≤3 sentences):** The authors report Impact Point Deviation falling from 8.4 cm (rotations-only baseline) to 1.9 cm, a Percussive Alignment Score of 0.82 versus 0.68 (baseline) and 0.91 (ground truth), and 92.8% preference over the baseline in a 22-participant study.
**Tools & method (≤3 sentences):** More than 3.5 hours (1,518,450 frames) of professional drumming captured at 120 Hz on a Roland TD-25KV with nine OptiTrack cameras, augmented to over 25,000 sequences; trained about 48 hours on an NVIDIA RTX 3090.
**Limitation (≤3 sentences):** The authors state the method needs isolated drum audio (polyphonic music requires stem separation) and assumes a fixed drum-kit layout.

---
## WorldMind: Decoupled Game World Model for State-Aware NPC Behavior
- **arXiv:** 2608.21439 · https://arxiv.org/abs/2608.21439
- **Submitted:** 2026-08-18
- **Authors:** Zhiyang Deng, Boran Zhang, Danze Chen, Yeying Jin
- **Qualifying affiliation(s):** Tencent — all authors (with National University of Singapore; work done during Tencent research internships)
- **Categories:** cs.CV
- **Open release:** demo (project page https://teawhite.cn/worldmind_projectpage/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** WorldMind is described as the first decoupled framework for state-aware NPC behaviour in game world models, separating interactive world modelling into Understanding, Decision, Control and Generation layers.
**Purpose (≤3 sentences):** To ground NPC behaviour in the evolving game state (boss-player distance, skill cooldowns), which is not achieved when behaviour is implicit in video generation or driven only by external control signals.
**Breakthrough (≤3 sentences):** The authors introduce BOSS-140K, gameplay videos paired with internal game states collected by an automated agent, and report WorldMind preferred over baselines in about 70% of pairwise comparisons for "more tactically appropriate and coherent NPC behavior."
**Tools & method (≤3 sentences):** The Understanding layer reconstructs a compact state from generated frames; the Decision layer uses a general-purpose language model to plan; the Generation layer renders gameplay in real time with a video diffusion model.
**Limitation (≤3 sentences):** The authors state "the Decision Layer shows partial cross-game generalization and remains state-sensitive, whereas compact-state reconstruction requires target-domain adaptation."

---
## SPVC: Structured and Panoptic Video Fixing for Cross-Dataset Driving Scene Rendering
- **arXiv:** 2608.17420 · https://arxiv.org/abs/2608.17420
- **Submitted:** 2026-08-18
- **Authors:** Gen Li, Shu Han, Yun Xi Qiao, Hua Chen, Xuyang Dai, Bohan Li, Hao Zhao, Chaojian Li
- **Qualifying affiliation(s):** Great Wall Motor Company Limited — Hua Chen, Xuyang Dai; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A two-stage controllable video-diffusion framework that repairs blur, temporal inconsistency and foreground/background misalignment in neural-rendered driving scenes viewed from novel trajectories or with inserted objects.
**Purpose (≤3 sentences):** To improve driving-simulation fidelity by fixing degraded novel-view renders with explicit geometric conditions (camera poses, HD maps, 3D boxes) across datasets.
**Breakthrough (≤3 sentences):** On Waymo (4 m lane shift) the authors report FID 45.3 versus 59.1 for Difix3D+ and FVD 658.5 versus 735.0; on nuScenes FID improves 33.62% and FVD 43.45% over the strongest baseline; in closed-loop VAD evaluation the collision rate drops from 50% to 30% and the NeuroNCAP score rises from 2.659 to 3.707.
**Tools & method (≤3 sentences):** Trained on paired degraded-to-clean video from Waymo, nuScenes and PandaSet, zero-shot tested on EUVS, at 800x448 over 25 frames on an NVIDIA H20 (about 252.64 s per sequence).
**Limitation (≤3 sentences):** The authors state the method still sits inside a reconstruction-then-rendering paradigm and that temporal consistency depends on input sequence quality.

---
## LumiTokens: 3D Relighting via Token-Space Lighting Transformation
- **arXiv:** 2608.18215 · https://arxiv.org/abs/2608.18215
- **Submitted:** 2026-08-18
- **Authors:** Yiwen Chen, Matheus Gadelha, Huaizu Jiang
- **Qualifying affiliation(s):** Adobe Research — Matheus Gadelha
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Performs 3D relighting as a direct transformation in a learned token space, without explicit material decomposition or physically based re-rendering.
**Purpose (≤3 sentences):** To replace costly inverse-rendering pipelines with a token-space method that handles environment maps, point lights and area lights through one interface.
**Breakthrough (≤3 sentences):** The authors report multi-view PSNR 30.48 dB (versus 28.40 dB for Neural Gaffer) and novel-view PSNR 27.76 dB (versus 26.17 dB for TensoIR) from only 8 input views versus 30 to 50 for other methods, at 3.79 s inference versus 3952.91 s for TensoIR.
**Tools & method (≤3 sentences):** Scene and lighting encoded as Plücker ray tokens edited by a self-attention Scene Token Editor; trained on 20,000 Objaverse objects under 16 lighting conditions (about 20.8M images) plus 3,000 multi-object scenes on 8 NVIDIA H100 GPUs.
**Limitation (≤3 sentences):** The authors state that extending to real captures with complex materials and imperfect poses remains future work.

---
## Love Handles: Decimation for Deformation Handles with Compact Support and Low Memory Footprints
- **arXiv:** 2608.17930 · https://arxiv.org/abs/2608.17930
- **Submitted:** 2026-08-18
- **Authors:** David IW Levin, Paul Kry, Kartic Subr, Ryan Schmidt, Etienne Vouga, Teseo Schneider
- **Qualifying affiliation(s):** NVIDIA — David IW Levin (also University of Toronto)
- **Categories:** cs.GR
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A decimation-based algorithm that computes sparse, compactly supported deformation handles for reduced-order elastodynamic simulation on arbitrary volumetric meshes.
**Purpose (≤3 sentences):** To lower per-timestep cost of physically based deformation for real-time, game and robotics use while bounding error against target modes such as linear vibration modes.
**Breakthrough (≤3 sentences):** The authors report reducing a 200,000-vertex basketball mesh to 268 handles at 5% error on 25 linear modes, 150 simulation steps per second for nonlinear elastodynamics, and up to 15.12x lower error than Brandt et al. (2018) at equal memory, with per-timestep cost rarely above 55 ms.
**Tools & method (≤3 sentences):** Iterative algebraic mesh decimation jointly optimising handle placement, weights and a spectrally informed reduced cubature; 15 tetrahedral meshes (699 to 201,942 vertices) on an NVIDIA DGX Spark.
**Limitation (≤3 sentences):** The authors state preprocessing can take up to 36 hours in worst cases, that the method is less effective on already-coarse meshes, and that it needs precomputed target displacement fields.

---
## Hydra-0: Action Flow for Generalist World Modeling and Control
- **arXiv:** 2608.18077 · https://arxiv.org/abs/2608.18077
- **Submitted:** 2026-08-18
- **Authors:** Hongyu Li, Bowen Wen, Xinghao Zhu, Yixuan Wang, Yilun Du, Yunzhu Li, George Konidaris, Stan Birchfield, Soha Pouya, Chenran Li, Yan Chang
- **Qualifying affiliation(s):** NVIDIA — Hongyu Li, Bowen Wen, Xinghao Zhu, Yixuan Wang, Yilun Du, Stan Birchfield, Soha Pouya, Chenran Li, Yan Chang
- **Categories:** cs.RO
- **Open release:** demo (project page https://nvidia-isaac.github.io/video_to_data/hydra-0/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Hydra-0 is a generalist world model that represents robot actions as "action flow," pixel motion, as a unified interface across robots, tasks and environments, so action consequences are learned once and reused across embodiments.
**Purpose (≤3 sentences):** A world model that generalises across robot morphologies and supports zero-shot composition of skills rather than being tied to one action space.
**Breakthrough (≤3 sentences):** The authors report a Pearson correlation of 0.96 between replayed and reference success rates on their RoboLab benchmark and an "emergent inverse mode" that predicts robot motion from object flow in human demonstrations.
**Tools & method (≤3 sentences):** A Wan2.2 I2V-A14B backbone trained for five days over 40,000 steps on 32 NVIDIA H100 GPUs.
**Limitation (≤3 sentences):** No explicit limitations paragraph was found in the fetched text (observed, not stated).

---
## GenRec: Knowing Where to Reconstruct and Where to Generate
- **arXiv:** 2608.17832 · https://arxiv.org/abs/2608.17832
- **Submitted:** 2026-08-18
- **Authors:** Ata Çelen, Jaewoo Jung, Federico Tombari, Marc Pollefeys, Sunghwan Hong, Michael Niemeyer, Daniel Barath
- **Qualifying affiliation(s):** Google — Federico Tombari, Daniel Barath; Microsoft — Marc Pollefeys
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GenRec is a multi-view flow-matching model for generative novel view synthesis that separates "reconstruction" of pixels visible in source views from "generation" of disoccluded pixels, using an observation mask and a monocular depth estimator to guide a backbone that jointly denoises RGB and scene-coordinate maps, followed by pixel-space refinement.
**Purpose (≤3 sentences):** Existing generative NVS methods apply one uniform loss to both reconstructable and purely generative regions, blurring the line between geometric fidelity and hallucination.
**Breakthrough (≤3 sentences):** The authors report the best reconstruction fidelity in observed regions and higher perceptual quality than purely generative baselines in unobserved regions on RealEstate10K, DL3DV-10K and Mip-NeRF 360, for single-view extrapolation and two-view interpolation.
**Tools & method (≤3 sentences):** Multi-view flow-matching backbone; observation mask from source cameras; monocular depth front-end; evaluated on RealEstate10K, DL3DV-10K, Mip-NeRF 360.
**Limitation (≤3 sentences):** The authors state the method inherits the limitations of its monocular depth front-end, that compute limits training to a small number of views per scene, and that Gen3C beats it on relative-pose metrics for RealEstate10K narrow-baseline cases.

---
## GS-Voxel: Fitting-Free Structured Latents for Large-Scale 3DGS Generation
- **arXiv:** 2608.17988 · https://arxiv.org/abs/2608.17988
- **Submitted:** 2026-08-18
- **Authors:** Ming Qian, Zijian Wang, Minchao Sun, Jincheng Xiong, Hang Zhang, Mu Xu, Chi Wang, Baoquan Chen
- **Qualifying affiliation(s):** Alibaba (Amap) — Ming Qian, Zijian Wang, Minchao Sun, Jincheng Xiong, Hang Zhang, Mu Xu
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GS-Voxel converts pre-optimised large-scale aerial 3DGS reconstructions into structured sparse-voxel latents without per-scene refitting, then generates new aerial 3DGS scenes from those latents.
**Purpose (≤3 sentences):** Million-scale unordered Gaussian primitives create a representation bottleneck for generative modelling of large aerial scenes.
**Breakthrough (≤3 sentences):** The authors report tile-level FID 28.0 / KID 0.020, geometry-VAE shape IoU 0.99, attribute-VAE PSNR 23.09 / SSIM 0.62 and PSNR 40.04 for direct conversion, and demonstrate generation over 1,400 m x 800 m scenes from 200 m x 200 m training tiles.
**Tools & method (≤3 sentences):** A factorised two-stage VAE (voxel geometry and local Gaussian attributes) with 0.3B-parameter image-conditioned flow DiTs and overlap-aware tiled inference; about 18,000 training samples from real aerial 3DGS reconstructions.
**Limitation (≤3 sentences):** The authors state training relies on real reconstructed scenes, that the implementation targets SH0 aerial scenes only, that primitives are discarded in very dense voxels, and that thin structures are hard to preserve.

---
## SplatGuide: Geometric Priors from 3D Gaussians for Pose-Free Novel View Synthesis
- **arXiv:** 2608.16863 · https://arxiv.org/abs/2608.16863
- **Submitted:** 2026-08-17
- **Authors:** Yejun Zhang, Zihan Wang, Xu Ji, Yihao Wang, Yuxin Hou, Junyuan Fang, Juho-Matti Kilpeläinen, Arno Solin, Hamed Rezazadegan Tavakoli, Esa Rahtu, Juho Kannala
- **Qualifying affiliation(s):** Nokia Technologies — Hamed Rezazadegan Tavakoli; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SplatGuide reuses one feed-forward 3DGS reconstruction for three roles in pose-free novel view synthesis: pixel-aligned geometric conditioning, occlusion-aware reference-view selection, and feature-level diffusion guidance.
**Purpose (≤3 sentences):** Prior pose-free NVS pipelines extract only one signal (depth or a single reference image) from reconstruction.
**Breakthrough (≤3 sentences):** On RealEstate10K (9-view) the authors report 30.00 PSNR / 0.88 SSIM / 0.04 LPIPS, above the ground-truth-pose baseline SEVA (29.63 PSNR); their visibility-aware selector reaches 28.25 PSNR versus 26.93 for the best baseline selector; out of domain on Mip-NeRF 360 (9-view) it reaches 16.01 PSNR.
**Tools & method (≤3 sentences):** A per-Gaussian visibility view selector and reconstruction-token feature guidance on a 3DGS backbone; trained on DL3DV (10,510 scenes) and RealEstate10K (67,477 videos) on 8 NVIDIA H200 GPUs.
**Limitation (≤3 sentences):** The authors state failure modes are correlated because renderings, tokens and view indices share one reconstruction, so textureless surfaces, wide baselines, repetitive structure and dynamic content hurt all three signals; dynamic scenes are called the most significant limitation.

---
## SCALE: State-Calibrated Latent Embeddings for JEPA Planning in the Right Geometry
- **arXiv:** 2608.16287 · https://arxiv.org/abs/2608.16287
- **Submitted:** 2026-08-17
- **Authors:** Jiaming Hu, Yan Zheng, Tian Wang, Florian Dubost, Alejandro Mottini, Junze Liu, Arvind Srinivasan, Kai Zhong, Kun Qian, Sharon Gao, Qingjun Cui
- **Qualifying affiliation(s):** Unity Technologies — Yan Zheng, Tian Wang, Florian Dubost, Alejandro Mottini, Junze Liu, Arvind Srinivasan, Kai Zhong, Kun Qian, Sharon Gao, Qingjun Cui (Jiaming Hu as a Unity intern, Boston University)
- **Categories:** cs.LG
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Compares two ways to obtain non-collapsed representations in JEPA world models used for planning, inheriting a pretrained feature space (DINO-WM) versus end-to-end training with anti-collapse regularisation (LeWM), and adds SCALE, a training-time regulariser that aligns latent distances with distances in a task-relevant state space.
**Purpose (≤3 sentences):** To give LeWM's end-to-end representation the planning geometry observed in DINO-WM without replacing its encoder.
**Breakthrough (≤3 sentences):** The authors report SCALE improves every one of 15 task-solver combinations (5 tasks, 3 solvers) over baseline LeWM across five compute budgets, and that a control matching SCALE's decodability "yields less consistent planning gains," attributing the benefit to geometry.
**Tools & method (≤3 sentences):** A single lightweight regulariser correlating sampled pairwise latent distances with standardised state distances; no planning-time overhead.
**Limitation (≤3 sentences):** The authors state SCALE requires simulator state during training (image-only at test time), that state selection "acts as a task-dependent inductive bias," and that gains range from modest (Push-T, Reacher) to substantial (Two-Room, PointMaze).

---
## CaliBench: Are the Stochastic Dynamics of Video World Models Physically Calibrated?
- **arXiv:** 2608.16829 · https://arxiv.org/abs/2608.16829
- **Submitted:** 2026-08-17
- **Authors:** Jonathan Sadeghi, Jenny Seidenschwarz, Jesse Allardice, Sirish Srinivasan, Benjamin Graham, Jeffrey Hawke
- **Qualifying affiliation(s):** Odyssey — all authors; FLAG: borderline (world-model startup, not on the tracked list)
- **Categories:** cs.LG, cs.AI
- **Open release:** code (https://github.com/odysseyml/calibench)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** CaliBench tests whether video world models reproduce the correct statistical distribution of physical outcomes, evaluating six image-to-video models on nine scenes with analytically known outcome distributions (Galton boards, dice, roulette, cards and others).
**Purpose (≤3 sentences):** To measure distributional calibration, split into "scorability" (share of valid generations) and "calibration" (distance from the true outcome distribution).
**Breakthrough (≤3 sentences):** The authors report "severe probability mass over-concentration" in most models despite plausible individual frames, across 1,728 generations and 5,184 VLM queries; models include WAN-2.7, SeeDance-2.0, HappyHorse-1.0, Veo 3.1, Runway Gen-4.5 and Cosmos3-Super.
**Tools & method (≤3 sentences):** A Mean Normalised Total Variation metric over nine discrete-outcome scenes with closed-form references; VLM-based outcome extraction validated at 93.8% agreement.
**Limitation (≤3 sentences):** The authors state the benchmark covers image-to-video pipelines only, that VLM extraction adds noise, that it tests marginal outcome distributions rather than trajectories, and that it cannot audit commercial training corpora.

---
## ES3D: Embedding Semantics into 3D Space for Component-Aware Editing
- **arXiv:** 2608.15749 · https://arxiv.org/abs/2608.15749
- **Submitted:** 2026-08-16
- **Authors:** Xuancheng Jin, Rengan Xie, Jiayuan Lu, Wenting Zheng, Rui Wang, Yuchi Huo, Lincheng Li, Yingfeng Chen
- **Qualifying affiliation(s):** NetEase Fuxi AI Lab — Wenting Zheng, Yingfeng Chen
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ES3D embeds semantics directly into 3D space to enable component-aware retrieval and editing of a 3D asset, conditioned on one or more local reference images and an optional text query.
**Purpose (≤3 sentences):** Finer component-level control over 3D asset editing than text-only methods, with a local reference image specifying which part to change.
**Breakthrough (≤3 sentences):** The authors report CLIP score 32.19 (versus 29.02 IP-Adapter, 29.38 TRELLIS, 30.29 Fuse3D), ImageReward 0.5853 and CD_keep 0.91e-3 (versus 13.12 / 11.25 / 9.87), and a user study rating 4.4 to 4.8 out of 5 on quality, accuracy and preservation.
**Tools & method (≤3 sentences):** 3D semantic embeddings from multi-view feature projection; semantic component retrieval; inpainting-based editing with an "image stacking" strategy bridging local conditioning and global training.
**Limitation (≤3 sentences):** The authors state voxel-level retrieval produces noisy boundaries that need clustering for stable component identification.

---
## VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?
- **arXiv:** 2608.15265 · https://arxiv.org/abs/2608.15265
- **Submitted:** 2026-08-15
- **Authors:** Yansong Ning, Jingwen Ye, Zhongkai Wu, Yang Sun, Yiqin Zhu, Xingyi Li, Weidong Zhang, Hao Liu
- **Qualifying affiliation(s):** Tencent (TEG AIPD) — Jingwen Ye, Zhongkai Wu, Yang Sun, Yiqin Zhu, Xingyi Li, Weidong Zhang
- **Categories:** cs.AI
- **Open release:** weights, code and demo (https://github.com/usail-hkust/VibeWorlding-Gym; https://huggingface.co/collections/usail-hkust/vibeworlder; https://huggingface.co/datasets/usail-hkust/VWE-Bench)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A framework and benchmark testing whether multimodal agents can infer user intent, plan scene layout, invoke 3D tools and reflect on feedback to build 3D open worlds end to end, with VWE-BENCH covering 2,616 3D assets, 323 annotated worlds and 6,828 queries.
**Purpose (≤3 sentences):** To measure and improve autonomous end-to-end 3D world construction rather than single-step asset generation.
**Breakthrough (≤3 sentences):** The authors report GPT-5.5 and Qwen3.8-Max both below 60% success on their rubric-based verifier, and that their RL-trained open VibeWorlder-30B-A3B outperforms the closed models tested.
**Tools & method (≤3 sentences):** VibeWorlding-Gym with a dual-constraint rubric verifier, an asset-retrieval embedding model and a unified post-training framework; 8 NVIDIA H20 GPUs for 8B models and three nodes for the 30B-A3B model.
**Limitation (≤3 sentences):** No explicit limitations paragraph was found in the fetched text (observed, not stated).

---
## SCOPE: Score-Isolated Agentic Optimization for Video World Models
- **arXiv:** 2608.15043 · https://arxiv.org/abs/2608.15043
- **Submitted:** 2026-08-15
- **Authors:** Yuhua Jiang, Jiaming Wang, Qingbin Liu, Feifei Gao
- **Qualifying affiliation(s):** Tencent — Qingbin Liu
- **Categories:** cs.AI
- **Open release:** code (https://github.com/YuhuaJiang2002/SCOPE)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SCOPE is a framework for auditable inference-time adaptation of frozen video world models used as planning simulators, representing prompts, samplers, verifiers and selectors as a typed state updated only through bounded evidence-supported changes before freezing for held-out evaluation.
**Purpose (≤3 sentences):** To close the "inference-control evaluation gap" so that reported gains from agentic optimisation are trustworthy.
**Breakthrough (≤3 sentences):** On Physics-IQ the authors report +14.24 points over the frozen base on Wan2.2 (95% CI +8.10 to +21.23) and +12.60 on CogVideoX, while the margin over the strongest matched agentic baseline (+2.07 on Wan) "remains statistically unresolved."
**Tools & method (≤3 sentences):** Physics-IQ, PAI-Bench-G (judged by Qwen2.5-VL-72B), OpenS2V-Eval, PhyGround and PhyT2V on Wan2.2 and CogVideoX backbones.
**Limitation (≤3 sentences):** The authors state "strong candidate proposals do not necessarily imply reliable deployment decisions," that effectiveness "is not fully invariant across backbones or metrics," and that further progress needs calibrated uncertainty and selectors that generalise under shift.

---
## ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models
- **arXiv:** 2608.14022 · https://arxiv.org/abs/2608.14022
- **Submitted:** 2026-08-14
- **Authors:** Xinye Li, Lingshuai Lin, Lei Wang, Liuzhou Zhang, Jialin Cui, Qingshan Li, Guanchu Wang, Qingbin Liu, Xi Chen, Jiang Bian, Wai Lam
- **Qualifying affiliation(s):** Tencent PCG — Lingshuai Lin, Qingbin Liu, Jiang Bian
- **Categories:** cs.CV, cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ForgeWM converts bidirectional action-conditioned video generators into few-step (1, 2 or 4 step) causal world models for low-latency game-native control through four-stage progressive training, with an optional post-hoc "replay" refinement pass.
**Purpose (≤3 sentences):** Interactive, game-like applications that need low-latency causal generation with reliable response to discrete and continuous controls.
**Breakthrough (≤3 sentences):** The authors report the best results on 6 of 7 quality and control metrics against Matrix-Game 2.0 and HY-WorldPlay (ForgeWM-2: LPIPS 0.6171, mouse accuracy 0.8268 at 50.31 FPS and 239.7 ms latency) and a 60.7% pooled preference for ForgeWM-4 in a 41-participant study.
**Tools & method (≤3 sentences):** 40,000 clips from GF-Minecraft (352x640) and 65,246 clips across seven games for cross-game evaluation; eight GPUs with bf16 and fully sharded data parallelism.
**Limitation (≤3 sentences):** The authors identify long-horizon drift with visible artefacts beyond a 77-frame window, motion over-response (1.45x flow-magnitude ratio on FPS games), and a metric-dependent effect where a later stage raises sharpness but not paired reconstruction fidelity.

Near-misses (on-topic candidates excluded, with reason):
- 2609.00901 · HELIOS: From midnight to noon, continuous outdoor urban scene relighting (Huawei Paris) · off-topic on reading (2D image-to-image relighting of driving images, no 3D component)
- 2609.10457 · MotionCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (Tencent) · withdrawn by the authors on 2026-09-10 pending internal review
- 2608.23206 · Learning Spherical Occupancy Profiles for Multi-View 3D Reconstruction and Generation · academic-only
- 2609.03931 · Sparse auto-regressive modeling for scene generation from multi-view images · academic-only (NAVER LABS Europe, CMU)
- 2609.03334 · Laplacian Frequency Hierarchies for Efficient 3D Gaussian Splatting Training · academic-only (HIT Shenzhen, XGRIDS)
- 2609.01740 · ZipTok3D · academic-only
- 2609.06948 · PRG-Fusion · academic-only
- 2609.06436 · PLSR · academic-only
- 2609.00732 · Inverse Rig Optimization from Line Drawings · academic-only (University of Tokyo)
- 2609.01698 · VirSqueezer · academic-only
- 2609.02675 · Projective Affine Body Dynamics for Multibody Systems · affiliation unverifiable (no HTML; 22.9 MB PDF)
- 2609.03666 · WebXR and Commercial Game Engines for the Metaverse · academic-only
- 2609.01215 · REFACTOR-VLA · off-topic (robot manipulation)
- 2608.12564 · Scaling Automatic Research Agents via World Models · out of window (v1 2026-08-12)
- 2608.01397 · SG-WAM · out of window (v1 2026-08-02)
- 2609.07051 · TrojanWorld · academic-only (SJTU, NTU)
- 2609.06207 · PhysWeep · academic-only (Hamad Bin Khalifa University)
- 2609.02811 · Do Better Imagined Rollouts Mean Better Robot Control? · academic-only (Georgia Tech, Emory)
- 2609.02046 · Modeling What Changes: Sparse, Residual World Models · academic-only
- 2609.03774 · Rethinking World Models for Safety-Critical Embodied Systems · academic-only (KAIST)
- 2608.15156 · Low-Rank Dynamics-Effective Latent Carriers · academic-only (Fudan)
- 2608.16859 · HarnessEval-W · affiliation unverifiable (no institutions listed for 43 authors)
- 2608.29925 · Dior: Drawing the Light of Image via Material-Decoupled Illumination Representation (Kuaishou KlingAI) · off-topic on reading (2D single-image relighting, no 3D component); code and demo released at https://github.com/little-misfit/DiOR-Light
- 2608.09735 · HandSplatter · out of window (v1 2026-08-10)
- 2608.12442 · MV2 driving dataset · out of window (v1 2026-08-12)
- 2608.10712 · Compact Feed-Forward 3D Gaussians via Saliency-Guided Primitive Merging · out of window (v1 2026-08-11)
- 2608.18388 · Depth Anything V4 · withdrawn (v2, "Major errors in research")
- 2608.17298 · 3D Gaussian Accelerated Ray Tracing · academic-only (University of Canterbury)
- 2608.27301 · Comparative Evaluation of 3D Reconstruction Methods for Laboratory Objects · affiliation unverifiable; user study, not a method
- 2608.31159 · BRF-GS · academic-only (CAS); remote sensing
- 2608.31023 · SMG: Semantic Motion Graph for Monocular Dynamic Gaussian Splatting · academic-only (Cornell)
- 2608.28288 · GeoFF3D · academic-only; UAV mapping
- 2608.29538 · As-Rigid-As-Possible Deformation of Gaussian Radiance Fields · academic-only (Zhejiang University, University of Utah)
- 2608.28102 · What Will This Copper Look Like Later? · academic-only
- 2608.26383 · Cross-Platform Benchmark of Neural 3D Reconstruction for Autonomous Laboratory Robots · academic/government lab (Argonne)
- 2608.19567 · Block3D · academic-only
- 2608.19527 · Does Listening Matter? Backchanneling and Nodding in AI Clone (Sony CSL) · off-topic on reading (HCI user study of a conversational voice clone; no animation or graphics method)
- 2609.04250 · Motion-Omni: End-to-End Joint Speech and Full-Body Motion for Spoken Dialogue · affiliation "LIGHTSPEED" could not be confirmed as a tracked company from the paper (see GameWAM flag)
- 2608.21424 · EditStream (Adobe) · off-topic on reading (generic interactive video generation and editing)
- 2608.15763 · TaoLive Digital Avatar Agent Technical Report (Alibaba) · off-topic on reading (LLM agent-harness training for a livestream chat agent)
- 2608.11216 · AutoWorldModel-Bench · out of window (v1 2026-07-20)
- 2608.13552 · PlayWorld · out of window (v1 2026-08-13)
- 2608.13602 · Omni-LiveAvatar · out of window (v1 2026-08-07)
- 2608.14125 · Traj-LeWM · academic-only
- 2608.29904 · Off-Manifold Refinement · academic-only (Fulbright University Vietnam, UCLA)
- 2608.25572 · ConfAL-WM · academic-only (Tsinghua)
- 2608.22187 · BehaviorWorldGen · affiliation unverifiable ("AFARI World Model Team" only)
- 2608.21075 · AudioWorldSim · academic-only (IMPA)
- 2608.18484 · Partition the Support, Reconstruct the Residual · academic-only (Texas A&M)
- 2608.17542 · No Gaussian Required (Quantexa) · non-qualifying company
Verification: every listed paper was checked twice against arXiv (v1 date and title on the abstract page; affiliations read from the paper's HTML or PDF author block; topic confirmed from the abstract) before inclusion. 21 papers list an open release (weights, code or demo).

# Part B — Research → Product
Window: last 90 days (2026-06-15 to 2026-09-13). Qualifying products: 12 (12 new, 0 previously reported, 3 flagged). Announced-only: 4. Open releases moved to Part A: 1. Retrieval: GitHub Releases API (rate-limited after 41 repo queries; NVIDIA orgs only, no qualifying leads) plus per-company newsroom/docs sweep via web search and fetch of primary pages. No prior `product_seen.json`, so every item is New.

---
## NVIDIA DLSS 5 with 3D-Guided Neural Rendering (in NBA 2K27)
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-09-03 · **New**
- **Surface:** shipped game feature (driver + game integration)
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/nba-2k27-dlss-5-3d-guided-neural-rendering-geforce-game-ready-driver/
- **Underlying research:** no traceable paper (NVIDIA's post cites none)
- **Availability:** GeForce RTX 50 Series GPUs only at launch; requires GeForce Game Ready Driver 616.64 WHQL; first and only title is NBA 2K27; no extra cost beyond the game and GPU.

**What shipped:** NVIDIA states "DLSS 5 is available now in the newly-released NBA 2K27" and that DLSS 5 introduces "3D-Guided Neural Rendering, infusing games with lifelike lighting and materials using advanced artist-guided AI models." It ships alongside Game Ready Driver 616.64.
**What research it translates:** NVIDIA describes an AI model that takes per-frame game colour and motion data and infers lighting and materials, positioned as the successor to the upscaling and frame-generation stages of earlier DLSS versions. No paper is cited.
**Practical significance:** Owners of RTX 50 Series hardware and NBA 2K27 get AI-modified lighting and materials (skin, hair, contact shadows per NVIDIA's description) in a shipped title today. NVIDIA reports NBA 2K27 reaching "370 FPS at 4K at Ultra Settings, with ray tracing, on a GeForce RTX 5090" with DLSS enabled.
**Engineering details:** Delivered through the GeForce driver and a game-side integration; inputs are the game's rendered colour and motion vectors; RTX 50 Series exclusive at launch.
**Limitation / caveats:** NVIDIA states RTX 40 Series support is planned but not available at launch. Only one game supports DLSS 5 as of the window's end (observed, not stated).

---
## NVIDIA DLSS 4.5 Ray Reconstruction, 2nd-generation transformer model (early access)
- **Company:** NVIDIA
- **Status:** Public beta/preview (NVIDIA App early access) · **Released:** 2026-08-25 · **New**
- **Surface:** app feature / driver
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/gamescom-2026-dlss-4-5-ray-reconstruction-release-announcements-trailers/
- **Underlying research:** no traceable paper
- **Availability:** Opt in via NVIDIA App (Settings > About > Early Access releases); requires GeForce Game Ready Driver 580.88 WHQL or newer; applicable to 30 games at time of writing (Alan Wake 2, Cyberpunk 2077, Portal with RTX, Indiana Jones and the Great Circle, Star Wars Outlaws among them). NVIDIA states "an official release will follow in September."

**What shipped:** NVIDIA states a "new 2nd generation transformer model" for DLSS Ray Reconstruction with "35% more compute capability" that "processes 20% more parameters, while maintaining similar performance to the previous model." It is available now as an early-access download.
**What research it translates:** An updated neural denoiser/reconstruction model for ray- and path-traced imagery in the DLSS Ray Reconstruction line. No paper is named.
**Practical significance:** Owners of RTX GPUs can apply the new model to 30 existing titles through the NVIDIA App without waiting for per-game patches.
**Engineering details:** Distributed via NVIDIA App override rather than game updates; driver 580.88 or newer required.
**Limitation / caveats:** Early-access status; NVIDIA gives only "September" for the official release and no numeric image-quality metrics. Whether the official release landed before 2026-09-13 was not confirmed from a primary source (observed, not stated).

---
## Autodesk 3ds Max 2027.2 — native 3D Gaussian Splat support
- **Company:** Autodesk — FLAG: not on the tracked list; comparable DCC vendor, included for the reader to judge
- **Status:** GA · **Released:** 2026-07-22 per trade press (CG Channel, 80.lv, CGPress); Autodesk's own pages are undated — FLAG · **New**
- **Surface:** studio tool (DCC application)
- **Primary source:** https://help.autodesk.com/cloudhelp/2027/ENU/3dsMax-WhatsNew/files/GUID-D11D1F34-C9FF-4981-AAE3-5A969986FCF4.html
- **Underlying research:** no traceable paper (Autodesk does not cite the 3DGS literature on the page)
- **Availability:** Included in the 3ds Max 2027.2 update for subscribers; Arnold for 3ds Max (MAXtoA) 5.9.3.0 bundled.

**What shipped:** Autodesk states "New 3D Gaussian Splat (3DGS) support in 3ds Max 2027.2 provides fast rendering, simple editing, and hyper-accurate output," with a new point object type and point-data modifiers to "edit 3DGS data or create point data from scratch." Arnold "now works with native 3ds Max 3DGS data."
**What research it translates:** Gaussian-splat radiance-field captures become a native, editable asset type in a mainstream DCC tool.
**Practical significance:** 3ds Max users can import, edit with standard modifiers, and render splat captures in Arnold without third-party plugins, per Autodesk.
**Engineering details:** New Points object type and Point Instance modifier (also usable for render-time instancing); Arnold 5.9.3.0 adds 3DGS rendering, a Shader to RGBA node and denoiser updates. Trade coverage lists PLY, SPZ and LCC import formats; the Autodesk What's New page fetched does not list formats.
**Limitation / caveats:** Release date not stated on Autodesk's own documentation pages (observed, not stated). No performance numbers given for splat rendering.

---
## Adobe Substance 3D Painter 12.1, Designer 16 and Sampler update (OpenPBR)
- **Company:** Adobe
- **Status:** GA · **Released:** 2026-07-21 · **New**
- **Surface:** studio tool
- **Primary source:** https://blog.adobe.com/en/publish/2026/07/21/adobe-substance-3d-unveils-new-innovations-deliver-faster-workflows-openpbr-everywhere-digital-twins-scale
- **Underlying research:** no traceable paper
- **Availability:** Substance 3D Collection desktop apps; Adobe states it released its "production-proven OpenPBR implementation as open source on GitHub."

**What shipped:** Adobe states Painter 12.1 adds Skew Map Painting, Auto Rebake (rebakes only affected mesh portions), a Hard Surface Auto UV mode and OpenPBR support; Designer 16 adds a Shape Splatter v2 node, Signed Distance Field nodes, a 3D Viewer node and new displacement controls; Sampler adds Material Creation Templates.
**What research it translates:** Adoption of the open OpenPBR shading model across the texturing pipeline, plus procedural-geometry (SDF) authoring inside Designer.
**Practical significance:** Adobe states the Assets library now holds 23,516 assets and that "14,000+ materials, decals, and atlases are being converted to OpenPBR," giving artists a portable material standard across tools.
**Engineering details:** OpenPBR supported end to end from Sampler through Painter; SDF and 3D Viewer nodes in Designer 16; open-source OpenPBR implementation on GitHub.
**Limitation / caveats:** No generative (Firefly) 3D features are mentioned in this release (observed, not stated). Pricing and subscription terms are not stated in the post.

---
## Fortnite / UEFN v41.20 — Control Rig for Sidekicks, in-world UMG widgets, LLM-powered NPCs
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-07-16 (LLM NPC publishing exits Experimental 2026-07-30) · **New**
- **Surface:** shipped game / creator tool (UEFN)
- **Primary source:** https://dev.epicgames.com/documentation/fortnite/41-20-fortnite-ecosystem-updates-and-release-notes-in-fortnite
- **Underlying research:** no traceable paper
- **Availability:** Live for all UEFN creators; LLM-powered NPC islands publishable from 2026-07-30.

**What shipped:** Epic's release notes state Control Rig support for Sidekicks arrives with "three archetypes — Dog Large, Dog Small, and Cat Small" built on Epic's internal rig structures; creators can "drag your UMG User Widget from the content browser into the viewport to display your UI in the level"; and on July 30 LLM conversations "exit Experimental and you'll be able to publish islands with LLM-powered NPCs and characters."
**What research it translates:** Epic's internal animation-rig tooling exposed to creators, and an LLM dialogue system for NPCs moving from experimental to publishable status.
**Practical significance:** Epic states it provides "consistent voices and personas to 36 Fortnite characters when used as NPCs," so creators can ship voiced, LLM-driven NPCs without engine code.
**Engineering details:** Control Rig limited to the three archetypes at launch; in-world widgets keep existing UMG functionality including Verse fields and UI animations.
**Limitation / caveats:** Epic states 36 characters get voices "with more coming over time," so coverage is partial at launch.

---
## Roblox Build — mobile AI creation tab (public alpha, New Zealand)
- **Company:** Roblox
- **Status:** Public beta/preview (public alpha) · **Released:** 2026-07-28 (announced 2026-07-16) · **New**
- **Surface:** app feature
- **Primary source:** https://about.roblox.com/newsroom/2026/07/build-without-limits-on-roblox
- **Underlying research:** no traceable paper
- **Availability:** Roblox states select Build features "will be available in public alpha to users in New Zealand beginning July 28," for age-checked users 9 and older; published games playable globally by age-checked users 16 and older; wider rollout "over the coming months."

**What shipped:** Roblox states a mobile-first creation tab inside the Roblox app that uses its AI tools, including Cube, which "turns a prompt into game-ready objects, from simple props to vehicles that drive and weapons that shoot," and already-launched Procedural Models.
**What research it translates:** Roblox's in-house 3D generative model (Cube) applied to an on-device, agentic creation flow for non-Studio users.
**Practical significance:** Users in one region can build and publish playable experiences from a phone without Roblox Studio, per Roblox.
**Engineering details:** Age-gated (9+ to build, 16+ to publish); region-gated (New Zealand first).
**Limitation / caveats:** Roblox states a scene-generation model and playtesting, analytics and experiment agents are "coming soon" rather than included; the alpha is limited to one country.

---
## Upgraded PSSR in Doom: The Dark Ages on PS5 Pro (Free Update 4)
- **Company:** Sony Interactive Entertainment (platform feature; post authored by id Software's Billy Khan on the PlayStation Blog)
- **Status:** GA · **Released:** 2026-07-07 · **New**
- **Surface:** shipped game / console platform feature
- **Primary source:** https://blog.playstation.com/2026/06/24/upgraded-pssr-comes-to-doom-the-dark-ages-on-ps5-pro/
- **Underlying research:** no traceable paper
- **Availability:** PS5 Pro only; free update shipping with Doom: The Dark Ages | Revelations on 2026-07-07.

**What shipped:** The PlayStation Blog states the upgraded PlayStation Spectral Super Resolution (PSSR) ML upscaler is applied to Doom: The Dark Ages on PS5 Pro from the July 7 update.
**What research it translates:** id Software's Billy Khan writes that PSSR "uses information such as motion, depth, exposure and sub-pixel sampling" from the idTech renderer to reconstruct a higher-resolution frame. No paper or model name is given.
**Practical significance:** PS5 Pro owners of the game receive the new upscaler at no cost; the post presents it as a clarity improvement most visible in motion.
**Engineering details:** Runs on PS5 Pro's ML reconstruction hardware with engine-provided motion, depth and exposure buffers; PS5 Pro exclusive.
**Limitation / caveats:** The post states its comparison images should be read "less as a color-grading comparison and more as a clarity comparison"; no numeric quality or performance figures are given.

---
## 《逆水寒：新世界》 (Justice Online: New World) character rendering upgrade
- **Company:** NetEase
- **Status:** GA · **Released:** 2026-06-26 · **New**
- **Surface:** shipped game (live MMO update)
- **Primary source:** https://h.163.com/news/official/20260612/37231_1304115.html
- **Underlying research:** no traceable paper
- **Availability:** Delivered in the existing 逆水寒 client (China); free-to-play title.

**What shipped:** NetEase's official channel states the New World version brings "全新超精度面部模型" (a new ultra-high-precision facial model) with improved contours, texture and lighting, a lighting system where hair stays clear when backlit ("逆光也清晰、发丝会呼吸"), and a "立体进化" (3D evolution) of hair-strand and cloth dynamics.
**What research it translates:** An internal character-rendering and simulation pipeline overhaul; no method or paper is named.
**Practical significance:** Existing players receive the upgraded characters automatically with the 2026-06-26 patch.
**Engineering details:** NetEase states improvements across facial geometry, muscle definition, hair lighting and hair/cloth dynamics; no engine, middleware or hardware targets are disclosed.
**Limitation / caveats:** The source is a patch announcement, not a technical document; no performance or platform specifics (observed, not stated).

---
## AMD FSR SDK 2.3 — FSR Upscaling 4.1.1 on RDNA 3
- **Company:** AMD — FLAG: not on the tracked list; comparable GPU vendor, included for the reader to judge
- **Status:** GA · **Released:** 2026-06-24 · **New**
- **Surface:** SDK
- **Primary source:** https://gpuopen.com/learn/amd-fsr-sdk-2-3-blog/
- **Underlying research:** no traceable paper
- **Availability:** AMD states "AMD FSR SDK 2.3 binaries and limited source are now available on GitHub"; ML-based FSR Upscaling 4.1.1 now supports Radeon RX 7000 Series (RDNA 3) discrete GPUs.

**What shipped:** SDK bundling FSR Upscaling 4.1.1, FSR Frame Generation 4.0.1 and FSR Ray Regeneration 1.2.0, extending the ML upscaler from RDNA 4 to RDNA 3 cards.
**What research it translates:** AMD's machine-learning upscaling model family made available to a previous GPU generation.
**Practical significance:** AMD states RDNA 3 owners get "image quality that closely matches what is already available on" RDNA 4, once developers integrate the SDK.
**Engineering details:** Frame Generation and Ray Regeneration remain "AMD Radeon RX 9000 Series GPUs and above" with analytical fallbacks for older hardware; distributed as binaries plus limited source.
**Limitation / caveats:** Requires per-game integration by developers; AMD gives no numeric performance metrics; RDNA 2 not included.

---
## Unreal Engine 5.8 (MetaHuman Animator markerless capture, MetaHuman Collections, Mesh Terrain, MegaLights, MCP plugin)
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-06-17 · **New**
- **Surface:** engine
- **Primary source:** https://forums.unrealengine.com/t/unreal-engine-5-8-released/2729274 (Epic staff announcement; the unrealengine.com news page returned HTTP 403 to fetch)
- **Underlying research:** no traceable paper
- **Availability:** "Download now on the Epic Games Launcher, GitHub, or our Linux page"; standard UE licensing.

**What shipped:** Epic states "MetaHuman Animator now supports markerless motion capture, enabling full-body and facial performance capture using something as simple as a single webcam"; MetaHuman Collections for scalable crowds; Mesh Terrain, "a new 3D mesh-based landscape system"; MegaLights "now Production-Ready"; a new MCP plugin that "connects LLMs directly to Unreal Engine"; and Lumen Lite.
**What research it translates:** Markerless video-based performance capture for MetaHuman characters and a production-ready many-light renderer.
**Practical significance:** Developers can capture body and face animation from a single webcam and light scenes with large numbers of dynamic shadowed lights, per Epic. Epic states Lumen Lite is "up to twice as fast as Lumen High Quality."
**Engineering details:** Hotfix 5.8.1 followed on 2026-07-28 with "over 260 fixes and updates" per Epic staff; 5.8.2 followed later.
**Limitation / caveats:** Mesh Terrain and MetaHuman Collections are labelled experimental in Epic's announcement; markerless capture quality is not quantified.

---
## HappyOyster 1.0 (快乐生蚝 1.0) — real-time interactive world model
- **Company:** Alibaba (ATH Innovation Business Group) — FLAG: attribution comes from consistent trade coverage (GeekPark, IT之家, Leiphone) and the site is served from Alibaba's CDN; no Alibaba newsroom statement was found
- **Status:** Public beta/preview · **Released:** 2026-06-17 per GeekPark; date not shown on the product site — FLAG · **New**
- **Surface:** consumer web app
- **Primary source:** https://www.happyoyster.cn
- **Underlying research:** no traceable paper
- **Availability:** Web app with open registration and daily free credits per GeekPark's report; the product site states API access will open soon ("近期还会全面开放 API 接口").

**What shipped:** The product site describes "一款实时可交互的开放世界模型产品" (a real-time interactive open-world model product) with a 执导 (Directing) mode to steer a continuously evolving world by text, voice or image, and a 漫游 (Wandering) mode for first-person exploration.
**What research it translates:** Described as a natively multimodal world model with joint audio-video generation and long-horizon consistency; no architecture or paper is named on the site.
**Practical significance:** Anyone can register and generate an explorable world from a sentence or image, per the site; stated target uses are games, short drama, virtual companions and tourism.
**Engineering details:** Text, voice and image input; first-person navigation; synchronized audio-video output; API not yet live.
**Limitation / caveats:** No pricing, quota, region or hardware details on the site; company attribution and release date are not stated on the primary page (observed, not stated).

---
## NVIDIA ACE Game Agent SDK (beta) and ACE plugins for Unreal Engine 5
- **Company:** NVIDIA
- **Status:** GA (UE5 plugins) / Public beta (Game Agent SDK) · **Released:** 2026-06-16 · **New**
- **Surface:** SDK / engine plugin
- **Primary source:** https://developer.nvidia.com/blog/build-on-device-ai-companions-with-the-nvidia-ace-game-agent-sdk-and-unreal-engine-5-plugins/
- **Underlying research:** no traceable paper (the post references NVIDIA's open-source Kimodo motion project without an arXiv id; see Part A open releases)
- **Availability:** NVIDIA states "a new suite of NVIDIA ACE plugins is now available" for UE5 and that developers can "download the NVIDIA ACE Game Agent SDK in beta"; on-device inference.

**What shipped:** An on-device conversational-companion pipeline for games: ASR ("nemo-conformer-ctc-120m"), a "Qwen 3.5 4B model" for function calling, and the "Chatterbox Turbo 350M TTS model," packaged as UE5 plugins and an SDK.
**What research it translates:** NVIDIA's ACE digital-human stack repackaged around small open models for local NPC dialogue; NVIDIA also describes Kimodo as "an open source project for promptable, controllable human motion."
**Practical significance:** UE5 developers can add local, non-cloud voice-interactive companions today, per NVIDIA.
**Engineering details:** Referenced against Unreal Engine 5.7; components are swappable open models; hardware requirements are not stated in the post.
**Limitation / caveats:** The SDK itself is labelled beta; no latency or quality figures are given.

### Announced only (not yet usable)
- Unity 7 roadmap (early beta targeted December 2026) · Unity · 2026-07-21 · https://unity.com/news/unity-7-roadmap-revealed-at-unite-seoul
- Adreno Neural Fusion (AI rendering pipeline for an unreleased Snapdragon) · Qualcomm · 2026-09-02 · https://www.qualcomm.com/news/onq/2026/09/adreno-neural-fusion-ai-rendering
- Roblox scene-generation model and playtesting/analytics/experiment agents ("coming soon") · Roblox · 2026-07-16 · https://about.roblox.com/newsroom/2026/07/build-without-limits-on-roblox
- NVIDIA ACE in Aniimo ("early 2027") · NVIDIA · 2026-08-25 · https://www.nvidia.com/en-us/geforce/news/gamescom-2026-dlss-4-5-ray-reconstruction-release-announcements-trailers/

Near-misses: PUBG "Ally Duo" AI companion beta (Krafton, borderline company; time-limited beta 2026-06-17 to 07-01, not usable today; https://pubg.com/en/news/10179) · NVIDIA Omniverse Kit 110.3 (August 2026 maintenance release, no feature on the four topics) · visionOS 27 RealityKit Gaussian splatting (Apple; developer beta 2026-06-08 before window, GA 2026-09-14 after window) · NVIDIA Cosmos 3 (2026-06-01, before window; open weights) · ByteDance Seedance 2.5 API (2026-08-07; general video generation, off-topic) · Huawei-hosted MoWorld-3D (developer is untracked MoCore; Huawei provides compute only) · Kling (no in-window feature verified from a primary source) · Meta "Hologram" avatar calling (app teardown only, unverified) · AWS "open source 3D game asset generation" post (tutorial, not a product) · Xbox Gaming Copilot on console (trade press only, no Microsoft primary source) · Tencent MagicDawn NDGI and 代号Craft (announced 2026-05-27/28, before window) · Intel, Baidu, miHoYo, Microsoft, Google, Meta, Amazon, Apple, Ubisoft, EA: no verified in-window items on the four topics.
Verification: every item above was double-checked by fetching the listed primary URL in a second pass (date, company, tier and quoted claims confirmed); the two flagged dates and the HappyOyster attribution could not be confirmed from a primary page and are marked as such.
