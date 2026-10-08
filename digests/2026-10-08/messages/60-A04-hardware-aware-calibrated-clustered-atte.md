**[A04] Hardware-aware Calibrated Clustered Attention for Efficient Visual Geometric Transformers**
- **arXiv:** 2610.09274 · <https://arxiv.org/abs/2610.09274>
- **Submitted:** 2026-10-07
- **Authors:** Weitian Wang et al.
- **Qualifying affiliation(s):** Robert Bosch GmbH — FLAG: borderline (automotive/industrial hardware company, not on the core tracked list; three of four authors list Bosch, the fourth lists Ruhr University Bochum only); comparable in kind to other hardware-adjacent companies on the "keep and flag" list
- **Categories:** cs.CV (primary), cs.LG (cross-list)
- **Open release:** none found on the arXiv page
- **Shipped counterpart:** none found

**Summary:** The paper speeds up the global attention layers of the Visual Geometry Grounded Transformer (VGGT), a 3D scene-reconstruction model, with a hardware-friendly "blockwise clustered attention" (BC attention) that restricts clustering to hardware-aligned neighborhood blocks.
**Purpose:** The authors aim to reduce VGGT's attention latency and off-chip memory traffic on GPUs without materially degrading 3D reconstruction accuracy, adding a calibration method to control the accuracy/speed trade-off.
**Breakthrough:** On ETH3D, calibrated BC attention reaches about 1% accuracy loss (overall error 0.700→0.707) with 2.10–2.63× faster global attention and 1.77–2.35× faster full-backbone latency; a looser setting (under 5% loss) reaches 2.26–2.87× and 1.90–2.55× respectively.
**Tools & method:** Evaluation used a single NVIDIA H200 GPU, PyTorch in bfloat16, and FlashAttention-2 as the attention kernel for both standard and BC attention; benchmarks were ETH3D (point-map estimation) and DTU (dense multi-view stereo), both scored by accuracy, completeness, and Chamfer-style overall error.
