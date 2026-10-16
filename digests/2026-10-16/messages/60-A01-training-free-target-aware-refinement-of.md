**[A01] Training-Free Target-Aware Refinement of 3D Gaussian Language Map**
- **arXiv:** 2610.21619 · <https://arxiv.org/abs/2610.21619>
- **Submitted:** 2026-10-15 (v1, 10:00:53 UTC)
- **Authors:** Sibaek Lee et al.
- **Qualifying affiliation(s):** Samsung Electronics, Republic of Korea — Taemin Choi, Minsu Kim, Hyungjoo Ahn, Wonsok Yoo (remaining authors: Sungkyunkwan University). FLAG: borderline — Samsung Electronics is not on the core qualified list; kept per the "clearly comparable top-tier industry lab" rule.
- **Categories:** cs.RO (primary), cs.CV
- **Open release:** code/demo — project page states "Project page and code:" <https://lab-of-ai-and-robotics.github.io/target-aware-langmap/>
- **Shipped counterpart:** none found

**Summary:** The paper presents a training-free method to refine an already-distilled 3D Gaussian Splatting (3DGS) language map so that a small set of user-specified text targets is retrieved reliably, without retraining the underlying map.
**Purpose:** Existing open-vocabulary 3DGS language maps often fail to localize specific user-named targets reliably because of embedding biases in the distilled features.
**Breakthrough:** The authors report the refinement roughly doubles base open-vocabulary segmentation mIoU on Replica (0.207 → 0.436) and raises top-1 instance-aware localization success from 44.6 to 76.8 on Replica.
**Tools & method:** A text-promptable segmenter (SAM 3) locates each target per view, and its visual embedding is blended toward the target's SigLIP 2 text embedding using a closed-form minimal blending coefficient (no tuning), on top of a SAM 2 + SigLIP 2 base map; a centering step at query read-out removes a shared bias the authors identify in injected embeddings.
