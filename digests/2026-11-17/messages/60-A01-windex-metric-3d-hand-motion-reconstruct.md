**[A01] WinDEX: Metric 3D Hand Motion Reconstruction in the Wild for Dexterous Teleoperation and Policy Learning**
- **arXiv:** 2611.21143 · <https://arxiv.org/abs/2611.21143>
- **Submitted:** 2026-11-16 (v1)
- **Authors:** Hongyu Ma et al.
- **Qualifying affiliation(s):** FLAG: borderline — CyberOrigin (Xin You); other co-authors are at City University of Hong Kong
- **Categories:** cs.RO
- **Open release:** demo — project website <https://fruitrabbit.github.io/WinDEX/> (no code, weights, or public dataset release mentioned in the visible text)
- **Shipped counterpart:** none found

**Summary:** Collecting large-scale, metrically accurate 3D hand-motion data in the wild is hard, limiting data for training dexterous robot hands.
**Purpose:** To produce accurate, metric-scale, real-time-capable 3D hand motion reconstruction from cheap in-the-wild video, for use in training dexterous robot manipulation policies and for live teleoperation.
**Breakthrough:** The authors report offline reconstruction running at 43.61 FPS and causal streaming at 171 FPS, with state-of-the-art held-out accuracy of 14.5 pixels in-the-wild reprojection error and 37.29 mm world-frame joint error (with visual-inertial odometry).
**Tools & method:** The pipeline integrates geometric-temporal optimization for metric 3D hand annotation with visual-inertial SLAM for world-frame grounding, a fisheye-native stereo network (WinDEX-Net) trained via a model-assisted "data-model flywheel," and distilled models for offline vs. causal streaming inference; training used 4x RTX 4090 GPUs, offline inference/speed tests used a single RTX 4090 (FP16), and the CyberCap capture rig uses 1920x1200 fisheye stereo at 30 fps plus a 300 Hz IMU.
