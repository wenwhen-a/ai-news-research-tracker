# Part A — Raw Scan (2026-09-15)

## DiVA: Enabling Interactive Digital Life Simulation via Video Models
- **arXiv:** 2609.13830 · https://arxiv.org/abs/2609.13830
- **Submitted:** 2026-09-12
- **Authors:** Cheng Chen, Hao Ouyang, Qiuyu Wang, Ka Leong Cheng, Wen Wang, Yihao Meng, Hanlin Wang, Yixuan Li, Jiacheng Wei, Zhenshan Tan, Yanhong Zeng, Yujun Shen, Guosheng Lin, Fayao Liu
- **Qualifying affiliation(s):** Ant Group — Hao Ouyang, Qiuyu Wang, Ka Leong Cheng, Wen Wang, Yihao Meng, Hanlin Wang, Yixuan Li, Yanhong Zeng, Yujun Shen (Cheng Chen also lists Ant Group alongside NTU/A*STAR); **flagged — Ant Group is a borderline/comparable lab, not on the core tracked list**
- **Categories:** cs.CV
- **Open release:** none yet — authors state inference/eval code, model adaptations, and prompt templates "will be made publicly available ... upon publication"
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** DiVA is an interactive digital-life simulator that supports long, open-ended, multi-turn interactions with a video-generated character (actions plus audio responses), pairing an MLLM router with a three-stage video generation pipeline. Its central novelty is an "Anchored Video Continuation" (AVC) module that periodically resets the character to a stable anchor frame to stop visual quality from drifting over long sessions. It reports substantially better long-term visual quality and realism than existing audio-driven avatar baselines.

**Purpose (≤3 sentences):** Current video/avatar generation models produce short clips and degrade visually over extended, user-driven interaction; DiVA aims to enable prolonged, open-ended digital-character experiences without that degradation. It targets multi-turn scenarios combining character actions and audio responses rather than one-shot clip generation.

**Breakthrough (≤3 sentences):** The authors report that the Anchored Video Continuation module cuts quality drift from 0.0947 (InfiniteTalk baseline) to 0.0341 — roughly a 64% reduction — while preserving the highest dynamic-motion score among compared methods and maintaining character identity consistency across a session.

**Tools & method (≤3 sentences):** An MLLM (GPT-4/Qwen-class model) acts as a semantic router choosing between "waiting" and "action" video segments; a segment-based continuation model transitions the last action-video frame back to a fixed high-quality anchor frame to reset drift. The system is trained on a 45k video-text pair in-house dataset at 480×832 resolution.

**Limitation (≤3 sentences):** The authors acknowledge DiVA inherits fine-grained generation failures from the underlying video model, including physically implausible interactions. When target anchors differ greatly from the current state, transitions can look "cross-fade-like" rather than fully plausible intermediate motion, and some evaluation errors trace to the base video model's instruction-following fidelity rather than the routing logic.

---

## When Should a World Model Move? Loss-Conditioned State Execution
- **arXiv:** 2609.15801 · https://arxiv.org/abs/2609.15801
- **Submitted:** 2026-09-14
- **Authors:** Jintao Xu, Zhengyu Chen, Ben Zhang, Yongzhi Qi, Jianshen Zhang
- **Qualifying affiliation(s):** JD.com (Supply Chain Tech Team Y) — all five authors; **flagged — JD is a borderline/comparable lab, not on the core tracked list**
- **Categories:** cs.AI, cs.LG, math.OC
- **Open release:** none found (no code/weights link stated; uses public benchmarks plus a proprietary JD.com dataset)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces "loss-conditioned state execution," a model-agnostic decision rule for whether a world model should actually update ("move") its state or simply persist the current one. It shows predictive informativeness (e.g., high AUROC) does not by itself guarantee an update reduces downstream loss, and proposes a statistically certified gate that only executes updates with a proven bounded-loss gain. It is validated across six domains spanning time-series forecasting, gridworld and MuJoCo control, and JD's internal inventory data.

