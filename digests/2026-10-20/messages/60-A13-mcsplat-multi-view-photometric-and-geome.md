**[A13] MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes**
- **arXiv:** 2610.25345 · <https://arxiv.org/abs/2610.25345>
- **Submitted:** 2026-10-18
- **Authors:** Yifei Wang, Wei Tian, Wenhua Bao, Jia Zhou, Hanshi Wang, Fudong Ge, Jianhua Wu, Shuai Yuan, Zhipeng Zhang, Xingliang Liu, Xianming Zeng, Jianyun Xu, Bingzhao Gao
- **Qualifying affiliation(s):** Zaofu Intelligent Technology Co., Ltd. — Yifei Wang (internship), Wenhua Bao, and other co-authors; project leaders are drawn from this company per the paper's footnote. FLAG: borderline — Zaofu is a Shanghai L4 autonomous-driving/robotaxi joint venture (founded 2025 by Hello, Ant Group and CATL, reportedly >RMB 3B initial investment) and not on the explicit qualifying list.
- **Categories:** cs.CV
- **Open release:** none (no code/weights statement); project page at <https://yfwang0824.github.io/mcsplat-project/>
- **Shipped counterpart:** none found

**Summary:** MCSplat is a feed-forward 3D Gaussian Splatting method for reconstructing driving scenes from sparse surround-view camera images.
**Purpose:** The paper targets two failure modes of feed-forward driving-scene Gaussian splatting: cross-camera exposure/ISP/lighting differences being wrongly absorbed into scene geometry, and normal-based geometric supervision becoming unreliable near depth edges.
**Breakthrough:** The authors report that weighting surface self-supervision with a Fisher-information-based uncertainty estimated from photometric sensitivity improves cross-view depth consistency, surface-normal agreement, and reduces geometric artifacts.
**Tools & method:** Evaluated on the Waymo Open Dataset and nuScenes; trained using 16 NVIDIA H20 GPUs.
**Limitation:** The authors state future work will explore stronger temporal appearance modeling and explicit modeling of ISP parameters.
