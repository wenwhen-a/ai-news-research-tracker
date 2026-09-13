**[A66] VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?**
- **arXiv:** 2608.15265 · https://arxiv.org/abs/2608.15265
- **Submitted:** 2026-08-15
- **Authors:** Yansong Ning, Jingwen Ye, Zhongkai Wu, Yang Sun, Yiqin Zhu, Xingyi Li, Weidong Zhang, Hao Liu
- **Qualifying affiliation(s):** Tencent (TEG AIPD) — Jingwen Ye, Zhongkai Wu, Yang Sun, Yiqin Zhu, Xingyi Li, Weidong Zhang
- **Categories:** cs.AI
- **Open release:** weights, code and demo (https://github.com/usail-hkust/VibeWorlding-Gym; https://huggingface.co/collections/usail-hkust/vibeworlder; https://huggingface.co/datasets/usail-hkust/VWE-Bench)
- **Shipped counterpart:** none found

**Summary:** A framework and benchmark testing whether multimodal agents can infer user intent, plan scene layout, invoke 3D tools and reflect on feedback to build 3D open worlds end to end, with VWE-BENCH covering 2,616 3D assets, 323 annotated worlds and 6,828 queries.
**Purpose:** To measure and improve autonomous end-to-end 3D world construction rather than single-step asset generation.
**Breakthrough:** The authors report GPT-5.5 and Qwen3.8-Max both below 60% success on their rubric-based verifier, and that their RL-trained open VibeWorlder-30B-A3B outperforms the closed models tested.
**Tools & method:** VibeWorlding-Gym with a dual-constraint rubric verifier, an asset-retrieval embedding model and a unified post-training framework; 8 NVIDIA H20 GPUs for 8B models and three nodes for the 30B-A3B model.
**Limitation:** No explicit limitations paragraph was found in the fetched text (observed, not stated).
