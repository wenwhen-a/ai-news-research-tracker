**[A08] IntactWorld: Joint World Modeling with Intact Features**
- **arXiv:** 2610.11174 · <https://arxiv.org/abs/2610.11174>
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Boming Tan, Xiangdong Zhang, Yan Xia, Qi Zhu, Deyi Ji, Xue Yang, Shaofeng Zhang
- **Qualifying affiliation(s):** KOKONI 3D / Moxin Technology — listed as one of the paper's three institutions, but the HTML extraction could not map the superscript to a specific named author (flag: this company's standing as a "clearly comparable top-tier industry lab" could not be confirmed and is less certain than typical borderline cases like Huawei/Samsung — kept and flagged for user judgment). Other authors: University of Science and Technology of China, Shanghai Jiao Tong University (academic).
- **Categories:** cs.CV
- **Open release:** none stated in the abstract
- **Shipped counterpart:** none found

**Summary:** The authors argue video generation models produce realistic visuals but lack genuine understanding of real-world logic, and that prior methods absorbing "world knowledge" compress features, losing structural information. They propose IntactWorld, a joint world-modeling architecture built on uncompressed features.
**Purpose:** To preserve structural detail in world-model features by avoiding the lossy compression used in prior approaches.
**Breakthrough (≤3 sentences, attributed):** The authors report IntactWorld outperforms established baselines by 2.46 points on VBench 2.0; a companion "Full-to-Compact" training paradigm (swapping full features for CLS tokens) cuts spatial memory use by 11.4% and inference latency by 43.8%, per the authors.
**Tools & method:** Predicts the clean feature at intermediate layers instead of flow velocity, which the authors say avoids a manifold gap during optimization, combined with the Full-to-Compact training paradigm.
**Limitation:** Not stated in the available abstract text.
