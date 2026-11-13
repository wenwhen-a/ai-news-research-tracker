**[A04] Neural Render Proxies for Interactive and Differentiable Lighting**
- **arXiv:** 2611.17185 · <https://arxiv.org/abs/2611.17185>
- **Submitted:** 2026-11-12
- **Authors:** Sergio Sancho et al.
- **Qualifying affiliation(s):** Disney Research|Studios — Sergio Sancho, Alexander Rath, Marco Manzi, Pascal Chang, Amit H. Bermano, Markus Gross, Marios Papas (all list affiliation 2); FLAG: borderline (Disney not on the explicit qualifying list but is a comparable top-tier entertainment/graphics industry lab)
- **Categories:** cs.GR (primary), cs.CV
- **Open release:** none stated (paper names third-party tools it builds on — PyTorch, tiny-cuda-nn, Triton, Mitsuba 3, Disney's Hyperion renderer — but does not say its own code/weights/demo will be released)
- **Shipped counterpart:** none found (Hyperion is Disney's existing production renderer, used as an evaluation baseline/testbed, not claimed as a new shipped feature)

**Summary:** The paper introduces a method for interactive, differentiable relighting of static scenes (fixed camera, fixed materials) by decoupling path sampling from emission computation.
**Purpose:** Production lighting iteration normally requires re-rendering with slow, often non-differentiable offline renderers, taking minutes to hours per frame.
**Breakthrough:** The authors report the method outperforms image-based baselines by 2.8 dB (PSNR) at 1024 training images, with a best ablation configuration reaching 41.07 dB PSNR.
**Tools & method:** Path data for a 960×402, 512-spp production scene took ~30 minutes to render (14–28 GB RAM); standard training took ~1 hour for 100k iterations on an NVIDIA RTX 5090 (32 GB), with path rendering on 32 threads of an Intel Xeon Gold 6342. Light optimization was benchmarked against Mitsuba 3 and ZeroGrads over 50 runs on Cornell Box, Bedroom, and Kitchen scenes.
