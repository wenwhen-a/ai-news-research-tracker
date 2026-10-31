**[A05] ETA-Motion: Efficient Topology-Agnostic Motion Diffusion via Sparse Joint Learning**
- **arXiv:** 2610.38259 · <https://arxiv.org/abs/2610.38259>
- **Submitted:** 2026-10-28
- **Authors:** Seoyoung Hwang et al.
- **Qualifying affiliation(s):** Samsung Electronics — Seoyoung Hwang (dual KAIST/Samsung Electronics); FLAG: borderline (Samsung is not on the core tracked list but is a comparable top-tier industry lab)
- **Categories:** cs.CV
- **Open release:** none (project page only: <https://sy-hwang.github.io/eta-motion-page/>)
- **Shipped counterpart:** none found

**Summary:** ETA-Motion generates motion for characters with arbitrary, varying skeletons by training a motion generator on only a compact subset of joints rather than all joints.
**Purpose:** The goal is efficient, topology-agnostic motion generation that generalizes across characters with different skeleton structures and joint semantics, without the computational overhead of modeling every joint densely.
**Breakthrough:** The authors report that dense full-joint modeling in prior topology-agnostic approaches incurs substantial computational overhead and pushes the model to learn topology-specific details that do not transfer; their sparse-joint approach instead reports better results than existing topology-agnostic baselines, with improved efficiency and generalization to unseen motions and topologies.
**Tools & method:** The method combines a visual joint embedding (computed from rigged-mesh vertex features) with textual joint-name cues to build semantic joint embeddings, and pairs these with topology-aware training objectives so training on sparse joint subsets still yields full-skeleton generation at inference.
