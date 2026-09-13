**[A30] NBS: No Bias Stereo**
- **arXiv:** 2608.28933 · https://arxiv.org/abs/2608.28933
- **Submitted:** 2026-08-28
- **Authors:** Vage Taamazyan, Zhuowen Shen, Stefan Hinterstoisser, Alberto Dall'Olio, Agastya Kalra, Aarrushi Shandilya, Xin Li, Wenping Wang, Kartik Venkataraman
- **Qualifying affiliation(s):** Intrinsic (Google) — Vage Taamazyan, Zhuowen Shen, Stefan Hinterstoisser, Alberto Dall'Olio, Agastya Kalra, Aarrushi Shandilya, Kartik Venkataraman (affiliation printed as "Intrinsic (Google)")
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** NBS is a stereo-matching model built as a plain Vision Transformer with no stereo-specific architectural bias (no cost volumes or geometry modules), trained on large-scale synthetic data, framed by the authors as a 3D reconstruction task.
**Purpose:** It challenges the assumption that stereo 3D reconstruction needs heavy architectural inductive biases for accuracy and efficiency.
**Breakthrough:** The authors report state-of-the-art ETH3D results (EPE 0.09, bad@0.5 of 0.65 on non-occluded pixels) and, on their SimpleProc-S benchmark, about 4x faster runtime (0.060 s vs 0.240 s) and 2.8x lower peak memory (1.23 GB vs 3.52 GB) than S2M2 while roughly halving its bad@4.0 error.
**Tools & method:** Standard ViT backbone; trained on 128 A100 GPUs and a final stage on 64 H100 GPUs; an internal ~2.4M-scene synthetic dataset plus 13 public datasets; evaluated on ETH3D, SimpleProc and XYZ-IBD.
**Limitation:** The authors state the model predicts only positive disparities, requires fixed input dimensions, and its quadratic-memory ViT prevented native-resolution evaluation on Middlebury and Booster.
