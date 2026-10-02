**[A01] RelationVGGT: Visual Geometry Transformers for 3D Spatial Relation Segmentation**
- **arXiv:** 2610.00970 · <https://arxiv.org/abs/2610.00970>
- **Submitted:** 2026-10-01
- **Authors:** Minsu Kim, Jaesung Choe, Jiwoo Lee, Yu-Chiang Frank Wang, Seon Joo Kim
- **Qualifying affiliation(s):** NVIDIA — Jaesung Choe, Yu-Chiang Frank Wang
- **Categories:** cs.CV; cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** RelationVGGT is a feed-forward framework for 3D spatial relation segmentation: given a visually specified subject and a relational text query (with no category name provided), it segments the related target object across multiple views in a pose-free setting.
**Purpose:** The authors note that existing feed-forward 3D scene-understanding methods remain object-centric and neglect spatial relations between objects; the paper addresses segmenting a target defined by its relation to a subject, without per-scene optimization or known camera poses.
**Breakthrough:** The authors present 3D spatial relation segmentation as a new task formulation and report results against baselines including MVGGT and ReferSplat-style 3D referring-segmentation methods, along with a fully automated annotation pipeline for generating training data at scale.
**Tools & method:** The annotation pipeline is built on ScanNet++ using VLMs and LLMs to produce relation-labeled training data; the architecture couples a VGGT-style visual geometry transformer with a subject-conditioned relation-prediction transformer head.
**Limitation:** The authors state the data pipeline currently depends on datasets with instance-level annotations such as ScanNet++, limiting extension to unannotated or in-the-wild scenes, and that the framework models only object-object spatial relations rather than functional relations or full scene graphs.
