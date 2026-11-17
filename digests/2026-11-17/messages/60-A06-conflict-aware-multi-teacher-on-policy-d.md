**[A06] Conflict-Aware Multi-Teacher On-Policy Distillation in Aligned Action Spaces for Cross-Game Generalization**
- **arXiv:** 2611.21094 · <https://arxiv.org/abs/2611.21094>
- **Submitted:** 2026-11-16 (v1)
- **Authors:** Jing Yi et al.
- **Qualifying affiliation(s):** FLAG: borderline — LIGHTSPEED (Jing Yi, Haitao Li; likely Tencent's Lightspeed Studios, not independently confirmed beyond the paper's own "LIGHTSPEED" affiliation label); other co-authors at HKUST(GZ)/HKUST
- **Categories:** cs.AI
- **Open release:** none found (paper page links only to the arXiv abstract/PDF)
- **Shipped counterpart:** none found

**Summary:** The authors target zero-shot cross-game generalization: consolidating several single-game vision-language-model (VLM) experts into one model that can control unseen games from raw pixels with no target-game training.
**Purpose:** To build a single VLM game-playing controller that generalizes zero-shot to new games it was never trained on, by better combining knowledge distilled from multiple single-game "teacher" experts without the teachers' conflicting advice canceling out.
**Breakthrough:** The authors report CAMOPD achieves 86.7% (26/30) and 80.0% (24/30) zero-shot Task-1 success on the unseen games GeoDash and Doodle Jump respectively, using a Qwen3.5-4B backbone with rank-16 LoRA fine-tuning, evaluated on GameWorld's "Paused 100-Step Reset-on-Fail" protocol (30 executions per task).
**Tools & method:** CAMOPD is a post-training (distillation) framework built on a Qwen3.5-4B VLM with LoRA (rank 16, attention + MLP projections, sequence length 2048, AdamW), evaluated on the GameWorld benchmark (Ouyang et al., 2026) using temporal-control (GeoDash) and directional-steering (Doodle Jump) transfer suites against prompting, weight-merging, and multi-task distillation baselines.
