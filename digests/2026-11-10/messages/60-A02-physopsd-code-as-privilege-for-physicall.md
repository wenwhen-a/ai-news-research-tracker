**[A02] PhysOPSD: Code as Privilege for Physically Plausible Video Generation**
- **arXiv:** 2611.12411 · <https://arxiv.org/abs/2611.12411>
- **Submitted:** 2026-11-09
- **Authors:** Harold Haodong Chen et al.
- **Qualifying affiliation(s):** Alibaba — Zilong Dong et al. (affiliation block lists "HKUST & Alibaba Token Hub" and "Alibaba Group"; footnote states the work was done at ATH@Alibaba Group)
- **Categories:** cs.CV
- **Open release:** code — <https://github.com/aigc3d/PhysOPSD>; project page — <https://haroldchen19.github.io/PhysOPSD-site>
- **Shipped counterpart:** none found

**Summary:** PhysOPSD is a framework for making video-generation models physically plausible by using executable simulation code as a "privileged" physical context during on-policy distillation, rather than relying on supervised fine-tuning or sparse physics-based RL rewards.
**Purpose:** The authors note that modern video generators achieve high visual fidelity but often fail at physically plausible motion and complex interactions; supervised fine-tuning suffers from state mismatch and RL struggles with sparse, poorly defined physics rewards.
**Breakthrough:** The authors report dual-level physical privilege via an intermediate bottleneck plus controlled physical variations under shared rollout noise, achieving better physical plausibility than SFT and RL baselines using only about 3K training samples (built from a 33K-instance PhysOPSD-3K dataset), while preserving general video quality across multiple backbones.
**Tools & method:** Applied to two unified video generators (OmniWeaving, 8.3B, and UniVideo, 13B); simulation/annotation tools include MuJoCo, Genesis, and Blender, with Qwen3-VL-32B for annotation and a coding agent (named GPT-6-Astra in the appendix) generating simulation programs.
