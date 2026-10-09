**[A01] What 30,000 Hours of Ego-centric Video Does Not Teach**
- **arXiv:** 2610.12464 · <https://arxiv.org/abs/2610.12464>
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Jiahua Dong et al.
- **Qualifying affiliation(s):** Toyota Research Institute (TRI) — listed as an affiliation for multiple co-authors in the HTML author block (per-author superscript mapping did not render, so the exact subset of the 10 authors is not individually resolvable from the HTML, but TRI is unambiguously one of the paper's stated affiliations, distinct from the academic ones). **Flag: TRI is not on the explicit tracked-company list; keeping as a comparable top-tier industrial research lab, for user judgment.** Academic co-affiliations: UIUC, CMU, Johns Hopkins.
- **Categories:** cs.CV
- **Open release:** not stated in the abstract or abs page (a project-style URL appears garbled in extraction; not independently confirmed, so omitted)
- **Shipped counterpart:** none found

**Summary:** The paper studies how far scaling ego-centric human video (30,000 hours, 1,000+ scene types, 14,000+ contributors) can push video world models as an alternative to physics-based simulators.
**Purpose:** The authors want to know whether scaling data alone closes the gap between video world models and physics simulators, and where it does not.
**Breakthrough:** The authors report a 100x increase in training data improves both agent and object fidelity, but unevenly: agent modeling becomes strong while object fidelity stays much lower and improves slowly.
**Tools & method:** The study trains on a 30,000-hour ego-centric video dataset and evaluates on a dedicated out-of-distribution benchmark; findings are also reported to transfer to downstream humanoid modeling.
**Limitation:** The authors state that a substantial object-fidelity gap remains even after their supervision change, and conclude that closing it depends on training methods, not data volume alone.
