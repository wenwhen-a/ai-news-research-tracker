**[A02] DiVA: Enabling Interactive Digital Life Simulation via Video Models**
- **arXiv:** 2609.13830 · https://arxiv.org/abs/2609.13830
- **Submitted:** 2026-09-12
- **Authors:** Cheng Chen et al.
- **Qualifying affiliation(s):** Ant Group — Hao Ouyang, Qiuyu Wang, Ka Leong Cheng, Wen Wang, Yihao Meng, Hanlin Wang, Yixuan Li, Yanhong Zeng, Yujun Shen (Cheng Chen also lists Ant Group alongside NTU/A*STAR); **flagged — Ant Group is a borderline/comparable lab, not on the core tracked list**
- **Categories:** cs.CV
- **Open release:** none yet — authors state inference/eval code, model adaptations, and prompt templates "will be made publicly available ... upon publication"
- **Shipped counterpart:** none found

**Summary:** DiVA is an interactive digital-life simulator that supports long, open-ended, multi-turn interactions with a video-generated character (actions plus audio responses), pairing an MLLM router with a three-stage video generation pipeline.
**Purpose:** Current video/avatar generation models produce short clips and degrade visually over extended, user-driven interaction; DiVA aims to enable prolonged, open-ended digital-character experiences without that degradation.
**Breakthrough:** The authors report that the Anchored Video Continuation module cuts quality drift from 0.0947 (InfiniteTalk baseline) to 0.0341 — roughly a 64% reduction — while preserving the highest dynamic-motion score among compared methods and maintaining character identity consistency across a session.
**Tools & method:** An MLLM (GPT-4/Qwen-class model) acts as a semantic router choosing between "waiting" and "action" video segments; a segment-based continuation model transitions the last action-video frame back to a fixed high-quality anchor frame to reset drift.
**Limitation:** The authors acknowledge DiVA inherits fine-grained generation failures from the underlying video model, including physically implausible interactions.
