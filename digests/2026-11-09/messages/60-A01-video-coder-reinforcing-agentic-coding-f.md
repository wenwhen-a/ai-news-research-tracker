**[A01] Video-Coder: Reinforcing Agentic Coding for Video Generation**
- **arXiv:** 2611.09894 · <https://arxiv.org/abs/2611.09894>
- **Submitted:** 2026-11-06
- **Authors:** Chaoyang Wang, Sicheng Gao, Junan Hu, Kunyang Li, Dongyang Chen, Yiyang Zhou, Huaxiu Yao, Yong Jae Lee, Radu Timofte, Yuzhang Shang
- **Qualifying affiliation(s):** Microsoft — Junan Hu (Microsoft Research); other co-authors are University of Central Florida, University of Würzburg, Tsinghua University, UNC-Chapel Hill, UW–Madison
- **Categories:** cs.CV
- **Open release:** code + weights (GitHub: <https://github.com/CYWang735/Video-Coder>; Hugging Face: <https://huggingface.co/Video-Coder>)
- **Shipped counterpart:** none found

**Summary:** The authors introduce Video-Coder, a video-generation agent that writes and executes code to construct a dynamic 3D scene ("Draft Video") providing structure and motion signals to downstream video generators, rather than generating pixels directly.
**Purpose:** Current video generators struggle to produce precise spatial structure, coherent motion dynamics, and controllable scene composition.
**Breakthrough:** The authors report Video-Coder improves about 7 points on PhyGenBench and about 24 points on VBench-2.0 compared with MiniMax-H3 (their stated baseline).
**Tools & method:** Training data: Video-Coder-SFT-6k and Video-Coder-RL-2k (prompt sources include captions from InternVid, OpenVid-1M, and MiraData); the paper's later sections cite SFT-10k/RL-4k instead, an internal inconsistency in the text.
**Limitation:** The authors state Video-Coder's Material score (75.02%) trails CogVideoX-1.5 (83.19%) because material appearance and response are not encoded in the white-model Draft Video.
