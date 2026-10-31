**[A07] METATRON: A Promptable Whole-Body Execution Layer for Humanoids**
- **arXiv:** 2610.38027 · <https://arxiv.org/abs/2610.38027>
- **Submitted:** 2026-10-27
- **Authors:** Chen Tessler, Yifeng Jiang, Alec Otto, Yi Shi, Umar Iqbal, Gal Chechik, Xue Bin Peng
- **Qualifying affiliation(s):** NVIDIA — Chen Tessler, Yifeng Jiang, Yi Shi, Umar Iqbal, Gal Chechik, Xue Bin Peng (Alec Otto, Dollhouse Robotics, interned at NVIDIA)
- **Categories:** cs.RO, cs.AI
- **Open release:** none (project page only: <https://research.nvidia.com/labs/par/projects/metatron/>)
- **Shipped counterpart:** none found

**Summary:** Metatron is a humanoid control system built on a frozen, generative whole-body base policy plus a programmable skill layer on top.
**Purpose:** The goal is a reusable, promptable execution layer for humanoid whole-body control that lets new skills be authored and refined as code on top of a single frozen motion policy, instead of retraining a policy for every new task.
**Breakthrough:** The authors report physical-robot tests covering walking, recovery, teleoperated object pickup, and sitting, with higher reaching success and push robustness than the reference-tracking baselines they compared against.
**Tools & method:** A frozen generative whole-body base policy is driven by prompts combining timed body-part targets, velocity commands, and style cues; skills built on top are authored as ordinary code that coding agents can refine from motion-capture data without retraining the underlying policy.
**Limitation:** The authors state that Metatron's motion repertoire depends on training coverage, so underspecified goals or incidental style cues can produce unintended motions (e.g., abruptly commanding 2 m/s from rest often triggers a front roll), and that all tested methods, including theirs, fall below 10% success under strong (600–800 N) pushes.
