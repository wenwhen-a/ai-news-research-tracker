**[A19] VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement**
- **arXiv:** 2609.03153 · https://arxiv.org/abs/2609.03153
- **Submitted:** 2026-09-02
- **Authors:** Wenzhuo Xu, Yuchen Zhu, Chongjian Ge, Xuan Shen, Jing Shi, Jason Kuen, Yongxin Chen, Molei Tao, Christopher McComb, Noelia Grande Gutiérrez, Jiuxiang Gu
- **Qualifying affiliation(s):** Adobe Research — Jason Kuen, Jiuxiang Gu
- **Categories:** cs.CV
- **Open release:** none stated (project page https://veriphy-ai.github.io)
- **Shipped counterpart:** none found

**Summary:** VeriPhy is an agentic physical-verification system that checks generated video against a natural-language prompt: a text-only planner compiles the prompt into typed physical obligations and a statically validated execution plan before any frame is observed.
**Purpose:** To evaluate and refine world models by verifying whether generated physics matches what was requested, beyond plausibility scoring.
**Breakthrough:** On a 149-clip core with 304 annotated flaws, the authors report VeriPhy identified 228 defects versus 164 for a published question-decomposition evaluator on identical clips and models.
**Tools & method:** Qwen3-VL-30B-A3B-Instruct as planner and verifier, SAM 3 for segmentation, TAPNext++ for tracking, FlexSED for audio, Wan 2.2-VACE for generation and MuJoCo for simulation rendered as depth controls; a 1,500-clip benchmark with 2,582 human-annotated flaw records.
**Limitation:** The authors state the corpus was labelled by a single annotator without inter-rater metrics, that multi-object interactions such as billiard collisions do not reliably reproduce simulated physics, and that closed-loop refinement is not yet implemented.