**Purpose (≤3 sentences):** Standard world-model evaluation focuses on likelihood/calibration, leaving open whether a prediction should replace the current state under a specific declared loss. The authors formalize the gap between "state movability" (whether any loss-reducing correction exists) and "proposal benefit" (whether a specific fitted model's proposal actually helps), aiming to prevent harmful updates in sparse or sticky dynamics.

**Breakthrough (≤3 sentences):** The authors report and prove that proposal benefit is always bounded by state movability, and demonstrate empirically that a model with strong occurrence ranking (AUROC 0.819) on JD.com's inventory data still produces worse MAE than simply persisting — showing high predictive discrimination can be actively misleading. On M4 Monthly (28,684 series), selective execution at 14% coverage beats both always-persist and always-execute baselines (0.588 vs. 0.599 vs. 0.621 loss).

**Tools & method (≤3 sentences):** The method builds Bayes-corrected state proposals from a predictive distribution, then certifies them via an independent calibration set using Hoeffding concentration bounds (with union-bound correction across pre-declared groups), executing only where a lower confidence bound on loss gain exceeds zero. It is evaluated on Monash Car Parts, M4 Monthly, FourRooms, MuJoCo (27 runs), a synthetic controlled phase-transition setting, and JD.com's proprietary unhealthy-inventory dataset.

**Limitation (≤3 sentences):** The confidence-based gating substantially reduces update frequency (22.2% → 14% on M4), trading coverage for statistical safety, and results are sensitive to how per-step losses aggregate within episodes and to the pre-declared grouping/bounding choices. The calibration guarantee also assumes the deployment population matches the calibration distribution, which may not hold under distribution shift.

---

# Near-misses
- 2609.15781 · When the World Lies: Backdoor Attacks on Latent World Models for Downstream Control · affiliation unverifiable — no HTML version exists (only PDF/TeX source on abs page); authors (Roberto Riaño, Gorka Abad, Stjepan Picek, Aitor Urbieta) appear academic, no affiliation confirmable
- 2609.15639 · SAM3D-Part: Interactive Part Selection and Generation from 3D Objects · no qualifying industry affiliation found — authors affiliated with CUHK-Shenzhen, FNii-Shenzhen, Nanjing University of Science and Technology, MBZUAI, and Meshy AI (a startup not on the tracked or borderline list)
- 2606.05035 · Anchor3R: Streaming 3D Reconstruction with Transient Anchors for Long-Horizon Visual Mapping · out of window — v1 actually submitted 2026-06-03, not within Aug 16–Sep 15 (the 2026-09-14 date in the lead generator was not the v1 date)
- 2604.28130 · MoCapAnything V2: End-to-End Motion Capture for Arbitrary Skeletons · out of window — v1 actually submitted 2026-04-30 (accepted to SIGGRAPH Asia 2026, later revisions through September do not count as v1)
- 2609.15478 · BVB: Benchmarking Agentic Video Understanding via Programmatic Reconstruction in Blender · off-topic — this is a benchmark for multimodal-agent video understanding/reconstruction fidelity, not a 3D generation, world-model, character-animation, or game-engine research contribution in itself
- 2605.04412 · Structured 3D Latents Are Surprisingly Powerful: Unleashing Generalizable Style with 2D Diffusion (DiLAST) · out of window — v1 actually submitted 2026-05-06, not within Aug 16–Sep 15 (Tencent flag from lead generator not verified due to window failure)
- 2609.13224 · Seeing What the Vehicle Sees: Video-Augmented Virtual Reality for Physical Autonomous Vehicles · off-topic — this is autonomous-vehicle/robotics teleoperation research (ROS 2 robot + Unity/Meta Quest VR dashboard), not games/3D-generation/world-models/animation/engine research; no Meta-affiliated author found, Meta Quest 3S is only used as consumer hardware
