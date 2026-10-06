**[A08] CleanMDM: Clean Motion Diffusion Model for Multimodal Motion Cleanup**
- **arXiv:** 2610.05411 · <https://arxiv.org/abs/2610.05411>
- **Submitted:** 2026-10-04
- **Authors:** Zhe Li, Shicheng Wang, Bowen Cai, Huan Fu
- **Qualifying affiliation(s):** Alibaba — Bowen Cai, Huan Fu
- **Categories:** cs.CV
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary:** CleanMDM is a unified Clean Motion Diffusion Model that formulates motion-capture cleanup — removing jitter, missing segments, drift and contact artifacts — as masked conditional generation, accepting combinations of noisy 3D motion, sparse 2D/3D keyframes and text as plug-and-play conditions.
**Purpose:** Motion capture data typically contains imperfections that require manual animator cleanup; the authors aim to unify cleanup and controllable generation in one multimodal framework instead of treating them as separate tools.
**Breakthrough:** The authors report that a Latent Motion Quality Discriminator and Mesh-Aware Contact Projection improve kinematic accuracy and physical realism, with superior performance against baselines (StableMotion, ACMDM, CondMDI, GenMo) on MPJPE, foot-skating ratio, acceleration error, penetration frequency/distance, jitter, FID and diversity, and show text and 2D-keyframe conditions providing effective controllable guidance.
**Tools & method:** The model is trained on AMASS and a filtered ~28K-clip subset of MotionLLaMA, evaluated on synthetic corruptions and real-world datasets (IDEA400, HuMMan, KungFu, HAA500), using 22 NVIDIA H20 GPUs (batch size 128, ~16 hours for 600 epochs) for training and 1 NVIDIA V100 for testing.
**Limitation:** The authors state evaluation relies on controlled corruption and a simplified ground model during Mesh-Aware Contact Projection, with future work planned on more realistic video-mocap degradations, stronger learned contact priors, and additional control modalities.
