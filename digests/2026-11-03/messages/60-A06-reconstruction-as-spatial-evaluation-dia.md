**[A06] Reconstruction as Spatial Evaluation: Diagnosing Cross-View Spatial Intelligence in Large Vision-Language Models**
- **arXiv:** 2611.02026 · <https://arxiv.org/abs/2611.02026>
- **Submitted:** 2026-11-01
- **Authors:** Junfei Wu, Qiuyue Wang, Xuhong Huang, Qihang Peng, Mingsheng Li, Jian Guan, Qiang Liu, Shu Wu, Liang Wang, Shuai Bai, Tieniu Tan
- **Qualifying affiliation(s):** Alibaba Group (Alibaba Token Hub) — Junfei Wu, Qiuyue Wang, Xuhong Huang, Qihang Peng, Mingsheng Li, Jian Guan, Shuai Bai
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** code — <https://github.com/Hyperwjf/ReconSpatial>
- **Shipped counterpart:** none found

**Summary:** The paper introduces ReconSpatial, a benchmark that diagnoses cross-view spatial intelligence in large vision-language models (LVLMs) by requiring multi-view 3D scene reconstruction in indoor, tabletop, and outdoor settings.
**Purpose:** The authors aim to diagnose whether LVLMs build coherent, metrically accurate 3D spatial representations across multiple views, rather than only locally plausible single-view outputs.
**Breakthrough:** The authors report that across 18 frontier LVLMs, models scored much higher on structural reconstruction than on metric accuracy, with the top model reaching 81.4% on the Structure metric versus 58.7% on the Metric score.
**Tools & method:** ReconSpatial evaluates models via oriented 3D bounding box prediction in a shared metric coordinate frame across multi-view inputs, nine atomic spatial QA tasks, and an offline open-loop navigation extension.
**Limitation:** The authors state that objects are modeled only as oriented 3D bounding boxes, omitting fine-grained surface meshes, articulated parts, and continuous free-space occupancy.
