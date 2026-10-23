# Part A — Papers
Window: last 30 days (2026-09-23 to 2026-10-23). Categories: cs.GR, cs.CV, cs.LG, cs.AI, cs.RO. Retrieval: arXiv API (primary) with affiliation pre-screen; field-name adapter used to bridge arxiv_fetch.py's schema to arxiv_affil_screen.py's expected schema (neither script modified). Qualifying papers: 6 (2 flagged).

---
## Gate3DGen: A Pre-processing Model that Selectively Purifies Real-World Images for 3D Generation
- **arXiv:** 2610.31649 · https://arxiv.org/abs/2610.31649
- **Submitted:** 2026-10-22
- **Authors:** Xiaolin Li, Zihao Huang, Fanpeng Meng, Chen Yang, Guanjun Wu, Kai Zhang, Jiemin Fang, Qi Tian
- **Qualifying affiliation(s):** Huawei Inc. — Xiaolin Li, Zihao Huang, Fanpeng Meng, Chen Yang, Guanjun Wu, Jiemin Fang, Qi Tian (FLAG: Huawei is not on the default qualified-company list but is a comparable large-scale tech company — kept and flagged)
- **Categories:** cs.CV
- **Open release:** none (no code/weights/demo link found on the abstract page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Gate3DGen is a pre-processing "gate" model for 3D-generation pipelines: clean input images pass through unchanged, while degraded ones are purified by a one-step, 3D-oriented restoration model that preserves object identity and edges. It is designed to slot in front of existing 3D generators without retraining them.
**Purpose (≤3 sentences):** Real-world input images for image-to-3D generation are often degraded (noise, compression, poor lighting), which the authors state hurts downstream 3D reconstruction quality; Gate3DGen aims to selectively fix only the images that need it, leaving clean images untouched.
**Breakthrough (≤3 sentences):** The authors report Gate3DGen cuts TRELLIS.2 mesh distance by 61.5% on a synthetic degraded-image benchmark compared with feeding degraded images directly into the 3D generator, at about 2.3 seconds of processing per image.
**Tools & method (≤3 sentences):** The model is trained on a synthetic data engine that generates paired clean/degraded views for supervision, combined with a one-step 3D-oriented purification network and a degradation-detection gate; it is evaluated against TRELLIS.2 as the downstream 3D generator.
**Limitation (≤3 sentences):** The authors' reported gains are measured on a synthetic degraded-image benchmark; the paper's current abstract/metadata do not state real-world deployment results or failure cases beyond this benchmark.

---
## AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark
- **arXiv:** 2610.31466 · https://arxiv.org/abs/2610.31466
- **Submitted:** 2026-10-22
- **Authors:** Ruicong Liu, Liangyang Ouyang, Fengbo Lan, Zhixiang Wang, Kaipeng Zhang
- **Qualifying affiliation(s):** Alaya Lab (affiliated with Shanda AI Research) — all authors (FLAG: Alaya Lab/Shanda AI Research is not on the default qualified-company list; kept and flagged as a comparable industry lab)
- **Categories:** cs.CV
- **Open release:** none (no code/weights/demo link found on the abstract page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** AnyGameRenderer is a video-to-video generative renderer that converts rough game footage — gray blockouts or wireframes — into detailed, game-like visuals while preserving the original layout, camera motion, and entity positions and timing.
**Purpose (≤3 sentences):** The authors target a gap in generative game rendering where existing models struggle to keep individual entities (characters, objects) visually and positionally consistent across frames and across different games; they introduce an entity-level benchmark to measure this specifically.
**Breakthrough (≤3 sentences):** The authors report that fine-tuning improves temporal entity-match accuracy from 50.9% to 62.9% over the base model on their new entity-level benchmark, and reduces missed entity-count changes.
**Tools & method (≤3 sentences):** AnyGameRenderer is built via LoRA fine-tuning of MiniMax-H3, a 33B-parameter reference-video-conditioned video generation model, trained on roughly 10,000 paired clips sourced from agent-made games, Unreal Engine footage, and real gameplay recordings.
**Limitation (≤3 sentences):** The paper's current abstract/metadata do not state limitations beyond the reported benchmark gains; no cross-engine generalization or real-time performance figures are given.

---
## DRILL: Training World Models to Improve Policies, Not Predict Pixels
- **arXiv:** 2610.30814 · https://arxiv.org/abs/2610.30814
- **Submitted:** 2026-10-22
- **Authors:** Zhaolu Kang, Tailong Luo, Lei Wei, Guangyuan Dong, Sihan Liu, Yingjie He, Siheng Wang, Shuaibo Li, Rongchao Zhang, Zhen Tian, Richeng Xuan, Zhichao Hu
- **Qualifying affiliation(s):** Hunyuan, Tencent — Zhaolu Kang, Richeng Xuan, Zhichao Hu
- **Categories:** cs.CV
- **Open release:** none (no code/weights/demo link found on the abstract page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** DRILL is a world-model training framework for reinforcement learning of vision-language-action (VLA) policies, built on the view that world models trained to predict next-frame pixels are misaligned with their real job of producing a useful learning signal for the policy.
**Purpose (≤3 sentences):** The authors aim to train the world model to directly maximize downstream policy performance rather than pixel-prediction accuracy, addressing a mismatch they identify between standard world-model objectives and policy-improvement objectives.
**Breakthrough (≤3 sentences):** DRILL is framed as a bilevel optimization: the world model is trained to maximize the policy's return after an inner policy update, with a closed-form variant and a full meta-gradient variant; the authors report the meta-gradient variant raises mean success rate by 13.1 points over the WMPO baseline, averaged across five manipulation simulators and two VLA backbones.
**Tools & method (≤3 sentences):** The method combines a bilevel/meta-gradient training scheme with "visitation-weighted imagination" (DRILL-VWI) and an implicit meta-gradient variant (DRILL-IMG), tested across five manipulation simulators and two VLA backbone architectures.
**Limitation (≤3 sentences):** The paper's current abstract/metadata do not list specific acknowledged limitations beyond the benchmark comparisons reported; no real-robot (as opposed to simulator) results are mentioned.

---
## Making MLLM Latents Matter: Factor-Aware Predictive Learning for Cinematic Video Generation
- **arXiv:** 2610.30926 · https://arxiv.org/abs/2610.30926
- **Submitted:** 2026-10-22
- **Authors:** Songlin Yang, Zhe Wang, Xiaotong Zhao, Xi Wang, Ran Zhang, Shuai Li, Taiyi Wu, Songlian Li, Eric Liu, Alan Zhao, Anyi Rao
- **Qualifying affiliation(s):** Tencent Video — Xiaotong Zhao, Ran Zhang, Shuai Li, Taiyi Wu, Songlian Li, Eric Liu, Alan Zhao
- **Categories:** cs.CV
- **Open release:** none (no code/weights/demo link found on the abstract page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper proposes Factor-Aware Predictive Learning (FAPL), a training method that makes latent representations from multimodal large language models (MLLMs) directly usable to condition video diffusion transformers for cinematic video generation.
**Purpose (≤3 sentences):** The authors address a gap between MLLM-derived representations (built for understanding) and the conditioning signals video diffusion transformers need for controllable generation, aiming to make a single latent space serve both generation and fine-grained editing.
**Breakthrough (≤3 sentences):** FAPL uses a three-stage training process — grounding the generator on frozen MLLM latents, training factor-specific edits with paired videos, then training limited-input representations (e.g., text-only) to predict complete-video targets — which the authors report outperforms baselines on sparse-to-video generation, factor-aware editing, and multi-shot generation tasks.
**Tools & method (≤3 sentences):** The method builds on frozen MLLM latent representations combined with a video diffusion transformer, trained in three stages with paired-video supervision for factor-specific (e.g., lighting, camera, subject) edits.
**Limitation (≤3 sentences):** The paper's current abstract/metadata do not state specific failure modes or compute/data-scale limitations beyond the reported comparative results.

---
## GSHeadRelight: Fast Relightability for 3D Gaussian Head Synthesis
- **arXiv:** 2610.30619 · https://arxiv.org/abs/2610.30619
- **Submitted:** 2026-10-22
- **Authors:** Henglei Lv, Bailin Deng, Jianzhu Guo, Xiaoqiang Liu, Pengfei Wan, Di Zhang, Lin Gao
- **Qualifying affiliation(s):** Kuaishou Technology — Jianzhu Guo, Xiaoqiang Liu, Pengfei Wan, Di Zhang
- **Categories:** cs.CV
- **Open release:** none (no code/weights/demo link found on the abstract page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GSHeadRelight addresses relighting and novel-view synthesis of human head portraits — producing photorealistic results in real time, for subjects unseen during training — using generative 3D Gaussians combined with a lighting model based on neural radiance transfer that responds linearly to incident light.
**Purpose (≤3 sentences):** The authors target the difficulty of doing portrait relighting that is simultaneously photorealistic, real-time, and generalizable to new (unseen) subjects, a combination prior 3D-aware relighting methods have not achieved together.
**Breakthrough (≤3 sentences):** The authors report state-of-the-art relighting quality while training only on in-the-wild images (no studio/light-stage capture required), with rendering about 12 times faster than prior 3D-aware portrait relighting methods.
**Tools & method (≤3 sentences):** The method represents heads as generative 3D Gaussians with a linear neural radiance transfer lighting model, enabling both relighting and novel-view synthesis from a single framework.
**Limitation (≤3 sentences):** The paper's current abstract/metadata do not state specific failure cases (e.g., extreme lighting, accessories, or hair) beyond the reported speed and quality comparisons.

---
## EgoHand: Monocular 3D Hand Reconstruction from Egocentric Video
- **arXiv:** 2610.30293 · https://arxiv.org/abs/2610.30293
- **Submitted:** 2026-10-21
- **Authors:** Chao-Yeh Chen, Tiffany Chen, Lin Duan, Tianyi Hu, Yu-Hsiang Huang, Umar Iqbal, Jiefeng Li, Edy Lim, Yanchen Liu, Yihan Pang, Hang Qiu, Jun Saito, Shao Su, Qingsi Wang, Xiufeng Xie (plus NVIDIA leadership contributors per Appendix A)
- **Qualifying affiliation(s):** NVIDIA — all listed core contributors (confirmed via the paper's Appendix A, "Contributors and Acknowledgments")
- **Categories:** cs.CV, cs.LG
- **Open release:** weights (the authors state "We release the EgoHand model"; no download link was found in the retrieved abstract/HTML text)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** EgoHand is a model for reconstructing 3D hand poses from monocular egocentric (head-worn-camera) video, aimed at hand-tracking for XR/AR and motion-capture-style applications.
**Purpose (≤3 sentences):** The authors address the difficulty of accurate, low-latency 3D hand-pose estimation from a single head-worn camera's viewpoint, where hands are frequently self-occluded, truncated at the frame edge, or seen under fast motion.
**Breakthrough (≤3 sentences):** The authors report that on zero-shot evaluation across the HOT3D, ARCTIC, and H2O benchmarks, EgoHand achieves lower error than baseline methods at about 9.69 ms latency, and a blinded user study favored its reconstructed hand poses over competing baseline systems including Apple EgoDex.
**Tools & method (≤3 sentences):** EgoHand is trained on a 14-million-image corpus combining synthetic data, in-the-wild video, and multi-camera motion-capture data; the authors state they release the EgoHand model.
**Limitation (≤3 sentences):** The paper's current abstract/metadata do not state specific failure modes (e.g., extreme occlusion, gloves, or multi-hand interaction) beyond the benchmark and user-study comparisons reported.

# Near-misses
- 2610.31066 · Dual Exam: Controlled Evaluation of Multimodal Agents and World Models · ~90 authors, all identified affiliations are universities (HKUST, NUS, PolyU, Tokyo, CMU, Berkeley, MIT, Stanford, Oxford, Cambridge, etc.) plus one unidentified "XGEN Labs" entry that could not be confirmed as a qualifying or comparable industry lab from the paper or a web search — treated as academic-only; the initial screener "Google" hit was a false positive ("Google Shopping" used as an example task, not an affiliation).
- 2610.30866 · Verus-Insight: Towards Explainable Artifact Detection in AI-Generated Videos · qualifying industry affiliation confirmed (Kuaishou "Kling Team": Zhuoran Zhang, Yang Shi, Qixun Wang, Jingyun Hua, Yuanxing Zhang, Pengfei Wan), but the paper's topic is detecting AI-generation artifacts/forgery in video (a forensics task), not 3D generation, world models, character animation, or game engines — excluded as off-topic despite the qualifying affiliation.

Verification: every listed paper was checked twice against arXiv (v1 submission date and title on the abstract page; affiliations read from the paper's HTML full-text author block or, for EgoHand, its Appendix A contributor list; topic confirmed from the abstract) before inclusion. 1 paper (EgoHand) lists an open release (weights, stated but no link found).
