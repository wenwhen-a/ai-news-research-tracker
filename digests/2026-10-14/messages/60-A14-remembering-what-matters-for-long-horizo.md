**[A14] Remembering What Matters for Long-Horizon Robotic World Models**
- **arXiv:** 2610.14583 · <https://arxiv.org/abs/2610.14583>
- **Submitted:** 2026-10-10
- **Authors:** Hao Wu et al.
- **Qualifying affiliation(s):** Tencent — Penghao Zhao, Weiyan Wang, Yufei Huang (other authors: HKUST(GZ), North China Electric Power University, LIGHTSPEED, Carnegie Mellon University, CUHK, USTC, Nanyang Technological University, UC Merced)
- **Categories:** cs.RO (primary), cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** The paper studies why autoregressive robot-video world models using discrete visual tokens degrade over long rollout horizons, arguing that keeping the entire generated history actually hurts because persistent scene context, recent visual-action states, and stale history compete for the model's attention.
**Purpose:** Long-horizon rollouts are central to using video world models for robot policy evaluation and planning, but naively keeping full generation history is both computationally expensive and, the authors argue, actively degrades prediction quality.
**Breakthrough:** ReCAP improves visual fidelity, action-conditioned consistency, and robot-structure preservation versus full-context decoding across all four benchmarks (their claim); on BridgeV2 it reduces LPIPS by 63.3%, and across the four benchmarks LPIPS at horizon H=64 degrades far less than Full Context (e.g., Full Context LPIPS rises from 0.204→0.237 on RT-1, 0.106→0.154 on CALVIN, 0.166→0.183 on LIBERO-90).
**Tools & method:** ReCAP is training-free and model-agnostic: it keeps a fixed initial "scene anchor" (to retain persistent scene information) plus a receding window of the most recent visual-action blocks, discarding intermediate history rather than retraining or fine-tuning the underlying discrete-token world model.
