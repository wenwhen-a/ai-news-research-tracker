**[A03] OmniCam: Omni-Camera Trajectory Generation via Geometry-Grounded Pose Token Learning**
- **arXiv:** 2610.09513 · <https://arxiv.org/abs/2610.09513>
- **Submitted:** 2026-10-07
- **Authors:** Zhenyang Liu et al.
- **Qualifying affiliation(s):** Tencent Hunyuan — FLAG: the paper's affiliation block lists "Fudan University, Shanghai Innovation Institute, Tencent Hunyuan, Zhejiang University" without per-author footnote markers in the rendered HTML; Tencent affiliation is inferred from co-author Chunchao Guo, who is independently confirmed as Tencent Hunyuan (tencent.com email, corresponding author) on the companion submission 2610.10342 the same week
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** none found on the arXiv page
- **Shipped counterpart:** none found

**Summary:** OmniCam is an autoregressive model that generates camera pose trajectories from a single panorama plus a text description of the desired camera motion, using a panoramic point-cloud encoder and a hybrid rotation/translation pose tokenization.
**Purpose:** The authors aim to produce geometry-grounded, text-controllable camera trajectories that generalize across trajectory styles, for downstream use in camera-controlled video generation and robotic active perception.
**Breakthrough:** The authors report 28–47% lower trajectory error and a 65.8% lower collision rate than GenDoP retrained on their own OmniCaT dataset.
**Tools & method:** The model combines a panoramic point-cloud encoder with separate geometric and semantic conditioning and a 3D target anchor; training used 8×NVIDIA H20 GPUs for roughly 100 epochs on the OmniCaT dataset.
**Limitation:** The authors state that geometry is estimated and incomplete and that supervision comes from a heuristic planner, so the model can inherit reconstruction errors and planner bias; observations are also limited to static scenes.
