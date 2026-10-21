**[A05] Latent Bridge: From Video Latents to 3D Geometry via Feature Alignment**
- **arXiv:** 2610.28521 · <https://arxiv.org/abs/2610.28521>
- **Submitted:** 2026-10-20 (v1)
- **Authors:** Shuai Zhang et al.
- **Qualifying affiliation(s):** Horizon Robotics — the paper gives one joint affiliation block ("Huazhong University of Science and Technology, Horizon Robotics") without mapping individual authors to either institution. **FLAG: borderline** — Horizon Robotics is not on the tracked-company list; it is a Chinese autonomous-driving/robotics AI chip and software company (publicly listed), kept here per the skill's "when unsure, flag rather than drop" rule for a human to judge as a possibly comparable industry lab.
- **Categories:** cs.CV
- **Open release:** code at <https://github.com/hustvl/Latent-Bridge> (per the abstract page link)
- **Shipped counterpart:** none found

**Summary:** Video generation and feed-forward 3D reconstruction normally use separate representations, requiring RGB decoding and re-encoding to recover geometry from generated video latents.
**Purpose:** The goal is a reusable, interface between video generation and 3D reconstruction that avoids a separate decode-then-reconstruct pipeline for each generative backbone.
**Breakthrough:** The authors report that one trained bridge transfers across image-to-video and text-to-video generation within the same latent space without retraining, and that on Co3Dv2 and WildRGB-D it gives competitive geometric reconstruction quality with faster latent-to-geometry decoding than decode-then-reconstruct baselines.
**Tools & method:** The authors build representation-specific bridges for the Wan2.1 and V-RAE video-latent spaces, trained via feature distillation on RGB video while the video encoder and geometry model stay frozen, requiring no ground-truth geometry.
