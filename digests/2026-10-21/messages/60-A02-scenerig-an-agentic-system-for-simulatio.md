**[A02] SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images**
- **arXiv:** 2610.28585 · <https://arxiv.org/abs/2610.28585>
- **Submitted:** 2026-10-20 (v1)
- **Authors:** Rundong Luo et al.
- **Qualifying affiliation(s):** Luma AI — the paper's affiliation block lists "Luma AI" and "Cornell University," with a footnote "Work done during an internship at Luma AI," confirming at least one author is Luma AI-affiliated (individual author-to-institution mapping was not resolvable from the extracted HTML). **FLAG: borderline** — Luma AI is not on the tracked-company list; it is a well-known applied-AI company for generative 3D/video (Genie, Dream Machine/Ray2). Kept per the skill's "when unsure, flag rather than drop" rule, for a human to judge.
- **Categories:** cs.RO (primary); cs.AI, cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** Simulation is valuable for robotics, but building diverse, simulation-ready 3D scenes at scale is difficult, and single-image reconstruction alone does not guarantee objects are correctly identified, placed, and physically grounded.
**Purpose:** The authors aim to produce 3D scenes from a single image that are not just visually plausible but physically stable and behave correctly under robot manipulation, addressing what they describe as frequent object misplacement from post-hoc physics settling in prior methods.
**Breakthrough:** The authors report that SceneRig improves instance segmentation, object-level appearance, and 3D placement while keeping reconstructed scenes physically stable, and that its scenes predict real-robot policy outcomes more accurately than their baseline and more reliably support replay of recorded manipulations without trajectory adaptation.
