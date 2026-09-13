# Part A verified blocks — batch 2a (3D)

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

# Near-misses (batch 2a)
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
