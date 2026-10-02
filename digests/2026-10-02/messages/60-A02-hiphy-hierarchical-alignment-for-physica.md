**[A02] HiPhy: Hierarchical Alignment for Physically-Plausible Multi-Principle Video Generation**
- **arXiv:** 2610.02197 · <https://arxiv.org/abs/2610.02197>
- **Submitted:** 2026-10-01
- **Authors:** Tahira Kazimi, Shubhankar Borse, Munawar Hayat, Fatih Porikli, Pinar Yanardag
- **Qualifying affiliation(s):** Qualcomm AI Research — Shubhankar Borse, Munawar Hayat, Fatih Porikli
- **Categories:** cs.CV
- **Open release:** none (authors state "we will share our data, code, and checkpoints publicly"; project page: <https://hiphy-video.github.io/>)
- **Shipped counterpart:** none found

**Summary:** HiPhy is a reinforcement-learning framework for video generation that uses hierarchical reward structures to enforce the temporal dynamics of individual physical principles while keeping global scene coherence when several principles act at once. The authors built a 50K-prompt training set and a 1K-prompt evaluation suite (MultiPhyBench) covering concurrent physical events.
**Purpose:** Existing video generation models often fail to produce physically plausible videos, especially when multiple physical principles (e.g. gravity, collision, fluid behavior) must hold simultaneously in one scene.
**Breakthrough:** The authors report improvements of up to 44% in physical commonsense and 80% in semantic alignment over prior methods on their benchmark, with inference overhead of about 2.4 seconds added to the base model.
**Tools & method:** The pipeline applies roughly 50 iterations of supervised fine-tuning followed by about 2,000 GRPO reinforcement-learning iterations, trained on two NVIDIA H200 GPUs using the VideoPhy2 and WISA-80k datasets plus the authors' curated 50K-prompt set.
**Limitation:** The authors state that output fidelity remains bounded by the frozen backbone model's visual capacity, and they note that physics-aware generation raises concerns about misinformation potential and non-consensual content creation.
