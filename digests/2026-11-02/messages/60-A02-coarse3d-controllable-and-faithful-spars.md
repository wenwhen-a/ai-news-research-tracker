**[A02] Coarse3D: Controllable and Faithful Sparse Structure Generation for Image-to-3D**
- **arXiv:** 2610.41231 · <https://arxiv.org/abs/2610.41231>
- **Submitted:** 2026-10-30
- **Authors:** Gaige Wang, Bowen Pan, Hao Ren, Jiangjing Lyu, Chengfei Lyu
- **Qualifying affiliation(s):** Alibaba Group (all listed authors)
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** none found (no code/weights/project-page link located on the paper)
- **Shipped counterpart:** none found

**Summary:** Coarse3D is a coarse-stage, sparse-structure generation model for image-to-3D pipelines that produces orientation-controllable, structurally faithful voxel geometry from arbitrary unposed images.
**Purpose:** The authors target two limitations of current coarse-to-fine 3D generators: orientation is hard to control because semantic canonicalization is ambiguous, and generated structures often don't match the input image because of weak 2D-3D grounding.
**Breakthrough:** The authors report that Coarse3D raises the F-Score from 0.54 (baseline, as stated in the paper's conclusion) and achieves state-of-the-art performance on sparse-structure quality, which they attribute to three design choices: a first-view-anchored canonical space, a dual-tower diffusion transformer trained jointly with feed-forward reconstruction, and cross-attention regularized by pixel-to-voxel correspondence.
**Tools & method:** The model is trained on roughly 2M 3D assets: about 500K filtered assets from TRELLIS-500K (Xiang et al., 2025) plus additional data, with training using a learning rate of 1e-5 and batch size 256 on 64 NVIDIA H20 GPUs (full details in the paper's Appendix A.2).
**Limitation:** The paper's conclusion restates the two problems it addresses (orientation control, structural consistency) as the limitations of prior pipelines; the authors do not state an explicit limitation of their own method in the sections checked.
