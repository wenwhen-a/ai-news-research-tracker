**[A15] Demiurge: Forging Navigable 4D Worlds via Autoregressive Video Rerendering**
- **arXiv:** 2610.14685 · <https://arxiv.org/abs/2610.14685>
- **Submitted:** 2026-10-10
- **Authors:** Hanxin Zhu et al.
- **Qualifying affiliation(s):** Tencent — Zhihao Hu, Weidong Zhang; Microsoft — Tianyu He (other authors: USTC, CASIA, Tongji University, PolyU)
- **Categories:** cs.CV
- **Open release:** code/demo — project page <https://hanxinzhu-lab.github.io/demiurge_project_page/> linking to GitHub repo <https://github.com/HanxinZhu-lab/Demiurge>
- **Shipped counterpart:** none found

**Summary:** Demiurge is an autoregressive video-rerendering pipeline for generating navigable 4D worlds from a single input video, built around a dynamic 4D point-cloud memory cache that enforces consistency across different camera trajectories.
**Purpose:** Existing novel-view video synthesis methods process each camera trajectory independently, so they lack the cross-trajectory consistency needed to build a single coherent, navigable 4D world (useful for world modeling, embodied intelligence, and robotic simulation, per the authors).
**Breakthrough:** The authors claim state-of-the-art performance and three capabilities: coherent spatiotemporal lattice construction over dense multi-view trajectories, large-parallax rerendering under challenging camera motion including 180-degree rotations with no input-view overlap, and geometry-faithful outputs that optimize into high-quality 3D Gaussian Splatting with "minimal artifacts" (their claim).
**Tools & method:** A dynamic 4D point-cloud memory cache is updated autoregressively as new trajectories are rendered; a video depth-completion model aligns newly generated depth with cached geometry to resolve scale ambiguity, and dual-stream warping supplies visual/occlusion guidance for the diffusion model before a geometry-aware refinement pass sharpens perceptual quality.
