**[A03] DuoMatching: Joint-Marginal Distribution Matching for Few-Step Video Generation**
- **arXiv:** 2610.03543 · <https://arxiv.org/abs/2610.03543>
- **Submitted:** 2026-10-02
- **Authors:** Jiahao Zhan, Yan Wang, Yongrui Ma, Qunliang Xing, Ruchang Yao, Runtao Liu, Shijie Zhao, Tianfan Xue
- **Qualifying affiliation(s):** ByteDance — Jiahao Zhan, Yan Wang, Yongrui Ma, Qunliang Xing, Shijie Zhao (joint CUHK MMLab / ByteDance Inc. affiliations; Shijie Zhao is ByteDance-only corresponding author)
- **Categories:** cs.CV
- **Open release:** demo/project page (<https://johnzhan2023.github.io/DuoMatching/>); no explicit code/weights release confirmed
- **Shipped counterpart:** none found

**Summary:** DuoMatching is a distillation framework for few-step video generation that combines joint distribution matching (video-level) with marginal distribution matching (frame-level, supervised by an image generator) to improve visual quality and semantic coherence.
**Purpose:** Existing few-step video distillation methods that rely solely on joint (video-level) distribution matching can suffer from limited visual quality and semantic coherence because they lack strong frame-level supervision.
**Breakthrough:** The authors report that adding image-generator-supervised marginal matching, via the new LatentBridge and Latent Variation Sampling components, yields human-preference rates above 80% against all evaluated baselines, with gains in visual quality, composition, and semantic alignment while motion dynamics are preserved throughout the sequence.
**Tools & method:** The method combines a video distribution-matching distillation objective with frame-level supervision from a separate image generator, bridged via LatentBridge, and samples supervision across time via Latent Variation Sampling.
**Limitation:** The abstract does not explicitly state limitations or failure cases.
