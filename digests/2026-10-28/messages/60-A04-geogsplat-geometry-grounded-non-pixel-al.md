**[A04] GeoGSplat: Geometry-Grounded Non-Pixel-Aligned Gaussian Splatting**
- **arXiv:** 2610.36760 · <https://arxiv.org/abs/2610.36760>
- **Submitted:** 2026-10-27
- **Authors:** Jiale Wang et al.
- **Qualifying affiliation(s):** Horizon Robotics — at least one author (exact name-to-institution mapping not recoverable from the HTML author block, which lists "Xi'an Jiaotong University, EPFL, Horizon Robotics, University of the Chinese Academy of Sciences" as a group without clear per-author linkage); FLAG: borderline (Horizon Robotics is not on the illustrative company list)
- **Categories:** cs.CV
- **Open release:** none found — project page at <https://comedy0913.github.io/projects/geogsplat> exists but no code/weights release is stated in the abstract
- **Shipped counterpart:** none found

**Summary:** GeoGSplat is a feed-forward Gaussian Splatting model for novel view synthesis that adds geometric priors to the non-pixel-aligned framework, which otherwise tends to place Gaussian centers poorly under large viewpoint changes.
**Purpose:** The authors target a tradeoff in feed-forward Gaussian Splatting: pixel-aligned methods scale primitive count with resolution and view count (costly), while non-pixel-aligned methods fix the primitive count but, without explicit ray/depth constraints, misplace Gaussian centers and cause artifacts under large viewpoint changes.
**Breakthrough:** The authors report that GeoGSplat surpasses both state-of-the-art pixel-aligned and non-pixel-aligned Gaussian Splatting baselines on the DTU and NRGBD datasets for novel view synthesis and reconstruction, and that the advantage grows as target viewpoints move farther from the input cameras.
**Tools & method:** The model uses a dual-branch encoder (Anchors + Triplane) to capture coarse and fine-grained 3D structure, followed by a hierarchical decoder that outputs dense 3D points and Gaussian primitives.
