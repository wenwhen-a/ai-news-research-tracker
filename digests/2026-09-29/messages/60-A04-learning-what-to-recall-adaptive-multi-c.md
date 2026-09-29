**[A04] Learning What to Recall: Adaptive Multi-Cue Episodic Memory for World Models**
- **arXiv:** 2609.34677 · <https://arxiv.org/abs/2609.34677>
- **Submitted:** 2026-09-28
- **Authors:** Beomsu Kim, Chieh-Hsin Lai, Bac Nguyen, Amir Bar, Jong Chul Ye, Yuki Mitsufuji
- **Qualifying affiliation(s):** Sony Group Corporation — Chieh-Hsin Lai, Yuki Mitsufuji (co-authors also at KAIST, Imperial College London)
- **Categories:** cs.LG; cs.AI; cs.CV
- **Open release:** none found (project page only: <https://1202kbs.github.io/FAR-Project-Page/;> no code repo or weights confirmed)
- **Shipped counterpart:** none found

**Summary:** The paper proposes Future-Aware Recall (FAR), a method for world models to learn which past episodic memories are useful for predicting future observations, using future-aware predictive supervision and adaptive multi-cue scoring (temporal, pose, visual, audio).
**Purpose:** The authors address the problem of determining which stored past memories a world model should retrieve and trust when predicting the future, rather than relying on fixed recall heuristics.
**Breakthrough:** The authors report FAR achieves 17% lower DreamSim error than LongLive-RAG and a 19% improvement over WorldMem using the same cues on LoopNav, and 94.6% accuracy on off-scene dynamics prediction in AI2-THOR, substantially outperforming temporal/geometry-only baselines.
**Tools & method:** FAR uses a negative diffusion prediction loss during training as a proxy for memory utility, enabling the retriever to learn query-dependent weighting across cues.
**Limitation:** The authors acknowledge the method focuses on external memory only, requires informative retrieval cues and extra training-time computation, and that the diffusion loss may underweight semantic changes.
