**[A08] WorldSculpt: Generating Compositional Worlds from Grounded Videos**
- **arXiv:** 2609.05416 · https://arxiv.org/abs/2609.05416
- **Submitted:** 2026-09-04
- **Authors:** Muyao Niu, Jixuan He, Ruihan Yu, Lian Fu, Yonghao Yu, Zheng-Hui Huang, Yifan Zhan, Fengbo Lan, Yongtao Ge, Yinqiang Zheng, Kaipeng Zhang, Zhixiang Wang
- **Qualifying affiliation(s):** Alaya Lab (Shanda Group) — Muyao Niu and ten co-authors; FLAG: borderline (an "AI x Gaming" industry lab under Shanda Group, not on the core list)
- **Categories:** cs.CV
- **Open release:** code and weights (https://github.com/AlayaLab/WorldSculpt; Hugging Face checkpoints "AlayaLab/WorldSculpt" and "TencentARC/Pixal3D")
- **Shipped counterpart:** none found

**Summary:** WorldSculpt generates compositional 3D scenes made of hundreds of individually separable object meshes from posed multi-view video, by extending the single-object generative prior Pixal3D with a multi-view conditioning pathway.
**Purpose:** Prior world-model and scene-reconstruction methods output one fused mesh or Gaussian set that cannot be decomposed into movable objects, which the authors say mismatches needs in gaming, AR/VR, simulation and robotics.
**Breakthrough:** The authors report generalisation to large, heavily occluded scenes with hundreds of objects despite fine-tuning only on single canonical objects, and that the method outperforms prior approaches on single-object, controlled multi-object and their new UE-MeshyScene benchmark, with larger gains as scene complexity grows. They also show converting generated 3DGS worlds (Marble, HY-World 2.0) into compositional mesh scenes.
**Tools & method:** Pixal3D base model plus multi-view conditioning; UE-MeshyScene benchmark of photorealistic cluttered scenes with per-object annotations and ground-truth meshes.
**Limitation:** Generation quality is bounded by the Pixal3D prior (observed, not stated); the paper's stated limitations were not captured by the fetch.
