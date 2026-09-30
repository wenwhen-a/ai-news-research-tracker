**[A04] Rethinking Representations for World-Action Modeling**
- **arXiv:** 2609.38163 · <https://arxiv.org/abs/2609.38163>
- **Submitted:** 2026-09-29 (v1)
- **Authors:** Haoyi Jiang, Liu Liu, Xinjiang Wang, Zhihao Sun, Zequn Chen, Sen Wang, Xinjie Wang, Xia Chen, Jingfeng Yao, Weiheng Zhao, Shanglin Yuan, Zhizhong Su, Wei Sui, Wenyu Liu, Xinggang Wang
- **Qualifying affiliation(s):** Horizon Robotics — Liu Liu, Xinjiang Wang, Zequn Chen, Xinjie Wang, Xia Chen, Zhizhong Su; D-Robotics — Wei Sui (Haoyi Jiang interned at D-Robotics). FLAG: borderline (Horizon Robotics / D-Robotics are not on the primary qualified-company list; treated as comparable-standing per instructions)
- **Categories:** cs.CV; cs.RO
- **Open release:** none yet (GitHub repo github.com/hustvl/ReWAM states "Coming soon — source code, pretrained models, and documentation will be released shortly")
- **Shipped counterpart:** none found

**Summary:** The paper studies how to design shared representations for systems that jointly do robot control and future-observation ("world") prediction.
**Purpose:** Prior world-action models pick representations based on reconstruction quality or off-the-shelf perceptual features alone, which the authors argue is not well matched to joint control-and-prediction objectives.
**Breakthrough:** The authors report 93.6% success on RoboTwin 2.0 and a 12.29 average score on RoboDojo, attributing gains to directing action-loss gradients into a dedicated Temporal Representation Bottleneck.
**Tools & method:** ReWAM builds on pretrained DINO visual features, adds a Feature Calibration module, and introduces a Temporal Representation Bottleneck through which action-loss gradients flow.
**Limitation:** No explicit "Limitations" section or caveats were found in the fetched HTML sections of this paper; none is stated here to avoid inventing one.
