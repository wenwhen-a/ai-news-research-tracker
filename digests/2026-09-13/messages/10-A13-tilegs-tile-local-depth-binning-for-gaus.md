**[A13] TileGS: Tile-Local Depth Binning for Gaussian Splatting Rasterization**
- **arXiv:** 2609.03613 · https://arxiv.org/abs/2609.03613
- **Submitted:** 2026-09-03
- **Authors:** Wei Tan, Matias Turkulainen, Lauri Ilola, Hamed Rezazadegan Tavakoli, Juho Kannala
- **Qualifying affiliation(s):** Nokia Technologies — Lauri Ilola, Hamed Rezazadegan Tavakoli; FLAG: borderline
- **Categories:** cs.GR
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** TileGS reorganises 3DGS rasterisation into tile-local depth bins rasterised front to back, with selective repair where coarse ordering is insufficient, replacing long globally sorted tile ranges.
**Purpose:** Standard 3DGS rasterisation traverses a globally sorted stream that creates long per-tile ranges and heavy geometry-attribute memory traffic, limiting real-time performance.
**Breakthrough:** The authors report, across a 9-scene benchmark, a mean 1.44x raster-kernel speedup on an RTX 4090 and end-to-end frame speedups of 1.069x (RTX 4090) and 1.094x (RTX 1000 Ada) over gsplat while matching its output (|ΔPSNR|, |ΔSSIM|, |ΔLPIPS| all below 0.001). Nsight Compute profiling attributes the gain to reduced raster traversal work, with geometry attributes still 85.8% of raster traffic.
**Tools & method:** Tile-local depth-binned rasteriser with a "No-GW" default variant; benchmarked against gsplat on RTX 4090 and RTX 1000 Ada with Nsight Compute.
**Limitation:** Gains are reported only relative to gsplat on Ada-generation NVIDIA GPUs (observed, not stated).
