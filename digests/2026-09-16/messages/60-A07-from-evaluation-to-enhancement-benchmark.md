**[A07] From Evaluation to Enhancement: Benchmarking and Improving Think-with-Video Reasoning for Video Generative Models**
- **arXiv:** 2609.11242 · <https://arxiv.org/abs/2609.11242>
- **Submitted:** 2026-09-10
- **Authors:** Meng Luo, Yicheng Liu, Jiahao Wang, Yuanxing Zhang, Xin Tao, Pengfei Wan, Kun Gai, Hao Fei
- **Qualifying affiliation(s):** Kuaishou Technology (Kling Team) — Jiahao Wang, Yuanxing Zhang, Xin Tao, Pengfei Wan, Kun Gai
- **Categories:** cs.CV, cs.AI
- **Open release:** code + data — <https://huggingface.co/datasets/KlingTeam/VWG-Bench>
- **Shipped counterpart:** none found

**Summary:** The paper introduces VWG-Bench, a benchmark spanning 9 reasoning dimensions and 38 fine-grained tasks (380 samples) that tests whether video generative models can perform logical, physical, and causal reasoning ("think with video") rather than only produce visually convincing footage.
**Purpose:** The authors state that existing video-generation benchmarks are fragmented and conflate visual quality with cognitive/reasoning correctness, leaving it unclear whether generators execute symbolic, physical, and intentional rules or merely exploit surface statistics.
**Breakthrough:** The authors report that video-quality scores consistently exceed reasoning scores across all six tested systems (e.g., Wan2.2 scores 2.32 on video quality vs.
**Tools & method:** Vid-PRE is built on Qwen3-VL-8B and trained in two stages: supervised fine-tuning on ~20K rejection-sampled reasoning-chain tuples, followed by GRPO on 1.5K hard samples using a four-part text-based reward (intent preservation, visual-spatial consistency, solution correctness, format compliance), with no video generated during training.
**Limitation:** The authors acknowledge that VWG-Bench's 10 instances per task (380 samples total) limit statistical robustness, and that Vid-PRE's SFT data relies on proprietary APIs, raising reproducibility concerns.
