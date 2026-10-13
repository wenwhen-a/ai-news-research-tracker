**[A02] Zebra3D: Efficient Hybrid Foundation Models For Scalable 3D Reconstruction**
- **arXiv:** 2610.12727 · <https://arxiv.org/abs/2610.12727>
- **Submitted:** 2026-10-08
- **Authors:** Utkarsh Saxena et al.
- **Qualifying affiliation(s):** AMD (Advanced Micro Devices) — all six authors, per the paper's affiliation block. **Flag: BORDERLINE** — AMD is on the borderline/comparable-labs list, not the main qualifying list. Note: the pre-screen's "Tencent" and "Google" flags are **false positives** — the paper's real affiliation is AMD; Tencent and Google appear only as citations to baseline models the authors benchmark against (HunyuanWorld-Mirror is a Tencent model, VGGT/π³ are associated with Google-adjacent prior work), not as author affiliations.
- **Categories:** cs.CV (primary), cs.LG
- **Open release:** none yet; authors state in a Reproducibility Statement that code, configs, custom kernels, and checkpoints "will be" released upon publication, but no link is given in the text read.
- **Shipped counterpart:** none found

**Summary:** Feed-forward 3D foundation models (e.g., VGGT, HunyuanWorld-Mirror, π³) reconstruct scenes from unposed images, but their global self-attention scales quadratically with view count, limiting them to modest numbers of views; the authors report attention accounts for 88% of VGGT's runtime at 512 views.
**Purpose:** To make existing dense-attention 3D foundation models scale efficiently to much larger numbers of input views without retraining them from scratch.
**Breakthrough:** The authors report end-to-end speedups that grow with view count, reaching up to 7.1x at 1,024 views, and after post-conversion training, Zebra3D-VGGT reaches 80.5% RealEstate10K AUC@30 at 94% mean attention sparsity, within 1.1 percentage points of dense VGGT trained under the same schedule.
