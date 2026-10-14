**[A05] FlowCred: Hierarchical Credit Assignment and Functional Coordination for Joint Text-to-Video Post-Training**
- **arXiv:** 2610.18142 · <https://arxiv.org/abs/2610.18142>
- **Submitted:** 2026-10-13
- **Authors:** Mingxuan Zhu et al.
- **Qualifying affiliation(s):** Kuaishou (KlingAI) — KlingAI is listed among the paper's institutions and a footnote confirms "this work was conducted during the author's internship at KlingAI"; the arXiv HTML page strips superscripts, so the exact author-to-institution mapping could not be independently confirmed beyond this
- **Categories:** cs.CV
- **Open release:** none found (paper links to external model pages Lightricks/LTX-2.5 and Qwen3.5-9B, but no project code repo)
- **Shipped counterpart:** none found

**Summary:** FlowCred addresses two problems in jointly training a prompt-rewriting policy and a video generator on the same terminal reward: prompt-quality credit gets entangled with generation randomness, and the two modules can make redundant, overlapping improvements.
**Purpose:** The goal is more sample-efficient, better-coordinated post-training of text-to-video systems where both a prompt policy and the generator are being optimized together.
**Breakthrough:** On LTX-2.5, the authors report FlowCred raises T2V-CompBench from 61.47 to 64.46 and StoryEval from 55.58 to 58.08 versus a matched joint-training control, without increasing decoded-video or reward-model-call budgets.
**Tools & method:** Experiments use the LTX-2.5 video backbone and Qwen3.5-9B as the prompt-policy model, evaluated on T2V-CompBench and StoryEval, with some baselines re-implemented in a common LTX-2.5 harness; main variants were trained for two or three independent runs.
