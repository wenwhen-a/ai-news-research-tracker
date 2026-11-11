# Part A — Papers
Window: last 30 days (2026-10-12 to 2026-11-11). Categories: cs.GR, cs.CV, cs.LG, cs.AI, cs.RO. Retrieval: API (arxiv_fetch.py, 614 in-window candidates; incremental screen vs state/papers_seen.json left 27 new ids to screen, 7 hits verified against HTML/abs pages). Qualifying papers: 3 (1 flagged).

---
## FlashMotion: Ultra-Fast Long-Term 3D Motion Generation
- **arXiv:** 2611.13626 · https://arxiv.org/abs/2611.13626
- **Submitted:** 2026-11-10
- **Authors:** Kaixing Yang, Xulong Tang, Ronghui Li, Xiangyue Zhang, Ziqiao Peng, Mingshuang Luo, Chenxi Zhao, Haoyu Wu, Ju Fan, Hongyan Liu, Puwei Wang, Zijiao Zeng, Jun He
- **Qualifying affiliation(s):** Tencent — Mingshuang Luo, Zijiao Zeng ("This work was conducted at Tencent IEG Motus Group")
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** FlashMotion is a framework for generating long 3D human motion sequences — text-to-motion, music-to-dance, and speech-to-gesture — under a tight inference budget. It combines a 3D motion-space MeanFlow formulation with a lightweight non-autoregressive BiMamba architecture.
**Purpose (≤3 sentences):** The authors target existing motion-generation methods being too slow for long-sequence or interactive use, aiming to cut both the number of required sampling steps and the compute cost per step.
**Breakthrough (≤3 sentences):** The authors report their 4-step model reaches 46,303 FPS at 10,000 frames on BABEL text-to-motion — 13.6× the throughput of the fastest external text-to-motion baseline they compare against — while reporting mixed quality results: FID of 0.907 on BABEL trails FloodDiffusion's 0.542, and FIDg of 21.13 on FineDance trails FlowerDance's 19.59, though FIDk (15.15 vs. 29.73) and BEAT2 FGD (0.3242 vs. SemTalk's 0.356) lead.
**Tools & method (≤3 sentences):** The method uses kinematic/dynamic-consistency-constrained MeanFlow sampling plus an Adaptive Soft masking mechanism for motion editing, evaluated on BABEL, FineDance, and BEAT2; benchmarks ran on an NVIDIA RTX 3090 GPU with an Intel Xeon Gold 5218 CPU, and a mobile test generated 200 frames in ~400ms on an iPhone 17.
**Limitation (≤3 sentences):** The paper has no dedicated limitations section; the conclusion lists future directions (finer facial/finger modeling, reducing motion artifacts in longer-sequence generation) and the method section notes 1-step sampling does not support motion editing.

---
## Camera3R: Feed-Forward 3D Reconstruction from Heterogeneous Camera Models
- **arXiv:** 2611.13453 · https://arxiv.org/abs/2611.13453
- **Submitted:** 2026-11-10
- **Authors:** Ruxiao Duan, Yunwen Zhou, Erin Hong, Dongxu Zhao, Eric Turner, Federico Tombari, Alex Wong
- **Qualifying affiliation(s):** Google — Yunwen Zhou, Erin Hong, Dongxu Zhao, Eric Turner, Federico Tombari (affiliation block lists "@google.com"; Ruxiao Duan and Alex Wong are dual-affiliated with Yale University)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Camera3R is a low-rank adaptation (LoRA) framework that extends feed-forward 3D reconstruction networks pretrained on perspective images to other camera models (fisheye, panoramic) without full retraining.
**Purpose (≤3 sentences):** Most feed-forward 3D reconstruction networks are trained only on perspective images and fail on fisheye or panoramic cameras; the authors adapt pretrained perspective models to heterogeneous camera geometries cheaply.
**Breakthrough (≤3 sentences):** Applied to the π³ baseline, the authors report relative rotation accuracy rising from 0.540 to 0.990 on the fisheye ADT benchmark and from 0.076 to 0.978 on the panoramic Stanford2D3DS benchmark, while adding ~0.5% extra parameters, training in under a day, and leaving perspective-image performance unchanged.
**Tools & method (≤3 sentences):** The framework uses synthetic cross-camera distortion augmentation with separate LoRA experts per camera category, trained on ScanNet++, ASE, KITTI360, Matterport3D, Gibson, TartanAirV2, and PanoCity, using 8 NVIDIA RTX 6000 Blackwell (48GB) GPUs.
**Limitation (≤3 sentences):** The authors state the method assumes each input image belongs to one of a predefined set of camera categories, so a new camera model requires training an additional LoRA expert; they also note the synthetic cross-camera distortion augmentation may not fully capture real lens- and sensor-specific effects.

---
## RF3DGS: Reflection-Free 3D Gaussian Splatting with Self-Priors
- **arXiv:** 2611.13772 · https://arxiv.org/abs/2611.13772
- **Submitted:** 2026-11-10
- **Authors:** Qiang Wen, Guotao Meng, Junhong Ruan, Hongyu Liu, Chenyang Lei, Qifeng Chen
- **Qualifying affiliation(s):** Huawei Research — Chenyang Lei (other authors: Hong Kong University of Science and Technology); **FLAG: borderline** (Huawei is not on the core tracked list — per product-criteria.md, kept and flagged as a comparable top-tier lab)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** RF3DGS removes reflections from 3D Gaussian Splatting reconstructions by exploiting the fact that, across multiple views of the same 3D point, the darkest pixel is usually reflection-free.
**Purpose (≤3 sentences):** Standard 3D Gaussian Splatting bakes reflections (e.g., off glass) into scene geometry and appearance, producing artifacts; the authors aim to reconstruct clean, reflection-free 3D scenes.
**Breakthrough (≤3 sentences):** The authors report 31.45 PSNR / 0.150 LPIPS on their new synthetic Unity-based benchmark versus 29.58 PSNR / 0.175 LPIPS for vanilla 3DGS, and 25.04 PSNR / 0.915 SSIM on the real-world TNeRF benchmark versus 22.75 PSNR / 0.841 SSIM for TNeRF itself; they also introduce a new Unity benchmark of 45 reflective-glass test cases varying transparency, glass thickness, and reflection strength.
**Tools & method (≤3 sentences):** The method fits a vanilla 3DGS model to estimate coarse per-view depth, warps reflection-free content from auxiliary views to build a pseudo-label per reference view, and trains with an "Adaptive Twin Rendering" loss that preserves high-frequency detail; it takes ~60.74 minutes per case on the 88-view benchmark (GPU type not stated in the paper).
**Limitation (≤3 sentences):** The paper does not state limitations of its own method directly; it notes only that vanilla 3DGS edges out RF3DGS on SSIM on the synthetic benchmark, which the authors attribute to SSIM's low sensitivity to reflection artifacts (observed, not stated as a limitation).

# Near-misses
- 2611.14365 · From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models · false-positive "Meta" match (from the title text "Meta-Frames," not a company affiliation); authors affiliated only with National University of Singapore / Guangzhou Research Translation and Innovation Institute; also a robot-manipulation world model, not game-relevant
- 2611.14307 · TaoMate-R1: Temporal Role Specialization for Streaming Multi-Reference Video Generation · Alibaba Group affiliation confirmed (Meiguang Jin et al., taobao.com contact), but topic (streaming multi-reference video generation of scenes with people/objects) does not clearly fall under 3D / world models / character animation / game engines
- 2611.13348 · ProTEUS: A mutation-resolved world model for closed-loop protein evolution · "world model" and "Google" keyword matches were false positives (protein-evolution domain, likely a Google Scholar link rather than an affiliation); off-topic (biology)
- 2611.12932 · URL-Sim: Unified and Regulated LiDAR Simulation for High-Fidelity Reconstruction of Dynamic Driving Scenes · "borderline" match traced to the Waymo dataset name, not an actual industry affiliation; domain is autonomous-driving LiDAR simulation, not games

Verification: all 3 qualifying papers double-checked against their arXiv abs and HTML pages (title, v1 date, categories, affiliation text, and all reported numbers quoted above match the source) before inclusion; the 4 near-misses were likewise checked against source text before being dropped.
