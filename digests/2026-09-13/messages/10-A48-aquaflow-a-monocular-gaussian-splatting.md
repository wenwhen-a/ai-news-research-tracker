**[A48] AquaFlow: A Monocular Gaussian Splatting SLAM for Underwater Streaming Reconstruction**
- **arXiv:** 2608.22906 · https://arxiv.org/abs/2608.22906
- **Submitted:** 2026-08-24
- **Authors:** Yingxiang Xu, Kerui Ren, Wenqi Guo, Changjian Jiang, Tao Lu, Linning Xu, Mulin Yu
- **Qualifying affiliation(s):** Shanghai AI Laboratory — Yingxiang Xu, Kerui Ren, Wenqi Guo, Tao Lu, Mulin Yu; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** A monocular 3DGS SLAM system for underwater streaming reconstruction that pairs a subsea-finetuned 3D vision foundation model with a hybrid representation of distance-aware neural Gaussians and a physics-inspired light attenuation and scattering model.
**Purpose:** To extend streaming 3DGS reconstruction to underwater scenes where attenuation and scattering degrade pose tracking and geometry.
**Breakthrough:** The authors report PSNR 34.53 dB (Canyons), 26.77 dB (RedSea) and 36.31 dB (UW-Stereo-VI), a 4.74 dB gain and 13.2% lower localisation error than WaterSplat-SLAM, and ATE RMSE of 0.422 m / 0.958 m / 0.157 m on the three benchmarks.
**Tools & method:** Fine-tuned on 224,273 underwater image pairs (TartanAir-Ocean, MIMIR-UW, UWStereo, FLSea-stereo, sweet-corals); a new 62-sequence benchmark; 1.08 FPS (Canyons) on an Intel i9-14900K with one RTX 4090.
**Limitation:** The authors state a need for better zero-shot generalisation of the underwater foundation model and leave dynamic underwater environments to future work.
