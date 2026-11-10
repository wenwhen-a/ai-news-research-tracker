## From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models
- **arXiv:** 2611.11136 · https://arxiv.org/abs/2611.11136
- **Submitted:** 2026-11-08
- **Authors:** Changran Liu, Qi Wu, Wenchao Ma, Sharon X. Huang, Haomiao Jiang
- **Qualifying affiliation(s):** Roblox — Changran Liu, Qi Wu, Haomiao Jiang
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents a framework that uses an LLM-powered coding agent to automatically build game environments, tasks, and scripted expert players from natural-language skill descriptions, which then generate keyboard-and-mouse demonstrations without any human gameplay data. On this synthetic data the authors train Script2Play, a 4B-parameter vision-language-action model, on 150.3 hours of synthetic Minecraft and Roblox gameplay (123.4 hours from Roblox). They report that the resulting model generalizes across game engines and performs strongly on public game benchmarks.
**Purpose (≤3 sentences):** The authors target the bottleneck of collecting human gameplay demonstrations for training game-playing VLA agents, aiming to fully automate both environment/task generation and the expert demonstrations used to train such agents.
**Breakthrough (≤3 sentences):** The authors report a fully automated pipeline that goes from natural-language skill descriptions to generated game environments, scripted expert players, and synthetic demonstrations, removing the need for human gameplay data entirely. They state the resulting Script2Play model generalizes across different game engines (Minecraft and Roblox) despite training only on synthetic data.
**Tools & method (≤3 sentences):** The pipeline uses an LLM coding agent to author environments/tasks and scripted "expert" players in Roblox (via Luau scripting and the Rojo build system) and Minecraft; it trains a 4B vision-language-action model (Script2Play) via behavior cloning on 150.3 hours of generated keyboard-and-mouse demonstration data. Evaluation uses public game benchmarks.
**Limitation (≤3 sentences):** Not stated by the authors in the abstract or main text reviewed.

## BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs
- **arXiv:** 2611.10768 · https://arxiv.org/abs/2611.10768
- **Submitted:** 2026-11-07
- **Authors:** Zilin Guo, Tianrui Zhang, Yi Rong, Yichen Liu, Yuxin Guo, Jingcheng Ni, Lewei Lu, Zehuan Wu, Dan Xu
- **Qualifying affiliation(s):** SenseTime Research — Yichen Liu, Yuxin Guo, Jingcheng Ni, Lewei Lu, Zehuan Wu (FLAG: borderline — SenseTime is not on the primary company list but is a comparable top-tier industrial AI lab)
- **Categories:** cs.AI
- **Open release:** code, weights, demo — https://github.com/SenseTime-FVG/BlenderFORGE (release includes data-generation/training/sandbox/evaluation code, test set, fine-tuned model weights, and a demo.zip of multi-turn conversations; some documentation items noted as "planned")
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** BlenderFORGE is a training framework for open-weight multimodal LLM agents that edit 3D scenes in Blender by generating Blender Python (bpy) code. It covers four editing task families — object placement, shape-key editing, lighting, and materials — using a perturbation-based data pipeline and an isolated Blender sandbox for deterministic execution and reward computation. The authors report that resulting Qwen3-VL-8B and Qwen3.5-9B agents improve substantially over their base models and are competitive with some zero-shot proprietary models on selected metrics.
**Purpose (≤3 sentences):** The authors aim to improve MLLM agents' ability to perform "reactive" 3D-graphics editing in Blender — iteratively adjusting a scene toward a goal rendering — rather than one-shot scene generation.
**Breakthrough (≤3 sentences):** The authors report a perturbation-based data-generation pipeline plus an isolated Blender sandbox enabling deterministic execution and automatic reward computation, combined with a two-stage SFT-then-RL training recipe. They state this produces open-weight 8B/9B agents that substantially outperform their base models and are competitive with some zero-shot proprietary models on selected benchmark metrics.
**Tools & method (≤3 sentences):** The framework targets Blender's bpy API across four task families (placement, shape-key, lighting, materials), using 3D-FRONT/3D-FUTURE assets (not redistributed), a two-stage supervised fine-tuning + reinforcement learning pipeline, and Qwen3-VL-8B / Qwen3.5-9B backbones with VLM-based judging of edits.
**Limitation (≤3 sentences):** The authors state the benchmark excludes object insertion/deletion, procedural modeling, animation, and physics-aware editing; general camera control "remains an open problem" (best valid rate 35% on held-out camera tasks); and the framework is Blender/bpy-specific with transfer to other 3D tools unexplored. They also note training may overfit to the perturbation-generated task distribution and that main model comparisons lack error bars or significance tests.

