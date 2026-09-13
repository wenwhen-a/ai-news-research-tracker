**[A39] 4DStreamCtrl: Interactive Video Generation with Online 4D Control**
- **arXiv:** 2608.25479 · https://arxiv.org/abs/2608.25479
- **Submitted:** 2026-08-26
- **Authors:** Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu
- **Qualifying affiliation(s):** Tencent Hunyuan — Shiqian Li (also Peking University), Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen
- **Categories:** cs.CV, cs.AI
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** A unified 3D point-track representation for joint camera and object control, depth editing and motion transfer in streaming video generation, integrated into a pretrained diffusion model through a "Geometric Motion Head."
**Purpose:** Real-time streaming 4D-controllable video generation rather than offline or single-signal control.
**Breakthrough:** The authors report 480p video at 20.6 FPS from a causal student distilled from 50 to 4 sampling steps, coherent over 350 frames with constant memory, and on DAVIS an EPE of 5.48 (student) versus 11.18 for MotionStream causal on the same backbone.
**Tools & method:** The OpenVidHD-Motion3D dataset mined from video; a 32x32 grid of 3D point tracks as the control interface; SpatialTrackerV2 for monocular geometry and camera recovery.
**Limitation:** The authors state monocular 3D estimation "can fail on challenging footage with extreme motion blur or occlusions," that the causal student shows a streaming-versus-offline quality gap, and that "small faces and background objects blur progressively" over long sequences.
