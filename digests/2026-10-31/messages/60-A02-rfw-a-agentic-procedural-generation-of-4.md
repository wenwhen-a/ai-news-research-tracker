**[A02] RFW-A: Agentic Procedural Generation of 400K Articulated Assets over 500 Categories**
- **arXiv:** 2610.40333 · <https://arxiv.org/abs/2610.40333>
- **Submitted:** 2026-10-29
- **Authors:** Yuanbo Lyu et al.
- **Qualifying affiliation(s):** Alibaba Group — Yuanbo Lyu, Yi Yang, Jiawei Weng, Weiyi Lin, Lin Qu, Zenan Meng, Hu Wei (corresponding authors' contact emails use @alibaba-inc.com), plus Wenyi Li, Jiarui Guo, Rui Zhang, Jingrun Du (dual Alibaba/Tsinghua)
- **Categories:** cs.CV
- **Open release:** none (project page only: <https://brain-labbb.github.io/RFW_A_web/>)
- **Shipped counterpart:** none found

**Summary:** RFW-A combines agentic program synthesis with procedural generation: agents build reusable, category-level generator programs from existing articulated-asset code, test and refine them across sampled configurations, then produce assets procedurally without further model calls.
**Purpose:** The goal is to make large-scale construction of high-quality articulated 3D assets for embodied perception, simulation, and manipulation far cheaper than manual annotation, procedural modeling, or per-asset agentic reasoning.
**Breakthrough:** The authors report an average generator-authoring cost of $10.62, dropping to about $0.05 per asset once amortized over 200 assets per category, while maintaining high structural and kinematic validity and stable execution across physics simulators.
**Tools & method:** Agents synthesize and refine category-level generator programs from sampled configurations, after which assets are produced procedurally without further model calls; the resulting RFW-A-400K dataset is validated for structural/kinematic correctness and simulator stability.
