**[A01] World Models' Last Exam in Physics**
- **arXiv:** 2610.08791 · <https://arxiv.org/abs/2610.08791>
- **Submitted:** 2026-10-06
- **Authors:** Mingju Gao et al.
- **Qualifying affiliation(s):** FLAG: borderline — the HTML author-notes block lists a combined affiliation "Navers Lab, Einsia.AI Peking University Tsinghua University" without per-author numbering; Peking University and Tsinghua University are academic, and "Navers Lab" / "Einsia.AI" could not be independently verified as established industry labs (web search was unavailable for this check). Kept per SKILL.md's "genuinely unsure → flag rather than drop" rule.
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** Video world models can produce visually convincing but physically inconsistent sequences, which is a concern for their use in prediction and planning for embodied AI.
**Purpose:** The goal is to evaluate physical consistency in video world models using direct, interpretable physical measurements rather than model-based judgments or reference-video comparisons, and to cover physical domains beyond mechanics.
**Breakthrough:** Across eight video generation models and 1,280 generated videos, the authors report persistent physical inconsistencies and substantial variation across tasks, with the best-performing model achieving an overall score of 57.76 out of 100; they also report that their evaluator achieves higher agreement with human judgments than a direct vision-language-model baseline, in both within-task rankings and pairwise comparisons.
**Tools & method:** The benchmark's evaluator combines task-observability screening with task-specific quantitative physical measurements, validated in part on synthetic videos with known physical relationships.
