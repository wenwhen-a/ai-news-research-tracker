**[A23] ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training**
- **arXiv:** 2609.00188 · https://arxiv.org/abs/2609.00188
- **Submitted:** 2026-08-31
- **Authors:** Xionghao Wu, Yijun Yang, Shiyang Zhou, Haoze Sun, Jianhui Liu, Songsong Yu, Jiyao Zhang, Wenbo Li, Bo Wang, Guoqing Ma, Lin Song, Renjie Liao, Shenghe Zheng, Wei Tang, Xiaojuan Qi, Yanwei Li, Yuan Zhang, Zhuotao Tian, Haoyang Huang, Nan Duan
- **Qualifying affiliation(s):** JD (Joy Future Academy, collective byline) — FLAG: borderline (JD.com)
- **Categories:** cs.CV
- **Open release:** code (https://github.com/ZimaBlue-WAM/ZimaBlue; project https://zimablue-wam.github.io/)
- **Shipped counterpart:** none found

**Summary:** ZimaBlue trains World Action Models through a three-stage curriculum: causal video pretraining on egocentric video without action labels, multi-embodiment video-action mid-training with a unified action representation, then target-robot post-training with a Slow-Fast dual-system architecture.
**Purpose:** To scale world-action-model pretraining on abundant action-free egocentric video for cross-embodiment manipulation.
**Breakthrough:** The authors report that scaling pretraining video from 300 to more than 120,000 hours raises zero-shot task success from 36.1% to 77.8%, and that the Slow-Fast design predicts actions at 30 Hz on an RTX 4090.
**Tools & method:** A unified 100-dimensional state-action representation; pretraining data including EPIC-KITCHENS, Egocentric-100K, EgoDex, DROID and RoboCOIN; evaluation on real Franka robots and the LIBERO-Plus, RoboTwin 2.0 and RoboCasa365 simulators.
**Limitation:** The authors state remaining failures include difficulty advancing from correct intermediate states and local interaction errors such as target displacement or lost contact.
