**[A03] Gnomon4D: Learning Where and When to Focus for Geometric Motion-Grounded World-Action Modeling**
- **arXiv:** 2611.02474 · <https://arxiv.org/abs/2611.02474>
- **Submitted:** 2026-11-02
- **Authors:** Lingwei Dang et al.
- **Qualifying affiliation(s):** Kuaishou/KlingAI Research — Lingwei Dang (work done during an internship at KlingAI Research), Yan Zhou (project lead), Guoxin Zhang, Pengfei Wan. Other authors list Nanjing University, Beijing Normal University, Shadow AI, Tsinghua University, and South China University of Technology (corresponding author: Qingyao Wu).
- **Categories:** cs.CV
- **Open release:** demo/project page (<https://droliven.github.io/Gnomon4D>) (no code or dataset release stated)
- **Shipped counterpart:** none found

**Summary:** The paper introduces Gnomon4D, a world-action model (WAM) that jointly generates future video, robot actions, and GeoDelta, an explicit 4D geometric motion field capturing how embodiment and object points move in the image plane and change in depth across frames.
**Purpose:** The authors aim to ground world-action models in explicit geometric motion so the model focuses on task-relevant interaction regions and transition moments (e.g., grasp/release), rather than treating the scene uniformly.
**Breakthrough:** The authors report that Gnomon4D leads on the RoboTwin 2.0, VLABench, and RoboDojo benchmarks, and beats the strongest real-robot baseline by 7.0 and 16.0 percentage points in in-distribution and out-of-distribution settings, respectively.
**Tools & method:** The model uses Interaction-Salient Attention (spatial readout focused on task-relevant interaction regions) and Transition-Anchored Aggregation (evidence gathering around motion-state transitions), pretrained on human egocentric data via a shared human-robot quasi-action representation and then mid-trained on robot data.
