**[A15] Latent evolving World Action Model**
- **arXiv:** 2609.27455 · <https://arxiv.org/abs/2609.27455>
- **Submitted:** 2026-09-23
- **Authors:** Xueji Fang et al.
- **Qualifying affiliation(s):** Baidu Inc. — Hua Wu
- **Categories:** cs.CV, cs.RO
- **Open release:** code (<https://github.com/XuejiFang/LeWAM)> | weights (<https://huggingface.co/XuejiFang/LeWAM)>
- **Shipped counterpart:** none found

**Summary:** The paper introduces LeWAM, a World Action Model that replaces large video-diffusion backbones with JEPA-derived predictive embeddings for robot action generation, arguing these support action generation better than compressed VAE latents.
**Purpose:** Existing World Action Models built on video-diffusion latents (VAE-compressed) are inefficient and poorly suited to direct action generation, while imitation learning alone cannot distinguish subtly superior from inferior actions even though small deviations cause task failures.
**Breakthrough:** The authors report that with only 0.4B trainable parameters, LeWAM achieves a 92.28% average success rate on the RoboTwin 2.0 benchmark, that DemoDPO raises success from 90.69% to 92.28%, and that frozen I-JEPA-Huge embeddings outperform V-JEPA2-Huge and Wan2.2 VAE latents in their encoder comparison.
**Tools & method:** LeWAM uses frozen I-JEPA embeddings with AdaFuse adaptive multi-layer fusion as visual input, a single predictor jointly handling action generation (via flow matching) and future embedding prediction, and DemoDPO for offline preference refinement without extra environment interaction; it was trained on RoboTwin 2.0 (50 tasks, 2,500 clean + 25,000 randomized demonstrations) using 16 NVIDIA H800 GPUs, plus real-world validation on an AgileX dual Piper robot across three bimanual tasks.
