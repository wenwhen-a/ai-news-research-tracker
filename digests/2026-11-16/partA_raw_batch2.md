## SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation
- **arXiv:** 2611.17821 · https://arxiv.org/abs/2611.17821
- **Submitted:** 2026-11-13
- **Authors:** Xingyi Li, Jiahao Yang, Yiqin Zhu, Jingwen Ye, Yang Sun, Weidong Zhang
- **Qualifying affiliation(s):** Tencent — Xingyi Li, Yiqin Zhu, Jingwen Ye, Yang Sun, Weidong Zhang (Jiahao Yang is affiliated with Fudan University)
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** none (project page has a "Code" button that links only to a placeholder `#`, no GitHub/weights/demo URL found)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SceneAgent is a multi-agent framework for generating 3D game scenes that can be ported across different game-engine backends without rebuilding the generation pipeline from scratch. It keeps a canonical, backend-agnostic scene representation (SceneContext) and distills human-approved construction traces into reusable "Layout" and "Content" skills that transfer across engines. The authors evaluate it on a new benchmark, GameSceneBench, against five baseline scene-generation systems.

**Purpose (≤3 sentences):** The authors argue that porting a scene generator to a new game engine is hard because planning logic, construction tools, and accumulated experience are often tied to the original backend, not just the final rendered output. SceneAgent is meant to separate the reusable planning/construction process from engine-specific execution so the same agent experience can be redeployed in a different engine. They introduce GameSceneBench (69 indoor/outdoor prompts) to evaluate scene generation quality across methods.

**Breakthrough (≤3 sentences):** The authors report SceneAgent wins human preference judgments over five baselines (AutoUE, Holodeck, SceneWeaver, Reason-3D, ImperativeScene) at rates of roughly 71.8%–83.4% in a human study (51 participants, 1,860 retained judgments), and 71.0%–85.4% in an automated VLM pairwise-preference evaluation. The authors state their ablations show the reusable skill library and multi-agent protocol mainly improve prompt alignment and scene completeness, at the cost of extra runtime. They also report a cross-engine deployment of all 69 prompts to a second engine ("Engine B"), which they describe as demonstrating portability through the backend-adapter boundary rather than a matched quality comparison.

**Tools & method (≤3 sentences):** The system splits roles among an Orchestrator (planning, building, refinement, export), a Planner (asset search and subtask commitment), and Builders (scene construction), with backend adapters handling coordinate conventions, asset bindings, and export to each engine's import schema. Asset retrieval uses `search_modules`, an entity-first approximate-nearest-neighbor search over offline-encoded asset-card embeddings. Experiments use DeepSeek-V4-Flash as the generation LLM for all methods, gpt-4o-2024-11-20 as the VLM judge, and CLIP ViT-L/14 for CLIPScore.

**Limitation (≤3 sentences):** The authors acknowledge that baselines were adapted to a shared asset repository, renderer, and LLM to allow comparison, which "does not reproduce each original system's full native capabilities," so results only hold in this common-backend setting. They also note the cross-engine study uses different asset catalogs in each engine, so it does not support a direct quality comparison between engines. The reusable-skill approach adds runtime overhead compared to simpler baselines, per their ablations.

---

# Near-misses
- 2611.17775 · Beyond Prediction Gain: LASR as a Metric for Action-Grounded Latents in World Models · purely academic (Tsinghua University, Beijing Jiaotong University), no industry co-author
- 2611.17752 · Stage-wise Lineage-aware Dropout for Sparse-View 3D Gaussian Splatting · purely academic (Hefei University of Technology, Victoria University of Wellington, UNSW), no industry co-author
- 2611.17681 · OCTAVE: A Capability-Resolved Benchmark for End-to-End HTML5 Game Generation · no qualifying-company co-author (authors from Shanghai Jiao Tong University, Shandong University, Zhongguancun Academy, and "Rezona Lab", none of which is a recognized top-tier industry lab on the qualifying list)
- 2611.17626 · Joint World Action Models through Differentiable Trajectory Optimization · purely academic (UC Berkeley / Hybrid Robotics, BAIR), no industry co-author
- 2611.17529 · Learning Latent Goal Costs for Visual World-Model Planning with an Expanding Curriculum · purely academic (Technical University of Crete), no industry co-author
