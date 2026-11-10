**[A03] HIST3R: Decomposing and Rectifying State Updates with History for Streaming 3D Reconstruction**
- **arXiv:** 2611.12011 · <https://arxiv.org/abs/2611.12011>
- **Submitted:** 2026-11-09
- **Authors:** Kenneth Yang, Yu-Chiang Frank Wang
- **Qualifying affiliation(s):** NVIDIA — Yu-Chiang Frank Wang (listed as National Taiwan University and NVIDIA)
- **Categories:** cs.CV
- **Open release:** none confirmed (project page given: <https://kennethyangg.github.io/HIST3R>; no explicit code/weights link found in the fetched text)
- **Shipped counterpart:** none found

**Summary:** HIST3R is a training-free framework for streaming 3D reconstruction that decomposes CUT3R-style recurrent state updates into a magnitude (how strongly a new observation is written into the scene state) and a direction (where the update moves the state), then rectifies the direction using locally consistent historical states.
**Purpose:** The authors observe that streaming 3D reconstruction with recurrent scene states can drift over long videos because unreliable updates overwrite historical context, and argue existing training-free extensions only control update magnitude, not direction.
**Breakthrough:** Built on top of CUT3R without retraining, the authors report improved long-horizon performance on camera pose estimation, 3D reconstruction, and video depth estimation, including ATE reductions on ScanNet and TUM-Dynamics at 1000 frames and accuracy gains on 7-Scenes and NRGBD at 500 frames, while preserving CUT3R's memory footprint and inference speed.
**Tools & method:** Backbone is CUT3R, with HIST3R applied as a training-free, inference-time extension.
**Limitation:** The authors state that, as a training-free method, HIST3R is bounded by the pretrained CUT3R model and cannot recover geometric information the underlying model does not encode, nor fully correct severely inaccurate candidate predictions.
