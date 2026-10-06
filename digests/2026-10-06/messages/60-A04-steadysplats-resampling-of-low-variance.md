**[A04] SteadySplats: Resampling of Low-Variance Gaussians for High-Fidelity Stochastic Rendering**
- **arXiv:** 2610.05576 · <https://arxiv.org/abs/2610.05576>
- **Submitted:** 2026-10-04
- **Authors:** Felix Windisch, Thomas Köhler, Lukas Radl, Chris Wyman, Georgios Kopanas, Bernhard Kerbl, Markus Steinberger
- **Qualifying affiliation(s):** NVIDIA — Chris Wyman; Google DeepMind — Georgios Kopanas
- **Categories:** cs.CV, cs.GR
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary:** The paper proposes SteadySplats, a method for high-fidelity stochastic order-independent-transparency rendering of 3D Gaussian Splatting scenes, combining a training-time color-variance regularizer with inference-time history-based spatial resampling and temporal resampling for camera-motion coherence.
**Purpose:** Stochastic rendering of 3DGS avoids expensive global depth sorting but previously produced high noise at low sample counts; the authors aim to make 1-sample-per-pixel stochastic rendering practical and visually close to sorted 3DGS.
**Breakthrough:** The authors report a 13 dB PSNR increase in quality over previous stochastic methods at 1 sample per pixel, with convergence approaching sorted-3DGS rendering quality, evaluated on Mip-NeRF 360 (7 scenes, 21 camera trajectories, 3,152 frames) using PSNR/SSIM/LPIPS and a temporal PSNR metric.
**Tools & method:** The approach is built on a custom Vulkan-based renderer and a standard 3DGS optimization pipeline, measured on an RTX 5090 GPU.
**Limitation:** The authors state the variance-reducing loss dilutes photometric loss and slightly lowers peak quality for fully converged models, spatial resampling adds buffer-management and neighbor-sampling overhead, and the spatial-reuse transmittance approximation (limited to K prior samples) sacrifices strict unbiasedness for faster convergence.
