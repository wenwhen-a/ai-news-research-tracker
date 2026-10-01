**[A10] Eulerian Motion Reconstruction for Water Scenery**
- **arXiv:** 2609.38622 · <https://arxiv.org/abs/2609.38622>
- **Submitted:** 2026-09-29
- **Authors:** Chuhan Chen et al. (Chuhan Chen et al.
- **Qualifying affiliation(s):** Meta — Ayush Saraf, Rajvi Shah, Tuotuo Li, Johannes Kopf, Chen Gao, Hung-Yu Tseng, Changil Kim
- **Categories:** cs.CV
- **Open release:** demo (project page: sally-chen.github.io/eulersplats/); no code or weights found
- **Shipped counterpart:** none found

**Summary:** The paper reconstructs a loopable 4D representation of water scenes from monocular video by combining canonical 3D Gaussian splats, a static 3D Eulerian velocity field, and a time-varying residual deformation field, with Gaussians advected via forward Euler integration and cyclically reborn with staggered start times.
**Purpose:** It addresses the gap that existing 4D reconstruction methods assume persistent objects and struggle with water, where particles continuously flow in and out of view rather than persisting across frames.
**Breakthrough:** The authors report PSNR 23.05 / SSIM 0.716 / LPIPS 0.315 on a 7-scene custom water-capture benchmark, outperforming baselines (AmbGS, 4DGS, MoSca, MoVieS) on FID/KID/FVD, and state their method was preferred in 97.6% of user-study judgments.
**Tools & method:** The system is initialized from optical flow and jointly optimized with rendering losses; a separate inference-time propagation algorithm is reported to run 3-4x faster than training-time propagation; training used 8 NVIDIA A6000 GPUs for about 8 hours per scene on a custom 7-scene, ~5,250-frame water capture dataset.
**Limitation:** The authors state the method fails on large water surfaces with reflections (lakes, rivers, oceans), that the static Eulerian field cannot represent time-varying stochastic motion, and that it requires accurate depth initialization from static reconstruction.
