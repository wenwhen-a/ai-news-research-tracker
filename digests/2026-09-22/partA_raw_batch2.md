## VGGT-Prime: Compute-Adaptive Mixture-of-Heads for Efficient Visual Geometry Transformers
- **arXiv:** 2609.23733 · https://arxiv.org/abs/2609.23733
- **Submitted:** 2026-09-20
- **Authors:** Abteen Arab, Guile Wu, Chengjie Huang, Dongfeng Bai
- **Qualifying affiliation(s):** Huawei Noah's Ark Lab — Guile Wu, Chengjie Huang, Dongfeng Bai (Abteen Arab: Huawei Canada internship + University of British Columbia); FLAG: borderline
- **Categories:** cs.CV
- **Open release:** project page at https://vggt-prime.github.io (no explicit code/weights release statement found)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** VGGT-Prime is a compute-adaptive variant of the Visual Geometry Transformer (VGGT) that speeds up multi-view 3D reconstruction (camera pose, depth, point clouds) by exploiting redundancy across attention heads rather than tokens. A lightweight router dynamically assigns each attention head to one of three computation modes based on its importance. The authors report 8x inference speedup over VGGT alone, and 14x when combined with token merging, while maintaining competitive geometric accuracy.

**Purpose (≤3 sentences):** Visual geometry transformers like VGGT suffer from quadratic attention cost as the number of input views grows, limiting their use on long image sequences. The authors note prior efficiency work targets token-level redundancy, leaving head-level architectural redundancy unaddressed. This paper aims to close that gap for practical multi-view 3D reconstruction.

**Breakthrough (≤3 sentences):** The authors report that attention heads in VGGT fall into distinct high/medium/low-saliency tiers (identified via integrated-gradient and attention-magnitude analysis), and that most heads can be replaced with cheaper surrogates without hurting accuracy. They report an 8x speedup on 1000-frame sequences (14x with token merging) while preserving Chamfer distance, camera-pose (RTA/AUC), and depth (AbsRel, δ<1.25) metrics comparable to full VGGT. They also report the approach generalizes to other backbones (VGGT-Ω, π³, Depth Anything 3) with roughly 2x speedup.

**Tools & method (≤3 sentences):** The method routes high-saliency heads to full softmax attention, medium-saliency heads to a learned surrogate attention with query pooling and residual correction, and low-saliency heads to simple mean pooling, trained via two-stage distillation from a frozen VGGT teacher. Evaluation used ScanNet, 7-Scenes, ETH3D, CO3Dv2, RealEstate10K, Sintel and Bonn, with training across 13 datasets including BlendedMVS, Mapillary and ScanNet++, implemented in PyTorch 2.12.0/CUDA 13.0 with xFormers/Triton, and evaluated with Open3D, PyCOLMAP and Trimesh.

**Limitation (≤3 sentences):** The authors state the method relies on a frozen teacher model, which "limits the method to matching the teacher rather than surpassing it." They identify training directly against ground truth (rather than distillation targets) as future work.

