**[A04] DRILL: Training World Models to Improve Policies, Not Predict Pixels**
- **arXiv:** 2610.30814 · <https://arxiv.org/abs/2610.30814>
- **Submitted:** 2026-10-22
- **Authors:** Zhaolu Kang, Tailong Luo, Lei Wei, Guangyuan Dong, Sihan Liu, Yingjie He, Siheng Wang, Shuaibo Li, Rongchao Zhang, Zhen Tian, Richeng Xuan, Zhichao Hu
- **Qualifying affiliation(s):** Hunyuan, Tencent — Zhaolu Kang, Richeng Xuan, Zhichao Hu
- **Categories:** cs.CV
- **Open release:** none (no code/weights/demo link found on the abstract page)
- **Shipped counterpart:** none found

**Summary:** DRILL is a world-model training framework for reinforcement learning of vision-language-action (VLA) policies, built on the view that world models trained to predict next-frame pixels are misaligned with their real job of producing a useful learning signal for the policy.
**Purpose:** The authors aim to train the world model to directly maximize downstream policy performance rather than pixel-prediction accuracy, addressing a mismatch they identify between standard world-model objectives and policy-improvement objectives.
**Breakthrough:** DRILL is framed as a bilevel optimization: the world model is trained to maximize the policy's return after an inner policy update, with a closed-form variant and a full meta-gradient variant; the authors report the meta-gradient variant raises mean success rate by 13.1 points over the WMPO baseline, averaged across five manipulation simulators and two VLA backbones.
**Tools & method:** The method combines a bilevel/meta-gradient training scheme with "visitation-weighted imagination" (DRILL-VWI) and an implicit meta-gradient variant (DRILL-IMG), tested across five manipulation simulators and two VLA backbone architectures.
**Limitation:** The paper's current abstract/metadata do not list specific acknowledged limitations beyond the benchmark comparisons reported; no real-robot (as opposed to simulator) results are mentioned.
