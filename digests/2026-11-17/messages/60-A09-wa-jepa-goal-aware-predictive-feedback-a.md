**[A09] WA-JEPA: Goal-Aware Predictive Feedback Action Refinement for a World-Action Model**
- **arXiv:** 2611.19183 · <https://arxiv.org/abs/2611.19183>
- **Submitted:** 2026-11-14 (v1)
- **Authors:** Tao An et al.
- **Qualifying affiliation(s):** Hikvision Research Institute — Wenming Tan, Kai Zhang, Haibo Lei; FLAG: borderline — Hikvision (not on explicit company list; other co-authors are Harbin Institute of Technology and Anhui Polytechnic University)
- **Categories:** cs.CV
- **Open release:** code — <https://github.com/Dovisya/WA-JEPA>
- **Shipped counterpart:** none found

**Summary:** WA-JEPA is a JEPA-based "world-action" model that generates robot action proposals and then iteratively refines them using the model's own latent predictions of future scenes, instead of searching over candidate action sequences.
**Purpose:** Prior JEPA-based world models plan by exhaustively searching and re-evaluating candidate action sequences in latent space, which the authors say incurs substantial online compute cost.
**Breakthrough:** The authors report WA-JEPA reaches 96% success on PushT, 100% on TwoRoom and Cube goal-reaching, and in long-horizon "Anchored Planning" it averages 80.21% (standard starts) and 66.28% (perturbed starts) success, 25.78 and 19.14 points above the LeWM baseline.
**Tools & method:** The model generates an action proposal, predicts resulting future latent scenes/proprioceptive states, and refines the proposal via "goal-discrepancy residual feedback" (comparing predicted-scene and goal latents) and "future-scene context feedback" (preserving fine-grained predicted representations), trained jointly from offline demonstrations.
**Limitation:** The paper has no dedicated limitations section, but the authors note that in the hierarchical setting the speedup over the LeWM baseline shrinks because the baseline only searches a five-action chunk and both methods share retrieval/rendering overhead.
