**[A06] GeomVLA: Unifying Scene, Motion, and Action in 3D**
- **arXiv:** 2609.13812 · <https://arxiv.org/abs/2609.13812>
- **Submitted:** 2026-09-12 (v1)
- **Authors:** Ziyin Xiong, Nikos Gkanatsios, Moritz Reuss, Katerina Fragkiadaki
- **Qualifying affiliation(s):** NVIDIA — Moritz Reuss
- **Categories:** cs.RO
- **Open release:** none (project page only, no code/weights/demo stated) — <https://ziyin-xiong.github.io/geomvla.io/>
- **Shipped counterpart:** none found

**Summary:** GeomVLA is a Vision-Language-Action model that unifies perception, latent scene-motion prediction, and action generation within a shared robot-centric 3D coordinate frame.
**Purpose:** The authors aim to ground VLA policies in explicit 3D geometry and motion so that action generation can be conditioned on predicted scene dynamics rather than raw 2D image features alone.
**Breakthrough:** The authors report state-of-the-art results on the CALVIN benchmark and competitive performance on LIBERO and RoboTwin2.0, achieved without large-scale robot-action pretraining, and demonstrate real-world manipulation across eight tasks (accepted to CoRL 2026).
**Tools & method:** The method lifts pretrained vision-language features into 3D using depth and camera calibration, trains a 3D Scene Trajectory Denoiser with SpatialTrackerV2 pseudo-labels via a motion-weighted rectified-flow objective, and conditions action generation on geometry-aware attention over these motion features.
**Limitation:** The authors state accuracy depends on precise camera calibration, with depth or extrinsic-calibration errors degrading geometric representations especially in real-world settings.
