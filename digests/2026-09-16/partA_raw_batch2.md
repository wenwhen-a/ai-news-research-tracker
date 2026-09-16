## From Evaluation to Enhancement: Benchmarking and Improving Think-with-Video Reasoning for Video Generative Models
- **arXiv:** 2609.11242 · https://arxiv.org/abs/2609.11242
- **Submitted:** 2026-09-10
- **Authors:** Meng Luo, Yicheng Liu, Jiahao Wang, Yuanxing Zhang, Xin Tao, Pengfei Wan, Kun Gai, Hao Fei
- **Qualifying affiliation(s):** Kuaishou Technology (Kling Team) — Jiahao Wang, Yuanxing Zhang, Xin Tao, Pengfei Wan, Kun Gai
- **Categories:** cs.CV, cs.AI
- **Open release:** code + data — https://huggingface.co/datasets/KlingTeam/VWG-Bench
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces VWG-Bench, a benchmark spanning 9 reasoning dimensions and 38 fine-grained tasks (380 samples) that tests whether video generative models can perform logical, physical, and causal reasoning ("think with video") rather than only produce visually convincing footage. It also introduces Vid-PRE, a model-agnostic prompt-rewriting module trained to improve reasoning performance of existing video generators without changing their architecture. Six systems were evaluated, including Wan2.2, Veo3.1, Sora2, and Kling-2.5-Turbo-Pro.

**Purpose (≤3 sentences):** The authors state that existing video-generation benchmarks are fragmented and conflate visual quality with cognitive/reasoning correctness, leaving it unclear whether generators execute symbolic, physical, and intentional rules or merely exploit surface statistics. VWG-Bench is designed to isolate reasoning ability with a three-level (video/task/sample) evaluation protocol, and Vid-PRE aims to close observed reasoning gaps as a drop-in enhancer.

**Breakthrough (≤3 sentences):** The authors report that video-quality scores consistently exceed reasoning scores across all six tested systems (e.g., Wan2.2 scores 2.32 on video quality vs. 1.56 on rule-following), with Veo3.1 the strongest overall baseline at 3.55/5. With Vid-PRE, they report Wan2.2's accuracy on V-ReasonBench rising from 26.65% to 44.48% (a 67% relative gain) and its VWG-Bench score improving from 2.13 to 2.51 (18% gain), with human–VLM judgment agreement of Spearman's ρ 0.69–0.80.

**Tools & method (≤3 sentences):** Vid-PRE is built on Qwen3-VL-8B and trained in two stages: supervised fine-tuning on ~20K rejection-sampled reasoning-chain tuples, followed by GRPO on 1.5K hard samples using a four-part text-based reward (intent preservation, visual-spatial consistency, solution correctness, format compliance), with no video generated during training. VWG-Bench's 380 samples were built via an automated text-to-image generation, consistency-filtering, and VLM-annotation pipeline.

**Limitation (≤3 sentences):** The authors acknowledge that VWG-Bench's 10 instances per task (380 samples total) limit statistical robustness, and that Vid-PRE's SFT data relies on proprietary APIs, raising reproducibility concerns. They also note Vid-PRE was validated mainly on Wan-family generators with more limited testing on Sora2/Veo3.1, and that it adds roughly 3–5 seconds (about 8% end-to-end latency) per sample at inference.

---

## PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control
- **arXiv:** 2609.17521 · https://arxiv.org/abs/2609.17521
- **Submitted:** 2026-09-15
- **Authors:** Chuhao Chen, Peter Wonka, Chaoyang Wang, Chen Wang, Qiao Feng, Sergey Tulyakov, Lingjie Liu
- **Qualifying affiliation(s):** Snap Inc. — Peter Wonka (also KAUST), Chaoyang Wang, Sergey Tulyakov; **FLAG: borderline — Snap Inc. is not on the core tracked list, treated as a comparable industry lab**
- **Categories:** cs.CV, cs.AI, cs.GR
- **Open release:** none stated — project page only, no code/weights/demo link given: https://czzzzh.github.io/PhysStream
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PhysStream is an autoregressive, physics-grounded image-to-video model that lets a user interactively steer multi-object rigid-body scenes with sparse 3D velocity-increment signals during generation, rather than requiring a full pre-planned control schedule. It maintains a "structured scene memory" — positional maps and object-tracking maps estimated online from previously generated frames — to keep motion physically plausible. The paper was accepted to SIGGRAPH Asia 2026.

