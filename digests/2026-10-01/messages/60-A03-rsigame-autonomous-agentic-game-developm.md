**[A03] RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement**
- **arXiv:** 2609.39045 · <https://arxiv.org/abs/2609.39045>
- **Submitted:** 2026-09-30
- **Authors:** Wenyi Wu et al. (Wenyi Wu et al.
- **Qualifying affiliation(s):** ByteDance Inc. — Aayush Salvi, Yiheng Lin
- **Categories:** cs.CL, cs.GT, cs.LG, cs.MA
- **Open release:** code (<https://github.com/WenyiWU0111/RSIGame>), demo/dataset (<https://huggingface.co/spaces/RSIGame/rsigame-page>)
- **Shipped counterpart:** none found

**Summary:** RSIGame is a framework for autonomous agentic game development that pairs a local explore-diagnose-improve loop with a global quality-monitoring loop to recursively self-improve LLM-generated games in the Godot and Phaser engines, evaluated on a new GameCraft-Bench benchmark (140 tasks across 15 game families).
**Purpose:** It addresses the problem that naive recursive self-improvement of LLM-based game generation converges to fragile, bug-ridden solutions that overfit to limited test cases rather than producing robust, playable games.
**Breakthrough:** The authors report that a fine-tuned Qwen3.8-27B model combined with RSIGame reaches a 61.38 overall score on Godot (vs. 37.07 for the unassisted baseline), exceeding one-shot GPT-5.5's 50.26, while reducing generation tokens by up to 1,111x versus baseline; comparable gains (50.24 vs. GPT-5.5's 49.44) are reported on Phaser.
**Tools & method:** A local loop (Controller, Explorer, Editor, Verifier) maintains an evolving issue checklist, while a global loop tracks the best checkpoint and detects convergence after 3 consecutive checkpoints without improvement; the base model is further fine-tuned via supervised learning on roughly 2,200 generation, planning, and verified-improvement traces.
