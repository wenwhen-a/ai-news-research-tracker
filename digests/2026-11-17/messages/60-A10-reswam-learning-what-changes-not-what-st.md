**[A10] ResWAM: Learning What Changes, Not What Stays, for World-Action Models**
- **arXiv:** 2611.19559 · <https://arxiv.org/abs/2611.19559>
- **Submitted:** 2026-11-14
- **Authors:** Chongyu Fan et al.
- **Qualifying affiliation(s):** FLAG: borderline — Cisco and IBM Research are listed among the paper's affiliations (alongside Michigan State University and University of Michigan); exact per-author mapping to Cisco/IBM was not clearly resolvable from the rendered HTML, but both corporate affiliations appear on the author block.
- **Categories:** cs.RO
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** The paper addresses world-action models (WAMs) — vision-language-action policies augmented with future prediction — which the authors argue waste capacity supervising mostly-static full future observations instead of task-relevant motion.
**Purpose:** The goal is to make world-action models more sample- and compute-efficient by focusing the prediction objective on task-relevant robot/object motion rather than static background, and to reduce the heavy training/inference compute that existing WAMs (reliant on large video generation or separate world models) incur for closed-loop deployment.
**Breakthrough:** The authors report ResWAM achieves top average success rates on LIBERO-Plus (81.1%), RoboTwin 2.0 (93.8%), and RoboDojo (9.40% success, 13.41 score) without any robot pretraining, at the lowest training (2.7-4.0 TFLOPs) and inference compute (1.0-1.4 TFLOPs) among compared methods.
**Tools & method:** ResWAM supervises only the DINOv3-space feature residual between current and future frames rather than the full future observation, which the authors report yields a higher feature rank and representations that spatially concentrate on the robot arm and manipulated objects rather than background.
