**[A02] OREO: Fidelity Alignment in 3D Generation via On-the-fly Rendering-Editing Optimization**
- **arXiv:** 2609.29788 · <https://arxiv.org/abs/2609.29788>
- **Submitted:** 2026-09-24
- **Authors:** Zhiyuan Ma, Wenbo Hu, Wang Zhao, Pengfei Wang, Ying Shan, Lei Zhang
- **Qualifying affiliation(s):** Tencent — Wenbo Hu, Wang Zhao, Ying Shan listed at Tencent ARC Lab (Zhiyuan Ma is dual-affiliated with Tencent ARC Lab and The Hong Kong Polytechnic University)
- **Categories:** cs.CV, cs.GR
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** OREO targets the gap between generated 3D assets and real-world visual fidelity, noting that generated assets "often lack intricate textures and fine-grained details observed in real-world subjects" because 3D training data is far scarcer than 2D imagery.
**Purpose:** The authors aim to close the fidelity gap without needing more 3D training data, by using a 2D image editor to improve rendered views of a 3D asset and feeding those improvements back into the generator itself.
**Breakthrough:** On a 2,396-image Conceptual Design Dataset the authors report OREO reaches 0.7834 CLIP similarity and 0.8065 DINO similarity versus a Trellis baseline's 0.7613 and 0.7916; on Google Scanned Objects the gap narrows (0.7764 vs 0.7722 CLIP).
**Tools & method:** "Reinforced Editing" uses inversion-free image editing that couples source/target flow trajectories to enhance a rendered view while preserving its spatial layout, and a contrastive distillation loss (`L_contrast = ||z⁰-z0+||² - ||z⁰-z0-||²`) treats the edited render as a positive target and the original as negative.
**Limitation:** The authors report viewpoint drift on face-like objects, where "the 2D editor may rotate the face toward the camera instead of preserving the intended 3D-facing direction," and style shifts inherited from the editor's bias on materials outside its photorealistic training distribution.
