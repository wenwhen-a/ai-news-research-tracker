**[A14] MVAgent: Multi-Agent Video Generation via Consistent Condition Construction and Shot-Level Policy Optimization**
- **arXiv:** 2609.30609 · <https://arxiv.org/abs/2609.30609>
- **Submitted:** 2026-09-24
- **Authors:** Xiangyu Kong et al.
- **Qualifying affiliation(s):** Alibaba Group — Wenjie Zhou, Fengping Tian, Lihua Fang, Haoqin Sun, Chenyang Lyu, Longyue Wang, Weihua Luo
- **Categories:** cs.CV
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary:** MVAgent is a multi-agent pipeline for generating multi-shot videos that keep characters, spatial layout, and camera angles consistent across shots, built on top of a frozen video generator.
**Purpose:** When each shot is a separate call to a frozen text-to-video generator, "repeated text does not determine appearance, layout or state," so multi-shot narratives lose character and scene consistency.
**Breakthrough:** The authors report the highest cross-shot Global Consistency score among compared methods (0.5689 vs. 0.5571 for ViMax) and a 61.39% human preference win rate on cross-scene consistency against ViMax, on their new ViMax-Bench benchmark, with an average narrative-quality score of 4.19/5.0.
**Tools & method:** The pipeline chains a Spatial Grounding agent (camera-view anchoring from traversal clips), an Observer and Transition agent (continuity memory of shot endings), and an Orchestrator that composes conditions for the frozen generator, optimized with a new "Trunk-GDPO" reinforcement-learning algorithm that compares shot-level rather than episode-level candidates; experiments use Veo 3.1 as the generator, Gemini 3 Pro as VLM, and GPT-5.4/Qwen3-32B as LLMs, evaluated on ViMax-Bench (35 stories) and NarrativeQA (50 novels).
