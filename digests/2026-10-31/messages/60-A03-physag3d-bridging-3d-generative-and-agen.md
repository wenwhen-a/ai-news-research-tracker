**[A03] PhysAg3D: Bridging 3D Generative and Agentic Models for High-Fidelity and Physically-Interactive Assets**
- **arXiv:** 2610.39924 · <https://arxiv.org/abs/2610.39924>
- **Submitted:** 2026-10-29
- **Authors:** Bi'an Du, Fanpeng Meng, Jiemin Fang, Chen Yang, Pufan Li, Daizong Liu, Qi Tian, Wei Hu
- **Qualifying affiliation(s):** Huawei — Fanpeng Meng, Jiemin Fang, Chen Yang, Qi Tian (also Guangdong Laboratory of Artificial Intelligence and Digital Economy); FLAG: borderline (Huawei is not on the core tracked list but is a comparable top-tier industry lab)
- **Categories:** cs.CV
- **Open release:** none (project page only: <http://supra-3d.github.io/PhysAg3D>)
- **Shipped counterpart:** none found

**Summary:** PhysAg3D couples 3D generative models with agentic reasoning and tool use to turn a single image into an interactive 3D asset.
**Purpose:** The goal is high-fidelity, physically-interactive 3D asset creation from a single image, bridging the gap between purely generative 3D reconstruction (visually faithful but not interactive) and agentic/procedural approaches (interactive but often lower visual fidelity).
**Breakthrough:** The authors report that feedback-based refinement, carried out within a fixed budget, and surface preservation together support appearance fidelity and plausible interactions, validated with evaluations on real photographs and external benchmarks plus ablations on bounded refinement and source-surface preservation.
**Tools & method:** A vision-language agent infers semantic parts, candidate interactions, and physical priors from an image; a 3D generative model produces a textured mesh; a hierarchical interaction representation (parts, joints, deformable regions, surface bindings) then guides iterative, budget-bounded refinement.
**Limitation:** The authors state that recovering hidden structure and material properties remains a limitation of their approach.
