**[A04] CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion**
- **arXiv:** 2610.29915 · <https://arxiv.org/abs/2610.29915>
- **Submitted:** 2026-10-21 (v1)
- **Authors:** Kai Zhu et al.
- **Qualifying affiliation(s):** NVIDIA — Duomin Wang. FLAG: borderline — core contribution is camera-ego-motion consistency in general-purpose video generation models (VGMs), not a world-model paper per se, though the authors tie results to world action model (WAM) gains on a robotics benchmark.
- **Categories:** cs.CV
- **Open release:** code (github.com/PKU-VaLuE-Lab/CausalAlign) and project page (pku-value-lab.github.io/CausalAlign-homepage)
- **Shipped counterpart:** none found

**Summary:** The paper addresses camera ego-motion drift over long horizons in diffusion-based video generation models.
**Purpose:** The authors state camera ego-motion is essential for consistent geometry and trajectories in generated video, but that it drifts over long horizons in existing video generation models, motivating a diagnostic-then-alignment approach.
**Breakthrough:** The authors report CausalAlign improves motion accuracy, geometric consistency, and temporal smoothness on fine-tuned Wan2.2, with geometric consistency improved by more than 20% relative to the base model.
**Tools & method:** The method combines linear probing and causal interventions to locate where/how ego-motion is represented during denoising, then aligns those layers' representations to a 3D foundation model in a delta-token space; it is applied by fine-tuning Wan2.2 on the DL3DV and RealEstate10K datasets.
**Limitation:** The authors' own diagnosis finds ego-motion representation "fades away" at late denoising timesteps and in the last few transformer layers, which they interpret as a retention failure of the internal ego-motion state rather than a failure to form camera geometry initially.
