**[A06] ALPS: Visual State Encoders for World Models**
- **arXiv:** 2610.30120 · <https://arxiv.org/abs/2610.30120>
- **Submitted:** 2026-10-21 (v1)
- **Authors:** Yanqing Liu, Letian Zhang, Chengzhi Liu, Zijun Wang, Jieru Mei, Hongliang Fei, Yuyin Zhou, Cihang Xie
- **Qualifying affiliation(s):** Google — Jieru Mei, Hongliang Fei
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** The paper argues that a world model's visual foundation should combine physical-state information, language alignment, and pixel reconstruction in one representation.
**Purpose:** The authors state existing visual encoders typically specialize in only one or two of the three capabilities (state, language, reconstruction), limiting their use as a shared foundation for world models that must predict, follow instructions, and be visually inspected.
**Breakthrough:** The authors report ALPS achieves the lowest aggregate LIBERO state-probe error among ViT-B models, matching a 3.5× larger V-JEPA 2-L, and the highest mean LIBERO policy success (85.5%) among tested encoders.
**Tools & method:** ALPS is pretrained only on still images and paired text (no video), using joint language, reconstruction, and spatial-correspondence objectives followed by cross-view self-distillation; it is evaluated against 15 public encoders on LIBERO and the PushT/Wall/Granular world-model planning benchmarks.
**Limitation:** The authors state in their "Limitations and future work" section that they focus on a single ViT-B/16 backbone and simulation benchmarks for controlled comparison, leaving larger model scales and real-robot deployment to future work.
