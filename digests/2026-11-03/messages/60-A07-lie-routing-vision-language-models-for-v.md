**[A07] Lie Routing Vision Language Models for View-Robust 3D Understanding**
- **arXiv:** 2611.02306 · <https://arxiv.org/abs/2611.02306>
- **Submitted:** 2026-11-01
- **Authors:** Jingjun Yi, Chen Hu, Qi Bi, Hao Zheng, Huimin Huang, Yongkang Li, Wei Ji, Yawen Huang, Xian Wu, Yefeng Zheng
- **Qualifying affiliation(s):** Tencent, China — Hao Zheng, Huimin Huang, Wei Ji, Yawen Huang, Xian Wu. Other authors list Westlake University (Jingjun Yi, Chen Hu, Yefeng Zheng) and University of Amsterdam (Qi Bi, Yongkang Li; Jingjun Yi is also now affiliated with University of Amsterdam).
- **Categories:** cs.CV, cs.LG
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** The paper studies "viewpoint-induced semantic drift," where vision-language models give inconsistent answers about the same object as the camera viewpoint changes. It proposes LieVLM, a routing framework that applies local SO(3) rotations to projected visual features within learned subspaces to make the model's understanding more view-robust.
**Purpose:** Multimodal large language models are reported to answer inconsistently about the same 3D object or scene depending on viewpoint, which the authors frame as a barrier to reliable 3D scene understanding.
**Breakthrough:** The authors report consistent gains over additive-fusion baselines on 3D captioning, grounding, detection, and spatial-reasoning tasks, supported by ablations and viewpoint analyses.
**Tools & method:** LieVLM predicts rotation parameters and routing coefficients from geometry tokens extracted by VGGT, then applies local SO(3) rotations to projected visual features within learned subspaces before fusing them into the VLM.
**Limitation:** Not confirmed from the fetched content — the paper's table of contents lists a "G Limitations" appendix, but its text was not retrievable from the pages fetched, so it is not reproduced here to avoid inventing content.
