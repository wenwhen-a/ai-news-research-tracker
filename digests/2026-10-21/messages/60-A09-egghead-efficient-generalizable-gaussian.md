**[A09] EGGHead: Efficient Generalizable Gaussian Heads from a Single Image**
- **arXiv:** 2610.26898 · <https://arxiv.org/abs/2610.26898>
- **Submitted:** 2026-10-16 (v1)
- **Authors:** Pilseo Park et al.
- **Qualifying affiliation(s):** Qualcomm Technologies, Inc. — Ning Bi (listed with current Qualcomm Technologies, Inc. affiliation); Michel Sarkis is listed as "Formerly of Qualcomm Technologies." Qualcomm is on the tracker's default list, so no borderline flag on the company itself.
- **Categories:** cs.CV
- **Open release:** none found (no code/project-page link stated in the paper)
- **Shipped counterpart:** none found

**Summary:** EGGHead reconstructs a photorealistic, generalizable 3D Gaussian head avatar from a single image in a single forward pass, using a Gaussian-allocation algorithm that assigns a fixed budget of Gaussians to the head's semantic regions.
**Purpose:** The paper addresses a three-way trade-off in head-avatar modeling between representation power, rendering/enrollment efficiency, and generalizability — prior Gaussian-splatting methods still scale with the number of rasterized Gaussians and often have high "enrollment" (optimization/preparation) time.
**Breakthrough:** On the NeRSemble dataset, the authors report EGGHead renders at 121.19 FPS versus 5.26 FPS (E3DGE), 33.61 FPS (G-NeRF), and 43.43 FPS (GAGAvatar), with an enrollment time of 1.54 seconds — slower than GAGAvatar's 0.06 seconds but faster than E3DGE's 8.63s and G-NeRF's 5.96s (Table 4).
**Tools & method:** EGGHead's Gaussian-allocation algorithm assigns Gaussians to semantic head regions under a fixed budget in a single forward pass; pseudo-ground-truth supervision for this allocation is derived from single in-the-wild FFHQ images.
