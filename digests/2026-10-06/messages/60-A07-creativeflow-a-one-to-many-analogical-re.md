**[A07] CreativeFlow: A One-to-Many Analogical Relation Transfer Method for 3D Asset Generation**
- **arXiv:** 2610.05167 · <https://arxiv.org/abs/2610.05167>
- **Submitted:** 2026-10-04
- **Authors:** Xuechen Li, Shuai Zhang, Nanxuan Zhao, Qing Chen
- **Qualifying affiliation(s):** Adobe Research — Nanxuan Zhao
- **Categories:** cs.AI; cs.GR
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary:** The paper presents CreativeFlow, an analogical generation framework inspired by cognitive science that explicitly models analogical divergent thinking to counter creative homogenization in text-to-3D pipelines.
**Purpose:** The authors state that current text-to-3D generation pipelines suffer from "creative homogenization" — a tendency to produce visually/structurally similar outputs — and aim to introduce controlled, analogy-driven diversity instead.
**Breakthrough:** The authors report that expert evaluations show the framework "substantially enhances creative novelty and visual fascination" compared to baselines, and that it yields a reusable dataset/benchmark for relation-aware 3D model training.
**Tools & method:** The method draws on Wikidata, the Getty Art & Architecture Thesaurus, and AskNature as knowledge sources for attribute and relation inference, combined with LLM-based reasoning and Structure Mapping Theory for analogical mapping; evaluation used custom expert assessments of 5–10 relations per source asset.
**Limitation:** The paper does not include a dedicated limitations section; in the Future Work discussion the authors note a need "to establish robust evaluation metrics specifically designed to quantify generative creativity," implying current evaluation is preliminary rather than standardized.
