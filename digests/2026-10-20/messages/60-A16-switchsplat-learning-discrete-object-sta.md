**[A16] SwitchSplat: Learning Discrete Object States from Casually Captured Scenes**
- **arXiv:** 2610.24812 · <https://arxiv.org/abs/2610.24812>
- **Submitted:** 2026-10-17
- **Authors:** Yizheng Xie et al.
- **Qualifying affiliation(s):** Wayve Labs (Vancouver) — Daniel Rebain, Shrisudhan Govindarajan, Andrea Tagliasacchi. FLAG: borderline — Wayve is a UK autonomous-driving software company (backed by $1B+ rounds from NVIDIA, Microsoft and SoftBank) not on the explicit qualifying list, though comparable in standing.
- **Categories:** cs.CV (cross-listed cs.GR)
- **Open release:** none found for code/dataset; project page at <https://switchsplat.github.io>
- **Shipped counterpart:** none found

**Summary:** SwitchSplat extends 3D Gaussian Splatting to casually captured scenes containing discrete object-state interactions (e.g., opening a door, toggling a switch), which standard static 3DGS and time-conditioned 4DGS methods can't model without tying state to a specific recorded timestamp.
**Purpose:** The goal is to let 3D Gaussian Splatting represent scenes with discrete interactable object states from ordinary casual video capture, rather than only replaying the exact recorded state sequence as 4DGS does.
**Breakthrough:** The authors report SwitchSplat outperforms static and dynamic (4DGS-style) baselines on a new casual-capture dataset and can render state combinations that were never observed together during capture.
**Tools & method:** Uses a VLM to seed the number of interactable slots and approximate interaction timing, with per-part geometry learned via a differentiable Gaussian-to-slot assignment.
**Limitation:** The authors state the method assumes binary (not continuous or multi-valued) object states and single-operator capture, and that "fully unsupervised discovery of both the number and timing of interactions from raw video remains an open problem" since slot count/timing are VLM-seeded.
