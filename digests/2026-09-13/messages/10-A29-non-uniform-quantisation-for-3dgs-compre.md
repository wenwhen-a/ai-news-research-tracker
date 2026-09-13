**[A29] Non-Uniform Quantisation for 3DGS Compression**
- **arXiv:** 2608.28272 · https://arxiv.org/abs/2608.28272
- **Submitted:** 2026-08-28
- **Authors:** Bert Van hauwermeiren, Patrice Rondao Alface, Adrian Munteanu
- **Qualifying affiliation(s):** Nokia — Patrice Rondao Alface; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** An importance-weighted, non-uniform quantisation scheme for 3D Gaussian Splatting compression with weighted merging to remove post-voxelisation redundancy, designed for the standard point-cloud codecs V-PCC and G-PCC.
**Purpose:** To cut 3DGS storage while minimising weighted reconstruction error, targeting MPEG standardisation.
**Breakthrough:** The authors report BD-Rate gains of -28.27% (MPEG Scenes, V-PCC), -48.08% (MPEG Scenes, G-PCC), -44.17% (MPEG Objects, V-PCC) and -32.95% (MPEG Objects, G-PCC) over PSNR, SSIM, IVSSIM and LPIPS, and state their weighted-merging strategy has been adopted into V-PCC Amendment 1.
**Tools & method:** Evaluated on the official MPEG 3DGS common-test-condition datasets on an Intel Core i9-13900 with an NVIDIA RTX 4090.
**Limitation:** The authors state preprocessing adds 112 to 116 seconds for large scenes and that the method underperforms FlexGaussian in some G-PCC configurations.
