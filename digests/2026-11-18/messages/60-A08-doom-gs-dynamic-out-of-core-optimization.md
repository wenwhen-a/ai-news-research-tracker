**[A08] DOOM-GS: Dynamic Out-of-core Optimization for Massive Gaussian Splatting**
- **arXiv:** 2611.22805 · <https://arxiv.org/abs/2611.22805>
- **Submitted:** 2026-11-17
- **Authors:** Doğa Yılmaz, Jialin Zhu, Binglun Wang, He Wang
- **Qualifying affiliation(s):** Baidu Research — Jialin Zhu
- **Categories:** cs.GR
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** DOOM-GS is presented as the first out-of-core optimization method designed specifically for massive-scale dynamic Gaussian Splatting, where spatio-temporal primitives exceed available GPU memory. Prior out-of-core GS methods handled only static scenes.
**Purpose:** The authors address the memory-management and training challenges created by dynamic primitives that move through space and time, which static out-of-core GS methods cannot handle.
**Breakthrough:** The authors report that DOOM-GS can reconstruct city-scale dynamic scenes with high quality on moderate hardware; they also contribute a new large-scale dynamic-GS dataset because, per the abstract, suitable datasets were lacking.
**Tools & method:** The method includes memory strategies for caching spatio-temporal primitives and a fast learning method for handling large primitive counts, with existing out-of-core approaches adapted as comparison baselines.
**Limitation:** No explicit limitation is stated in the fetched abstract.
