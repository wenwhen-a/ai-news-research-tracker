**[A09] Anchor3DGS: Feed-Forward 3D Gaussian Splatting with Compact Anchor-Based Representation**
- **arXiv:** 2610.21634 · <https://arxiv.org/abs/2610.21634>
- **Submitted:** 2026-10-15 (v1, 10:18:41 UTC)
- **Authors:** Sheng Ye et al.
- **Qualifying affiliation(s):** Ant Group, Inclusion AI — Sheng Ye, Jiangke Lin, Fudong Wang, Yi Yuan (Sheng Ye is also Tsinghua University; Zhen-Hui Dong and Yong-Jin Liu are Tsinghua University only). **FLAG: borderline** (Ant Group — not Alibaba Group; these are distinct, separately-operating companies. Screening had expected an Alibaba co-author; the real, verified affiliation is Ant Group / Inclusion AI, which does not appear in the default qualified-company list but is included here per the skill's "comparable top-tier lab, flag if unsure" rule given Ant Group's scale and its Inclusion AI research org).
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** Anchor3DGS is a feed-forward 3D Gaussian Splatting method that does not require known camera poses and replaces the common one-Gaussian-per-pixel design with a compact, fixed budget of 3D anchors.
**Purpose:** Pixel-aligned feed-forward 3DGS methods tie the number of Gaussians to input image resolution and view count, which the authors say does not scale well.
**Breakthrough:** With an anchor budget of N=32,768 anchors and K=8 Gaussians per anchor (about 0.26M Gaussians per scene), the authors report 3-view PSNR/SSIM/LPIPS of 23.69/0.764/0.320 on VR-NeRF versus 21.31/0.729/0.340 for the AnySplat baseline, and 21.36/0.678/0.307 vs. 15.65/0.624/0.331 on MipNeRF360.
**Tools & method:** Anchors are placed on a VGGT-based geometry scaffold via entropy-guided sampling, aggregate multi-view image features with occlusion-aware weighting, exchange information via self-attention, and decode into local Gaussians; a lightweight UNet refines the splatted features into an RGB residual.
