**[A02] GameASG-Bench: Benchmarking Autonomous Software Generation for Game Development**
- **arXiv:** 2609.21293 · <https://arxiv.org/abs/2609.21293>
- **Submitted:** 2026-09-18
- **Authors:** Xiuhui Zhang et al.
- **Qualifying affiliation(s):** Ant Group — Xiuhui Zhang, Yi Chen, Shusheng Xu, Fan Li, Huan Wang, Tongkai Yang, Binhang Yuan (co-affiliated with Beihang University and HKUST for two authors); FLAG: Ant Group is a borderline-listed organization (not on the core tracked list; kept and flagged per policy)
- **Categories:** cs.AI, cs.SE
- **Open release:** code — <https://github.com/areal-project/GameASG-Bench>
- **Shipped counterpart:** none found

**Summary:** The paper introduces GameASG-Bench, a benchmark for evaluating whether AI agents can autonomously generate complete, working browser-based games rather than just individual code components.
**Purpose:** Existing code-generation benchmarks check source-level compliance but not whether the resulting application actually behaves correctly at runtime; the authors argue high structural compliance does not guarantee interactive gameplay logic works.
**Breakthrough:** The authors report that across nine agent stacks, the highest "strict task success" rate (passing all L1 checks plus applicable L2 P0/P1 checks) was only 55.3% (26/47 tasks, GPT-6-Astra with Codex CLI), despite mean L2 check pass rates of 93.2% for the same model — a gap the authors say shows partial-credit metrics overstate real capability.
**Tools & method:** Evaluation runs in headless Chromium at a fixed 1280×800 viewport; the benchmark combines tool checks, regex checks, and anti-pattern checks (L1) with P0/P1/P2-tiered runtime checks (L2).
**Limitation:** The authors state the benchmark excludes concepts requiring backends, user accounts, external databases, paid assets, unbounded multiplayer, or behavior unreachable within bounded browser execution, so it does not test full production game stacks.
