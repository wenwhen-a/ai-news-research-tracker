**[A08] StoryEngine: A State-Grounded Agentic Framework for Video Storytelling**
- **arXiv:** 2609.33627 · <https://arxiv.org/abs/2609.33627>
- **Submitted:** 2026-09-27
- **Authors:** Yingrui Wang, Zeqing Wang, Yeying Jin
- **Qualifying affiliation(s):** Tencent (joint affiliation listed as "Tencent / National University of Singapore" for the author group; all three authors use @u.nus.edu emails)
- **Categories:** cs.CV; cs.AI
- **Open release:** none found (project page only: <https://wwwtaylor.github.io/StoryEngine/;> no code repo mentioned)
- **Shipped counterpart:** none found

**Summary:** StoryEngine is an agentic framework for long-form, multi-shot video storytelling that separates authoritative semantic story-state planning from fallible visual rendering to prevent error propagation across shots.
**Purpose:** The paper addresses consistency failures in long-form generated video narratives, where prior agentic video-generation pipelines lack explicit mechanisms for propagating story consequences (e.g., entity placement and state) across shots.
**Breakthrough:** On a Veo 3.1 backbone, the authors report StoryEngine reaches an average score of 0.7690 versus 0.6274 for ViMax, and an anchor-persistence (APR) score of 0.9389 versus a 0.5500 baseline, on a new 60-story benchmark (three 20-story diagnostic suites: N20, T20, C20).
**Tools & method:** The pipeline uses GPT-5.5 for planning, GPT-Image-2 for images, Veo 3.1 and Wan2.2-TI2V-5B for video generation, and Gemini-3.5-Flash as a VLM judge across a custom 8-metric evaluation protocol; baselines compared were ViMax, MovieAgent, and Direct I2V.
**Limitation:** The authors state that planner-supplied errors propagate downstream, that generative-model visual evidence is limited, and that state progression "remains challenging" (their SPS metric stays below 0.67).
