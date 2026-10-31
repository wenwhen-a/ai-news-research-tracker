**[A08] GOFish: Full Field-of-View Gaussian Splatting and Mesh Extraction**
- **arXiv:** 2610.37818 · <https://arxiv.org/abs/2610.37818>
- **Submitted:** 2026-10-27
- **Authors:** Allen Tu et al.
- **Qualifying affiliation(s):** Amazon — Allen Tu, Meher Gitika Karumuri, Shifan Zhu, Hailing Wang, Yen-Liang Lin, David Held (per PDF affiliation superscript "1 = Amazon"; most likely as an internship collaboration, since other authors hold University of Maryland/Northeastern/CMU affiliations)
- **Categories:** cs.CV, cs.GR, cs.RO
- **Open release:** none (project page only: <https://3dgofish.github.io/>)
- **Shipped counterpart:** none found

**Summary:** GOFish is the first 3D Gaussian Splatting surface reconstruction method that trains directly on fisheye images, rasterizing fields of view beyond 180° and extracting an aligned mesh from the same scene.
**Purpose:** The goal is to build simulation-ready digital twins directly from wide-FoV fisheye cameras (used by robots, autonomous vehicles, and consumer 360° cameras) without requiring LiDAR, since prior fisheye Gaussian Splatting methods cap out at 180° and don't produce meshes, while Gaussian surface-reconstruction methods assume pinhole images.
**Breakthrough:** The authors report PSNR improvements over the best prior method of 2.28 dB and 1.97 dB on the 200° FIORD and 205° FullCircle benchmarks respectively, and the highest mesh F-score on FIORD and the main ScanNet++ set.
**Tools & method:** The method combines calibrated densification, Calibrated Mip Filtering, and Wide-Angle Appearance Modeling on top of 3D Gaussian Splatting, trained directly on calibrated fisheye images, and extracts a mesh aligned to the reconstructed Gaussian scene; it is evaluated on the FIORD, FullCircle, and ScanNet++ benchmarks.
