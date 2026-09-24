**[A03] Learn2Splat: Extending the Horizon of Learned 3DGS Optimization**
- **arXiv:** 2605.15760 · <https://arxiv.org/abs/2605.15760>
- **Submitted:** 2026-05-15
- **Authors:** Naama Pearl et al.
- **Qualifying affiliation(s):** Meta — Haofei Xu, Lorenzo Porzi, Peter Kontschieder listed at "Meta Reality Labs"; other authors list University of Tübingen / Tübingen AI Center and ETH Zurich
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** The paper introduces Learn2Splat, a learned optimizer for 3D Gaussian Splatting (3DGS) that replaces manually-scheduled optimizers like Adam, targeting the problem that prior learned optimizers for 3DGS degrade once training runs beyond their training horizon.
**Purpose:** Standard 3DGS optimization requires thousands of hand-tuned iterations per scene; the authors aim for a learned optimizer that remains stable across arbitrarily extended optimization horizons without manual learning-rate scheduling and that generalizes zero-shot to new scenes.
**Breakthrough:** The authors report Learn2Splat achieves the highest PSNR of the compared methods on all eight tested benchmarks (DL3DV, DTU, LLFF, Mip-NeRF360, RealEstate10K) within a fixed runtime budget, outperforming Adam by 0.1–1.7 dB on dense-view settings and outperforming second-order methods (LMRS, 3DGS-LM) by 0.3 dB while using half the memory, despite running roughly 2x slower per iteration.
**Tools & method:** The method combines a meta-training scheme (a checkpoint buffer plus an optimizer-rollout strategy exposing the network to diverse training phases) with a kNN-based Point Transformer architecture and a "State Scale MLP" that encodes gradient-magnitude information, trained with rendering loss plus low-visibility and stability losses.
