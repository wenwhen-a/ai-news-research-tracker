**[A04] Budget-aware Correspondence-driven View Selection for Real-time 3D Perception of Mobile Robots**
- **arXiv:** 2611.11809 · <https://arxiv.org/abs/2611.11809>
- **Submitted:** 2026-11-09
- **Authors:** Vaishnav Ramesh, Jacob Carter, Shivali J. Patel, Sanjeev J. Koppal, Md Jahidul Islam
- **Qualifying affiliation(s):** Amazon — Sanjeev J. Koppal (FLAG: borderline — footnote states a concurrent appointment as "Associate Professor at ECE-UF and a Scholar at Amazon Robotics," not a primary industry affiliation)
- **Categories:** cs.RO, cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** The paper introduces BCVS, a pose-free, correspondence-driven view-selection algorithm that runs at over 22 FPS on CPU to filter redundant frames from image sequences for real-time 3D perception on mobile robots.
**Purpose:** The authors target efficient, on-the-fly reduction of redundant imagery for downstream 3D reconstruction on resource-constrained mobile robots (aerial, marine), where full SfM/pose pipelines are too costly to run online.
**Breakthrough:** The authors report BCVS outperforms CPU-friendly baselines at tight view budgets and stays competitive as budgets grow, with aerial and marine field trials showing up to 16% redundancy reduction while maintaining SfM registration and reconstruction quality.
**Tools & method:** Evaluation combines field trials (aerial drone and marine/underwater sequences) with COLMAP-based SfM registration and reconstruction quality checks against CPU-friendly baseline view-selection methods under varying view budgets.
**Limitation:** The authors state BCVS is sensitive to the balance between connectivity and parallax weighting — overweighting connectivity can retain rotation-only redundancy, while prioritizing parallax can fragment overlap.
