**[A56] SPVC: Structured and Panoptic Video Fixing for Cross-Dataset Driving Scene Rendering**
- **arXiv:** 2608.17420 · https://arxiv.org/abs/2608.17420
- **Submitted:** 2026-08-18
- **Authors:** Gen Li, Shu Han, Yun Xi Qiao, Hua Chen, Xuyang Dai, Bohan Li, Hao Zhao, Chaojian Li
- **Qualifying affiliation(s):** Great Wall Motor Company Limited — Hua Chen, Xuyang Dai; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** A two-stage controllable video-diffusion framework that repairs blur, temporal inconsistency and foreground/background misalignment in neural-rendered driving scenes viewed from novel trajectories or with inserted objects.
**Purpose:** To improve driving-simulation fidelity by fixing degraded novel-view renders with explicit geometric conditions (camera poses, HD maps, 3D boxes) across datasets.
**Breakthrough:** On Waymo (4 m lane shift) the authors report FID 45.3 versus 59.1 for Difix3D+ and FVD 658.5 versus 735.0; on nuScenes FID improves 33.62% and FVD 43.45% over the strongest baseline; in closed-loop VAD evaluation the collision rate drops from 50% to 30% and the NeuroNCAP score rises from 2.659 to 3.707.
**Tools & method:** Trained on paired degraded-to-clean video from Waymo, nuScenes and PandaSet, zero-shot tested on EUVS, at 800x448 over 25 frames on an NVIDIA H20 (about 252.64 s per sequence).
**Limitation:** The authors state the method still sits inside a reconstruction-then-rendering paradigm and that temporal consistency depends on input sequence quality.
