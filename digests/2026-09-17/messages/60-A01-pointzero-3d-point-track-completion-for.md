**[A01] PointZero: 3D Point Track Completion for Learning Transferable 3D Dynamics**
- **arXiv:** 2609.19142 · <https://arxiv.org/abs/2609.19142>
- **Submitted:** 2026-09-16 (v1)
- **Authors:** Bardienus P. Duisterhof et al.
- **Qualifying affiliation(s):** NVIDIA — Bowen Wen, Stan Birchfield (co-authors also at CMU and Columbia University)
- **Categories:** cs.CV; cs.RO
- **Open release:** code | dataset | weights (announced) — project page <https://pointzero-wm.github.io;> paper states "We release the dataset, checkpoints, and full training recipe"
- **Shipped counterpart:** none found

**Summary:** The paper studies "3D point track completion" — predicting future 3D trajectories of all observed points from a single RGB-D frame plus sparse partial 3D tracks — as a pre-training objective for learning 3D dynamics without robot action labels.
**Purpose:** Existing action-conditioned 3D dynamics methods require robot action labels, which excludes web video data from training.
**Breakthrough:** The authors report that PointZero "outperforms prior methods on the same data" for the pre-training objective, outperforms baselines on the recent PGND 3D dynamics benchmark when fine-tuned to condition on end-effector pose, and outperforms or matches baselines on 6 of 7 simulated and real-world robot manipulation tasks when fine-tuned to predict robot actions and 3D tracks.
**Tools & method:** PointZero is a transformer architecture trained via the 3D point track completion objective; the training data is a 2.9-million-frame synthetic dataset generated with NVIDIA FleX physics for deformable-object simulation.
**Limitation:** The authors state PointZero "remains limited by the coverage and realism of its pre-training data," which does not capture the full diversity of real-world materials, contact-rich hand-object interaction, cluttered scenes, or long-horizon dynamics.