**Purpose (≤3 sentences):** The authors state that prior interactive video-control methods either require the entire control sequence specified upfront or use pixel-space signals (e.g., drag points) that dictate object positions directly rather than encoding real physical dynamics. PhysStream aims for direct, end-to-end, scene-level physics-grounded control that responds to sparse velocity commands the way a physics engine would.

**Breakthrough (≤3 sentences):** On a synthetic multi-object benchmark, the authors report PhysStream reduces motion-distribution distance (FVMD) by 33% and trajectory error by 12% versus the strongest baselines (FVMD 787.0 vs. 1183 for RealWonder and 2662 for DragStream). In an in-the-wild human study across 20 scenes, they report PhysStream was preferred over baselines in 91.8% of physics-plausibility, 88.4% of motion, and 91.2% of visual-quality comparisons.

**Tools & method (≤3 sentences):** The model fine-tunes a Wan2.2-TI2V-5B backbone in two stages — first bidirectional fine-tuning with velocity-increment conditioning, then conversion to a causal autoregressive model via teacher-forcing that adds the online scene-memory signals (estimated with Depth-Anything-3 and SAM2) — using shifted channel concatenation to inject conditions without frame leakage. Training used 100k synthetic PyBullet/Blender-rendered clips (plus smaller deformable-ball and cloth sets) on 8×H100 GPUs, about 30 hours per stage.

**Limitation (≤3 sentences):** The authors acknowledge the model struggles with highly complex motion such as tumbling and is largely scoped to rigid-body dynamics, with richer materials requiring additional fine-tuning data. They also report accumulated appearance drift over long autoregressive horizons — a "well-known failure mode of autoregressive generation" — note that consistency metrics can be inflated by degenerate static-object generations, and defer real-time generation to future work (66.3s per 49-frame clip unaccelerated, 19.3s with optimization).

---

# Near-misses
- 2609.07398 · OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining · affiliation unverifiable — no HTML version exists at arxiv.org/html/2609.07398 or /v1 (both return HTTP 404); the abs page carries no affiliation information, so the expected Google affiliation could not be confirmed from a primary source despite the paper being on-topic (world-action model pretraining)
- 2609.00646 · DramaChain Bench: An End-to-End Benchmark for Short-Drama Generation · off-topic despite a confirmed qualifying affiliation (Hunyuan, Tencent) — this is a production-pipeline/content-fidelity benchmark for short-drama video generation (scriptwriting through shot assembly), not 3D, world-model, character-animation, or game-engine research
- 2609.09187 · AgenticGen: Reward-Guided Agentic Video Generation for Advertising · off-topic (advertising video generation optimized via online business metrics such as CTR/CVR, not 3D/world-model/character-animation/game-engine) and affiliation unverifiable — no HTML version exists (404 at arxiv.org/html/2609.09187 and /v1); the abs page confirms deployment in "the TikTok advertising system" but provides no formal author affiliation block
- 2608.29621 · CineForge: Self-Improving Agents for Long-Horizon Video Generation · off-topic despite a confirmed qualifying affiliation (Kuaishou Technology) — this is an agentic story/film production system and its CineScope evaluation suite, not 3D, world-model, character-animation, or game-engine research in the tracked sense
- 2608.25452 · VGA-BenchV2: An Expanded Unified Benchmark and Multi-Model Framework for Evaluating Video Aesthetics and Generation Quality · off-topic despite a confirmed qualifying affiliation (Ant Group, also FLAG: borderline org) — this is a general video-aesthetics/generation-quality benchmark and reward model, not 3D, world-model, character-animation, or game-engine research
- 2609.16724 · CorrRisk-WM: Corridor-Conditioned Risk World Modeling for Safety-Critical Trajectory Planning · academic-only — both authors (Tingyu Guo, Reza Langari) are affiliated solely with Texas A&M University; "Waymo validation shards" refers only to the Waymo Open Dataset used for evaluation, not an author affiliation, and no company is mentioned anywhere in the paper
- 2609.14985 · Converting Sequenced Fuzzy Cognitive Maps to Causal Virtual Worlds with Large Video Generators · academic-only — all three authors are affiliated solely with USC and Florida International University; Google Gemini 3.1 and Veo 3.1 are used only as third-party tools in the demonstration, not as author employers, and no company affiliation was found