## Dynamics-Informed Action Learning for Goal-Conditioned Latent Planning
- **arXiv:** 2611.10660 · https://arxiv.org/abs/2611.10660
- **Submitted:** 2026-11-07
- **Authors:** Yinuo Jiang, Guangzhi Wang, Yiran Wang, Junfu Pu, Cheng Cheng, Honghao Chen, Ying Shan
- **Qualifying affiliation(s):** Tencent ARC Lab — Yiran Wang, Cheng Cheng, Ying Shan (Ying Shan is Tencent ARC Lab's well-known lead; author-to-footnote mapping was partly garbled in the HTML but the Tencent ARC Lab affiliation is clearly listed)
- **Categories:** cs.CV (primary), cs.RO
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces Dynamics-Informed Action Learning (DIAL), a method for latent world models used in visual control planning. It addresses two gaps: teacher-forced training never exposes the forward/dynamics model to its own recursive predictions, and sampling-based planners start action search from goal-agnostic proposals. The authors report DIAL outperforms existing latent world models and planning baselines on four visual control benchmarks, in both standard and long-horizon settings.
**Purpose (≤3 sentences):** The authors aim to align latent world-model training with how the model is actually used at planning/test time, closing the train-test mismatch between teacher-forced dynamics training and autoregressive rollout-based planning.
**Breakthrough (≤3 sentences):** The authors report a rollout-alignment training scheme that exposes the forward model to its own predictions, paired with a lightweight inverse dynamics head that infers actions from latent transitions and is also applied (frozen) to model-generated rollouts. At test time this inverse/forward dynamics pairing builds a goal-directed action sequence that initializes the Cross-Entropy Method (CEM) planner's proposal mean, which the authors state improves over goal-agnostic initialization.
**Tools & method (≤3 sentences):** The method is evaluated on latent world models for visual control, using a Cross-Entropy Method (CEM) planner refined from the learned inverse-dynamics-informed initialization, tested across four visual control benchmarks in both standard and long-horizon scenarios.
**Limitation (≤3 sentences):** Not stated by the authors in the abstract or main text reviewed.

## Tiresias: Towards Language-Conditioned World Models
- **arXiv:** 2611.10392 · https://arxiv.org/abs/2611.10392
- **Submitted:** 2026-11-07
- **Authors:** Fengyi Wu, Yifei Dong, Yetong Sha, Lingdong Kong, Qiyu Hu, Bohan Xiong, Qi Dai, Alexander G. Hauptmann, Zhi-Qi Cheng
- **Qualifying affiliation(s):** Microsoft Research — Qi Dai
- **Categories:** cs.CV
- **Open release:** none found (benchmark LCWM-Bench used but no confirmed public release found)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper argues that language-conditioned world modeling is fragmented across domains with different action spaces, datasets, and evaluation protocols. It introduces LCWM, a unified task that maps an observation plus a language instruction to an action sequence, together with LCWM-Bench, a benchmark spanning 15 datasets across navigation, robotics, gaming, and driving. The authors also propose Tiresias, an agent that plans by imagining outcomes of candidate trajectories using a diffusion policy, trajectory/visual rankers, and a video-pretrained world model.
**Purpose (≤3 sentences):** The authors aim to unify the scattered landscape of language-conditioned world-model research under one task formulation and one cross-domain benchmark, to enable fair comparison across navigation, robotics, gaming, and driving settings.
**Breakthrough (≤3 sentences):** The authors report the introduction of LCWM-Bench, a 15-dataset benchmark spanning four domains, plus Tiresias, an agent that imagines candidate-trajectory outcomes with a video-pretrained world model and ranks them with trajectory and visual rankers before acting.
**Tools & method (≤3 sentences):** Tiresias combines a diffusion policy for action-sequence proposals, trajectory and visual rankers for selecting among imagined futures, and a video-pretrained world model for outcome imagination, evaluated on LCWM-Bench's train/val-seen/val-unseen splits covering navigation, robotics, gaming, and driving data.
**Limitation (≤3 sentences):** The authors state (Appendix D) that evaluation covers real and simulated data within LCWM-Bench but does not deploy Tiresias on physical robots, so its effectiveness on real hardware "remains to be validated," deferring physical navigation/manipulation deployment to future work.

## ReelCache: An Efficient KV Cache Compression and Management System for Multi-Round Video Generation
- **arXiv:** 2611.09973 · https://arxiv.org/abs/2611.09973
- **Submitted:** 2026-10-31
- **Authors:** Tianyu Wang, Daiyang Yu, Zhiwei Ren, Junbo Li, Jitian Zhang, Longfei Shangguan
- **Qualifying affiliation(s):** Google — Jitian Zhang
- **Categories:** cs.CV, cs.DC
- **Open release:** code — https://github.com/Tianyu9748/ReelCache
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ReelCache is a system that compresses and manages the attention key-value (KV) caches of autoregressive video diffusion models during multi-round, interactive video generation. It pairs an intra-chunk compressor (low-rank decomposition plus video coding) with an inter-chunk manager that shares basis directions and organizes chunk states in a tree to support resume, rewind, and fork operations during creative editing. The authors report 14.46-21.13x lower KV storage and 1.25-3.36x faster next-chunk generation with less than 1% VBench score drop.
**Purpose (≤3 sentences):** The authors motivate the work around consumer-facing creative video tools (citing Google Veo, ByteDance Seedance, Adobe Firefly) where users iteratively extend, review, and revise generated video clips — returning to earlier points to replace unsatisfactory segments or explore alternative continuations. They aim to make the KV-cache memory and latency cost of this multi-round, interactive generation workflow tractable.
**Breakthrough (≤3 sentences):** The authors report a combined intra-chunk (low-rank + video coding) and inter-chunk (shared basis directions, tree-structured chunk-state management) compression scheme implemented in SGLang-Diffusion, enabling resume/rewind/fork operations with large storage and latency reductions. They built a new Synthetic-500 dataset (partly LLM-written prompts) since no public multi-round video-generation dataset existed for evaluation.
**Tools & method (≤3 sentences):** The system targets chunk-autoregressive video diffusion transformers, implemented atop SGLang-Diffusion, and is evaluated using six VBench dimensions plus SSIM against uncompressed references on the authors' Synthetic-500 multi-round generation dataset.
**Limitation (≤3 sentences):** The authors state the method's scope excludes bidirectional-denoising and in-place-editing video models, since their KV may not remain valid as an unchanged prefix; full-attention models see decompression slowdowns of 3.2-4.2%; and the speedup advantage shrinks as rewind frequency increases.

# Near-misses
- 2611.11561 · From Sketch to Design: A Cross-scale Workflow for Procedural Generative Urban Design · co-author is from Digital Blue Foam, a small niche urban-design-software startup, not a top-tier industrial lab comparable to the tracked companies — no qualifying industry affiliation
- 2611.11554 · Kimodo-Policy: Learning Kinematic Action Models for Humanoid Loco-Manipulation · off-topic: low-level humanoid robot loco-manipulation control, explicitly not a general world-model/simulation contribution (despite JD Explore Academy co-authors, flagged borderline company)
- 2611.11500 · ForeAct: Geometry-Guided Action Learning from World Representations · off-topic: adapts a pretrained video world model purely as a backbone for low-latency robot manipulation control; goal is an action policy, not a general world-model technique (JD Explore Academy co-authors, flagged borderline company)
- 2611.10199 · RigidGS: Geometry-Aware Object Decoupling for Rigid-Body Interaction in 3D Gaussian Splatting · academic-only (University of Wyoming authors only; no industry affiliation found)
- 2611.10160 · Improving the Diffusability of Motion Tokenizer · academic-only (all four authors affiliated with King's College London; no industry affiliation found)
- 2611.10137 · A Unified Inertial Encoder for Human and Humanoid Motion · off-topic: robot/human state estimation (inertial velocity/odometry) and humanoid locomotion control, not character-animation research, despite a qualifying Amazon FAR co-affiliation
- 2611.10013 · From Video to Digital Twin: An Exploratory Study of World Models and Gaussian Splatting on In-the-Wild Video · academic/independent-only (sole author listed as "Independent Researcher"; no industry affiliation found)
