**[A03] InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation**
- **arXiv:** 2610.06850 · <https://arxiv.org/abs/2610.06850>
- **Submitted:** 2026-10-05
- **Authors:** Yucheng Zhang et al.
- **Qualifying affiliation(s):** NVIDIA — Yucheng Zhang, Sirui Xu, Jinhong Li, Liuyu Bian, Anatulya Nandi, Derek Zhang, Xiangchen Liu, Xueting Li, Umar Iqbal, Yu-Xiong Wang, Liang-Yan Gui (all authors listed with dual University of Illinois Urbana-Champaign / NVIDIA affiliation in the paper header)
- **Categories:** cs.RO, cs.CV, cs.GR
- **Open release:** demo/project page (<https://sirui-xu.github.io/InterMimicGen>) | code — none confirmed
- **Shipped counterpart:** none found

**Summary:** The paper presents InterMimicGen, a framework that retargets motion-captured human-object interaction data to humanoid robots with dexterous hands, trains a physics-based tracking policy in simulation, and uses an iterative "self-evolving" augmentation loop to expand the motion dataset while keeping only variants whose simulated execution completes the task.
**Purpose:** Humanoid loco-manipulation research is limited by scarce, diverse, physically executable human-object interaction references; the authors aim to scale usable training data for whole-body dexterous manipulation without manual re-collection.
**Breakthrough:** The authors report that the self-evolution loop grows the verified reference library by up to 150.5× by round 5 in a bimanual Inspire-hand setting and 146.4× in grasping scenarios, with retargeting achieving 5.62 cm MPJPE and 83.45% hand-contact preservation, and policies that transfer to physical robot execution.
