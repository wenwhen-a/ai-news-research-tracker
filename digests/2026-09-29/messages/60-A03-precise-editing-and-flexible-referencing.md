**[A03] Precise Editing and Flexible Referencing for Interactable Worlds**
- **arXiv:** 2609.34470 · <https://arxiv.org/abs/2609.34470>
- **Submitted:** 2026-09-28
- **Authors:** Xinyao Liao et al.
- **Qualifying affiliation(s):** StepFun — Xianfang Zeng (project leader), Zhu Liang, Qianxun Xu, Gang Yu (corresponding); FLAG: borderline (StepFun is not on the fixed tracked-company list but is a comparable top-tier Chinese AI lab) (co-authors also at Nanyang Technological University)
- **Categories:** cs.CV; cs.AI
- **Open release:** code (<https://github.com/leoisufa/EditWorld,> CC BY 4.0 license); no weights or public demo confirmed
- **Shipped counterpart:** none found

**Summary:** The paper introduces EditWorld, a video world model (referred to as "EditWorld" throughout the paper body) that extends interactive world modeling from pure exploration to precise, streaming content editing with flexible reference images.
**Purpose:** The authors state that existing video world models "primarily focus on navigation," letting users explore generated worlds but offering limited control over modifying existing world content.
**Breakthrough:** The authors report EditWorld "achieves the best overall performance on WBench-Editing with an overall score of 73.8 and an editing score of 80.0," which they describe as "substantially outperforming existing methods on editing-related metrics" (editing score 25.2 points above the second-best model at 54.8).
**Tools & method:** Gated Causal Attention manages temporally varying editing conditions and reference images while preserving causal generation; a Sparse Context mechanism bounds historical context to a sink chunk plus two recent chunks plus k relevant historical chunks.
