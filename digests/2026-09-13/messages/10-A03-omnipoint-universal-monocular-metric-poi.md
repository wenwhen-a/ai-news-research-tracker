**[A03] OmniPoint: Universal Monocular Metric Pointcloud from Any Camera**
- **arXiv:** 2609.09394 · https://arxiv.org/abs/2609.09394
- **Submitted:** 2026-09-08
- **Authors:** Botao Ye, Marc Pollefeys, Ming-Hsuan Yang, Abhijit Kundu
- **Qualifying affiliation(s):** Google DeepMind — Botao Ye (intern), Ming-Hsuan Yang, Abhijit Kundu
- **Categories:** cs.CV
- **Open release:** none (project page lists paper and poster only)
- **Shipped counterpart:** none found

**Summary:** OmniPoint predicts metric 3D point clouds from a single image for pinhole, fisheye or panoramic cameras, using a representation that decouples projection geometry from scene structure.
**Purpose:** Existing monocular metric-depth methods are tied to a fixed camera model; the work aims to generalise metric point-cloud estimation across camera types without per-camera retraining.
**Breakthrough:** The authors report a "ray direction and radial distance" representation that lets one distance predictor serve pinhole, fisheye and panoramic inputs, trained on 29 labelled datasets plus 2 unlabelled panoramic datasets with a bidirectional augmentation that converts between pinhole and wide-angle views.
**Tools & method:** DINOv2 ViT-Large backbone; trained on 72 A100 GPUs; labelled and unlabelled panoramic data with synthetic camera-conversion augmentation.
**Limitation:** No code, weights or demo are released, limiting independent verification of the reported cross-camera generalisation (observed, not stated).
