**[A01] PART: Learning 3D Part Assembly and Retrieval with Transformers**
- **arXiv:** 2609.19872 · <https://arxiv.org/abs/2609.19872>
- **Submitted:** 2026-09-17
- **Authors:** Ruchao Bao, Wenzheng Wu, Chucheng Xiang, Zhongyuan Liu, Yuan Liu, Jinxin Dong, Ligang Liu, Ziqi Wang
- **Qualifying affiliation(s):** Tencent — Zhongyuan Liu, Jinxin Dong
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** The paper presents PART, a unified transformer-based framework that reconstructs target 3D shapes by retrieving appropriate parts from a library and predicting their 6-DoF poses. It formulates retrieval and assembly jointly as a set-prediction problem, accepted as a SIGGRAPH Asia 2026 Conference Paper.
**Purpose:** The authors target the practical problem of assembling target shapes from existing part libraries rather than generating geometry from scratch, useful for asset reuse and shape editing pipelines.
**Breakthrough:** The authors report exploiting a duality between assembly and segmentation through joint training and segmentation-enhanced optimization, and report a Shape Chamfer Distance of 1.19 on PartNet Chair versus roughly 5–6 for prior best methods, 86.44% part accuracy and 69.90% connectivity accuracy.
**Tools & method:** Trained on curated part datasets exceeding 80K shapes drawn from PartNet, PartNeXt, 3DCoMPaT++ and PartVerse-XL, with 3D-FRONT used for scene-level evaluation and Redwood for real-world scan generalization; training used 8 NVIDIA A800 GPUs.
**Limitation:** The authors state the method does not consider inter-part connections or physical constraints, and assumes rigid transformations without part scaling or non-rigid deformation.
