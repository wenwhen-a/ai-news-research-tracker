**[A03] VGGT-Prime: Compute-Adaptive Mixture-of-Heads for Efficient Visual Geometry Transformers**
- **arXiv:** 2609.23733 · <https://arxiv.org/abs/2609.23733>
- **Submitted:** 2026-09-20
- **Authors:** Abteen Arab, Guile Wu, Chengjie Huang, Dongfeng Bai
- **Qualifying affiliation(s):** Huawei Noah's Ark Lab — Guile Wu, Chengjie Huang, Dongfeng Bai (Abteen Arab: Huawei Canada internship + University of British Columbia); FLAG: borderline
- **Categories:** cs.CV
- **Open release:** project page at <https://vggt-prime.github.io> (no explicit code/weights release statement found)
- **Shipped counterpart:** none found

**Summary:** VGGT-Prime is a compute-adaptive variant of the Visual Geometry Transformer (VGGT) that speeds up multi-view 3D reconstruction (camera pose, depth, point clouds) by exploiting redundancy across attention heads rather than tokens.
**Purpose:** Visual geometry transformers like VGGT suffer from quadratic attention cost as the number of input views grows, limiting their use on long image sequences.
**Breakthrough:** The authors report that attention heads in VGGT fall into distinct high/medium/low-saliency tiers (identified via integrated-gradient and attention-magnitude analysis), and that most heads can be replaced with cheaper surrogates without hurting accuracy.
**Tools & method:** The method routes high-saliency heads to full softmax attention, medium-saliency heads to a learned surrogate attention with query pooling and residual correction, and low-saliency heads to simple mean pooling, trained via two-stage distillation from a frozen VGGT teacher.
**Limitation:** The authors state the method relies on a frozen teacher model, which "limits the method to matching the teacher rather than surpassing it." They identify training directly against ground truth (rather than distillation targets) as future work.
