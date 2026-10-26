**[A02] Easy-3Dfy: Object-Level Geometric Composition for Single-Image 3D Scene Construction**
- **arXiv:** 2610.32250 · <https://arxiv.org/abs/2610.32250>
- **Submitted:** 2026-10-23
- **Authors:** Ziang Zhang, Wenyou Yi, Zehan Wang, Jiachen Xu, Xintong Han, Chunchao Guo, Zhou Zhao
- **Qualifying affiliation(s):** Tencent — Jiachen Xu, Xintong Han, Chunchao Guo (and Ziang Zhang, Zehan Wang hold dual Zhejiang University / Tencent affiliations). Wenyou Yi and Zhou Zhao are affiliated with Zhejiang University.
- **Categories:** cs.CV, cs.AI
- **Open release:** none found (no code/project link located on the abstract or HTML page)
- **Shipped counterpart:** none found

**Summary:** The paper addresses single-image 3D scene construction, noting that existing end-to-end methods (e.g., SAM-3Dfy) can reconstruct 3D assets and layouts but struggle with fine scene geometry and asset quality. The authors propose Easy-3Dfy, a workflow that separates object generation from scene layout estimation so each sub-problem can use a specialized model, with an RPF-based aligner matching object-local meshes to partial scene pointmaps to recover object placement.
**Purpose:** Single-image 3D scene reconstruction needs both high-quality individual object geometry and accurate scene-level spatial layout, which end-to-end methods trade off against each other.
**Breakthrough:** The authors report that Easy-3Dfy outperforms SAM-3Dfy on several geometric metrics on the Scene-Maker and 3D-FUTURE200 benchmarks, without requiring complete scene-level supervision.
**Tools & method:** The method decouples object generation (via a dedicated 3D object generator) from scene layout estimation, then uses an RPF-based alignment procedure to fit object meshes into partial scene pointmaps; evaluated on Scene-Maker and 3D-FUTURE200.
**Limitation:** Not stated by the authors (not surfaced in the available abstract/summary text).
