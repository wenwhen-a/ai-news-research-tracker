**[A08] MatrixSplat: Matrix-Parallel and Feature-Scalable 3D Gaussian Splatting Rendering on GPUs**
- **arXiv:** 2611.15153 · <https://arxiv.org/abs/2611.15153>
- **Submitted:** 2026-11-11
- **Authors:** Yangming Zhang et al.
- **Qualifying affiliation(s):** Snap Inc. — Jian Wang. FLAG: borderline (Snap is not on the illustrative list but is a comparable industry research lab; other co-authors are from UT Arlington, UT Dallas, University of Georgia, and Argonne National Laboratory)
- **Categories:** cs.CV (accepted to NeurIPS 2026)
- **Open release:** none yet — authors state they "will release our CUDA implementation and evaluation scripts" (no link given in fetched text)
- **Shipped counterpart:** none found

**Summary:** MatrixSplat re-engineers 3D Gaussian Splatting (3DGS) rendering to better use GPU Tensor Cores, replacing the standard sequential depth-sorted alpha-compositing with an order-independent weighted accumulation expressible as matrix operations.
**Purpose:** Standard 3DGS rendering pipelines map poorly to modern GPUs because depth-sorted alpha compositing creates sequential per-pixel dependencies, leaving Tensor Cores (matrix units) underused and becoming worse as semantic feature dimensionality grows.
**Breakthrough:** The authors report 599.9 FPS vs. 156.0 FPS for 3DGS on Mip-NeRF 360 (PSNR 30.35 vs. 30.12), 702.6 vs. 237.9 FPS on LERF, and 510.9 vs. 162.0 FPS on 3D-OVS, plus up to 36.7x lower render-kernel time at 256 feature dimensions.
**Tools & method:** The method has three parts: a tile-based pipeline mapping accumulation to warp-level matrix-multiply-accumulate (MMA) on Tensor Cores; warp-level packing of valid Gaussians to reduce visibility irregularity; and lazy, channel-batched feature fetching (8-channel slices) to cut shared-memory pressure at high feature dimensions.
