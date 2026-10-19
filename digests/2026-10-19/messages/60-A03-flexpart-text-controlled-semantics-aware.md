**[A03] FlexPart: Text-Controlled Semantics-Aware 3D Part Segmentation at Flexible Granularity**
- **arXiv:** 2610.23659 · <https://arxiv.org/abs/2610.23659>
- **Submitted:** 2026-10-16 (v1)
- **Authors:** Yiqun Zhao et al.
- **Qualifying affiliation(s):** Tencent Hunyuan — Jiachen Xu, Yunfei Zhao, Zibo Zhao, Xintong Han, Chunchao Guo (others are University of Hong Kong / CUHK-Shenzhen)
- **Categories:** cs.CV
- **Open release:** none (project page only, <https://zhao-yiqun.github.io/flexpart/>; builds on open-source Hunyuan3D 2.1 as a base dependency, but states no own code/weights release)
- **Shipped counterpart:** none found

**Summary:** FlexPart segments 3D meshes into parts chosen and described by the user in free text, at whatever granularity the prompt implies, rather than following one fixed artist partition.
**Purpose:** It addresses the lack of 3D part datasets and controls that support multiple valid granularities and semantic (rather than purely geometric or click-based) part selection, framed as "what you ask for is what you get."
**Breakthrough:** The authors report their model beats the strongest baseline by 15% mIoU on PartObjaverse-Tiny even when that baseline uses ground-truth guidance, by 22% average mIoU on their new FlexPartBench, and by 35% IoU over the strongest click-based baseline on selective segmentation.
**Tools & method:** A VLM (Gemini) pipeline mines artist-authored components from HY3D-Bench into multi-granularity, text-labeled training data; a text-conditioned dual-stream DiT with a frozen Qwen3-VL-4B text encoder predicts a continuous part-identity field (6-bit codes per face) via flow matching, trained with background-dropping augmentation, with a frozen planner VLM able to fill in part descriptions from renderings at inference.
