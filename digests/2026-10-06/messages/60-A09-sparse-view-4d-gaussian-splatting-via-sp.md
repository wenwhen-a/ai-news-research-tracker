**[A09] Sparse-View 4D Gaussian Splatting via Spatiotemporal Priors and Generative Assistance**
- **arXiv:** 2610.04606 · <https://arxiv.org/abs/2610.04606>
- **Submitted:** 2026-10-03
- **Authors:** Shengqi Wang et al.
- **Qualifying affiliation(s):** JD.com — Yang Liu, Taicheng Huang (FLAG: borderline)
- **Categories:** cs.CV
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary:** The paper presents a 4D Gaussian Splatting framework built for the Sparse-View Track of the SIGGRAPH Asia 2026 Volumetric Video Challenge, which requires dynamic scene reconstruction from only six wide-baseline cameras.
**Purpose:** The authors state the goal is robust dynamic scene reconstruction under extremely sparse, wide-baseline camera setups (six cameras), where standard dense-view 4D Gaussian Splatting methods are not applicable.
**Breakthrough:** The authors report improving full-frame PSNR from a 25.60 dB baseline to 29.75 dB on the validation set, and achieving 30.04 dB full-frame PSNR / 27.88 dB foreground PSNR on the official test benchmark, ranking first overall in the Sparse-View Track of the SIGGRAPH Asia 2026 Volumetric Video Challenge.
**Tools & method:** The pipeline uses YOLO11 and SAM 2 for foreground masks, RoMa for point correspondences, Depth Anything V2 for monocular depth, RIFE for frame interpolation, VideoFlow for optical flow, and an "ArtiFixer" diffusion model for virtual-view restoration; training/evaluation used the official SIGGRAPH Asia 2026 Volumetric Video Challenge data (six training cameras, eight held-out test cameras) on a single NVIDIA RTX 3090 GPU.
**Limitation:** The paper states in its Conclusion and Future Work that "future work will focus on reducing reconstruction time and model size to support real-time applications on standalone VR headsets," implying the current method is not yet real-time or lightweight enough for standalone VR deployment.
