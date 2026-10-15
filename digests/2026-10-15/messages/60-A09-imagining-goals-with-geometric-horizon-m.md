**[A09] Imagining Goals with Geometric Horizon Models for Policy Generalization**
- **arXiv:** 2610.19129 · <https://arxiv.org/abs/2610.19129>
- **Authors:** Daniel Lawson et al.
- **Submitted:** 2026-10-13
- **Qualifying affiliation(s):** Google DeepMind — Khimya Khetarpal (listed as "Equal Advising"; also affiliated with Mila and Université de Montréal); other authors are Mila-affiliated
- **Categories:** cs.LG, cs.AI
- **Open release:** project page at <https://td-aug.github.io>; no code repository link found
- **Shipped counterpart:** none found

**Summary:** The paper addresses zero-shot goal generalization in goal-conditioned reinforcement learning, where a policy must handle unseen tasks by composing existing skills.
**Purpose:** Generating new, longer-horizon experience with world/horizon models has been difficult, which limits how well policies generalize to goals not seen during training; TD-Aug aims to make this kind of imagined-goal data generation practical for stitching-style generalization.
**Breakthrough:** On OGBench stitching tasks, the authors report average success rising from 31% to 79% on state-based pointmaze-stitch tasks (e.g., pointmaze-giant-stitch from 0% to 54%), from 29% to 56% on visual-antmaze navigation, and from 13% to 52% on manipulation (cube/puzzle) stitching tasks, in each case comparing TD-Aug against a goal-conditioned flat behavioral-cloning baseline.
**Tools & method:** Geometric horizon models are trained via temporal-difference learning combined with flow matching (TD-Flows) and sampled in a small number of steps; GHM samples serve as augmented imagined goals for training goal-conditioned behavioral-cloning policies; evaluation uses the OGBench suite (state-based and visual maze navigation, and manipulation tasks).
