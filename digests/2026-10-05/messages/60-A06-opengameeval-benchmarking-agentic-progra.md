**[A06] OpenGameEval: Benchmarking Agentic Programming and Exploration in a Stateful Game Engine**
- **arXiv:** 2610.02563 · <https://arxiv.org/abs/2610.02563>
- **Submitted:** 2026-10-01
- **Authors:** Eray Turkel, Mengsha Sun, Kartik Ayyar, Sean Dunigan, Jack Lu, Vlad Shcherban, Hsiang-Shun Shih, Xin Wang, Tiantian Zhang
- **Qualifying affiliation(s):** Roblox — all nine listed authors
- **Categories:** cs.LG (primary), cs.AI
- **Open release:** code — task suite, per-task annotations, a Roblox Studio plugin, and a leaderboard released under MIT license at <https://github.com/Roblox/open-game-eval>
- **Shipped counterpart:** none found

**Summary:** The authors introduce OpenGameEval, a benchmark that evaluates LLM agents acting inside Roblox Studio on 84 curated game-development tasks (scripting and scene modification), each attempted 16 times by 13 frontier models.
**Purpose:** Existing agent benchmarks largely score only final outcomes, which can mask whether an agent actually understood the environment it was working in.
**Breakthrough:** The authors report that thorough exploration behavior (inspecting scripts and object hierarchies before acting) correlates strongly with success, improving pass rates by 13.4 percentage points on scene-only tasks and 9.8 points on script-only tasks.
**Tools & method:** The benchmark provides 84 tasks with place files and per-task annotations inside Roblox Studio, exposing eight tools split between observation (e.g., script/hierarchy inspection) and action categories, and tests 13 frontier LLMs with 16 attempts each.
**Limitation:** The paper itself notes six tasks remain unsolved by every tested model and that model performance diverges sharply by task type (e.g., 12.5-point variance on scene-modification tasks), indicating the benchmark exposes systematic blind spots rather than a single difficulty axis.
