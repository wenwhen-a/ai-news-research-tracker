**[A02] Gate3DGen: A Pre-processing Model that Selectively Purifies Real-World Images for 3D Generation**
- **arXiv:** 2610.31649 · <https://arxiv.org/abs/2610.31649>
- **Submitted:** 2026-10-22
- **Authors:** Xiaolin Li et al.
- **Qualifying affiliation(s):** Huawei Inc. — Xiaolin Li, Zihao Huang, Fanpeng Meng, Chen Yang, Guanjun Wu, Jiemin Fang, Qi Tian (FLAG: Huawei is not on the default qualified-company list but is a comparable large-scale tech company — kept and flagged)
- **Categories:** cs.CV
- **Open release:** none (no code/weights/demo link found on the abstract page)
- **Shipped counterpart:** none found

**Summary:** Gate3DGen is a pre-processing "gate" model for 3D-generation pipelines: clean input images pass through unchanged, while degraded ones are purified by a one-step, 3D-oriented restoration model that preserves object identity and edges.
**Purpose:** Real-world input images for image-to-3D generation are often degraded (noise, compression, poor lighting), which the authors state hurts downstream 3D reconstruction quality; Gate3DGen aims to selectively fix only the images that need it, leaving clean images untouched.
**Breakthrough:** The authors report Gate3DGen cuts TRELLIS.2 mesh distance by 61.5% on a synthetic degraded-image benchmark compared with feeding degraded images directly into the 3D generator, at about 2.3 seconds of processing per image.
**Tools & method:** The model is trained on a synthetic data engine that generates paired clean/degraded views for supervision, combined with a one-step 3D-oriented purification network and a degradation-detection gate; it is evaluated against TRELLIS.2 as the downstream 3D generator.
**Limitation:** The authors' reported gains are measured on a synthetic degraded-image benchmark; the paper's current abstract/metadata do not state real-world deployment results or failure cases beyond this benchmark.
