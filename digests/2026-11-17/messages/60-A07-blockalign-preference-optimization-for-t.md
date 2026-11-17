**[A07] BlockAlign: Preference Optimization for Trajectory-Distilled Video Generation**
- **arXiv:** 2611.20351 · <https://arxiv.org/abs/2611.20351>
- **Submitted:** 2026-11-16 (v1)
- **Authors:** Jingyuan Zhu et al.
- **Qualifying affiliation(s):** Alibaba Group — all eight authors (contact emails on alibaba-inc.com domain).
- **Categories:** cs.CV
- **Open release:** none (no GitHub/HuggingFace/project page found in abstract or HTML body)
- **Shipped counterpart:** none found

**Summary:** BlockAlign is a preference-optimization framework for aligning few-step, "trajectory-distilled" video generators (e.g., Parallel Decoding Distillation and Parametric Trajectory Distillation models) without teacher fine-tuning or re-distillation.
**Purpose:** The goal is to directly align deployed few-step video generators on their native sampling interface — cutting rollout costs relative to full-trajectory alignment — rather than naively supervising only the primary velocity sub-head, which the authors show induces a training-inference mismatch (their "DirectAlign" baseline) that degrades quality below the unaligned model.
**Breakthrough:** The authors report BlockAlign unlocks the underlying distilled model's (PDD) 5x few-step rollout speedup, yielding 3x faster end-to-end online training, and achieves statistically significant human-preference wins over PDD baselines (54.0% vs. 33.3% wins/losses, a 61.8% non-tie win rate, on RefVid-V4; 51.3% vs. 34.7%, a 59.7% non-tie win rate, on MiniMax-H3).
**Tools & method:** BlockAlign constructs states at valid block boundaries and supervises "span-normalized transition residuals" against the fused block-level velocity predictor, supporting DPO-, NFT-, and rollout-style objectives while preserving the native few-step sampler.
