**[A08] The Flip Test: Video World Models Fail to Learn the World State**
- **arXiv:** 2611.19822 · <https://arxiv.org/abs/2611.19822>
- **Submitted:** 2026-11-15
- **Authors:** Mi Luo, Lijun Yu, Adams Wei Yu, Ang Cao, Baochen Sun, Ming-Hsuan Yang, Nan Hua, Yuan Hao, Alex Dimakis, Ya Xu, Ed H. Chi, Xuezhi Wang, Yinxiao Liu
- **Qualifying affiliation(s):** Google DeepMind — Lijun Yu, Adams Wei Yu, Ang Cao, Baochen Sun, Ming-Hsuan Yang, Nan Hua, Yuan Hao, Ya Xu, Ed H. Chi, Xuezhi Wang, Yinxiao Liu (Mi Luo: UT Austin, work done as a Google DeepMind intern; Alex Dimakis: UC Berkeley)
- **Categories:** cs.CV, cs.AI, cs.RO
- **Open release:** demo (project page <https://flip-test.github.io/>); no GitHub/HuggingFace link found
- **Shipped counterpart:** none found

**Summary:** The authors introduce FlipTest, a counterfactual benchmark that probes whether video world models actually track physical world state rather than just drawing plausible pixels.
**Purpose:** The paper asks whether current video world models encode genuine causal/physical state needed to predict divergent futures, as opposed to merely generating visually plausible continuations.
**Breakthrough:** The authors report the best video model (Gemini Omni Flash 1.1) averages only 18.3% pair accuracy, below the 25% chance baseline, and that models flip their prediction about as often on steps that leave the future unchanged as on steps that change it.
**Tools & method:** FlipTest has a three-level hierarchy: visual minimal pairs (detection), matched four-state controls (selectivity), and dense sweeps (localization of the model's implicit decision boundary).
**Limitation:** The authors rely on VLM judges (two Gemini variants) whose agreement with human labels is reported at 79%, and the full limitations discussion (Appendix G) was not accessible in the fetched text.
