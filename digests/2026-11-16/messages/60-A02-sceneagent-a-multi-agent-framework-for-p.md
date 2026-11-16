**[A02] SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation**
- **arXiv:** 2611.17821 · <https://arxiv.org/abs/2611.17821>
- **Submitted:** 2026-11-13
- **Authors:** Xingyi Li, Jiahao Yang, Yiqin Zhu, Jingwen Ye, Yang Sun, Weidong Zhang
- **Qualifying affiliation(s):** Tencent — Xingyi Li, Yiqin Zhu, Jingwen Ye, Yang Sun, Weidong Zhang (Jiahao Yang is affiliated with Fudan University)
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** none (project page has a "Code" button that links only to a placeholder `#`, no GitHub/weights/demo URL found)
- **Shipped counterpart:** none found

**Summary:** SceneAgent is a multi-agent framework for generating 3D game scenes that can be ported across different game-engine backends without rebuilding the generation pipeline from scratch.
**Purpose:** The authors argue that porting a scene generator to a new game engine is hard because planning logic, construction tools, and accumulated experience are often tied to the original backend, not just the final rendered output.
**Breakthrough:** The authors report SceneAgent wins human preference judgments over five baselines (AutoUE, Holodeck, SceneWeaver, Reason-3D, ImperativeScene) at rates of roughly 71.8%–83.4% in a human study (51 participants, 1,860 retained judgments), and 71.0%–85.4% in an automated VLM pairwise-preference evaluation.
**Tools & method:** The system splits roles among an Orchestrator (planning, building, refinement, export), a Planner (asset search and subtask commitment), and Builders (scene construction), with backend adapters handling coordinate conventions, asset bindings, and export to each engine's import schema.
**Limitation:** The authors acknowledge that baselines were adapted to a shared asset repository, renderer, and LLM to allow comparison, which "does not reproduce each original system's full native capabilities," so results only hold in this common-backend setting.
