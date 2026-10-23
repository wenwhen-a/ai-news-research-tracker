**[A06] EgoHand: Monocular 3D Hand Reconstruction from Egocentric Video**
- **arXiv:** 2610.30293 · <https://arxiv.org/abs/2610.30293>
- **Submitted:** 2026-10-21
- **Authors:** Chao-Yeh Chen, Tiffany Chen, Lin Duan, Tianyi Hu, Yu-Hsiang Huang, Umar Iqbal, Jiefeng Li, Edy Lim, Yanchen Liu, Yihan Pang, Hang Qiu, Jun Saito, Shao Su, Qingsi Wang, Xiufeng Xie (plus NVIDIA leadership contributors per Appendix A)
- **Qualifying affiliation(s):** NVIDIA — all listed core contributors (confirmed via the paper's Appendix A, "Contributors and Acknowledgments")
- **Categories:** cs.CV, cs.LG
- **Open release:** weights (the authors state "We release the EgoHand model"; no download link was found in the retrieved abstract/HTML text)
- **Shipped counterpart:** none found

**Summary:** EgoHand is a model for reconstructing 3D hand poses from monocular egocentric (head-worn-camera) video, aimed at hand-tracking for XR/AR and motion-capture-style applications.
**Purpose:** The authors address the difficulty of accurate, low-latency 3D hand-pose estimation from a single head-worn camera's viewpoint, where hands are frequently self-occluded, truncated at the frame edge, or seen under fast motion.
**Breakthrough:** The authors report that on zero-shot evaluation across the HOT3D, ARCTIC, and H2O benchmarks, EgoHand achieves lower error than baseline methods at about 9.69 ms latency, and a blinded user study favored its reconstructed hand poses over competing baseline systems including Apple EgoDex.
**Tools & method:** EgoHand is trained on a 14-million-image corpus combining synthetic data, in-the-wild video, and multi-camera motion-capture data; the authors state they release the EgoHand model.
**Limitation:** The paper's current abstract/metadata do not state specific failure modes (e.g., extreme occlusion, gloves, or multi-hand interaction) beyond the benchmark and user-study comparisons reported.
