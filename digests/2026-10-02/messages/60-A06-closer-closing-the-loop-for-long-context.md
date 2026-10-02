**[A06] CLoSeR: Closing the Loop for Long-Context Streaming Reconstruction**
- **arXiv:** 2610.01927 · <https://arxiv.org/abs/2610.01927>
- **Submitted:** 2026-10-01
- **Authors:** Moyang Li, Zihan Zhu, Wei Zhang, Marc Pollefeys, Daniel Barath
- **Qualifying affiliation(s):** Microsoft — Marc Pollefeys (listed as ETH Zurich, Microsoft)
- **Categories:** cs.CV; cs.RO
- **Open release:** code (GitHub: <https://github.com/MoyangLi00/CLoSeR.git>)
- **Shipped counterpart:** none found

**Summary:** CLoSeR augments a streaming 3D-reconstruction foundation model (LoGeR) with loop-closure detection to perform kilometer-scale 3D reconstruction from monocular video, correcting accumulated tracking drift over long sequences. It detects loop candidates via global descriptors, builds windows combining current and revisited frames, and optimizes camera poses on the SE(3) manifold.
**Purpose:** Streaming reconstruction models accumulate pose drift over long trajectories; the authors address eliminating that drift at kilometer scale without resorting to the more complex optimization manifolds used in prior loop-closure work.
**Breakthrough:** The authors report exploiting two properties of the LoGeR backbone — globally consistent scale across windows and flexibility in temporal frame ordering — to detect loops via SALAD descriptors and perform pose-graph optimization combining sequential and loop-closure constraints.
**Tools & method:** The system is evaluated on the VBR (Vision Benchmark in Rome), KITTI Odometry, Oxford Spires, and DROID-W (dynamic sequences) datasets, with code released on GitHub.
**Limitation:** The authors acknowledge that when the underlying odometry suffers not from accumulated drift but from complete failure — e.g. the frontend model failing under highly dynamic environments or aggressive camera motion — recovery is not possible.
