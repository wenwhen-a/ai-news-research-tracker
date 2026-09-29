**[A11] HapticWorld: an Interactive World Simulator with Real-time Torque Feedback**
- **arXiv:** 2609.31924 · <https://arxiv.org/abs/2609.31924>
- **Submitted:** 2026-09-25
- **Authors:** Shaoting Peng et al.
- **Qualifying affiliation(s):** NVIDIA — Yixuan Wang
- **Categories:** cs.RO
- **Open release:** none confirmed (project page only: <https://haptic-world.github.io/;> no code/weights link stated)
- **Shipped counterpart:** none found

**Summary:** HapticWorld extends a learned interactive video-based world simulator with a lightweight torque-prediction head so that an operator collecting robot manipulation demonstrations gets real-time force/torque feedback during teleoperation, not just visuals.
**Purpose:** Contact-rich manipulation needs force sensing that vision alone cannot supply, but real-robot force data collection is hardware-bound, physics simulators mis-model contact forces, and prior learned world simulators are vision-only.
**Breakthrough:** The authors report a 1.6x average improvement in data-collection throughput with haptic feedback, torque-prediction RMSE of 0.26-0.38 N·m (3.5-4.8% normalized error), and real-world policy success of 54/60 trials — close to the 56/60 real-data upper bound and far above the 19/60 vision-only baseline.
**Tools & method:** A torque-prediction head (181K parameters, 0.5% of model size) reads intermediate features from an action-conditioned consistency-model visual backbone (built on the "Interactive World Simulator") and is jointly trained with the visual dynamics loss; data collection used bilateral teleoperation via an OpenArm 1 leader device across three tasks (microwave opening, whiteboard wiping, box pivoting), with training on 8 NVIDIA A100 GPUs over ~2 days and policies trained with ACT (Action Chunking with Transformers).
