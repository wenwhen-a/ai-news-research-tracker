**[A04] PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM**
- **arXiv:** 2609.17387 · <https://arxiv.org/abs/2609.17387>
- **Submitted:** 2026-09-15 (v1)
- **Authors:** Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang
- **Qualifying affiliation(s):** Ant Group — Hao Shi (dual-affiliated with Zhejiang University) — FLAG: borderline
- **Categories:** cs.CV
- **Open release:** code (announced, no link live yet) — paper states "The source code will be made publicly available"
- **Shipped counterpart:** none found

**Summary:** The paper presents PanoGS-SLAM, described as the first dense SLAM system for panoramic cameras built on 3D Gaussian Splatting.
**Purpose:** Prior 3DGS-based SLAM methods are designed for narrow-FoV pinhole cameras, where limited angular coverage weakens pose observability and destabilizes photometric optimization under rapid motion or large viewpoint changes.
**Breakthrough:** The authors report that PanoGS-SLAM "consistently outperforms geometric and GS-based baselines in tracking accuracy and rendering quality" on the PALVIO and SynPano benchmarks while achieving fast front-end convergence and real-time performance.
**Tools & method:** The method performs differentiable rendering and pose optimization directly in the spherical domain rather than projecting to pinhole views, introducing (1) a sphere-consistent photometric loss that compensates for equirectangular-projection area distortion, and (2) a depth-guided Gaussian initialization strategy for newly observed regions.
**Limitation:** The authors note that even with panoramic input, differentiable photometric pose estimation has a fundamental limitation: the optimization landscape depends heavily on the spatial/angular distribution of image gradients, and under narrower FoV settings gradients concentrate within a narrow viewing cone, weakening rotational observability.