## ConsistWorld: Evidence Routing for Consistent Multi-Agent World Models
- **arXiv:** 2609.22641 · https://arxiv.org/abs/2609.22641
- **Submitted:** 2026-09-18
- **Authors:** Qianxun Xu, Xianfang Zeng, Xinyao Liao, Wei Cheng, Gang Yu, Chi Zhang
- **Qualifying affiliation(s):** StepFun — Xianfang Zeng, Xinyao Liao, Wei Cheng, Gang Yu (Qianxun Xu also lists StepFun alongside Westlake University and UCLA); FLAG: borderline
- **Categories:** cs.CV
- **Open release:** code (https://github.com/CeciliaTheBirb/ConsistWorld), weights (https://huggingface.co/CeciliaXu00/ConsistWorld), eval data (https://huggingface.co/datasets/CeciliaXu00/multicam_no_person)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ConsistWorld is a multi-agent video world model that generates camera-controlled video streams of a static scene from a single shared source image, with multiple independently steered "agents" (viewpoints) exploring the same world. It introduces two mechanisms to keep the different camera streams visually consistent with each other and with themselves over time. The authors report it maintains strong cross-time and cross-agent consistency while preserving competitive generation quality across several evaluation settings.

**Purpose (≤3 sentences):** Existing autoregressive video world models handle a single observer well, but extending them to several independently-controlled cameras raises the problem of keeping revisited or jointly-explored regions of the world visually consistent across agents and over long time horizons. The paper targets this multi-agent consistency gap in interactive world simulation. It frames "committed observations" established by one agent as constraints subsequent generations from any agent must respect.

**Breakthrough (≤3 sentences):** The authors report that "Pose Conditioned Memory Retrieval" (selecting relevant historical observations via camera-geometry overlap rather than keeping full history active) and "Visibility-Gated Peer Sharing" (a gate that suppresses peer information over already-committed regions while preserving it for new content) together substantially reduce inconsistency. They report Region-LPIPS scores of 0.1181 (self-revisit), 0.1179 (synchronous cross-agent sharing) and 0.0700 (asynchronous cross-agent handoff), and that removing retrieval causes Region-LPIPS to worsen to 0.3374. They also report the model remains stable when extended to 32 autoregressive chunks beyond its 9-chunk training horizon, and generalizes to an unseen agent count (K=5).

**Tools & method (≤3 sentences):** Training proceeds in two stages: first on MultiCamVideo (3,400 Unreal Engine-rendered scenes with ten cameras, 81 frames at 240x416), then on 1,000 Infinigen scenes with eight synchronized cameras (141 frames). Evaluation uses held-out MultiCamVideo and Infinigen scenes plus Ditto-1M real-world images, measured with Region LPIPS, LPIPS-MG, GT-LPIPS, VBench (IQ/AQ), PSNR and SSIM; the authors also report GT-LPIPS of 0.4206 versus 0.5203 for a full-history baseline.

**Limitation (≤3 sentences):** The paper does not include an explicit limitations section, but notes that some directly comparable methods lacked released code, preventing direct quantitative comparison. The work is scoped to static scenes generated from a single starting image and requires camera calibration/pose data as input.

## D3GS: Depth, DINO, and RGB Diffusion Co-Guided 3D Gaussian Splatting for Sparse-View Reconstruction
- **arXiv:** 2609.22941 · https://arxiv.org/abs/2609.22941
- **Submitted:** 2026-09-19
- **Authors:** Yunqi Gao, Zhanfeng Liao, Hanzhang Tu, Zhaoqi Su, Guoqing Zheng, Songtao Wang, Hongwen Zhang, Zhou Xue, Leyuan Liu, Yebin Liu
- **Qualifying affiliation(s):** ByteDance Inc. — Zhou Xue
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** D3GS is a 3D Gaussian Splatting method for reconstructing scenes from only a few input views, combining metric depth estimation, DINO-feature-guided multi-view consistency, and diffusion-based novel-view refinement. The authors report consistent, substantial improvements over strong sparse-view baselines on standard benchmarks. Ablations reportedly confirm each of the three guidance components contributes to the gains.

**Purpose (≤3 sentences):** Sparse-view 3D Gaussian Splatting suffers from ambiguous geometry, cross-view inconsistency, and missing detail in regions under-constrained by the few available views, which degrades reconstruction quality and rendering stability. The paper aims to address these three failure modes jointly rather than individually.

**Breakthrough (≤3 sentences):** The authors report that combining (1) high-resolution metric depth recovered via diffusion-based completion and DPT refinement, (2) DINOv3-feature-based multi-view consistent supervision, and (3) single-step diffusion refinement of rendered novel views fed back into the Gaussians, yields consistent gains over baselines such as CoR-GS, BinocularGS and Difix3D+. Reported 3-view results include PSNR/SSIM/LPIPS of 21.47/0.775/0.131 on LLFF, 21.34/0.876/0.087 on DTU, and 17.69/0.538/0.442 on Mip-NeRF 360.

**Tools & method (≤3 sentences):** The pipeline uses MapAnything and bundle adjustment for sparse metric depth, a denoising U-Net plus DPT decoder for high-resolution metric depth completion, DINOv3 features (top-3 PCA components) attached to each Gaussian for cross-view consistency, and a single-step diffusion model fine-tuned on the SynCamMaster dataset for iterative novel-view refinement. Experiments were run on standard 3/6/9-view splits of LLFF, DTU, and Mip-NeRF 360 using an NVIDIA RTX 3090 GPU, training 15,000 iterations per scene.

**Limitation (≤3 sentences):** The authors acknowledge computational overhead of roughly 25 minutes per scene from depth estimation, feature extraction and diffusion processing combined. They note future work should focus on reducing this overhead and extending the framework to dynamic scenes via temporal modeling.

# Near-misses
- 2609.23010 · MixiMotion: One-Step Text-to-Motion Generation via Asymmetric Set Distillation · no arXiv HTML version available, so affiliation could not be verified; author list (Hung Dinh, Binh Mai, Tran Quoc Bao Le, Lam Nguyen, Cong Tran) shows no evidence of the claimed Google affiliation.
- 2609.23142 · CraftBench-UE: Deterministic Evaluation for Coding Agents in Unreal Engine · confirmed affiliations are University of Rochester and RamenVR (a small indie VR studio), not Google as pre-screened; RamenVR is not a qualifying or borderline top-tier company, so it fails the affiliation gate.
- 2609.22519 · The Choreographic Genome: Amplifying the Silent Structure of Text into Dance · no arXiv HTML version available, so the claimed Google affiliation could not be verified (only 2 listed authors, no visible industry affiliation in the abstract page).
- 2609.22611 · HIGenNTO: Scalable Humanoid Interaction Generation via Noise-Space Trajectory Optimization · confirmed affiliations are Carnegie Mellon University and Keio University only, a purely academic paper with no industry co-author (not Google as pre-screened); additionally the work targets deployment of physical control policies on a Unitree G1 robot, which falls under excluded robotic-manipulation/physical-control topics rather than the tracked topics.
