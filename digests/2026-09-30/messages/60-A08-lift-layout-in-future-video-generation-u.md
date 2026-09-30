**[A08] LIFT: Layout-In-Future Video Generation under Large Viewpoint Change via On-Policy Self-Distillation**
- **arXiv:** 2609.38146 · <https://arxiv.org/abs/2609.38146>
- **Submitted:** 2026-09-29 (v1)
- **Authors:** Shengxiang Ji, Boyang Wang, Haiyang Xu, Bingnan Li, Yucheng Mao, Zeyuan Chen, Xiaojun Shan, Xiang Zhang, Gang Hua, Jianwen Xie, Zezhou Cheng, Zhuowen Tu
- **Qualifying affiliation(s):** Meta — Xiang Zhang; Amazon — Gang Hua (other authors: UC San Diego, University of Virginia, Lambda)
- **Categories:** cs.CV
- **Open release:** code + weights + dataset (LIFT-Vista) — per project page <https://jsxzs.github.io/LIFT/>, which links GitHub and Hugging Face
- **Shipped counterpart:** none found

**Summary:** LIFT is a controllable video generation framework combining camera-trajectory control with "Layout-In-Future" control, letting users specify object content and spatial position in future frames.
**Purpose:** Existing controllable video generators degrade under large camera-viewpoint changes because sparse, future-only layout signals are hard to learn from directly.
**Breakthrough:** The authors report improved video quality and controllability from an on-policy self-distillation (OPSD) scheme that transfers guidance from a dense-layout teacher model to a sparse-layout student, operating on the student's own rollout states.
**Tools & method:** The final frame's layout is used as an explicit control signal; on-policy self-distillation trains a sparse-layout student against a dense-layout instructor in both last-frame-layout and camera-only modes.
**Limitation (≤3 sentences, authors' own):** The authors state that LIFT currently represents future-view composition with 2D bounding boxes and local text prompts, which provides only coarse spatial constraints and does not explicitly capture depth, orientation, or occlusion relationships between objects.
