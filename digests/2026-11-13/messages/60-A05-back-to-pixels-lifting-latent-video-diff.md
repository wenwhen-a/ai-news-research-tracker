**[A05] Back to Pixels: Lifting Latent Video Diffusion into Pixel Space**
- **arXiv:** 2611.17336 · <https://arxiv.org/abs/2611.17336>
- **Submitted:** 2026-11-12
- **Authors:** Yanke Song, Shuo Chen, Chris Rockwell, Guande He, Nan Liu, Desai Xie, Tianpei Gu, Yong-Hyun Park, Aryan V S, Dennis Yuren Menn, Ming-Hsuan Yang, Xun Huang
- **Qualifying affiliation(s):** Roblox (listed affiliation block; other listed affiliations are UC Merced, UPenn, UT Austin)
- **Categories:** cs.CV
- **Open release:** none (project page only: <https://chenshuo20.github.io/PixVid/>; no explicit code/weights statement)
- **Shipped counterpart:** none found (Roblox-affiliated; no named shipping product claimed in the paper)

**Summary:** The paper presents PixVid, which adapts a pretrained latent video diffusion model (Wan2.1-14B) to generate video directly in pixel space instead of a compressed VAE latent space.
**Purpose:** Latent compression in standard video diffusion models limits high-resolution generation, frame-level control, and response latency, which matters for interactive/world-model-style applications.
**Breakthrough:** The authors report VBench totals of 84.78 (480p) and 85.09 (960p) for PixVid versus 84.05 for Wan2.1 and 83.72 for PixelUMM, and a human study where PixVid won all pairwise comparisons against baselines on 100 Movie Gen prompts.
**Tools & method:** Training used roughly 6.4M Wan2.1-generated clips (convergence ~1.3M clips, ~44K B200 GPU-hours), on NVIDIA B200 GPUs with batch size 64 across 64 GPUs.
**Limitation:** Without temporal compression, PixVid processes ~3.9x as many tokens per second as Wan2.1 at 480×832, raising cost for short low-resolution clips.
