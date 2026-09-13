**[A47] Object-Uni: A Unified Model for Object-Centric Spatial Understanding and Controllable Generation**
- **arXiv:** 2608.22757 · https://arxiv.org/abs/2608.22757
- **Submitted:** 2026-08-24
- **Authors:** Mining Tan, Yinuo Wang, Ziqi Zhou, Weize Quan, Sifei Li, Jingdong Chen, DanDan Zheng, Libin Wang, Weiming Dong
- **Qualifying affiliation(s):** Ant Group — Weiming Dong (corresponding author); FLAG: borderline
- **Categories:** cs.CV, cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** Object-Uni unifies object pose perception, spatial reasoning, pose-conditioned generation and object-centric novel-view synthesis by treating object pose as an explicit geometric variable, with a viewpoint-based orientation abstraction so multimodal LLMs can reason about 3D orientation in natural language.
**Purpose:** To move unified vision-language models from describing objects to manipulating their spatial state.
**Breakthrough:** The authors report azimuth error 22.87 degrees (74.44% AUC@30) versus 29.94 degrees (55.40%) for Orient Anything V2 on KITTI-Cityscapes, and on ImageNet3D generation 74.31 mIoU / 83.40% success versus 66.45 / 68.81% for SceneDesigner.
**Tools & method:** The UniSpatial-80K dataset (83,252 images, 91,392 annotated objects, 122 categories) and an "Object-Token-Grounded Pose Anchor"; about 18 hours on 8 NVIDIA H20 GPUs.
**Limitation:** The authors state the model "still has limitations in generating fine-grained text and human details," attributed partly to the generative backbone.
