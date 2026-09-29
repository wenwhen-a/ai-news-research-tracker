**[A10] Adaptive Latent Capacity for World Models**
- **arXiv:** 2609.32921 · <https://arxiv.org/abs/2609.32921>
- **Submitted:** 2026-09-26
- **Authors:** Idan Achituve, Lior Dikstein, Idit Diamant, Arnon Netzer, Hai Victor Habi
- **Qualifying affiliation(s):** Arm Research, Israel (all authors); FLAG: borderline
- **Categories:** cs.LG
- **Open release:** none (no code/weights link found; only the arXiv listing itself)
- **Shipped counterpart:** none found

**Summary:** The paper presents Adaptive LeWorldModel (ALeWM), a JEPA-based world model that learns to concentrate predictive information into compact prefixes of a wide latent space rather than using a fixed-width embedding.
**Purpose:** Standard latent world models must choose between narrow embeddings (limited expressivity) and wide embeddings (costly, harder-to-plan-over) that spread information uniformly across coordinates.
**Breakthrough:** The authors report that ALeWM "consistently achieves higher mean success rates than tuned fixed-width LeWM, with lower planning capacity on average," citing success-rate gains alongside an average 56% reduction in planning capacity across their benchmarks.
**Tools & method:** ALeWM combines a learned capacity network (predicting sequence-conditioned prefix-length distributions), the MixSIGReg regularizer, and a nested predictor trained with a straight-through Gumbel-Softmax estimator; it is evaluated on a synthetic damped-oscillator toy task and on TwoRoom, PushT, Reacher, and OGBench-Cube visual-control benchmarks using ViT-Tiny/ViT-Small encoders.
**Limitation:** The authors note the capacity network's behavior varies with initialization and random seed, the MixSIGReg prior depends on an arbitrary polynomial-degree choice, the Gumbel-Softmax gradient estimator is biased, and mixed-dataset training shows performance degradation.
