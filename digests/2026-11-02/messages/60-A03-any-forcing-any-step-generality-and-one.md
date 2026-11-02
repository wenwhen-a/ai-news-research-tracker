**[A03] Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation**
- **arXiv:** 2610.42031 · <https://arxiv.org/abs/2610.42031>
- **Submitted:** 2026-10-30
- **Authors:** Jiahua Xu et al.
- **Qualifying affiliation(s):** FLAG: borderline — Huawei (Technology Planning Dept of the Computing Technology Research Institute, Huawei, Shanghai; and Huawei Noah's Ark Institute, Shenzhen); lead affiliation is Xidian University (academic). Huawei is on the tracker's "borderline, keep + flag" list, not the core tracked-company list.
- **Categories:** cs.CV (primary)
- **Open release:** demo (project page, <https://medcx.github.io/Any-Forcing> — exact path truncated in source; no code/weights release found)
- **Shipped counterpart:** none found

**Summary:** Any Forcing is a framework for autoregressive (streaming) video generation that supports both flexible sampling-step counts and stable one-step generation, addressing the quality/speed tradeoff and the content drift/collapse that one-step methods suffer over long sequences.
**Purpose:** Existing autoregressive video generators fix the number of sampling steps, limiting the quality/speed tradeoff; one-step generation is fast but degrades visual quality and accumulates errors over long sequences.
**Breakthrough:** The authors report 20.9 FPS for short videos and 24.7 FPS for long videos on a single NVIDIA H100 GPU, evaluated on VBench (5-second videos) and VBench++ (30- and 60-second videos) at 480p, with five independent evaluation runs reported for robustness.
