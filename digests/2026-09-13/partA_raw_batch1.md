# Part A verified blocks — batch 1 (as returned by verification agents; to be assembled/edited)

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

# Near-misses (batch 1)
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
