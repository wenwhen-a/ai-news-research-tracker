**[A02] MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion Transformers**
- **arXiv:** 2610.06801 · <https://arxiv.org/abs/2610.06801>
- **Submitted:** 2026-10-05
- **Authors:** Jiarui Chen et al.
- **Qualifying affiliation(s):** Tencent (Tencent Hunyuan / "Tencent HY") — Jiarui Chen, Zeqiang Lai, Jiangshan Wang, Ziheng Ouyang
- **Categories:** cs.CV, cs.AI
- **Open release:** demo/project page (<https://dodododddo.github.io/mcsparse-project-page/>) | code — none confirmed
- **Shipped counterpart:** none found

**Summary:** The paper proposes MC-Sparse (Meta-Cached Sparse Attention), a training-free sparse-attention framework for diffusion transformers that combines tile-aligned query grouping, token-level key-value selection, and temporal reuse of selections and residuals across denoising steps.
**Purpose:** Existing sparse-attention methods for diffusion transformers degrade generation quality due to token-grouping constraints, inaccurate interaction selection, and lost attention contributions from discarded tokens; the authors aim to close this dense-sparse quality gap without retraining.
**Breakthrough:** The authors report a 1.80× denoising speedup on Minimax-H3-Base and a 2.32× speedup on 3D asset generation (an internal model, HY3D-Internal), both with negligible quality loss, validated using PSNR, SSIM, LPIPS, VBench scores, Chamfer distance and volumetric IoU/F1 metrics.
**Tools & method:** The method is evaluated on Minimax-H3-Base (768p), HunyuanVideo-13B (720p), Wan2.1 (720p) and HY3D-Internal using Penguin Benchmark and VBench prompt sets (50 samples per task, 345-frame videos), on a single Hopper GPU for most models and 8 Hopper GPUs with Ulysses sequence parallelism for Minimax-H3-Base.
**Limitation:** Not stated beyond the three quality-degradation sources (token-grouping constraints, selection inaccuracy, lost discarded-token contributions) that the method is designed to address.
