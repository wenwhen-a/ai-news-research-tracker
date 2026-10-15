**[A05] WorldMemBench: A Comprehensive Benchmark for Memory of Video World Models**
- **arXiv:** 2610.19063 · <https://arxiv.org/abs/2610.19063>
- **Submitted:** 2026-10-13
- **Authors:** Nan Zhou et al.
- **Qualifying affiliation(s):** Ant Group — Nan Zhou, Jianxiong Gao, Qiuyu Wang, Jiahao Wang, Yufeng Yuan, Shuaiting Li, Hao Ouyang, Yujun Shen; FLAG: borderline — Ant Group
- **Categories:** cs.CV
- **Open release:** homepage <https://zju-real.github.io/WorldMemBench/> · code <https://github.com/ZJU-REAL/WorldMemBench> · dataset <https://huggingface.co/datasets/rescuerz/WorldMemBench>
- **Shipped counterpart:** none found

**Summary:** WorldMemBench is a benchmark testing whether video world models remember their own past, spanning 260 test cases.
**Purpose:** The authors argue that world memory is a critical capability to evaluate in video world models alongside visual fidelity and video duration, and built this benchmark because existing evaluation did not systematically test it.
**Breakthrough:** Evaluating nine video world models (including HY-WorldPlay, Matrix-Game 3, Matrix-Game 3.5, SANA-WM, YUME, LingBot-World, LingBot-World-v2, Evoke, and DreamX-World), the authors report that good static content retention does not guarantee reliable dynamic state tracking, and that memory reliability degrades over repeated revisits; human studies corroborated the automatic evaluation metrics.
**Tools & method:** Static content is checked against fixed reference images and dynamic events against expected state changes, combining appearance and geometry metrics with event-specific checks; video quality and camera-following accuracy are reported as supplementary measures; the benchmark, code, and dataset are publicly released.
