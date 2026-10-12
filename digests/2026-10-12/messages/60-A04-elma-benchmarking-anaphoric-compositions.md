**[A04] ELMA: Benchmarking Anaphoric Compositions for Long-Term Text-to-Motion**
- **arXiv:** 2610.13549 · <https://arxiv.org/abs/2610.13549>
- **Submitted:** 2026-10-09 (v1)
- **Authors:** Shun Kato et al.
- **Qualifying affiliation(s):** Sony — authors affiliated with Sony Group Corporation (alongside Keio University / Keio AI Center); accepted at NeurIPS 2026 Evaluations & Datasets Track
- **Categories:** cs.CV
- **Open release:** none yet — project page <https://elma-dataset.github.io/>; dataset planned via gated access on Kaggle (CC BY-NC 4.0, URL not given); code currently only in an anonymized review repository, with public release stated as forthcoming
- **Shipped counterpart:** none found

**Summary:** ELMA is a dataset and task for long-term text-to-motion generation that specifically targets "anaphoric" instructions — later text segments that refer back to and must remain consistent with earlier motion segments.
**Purpose:** The authors aim to expose and address a gap in current long-term motion generation: models are not evaluated on, and struggle with, instructions whose meaning depends on earlier segments of a long motion sequence.
**Breakthrough:** The authors report that existing motion-generation models struggle with context-dependent (anaphoric) instructions, and that fine-tuning current models to use long-range context on ELMA improves both physical realism and semantic alignment.
**Tools & method:** Clips are built using YOLOv8l-pose, ByteTrack, SAM 2, GVHMR, VPoser/SMPL-X, and PySceneDetect for extraction, with VLM-assisted annotation (Gemini-2.5-Pro, GPT-4o); baselines FlowMDM, DoubleTake, UniMotion, and DARTControl are fine-tuned and evaluated on a single NVIDIA RTX 6000 Ada GPU, drawing comparison data from HumanML3D, BABEL, AMASS, Kinetics-700, and Motion-X.
