**[A11] Prepare Lighter and Faster for Open-Vocabulary Queries: A Query-Wise 3D Segmenter for Gaussian Splatting**
- **arXiv:** 2611.19429 · <https://arxiv.org/abs/2611.19429>
- **Submitted:** 2026-11-14
- **Authors:** Nhat-Quynh Le-Pham et al.
- **Qualifying affiliation(s):** Qualcomm (Qualcomm AI Research) — Khoi Nguyen; Nhat-Quynh Le-Pham (work done while at Qualcomm)
- **Categories:** cs.CV, cs.AI, cs.GR
- **Open release:** none found (no GitHub/project-page link located in the fetched text)
- **Shipped counterpart:** none found

**Summary:** The paper presents a training-free, query-driven framework for open-vocabulary 3D instance segmentation directly on pretrained 3D Gaussian Splatting scenes, avoiding the expensive preprocessing and per-scene training of prior methods.
**Purpose:** The goal is fast, lightweight, text-driven 3D instance segmentation on Gaussian Splatting scenes for arbitrary (open-vocabulary) object categories, without the lengthy training or heavy preprocessing that limits existing approaches' practicality.
**Breakthrough:** The authors report 63.02 mIoU on LERF-OVS with a 1.5-minute time-to-first-query, versus 50.58 mIoU/10 minutes for LUDVIG and 59.90 mIoU/10 hours for LangSplatV2; on ScanNet they report 43.74 mIoU in 2 minutes versus LangSplatV2's 39.44 mIoU in 10 hours.
**Tools & method:** The pipeline uses dense pixel-level CLIP features (via ProxyCLIP) instead of mask-wise CLIP embeddings, a video tracking segmentor (the authors compare HQ-SAM2 vs. EfficientTAM) to propagate 2D masks across views, and a visibility-voting step to assign 3D Gaussians to instances using foreground/background votes from visible views.
