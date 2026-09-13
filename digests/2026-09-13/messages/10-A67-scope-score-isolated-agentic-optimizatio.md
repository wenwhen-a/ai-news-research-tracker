**[A67] SCOPE: Score-Isolated Agentic Optimization for Video World Models**
- **arXiv:** 2608.15043 · https://arxiv.org/abs/2608.15043
- **Submitted:** 2026-08-15
- **Authors:** Yuhua Jiang, Jiaming Wang, Qingbin Liu, Feifei Gao
- **Qualifying affiliation(s):** Tencent — Qingbin Liu
- **Categories:** cs.AI
- **Open release:** code (https://github.com/YuhuaJiang2002/SCOPE)
- **Shipped counterpart:** none found

**Summary:** SCOPE is a framework for auditable inference-time adaptation of frozen video world models used as planning simulators, representing prompts, samplers, verifiers and selectors as a typed state updated only through bounded evidence-supported changes before freezing for held-out evaluation.
**Purpose:** To close the "inference-control evaluation gap" so that reported gains from agentic optimisation are trustworthy.
**Breakthrough:** On Physics-IQ the authors report +14.24 points over the frozen base on Wan2.2 (95% CI +8.10 to +21.23) and +12.60 on CogVideoX, while the margin over the strongest matched agentic baseline (+2.07 on Wan) "remains statistically unresolved."
**Tools & method:** Physics-IQ, PAI-Bench-G (judged by Qwen2.5-VL-72B), OpenS2V-Eval, PhyGround and PhyT2V on Wan2.2 and CogVideoX backbones.
**Limitation:** The authors state "strong candidate proposals do not necessarily imply reliable deployment decisions," that effectiveness "is not fully invariant across backbones or metrics," and that further progress needs calibrated uncertainty and selectors that generalise under shift.
