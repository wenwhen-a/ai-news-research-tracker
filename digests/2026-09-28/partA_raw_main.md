## WALT: Learning World-Model-Aligned Latent Trajectories for Autonomous Driving
- **arXiv:** 2609.30436 · https://arxiv.org/abs/2609.30436
- **Submitted:** 2026-09-24
- **Authors:** Mingkai Jia, Jiaxin Guo, Zhijian Shu, Jiawei Xu, Mingxiao Li, Jintao Cheng, Ping Tan, Wei Yin
- **Qualifying affiliation(s):** Horizon Robotics — Mingkai Jia, Zhijian Shu, Jiawei Xu, Mingxiao Li, Wei Yin; FLAG: borderline (Horizon Robotics is not on the core tracked list; kept per the "comparable labs, flag" rule)
- **Categories:** cs.RO, cs.CV
- **Open release:** none (no code/project page found in the paper)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper proposes WALT (World-Model Alignment for Latent Trajectories), a method that builds a compact generative trajectory latent space by transferring knowledge from a frozen, pretrained driving world model (EponaV2) into a dual-branch trajectory autoencoder. Tested on the NAVSIM v1 and v2 autonomous-driving planning benchmarks, it reports PDMS improving from 89.4 to 89.8 (v1) and EPDMS from 87.3 to 87.9 (v2), while cutting compute requirements by 30.5%.

**Purpose (≤3 sentences):** The authors state that driving world models learn rich predictive visual representations, but accurate visual prediction does not automatically translate into effective trajectory planning because visual world states and raw geometric trajectories are misaligned. WALT aims to close that gap so planners can use action-relevant semantic information already captured by the world model.

**Breakthrough (≤3 sentences):** The authors report that rather than generating raw waypoints directly, their dual-branch trajectory autoencoder imports semantic knowledge from the frozen visual world model into trajectory representations via Joint-Embedding Predictive Architecture and Representation Alignment techniques. They state this yields the reported NAVSIM score gains alongside a 30.5% reduction in computational cost versus their baseline.

**Tools & method (≤3 sentences):** The tokenizer stage was trained for 100 epochs on 32 H20 GPUs with a fixed learning rate of 1×10⁻⁴, using a frozen EponaV2 world model and a latent configuration of two 32-dimensional tokens (24 semantic + 8 reconstruction channels each). Evaluation used the official NAVSIMv1 (navtest split) and NAVSIMv2 protocols.

**Limitation (≤3 sentences):** The paper does not include an explicit stated-limitations section; the authors frame the core unresolved challenge as further study of "learning world-model-aligned trajectory representations for autonomous driving" as future work (observed, not stated as a limitation).

# Near-misses
- 2609.30667 · StarWM: Self-Supervised Trained Attention Routing for Robust World Models · affiliation screen matched "Google" only via a "DeepMind Control Suite" benchmark-name mention; verified authors are all German Aerospace Center (DLR) and Ulm University — no qualifying industry affiliation, academic-only.
- 2609.30650 · Causal Retention in Interactive Agents: Interface Factorization and Selective Adaptation · verified industry affiliation (Dong Xie, Baidu Inc.), but the paper's actual topic is a causal-probing/interpretability framework tested across finite causal systems, TD-MPC2 world models, and an LLM (Qwen2.5-7B) — not genuinely a 3D/world-model-generation, character-animation, or game-engine paper; off-topic.
- 2609.31133, 2609.31059, 2609.31396, 2609.31344 · (materials science / condensed-matter / human-robot-collaboration papers) · affiliation screen false-positive: "Google" matched only the "Google Scholar" citation-export link on abstract-only pages, no real Google/DeepMind affiliation; also off-topic (physics/HRI, not one of the four tracked topics).

Verification: each candidate's arXiv abstract page (v1 date, categories, withdrawal status) and HTML page (author affiliation block) were fetched directly and cross-checked before inclusion or exclusion; WALT's affiliation, topic, and reported numbers were confirmed against the paper's own abstract and body text.
