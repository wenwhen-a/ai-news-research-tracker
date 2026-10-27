**[A01] PosePlaner: Denoising Any Feed-Forward Pose Predictor from Pairwise Planar Geometry**
- **arXiv:** 2610.34845 · <https://arxiv.org/abs/2610.34845>
- **Submitted:** 2026-10-26
- **Authors:** Yihang Chen et al.
- **Qualifying affiliation(s):** Ant Group (Robbyant) — Bin Tan (superscript 2, corresponding author), Yujun Shen (superscript 2), Nan Xue (superscript 2); Yihang Chen is dual-affiliated (HKUST + Ant Group, superscript 1,2). FLAG: borderline (Ant Group is explicitly named as a borderline example in the task brief).
- **Categories:** cs.CV
- **Open release:** none found beyond a project page (<https://robbyant-research.github.io/PosePlaner/>); no code or weights link was located. Comments on the abstract page note the paper was accepted at NeurIPS 2026.
- **Shipped counterpart:** none found

**Summary:** PosePlaner refines camera poses from any feed-forward multi-view 3D predictor (e.g., DUSt3R, VGGT) using flow matching conditioned on pairwise planar geometry, treating pose refinement as a conditional generation problem.
**Purpose:** The paper addresses the fact that modern feed-forward multi-view Transformers collapse the classical SfM/SLAM pipeline (feature matching, geometry, pose) into a single forward pass, which hides the interfaces between stages and leaves supervised fine-tuning as the main path to improving them, with no mechanism to correct predictions from geometric evidence at test time.
**Breakthrough:** The authors report that PosePlaner, trained only on two-view data, can periodically refine streaming n-view pose estimators without retraining.
**Tools & method:** The method uses flow matching as a single-Euler-step diffusion adapter conditioned on matched planar primitives for rotation refinement, combined with geometric translation recovery, and extends to n-view streaming via per-edge view-graph refinement aggregated by rotation averaging and a Glomap-style positioner.
