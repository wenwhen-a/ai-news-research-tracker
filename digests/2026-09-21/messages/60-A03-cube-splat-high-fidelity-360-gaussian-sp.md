**[A03] Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Pose Tracking**
- **arXiv:** 2609.21347 · <https://arxiv.org/abs/2609.21347>
- **Submitted:** 2026-09-18
- **Authors:** Xiangfei Guo et al.
- **Qualifying affiliation(s):** Ant Group — Xiangfei Guo, Hao Shi (co-affiliated with Zhejiang University; other authors are Zhejiang University only); FLAG: Ant Group is a borderline-listed organization (not on the core tracked list; kept and flagged per policy)
- **Categories:** cs.CV
- **Open release:** code + dataset — <https://github.com/guoxf304/CubeSplat> (source code and the SynPano dataset)
- **Shipped counterpart:** none found

**Summary:** The paper presents Cube-Splat, a 3D Gaussian Splatting SLAM system for 360° panoramic cameras, built to overcome the limited field of view of pinhole-camera SLAM pipelines that increases drift in large scenes.
**Purpose:** Most existing 3DGS SLAM pipelines assume pinhole cameras, which the authors say reduces scene coverage and worsens drift; panoramic imagery is harder to integrate into a single coherent pose because observations from different directions must stay geometrically consistent.
**Breakthrough:** On the PALVIO indoor benchmark, the authors report a tracking error (ATE) of 0.0769 m versus 2.23 m (Photo-SLAM), 2.89 m (MonoGS), and 1.93 m (S3PO-GS); on their new outdoor SynPano benchmark, Cube-Splat reaches 0.1058 m ATE while S3PO-GS fails to track.
**Tools & method:** The system runs on a single NVIDIA RTX 4070 Ti SUPER GPU in PyTorch on Ubuntu 22.04, processing at roughly 1.53 FPS (12.8 ms/iteration, ~35 tracking iterations per frame).
