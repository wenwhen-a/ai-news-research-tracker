**[A06] MotionInsight: Diagnosing Object Motion Deficiencies in Generated Videos**
- **arXiv:** 2609.37030 · <https://arxiv.org/abs/2609.37030>
- **Submitted:** 2026-09-29
- **Authors:** Jiahao Zhan et al.
- **Qualifying affiliation(s):** ByteDance Inc. — Jiahao Zhan, Yongrui Ma, Qunliang Xing, Junlin Li, Li Zhang, Shijie Zhao (project lead); other authors from MMLab CUHK, Peking University, Fudan University, CPII under InnoHK
- **Categories:** cs.CV; cs.AI
- **Open release:** code — <https://github.com/JohnZhan2023/MotionInsight> (paper states "the code is publicly available")
- **Shipped counterpart:** none found

**Summary:** The paper introduces MotionInsight, an evaluator that diagnoses object-motion deficiencies (object consistency, motion continuity, physical plausibility) in AI-generated videos, paired with the VidMotion dataset of 6,879 annotated videos with 12 failure-cause categories.
**Purpose:** Existing video-generation evaluation focuses on aesthetics and text-video alignment while ignoring whether generated object motion is physically and temporally realistic; the authors aim to close that gap with an object-centric, explainable motion-fidelity evaluator.
**Breakthrough:** The authors report MotionInsight reaches near-human correlation with human judgments (SRCC 0.761/0.633/0.727 on the three dimensions, versus 0.370/0.276/0.246 for GPT-5.4) and a Jaccard similarity of 0.58 for failure-cause identification versus 0.15 for GPT-5.4. They also report that using MotionInsight as a DPO reward signal yields videos preferred 92.86% of the time over a baseline Wan 2.1 model for motion fidelity.
**Tools & method:** The system combines CoTracker3 point tracking and ViPE camera-pose estimation into structured "motion embeddings," aligns them to a VLM's semantic space using 80,721 auto-generated motion-description QA pairs from OpenVid, and fine-tunes with GRPO on 8 NVIDIA A100 GPUs.
