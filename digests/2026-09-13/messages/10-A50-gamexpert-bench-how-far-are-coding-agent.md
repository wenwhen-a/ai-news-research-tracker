**[A50] GameXpert-Bench: How Far Are Coding Agents from Expert Game Development?**
- **arXiv:** 2608.21833 · https://arxiv.org/abs/2608.21833
- **Submitted:** 2026-08-22
- **Authors:** Kun Chen, Haorong Hong, Peizhong Gao, Jianfeng Lin, Tongxu Luo, Yuxuan Xie, Chenxu Liu, Jieling He, Zhongyuan Liu, Zeno Zeng
- **Qualifying affiliation(s):** Tencent — Yuxuan Xie, Jieling He, Zhongyuan Liu (Lightspeed Studios); Zeno Zeng (Hunyuan Team)
- **Categories:** cs.AI, cs.CL
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** GameXpert-Bench evaluates LLM coding agents on end-to-end game development in three stages: generating a game from a request (97 tasks, 11 genres), diagnosing and fixing injected bugs (100 human-verified tasks) and iterative multi-turn improvement (17 chains), tested by live game interaction and behavioural checks.
**Purpose:** To measure how far coding agents are from expert game development, since prior benchmarks neglect bug-fixing and iterative refinement.
**Breakthrough:** The authors report Claude-Opus-5 leading GameGen with 79.7/100 (15 models, 1,455 runs; richness averages only 46.1), scoring 39.0/100 on GameFix under strict scoring, and 93.96/100 on GameOpt.
**Tools & method:** 50 confidential human-verified game levels with 19 to 27 injected bugs each; 701 acceptance criteria for optimisation; Playwright and headless Chromium runtime verification plus annotation by game-design specialists.
**Limitation:** The authors conclude "initial generation quality alone is insufficient to characterize an agent's game development capability," citing gaps in self-discovery, verification, regression control and long-horizon task management.
