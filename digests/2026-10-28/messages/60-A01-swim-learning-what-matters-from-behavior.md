**[A01] SWIM: Learning What Matters from Behaviors for JEPA World Models**
- **arXiv:** 2610.36662 · <https://arxiv.org/abs/2610.36662>
- **Submitted:** 2026-10-27
- **Authors:** Jiaming Hu et al.
- **Qualifying affiliation(s):** Unity Technologies — Yan Zheng, Tian Wang, Florian Dubost, Alejandro Mottini, Junze Liu, Arvind Srinivasan, Kai Zhong, Kun Qian, Sharon Gao, Vianne Gao, Houyu Zhang, Qingjun Cui; Jiaming Hu and Shi Bo are listed with dual affiliation (Boston University and Unity Technologies). Verified from the HTML author block ("Unity Technologies" stated explicitly, not the generic word "unity").
- **Categories:** cs.RO (primary), cs.CV
- **Open release:** none found (comment field only says "25 pages, 1 figure"; no code/weights link found)
- **Shipped counterpart:** none found

**Summary:** SWIM is a method for training JEPA (joint-embedding predictive architecture) world models so that their learned state representation better reflects physical task progress rather than only visual similarity.
**Purpose:** The authors address a known gap in JEPA world models: their visual prediction objective may not capture the physical state that actually determines task progress, and naive state supervision (hand-picked or uniform feature weights) lets redundant features overcount and irrelevant ones obscure meaningful differences.
**Breakthrough:** The authors report that across five simulated robotic manipulation tasks, SWIM's learned state weighting improves planning success over uniform weighting of state features, and that the inverse-dynamics model is used only during training so it adds no computation at planning time.
**Tools & method:** SWIM uses an inverse-dynamics model trained on offline trajectories to learn feature weights, which define a weighted state metric used to align latent and state distances during world-model training.
