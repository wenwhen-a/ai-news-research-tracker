**[A06] StereoSplat: Metric-Scale Novel View Synthesis via Stereo-Grounded Gaussian Splatting**
- **arXiv:** 2610.35902 · <https://arxiv.org/abs/2610.35902>
- **Submitted:** 2026-09-29
- **Authors:** Vladimir Yugay, Denis Rozumny, Theo Gevers, Elias Vansteenkiste, Martin R. Oswald, Diogo C. Luvizon
- **Qualifying affiliation(s):** Meta — Denis Rozumny, Elias Vansteenkiste, Diogo C. Luvizon (verified as the company Meta in the HTML author block, not a "meta-learning" text match; Vladimir Yugay is University of Amsterdam with a footnote noting an internship at Meta)
- **Categories:** cs.GR, eess.IV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** StereoSplat is a feed-forward 3D Gaussian Splatting architecture built specifically for stereo video, aimed at reliable, metric-scale novel view synthesis.
**Purpose:** The authors address the fact that monocular feed-forward Gaussian Splatting approaches don't exploit the structure of binocular stereo pairs, and aim for metric-scale (not just relative-scale) novel view synthesis that generalizes from synthetic to real stereo video.
**Breakthrough:** The authors report substantial improvements in rendered-novel-view depth accuracy over established baselines while maintaining high-fidelity view synthesis, and state that the model transfers zero-shot to real-world stereo video despite being trained exclusively on synthetic data.
**Tools & method:** The architecture uses a foundation stereo backbone, a Gaussian decoder with cross-view feature fusion and gated depth refinement, and a learnable depth-adaptive aggregation mechanism operating in inverse-depth space.
**Limitation:** The model is trained exclusively on synthetic data (stated), and the authors frame real-world deployment (mixed reality, autonomous driving, robotics) as an application area rather than a setting with reported quantitative results in the abstract.
