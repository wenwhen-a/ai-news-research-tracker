**[A06] Plan4D: Generative Plannable 4D Worlds**
- **arXiv:** 2611.26516 · <https://arxiv.org/abs/2611.26516>
- **Submitted:** 2026-11-19
- **Authors:** Hangwei Zhang, Rujing Dang, Ruimin Lin, Jiahong Wu, Xiangxiang Chu, Chuanxia Zheng
- **Qualifying affiliation(s):** Alibaba — Hangwei Zhang, Rujing Dang, Ruimin Lin, Jiahong Wu, Xiangxiang Chu, Chuanxia Zheng (listed under "AMAP, Alibaba Group")
- **Categories:** cs.CV
- **Open release:** project page (<https://fogradio.github.io/plan4d-project>); accepted at NeurIPS 2026
- **Shipped counterpart:** none found

**Summary:** Plan4D is a world model that, given an observed scene and text-specified actions, predicts future RGB video together with dense 4D geometry — depth, cameras, point clouds, and scene flow.
**Purpose:** The authors note most world models focus on RGB synthesis without explicit 4D geometry, and that action-conditioned datasets with dense 3D annotations are scarce.
**Breakthrough:** The authors report state-of-the-art results on synthetic and real-world benchmarks for generative 4D modeling of environmental reactions, with examples including an EPE of 0.97 on MOVi-F scene flow and, on HoiGen, AbsRel of 0.1125 and RRA@5 of 0.9809 versus 1.850 AbsRel/0.9256 RRA@5 for the TesserAct baseline.
**Tools & method:** A DPT-style scene-flow head is added to a frozen Depth Anything 3 (DA3) backbone; a learnable 3D convolution stitches upsampled Wan-VAE video latents into a selected DA3 encoder block, and the stitched decoder is trained via teacher-student distillation plus ground-truth 3D supervision before joint training with a flow-matching loss and a geometry loss from the frozen stitched decoder.
**Limitation:** The paper's table of contents lists a dedicated limitations appendix, but its content was not accessible in the retrieved text, so no specific stated limitations could be verified beyond what the method and results sections imply.
