**[A31] SpatialCrafter: Single Image World Modeling with Generative 3D Proxies**
- **arXiv:** 2608.27073 · https://arxiv.org/abs/2608.27073
- **Submitted:** 2026-08-27
- **Authors:** Chuan Fang, Lingteng Qiu, Yixun Liang, Rui Chen, Kunming Luo, Zhaohua Zheng, Tongyuan Bai, Feipeng Tian, Zilong Dong, Zihan Zhou, Ping Tan
- **Qualifying affiliation(s):** Alibaba Group (Tongyi Lab) — Lingteng Qiu, Zilong Dong
- **Categories:** cs.CV, cs.RO
- **Open release:** demo (project page https://fangchuan.github.io/SpatialCrafter/)
- **Shipped counterpart:** none found

**Summary:** SpatialCrafter turns one image into an explorable 3D scene by generating a global 3D proxy and refining its appearance with a video diffusion model, to reduce hallucination and drift compared with video-diffusion-only methods; the authors also build a 115K-scene dataset with geometric annotations.
**Purpose:** Image-to-scene generation for gaming, robotics and VR where video-diffusion methods lack global 3D consistency under large camera motion.
**Breakthrough:** At 81-frame generation the authors report FVD 193.54 on SpatialGen-Video (versus 339.04 for ViewCrafter and 525.23 for GEN3C), and on RealEstate10K FVD 148.71 / PSNR 17.185 / SSIM 0.659.
**Tools & method:** A Point-anchored Sparse Structure Flow module builds the proxy and a Generative Deferred Refiner handles appearance; 115,295 training pairs from SpatialGen, RealEstate10K and DL3DV; 16 then 32 NVIDIA H20 GPUs.
**Limitation:** No explicit limitations section was extracted (observed, not stated).
