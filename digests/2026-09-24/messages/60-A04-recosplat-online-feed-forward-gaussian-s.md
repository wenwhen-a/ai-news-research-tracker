**[A04] ReCoSplat: Online Feed-Forward Gaussian Splatting via Render-and-Compare**
- **arXiv:** 2603.09968 · <https://arxiv.org/abs/2603.09968>
- **Submitted:** 2026-03-10
- **Authors:** Freeman Cheng et al.
- **Qualifying affiliation(s):** NVIDIA — Botao Ye, also listed at ETH Zürich; other authors list UC Merced, Shanghai Jiao Tong University, and HKUST
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** The paper addresses online (causal, streaming) novel view synthesis, where a system must build a renderable 3D Gaussian scene incrementally from sequential images without access to future frames, and must handle a "pose distribution mismatch" between ground-truth poses used in training and predicted poses used at inference.
**Purpose:** Existing 3DGS reconstruction methods largely assume all images are available offline; the authors aim for a feed-forward, causal method that reconstructs and renders scenes on the fly from a live image stream while staying robust to imperfect predicted camera poses.
**Breakthrough:** The authors report on DL3DV (256 views, posed+calibrated) 22.003 PSNR / 0.751 SSIM / 0.202 LPIPS, approaching offline YoNoSplat's 21.549 PSNR while outperforming online baselines (OF3GS, S3PO-GS, a KV-cache variant); for camera pose estimation on the same setting they report 0.709 AUC at a 5° threshold, and processing throughput of 45.1 FPS average (41.1 FPS at end-of-stream) with peak memory under 12 GiB versus 41 GiB for an offline baseline.
