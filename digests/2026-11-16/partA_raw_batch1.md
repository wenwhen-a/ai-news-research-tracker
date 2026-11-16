## Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agents
- **arXiv:** 2611.18397 · https://arxiv.org/abs/2611.18397
- **Submitted:** 2026-11-13
- **Authors:** Run Luo, Kuan Zhang, Qi Deng, Yukun Chen, Zhihao Yang, Yufei Zhang, Renrong Hu, Yi Zhang, Guiyu Ma, Tianyu Fan, Longze Chen, Hao Sun, Jiaming Li, Jiaming Yang, Xiaohao Liu, Tao Tan, Minzheng Wang, Hangtian Jia, Shuai Yuan, Lvdi Wang, Xiao Liu, Chao Ma, Yuting Zou, Yinhe Zheng, Xiaobo Xia, Dawei Jiang, Shaoqing Ren
- **Qualifying affiliation(s):** miHoYo (Honkai AI R&D Team) — all authors listed under this team affiliation
- **Categories:** cs.CL (primary), cs.AI, cs.CV
- **Open release:** code/weights — authors state they open-source the inference engine and checkpoints for CPT scaling behaviors; project page https://mihoyo-gamer.github.io/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Gamer is a generalist vision-language-action agent framework built by miHoYo's Honkai AI R&D Team for long-horizon, real-time play across both 2D interfaces and 3D open-world games, including miHoYo's own title Honkai: Star Rail (HSR). It combines a perception/memory/reasoning pipeline, continued pretraining on large-scale gameplay data, sparse-thinking instruction tuning, multi-turn reinforcement learning, and a cloud-edge inference engine for low-latency concurrent play.
**Purpose (≤3 sentences):** The authors aim to build a single agent that generalizes across long-horizon tasks in complex interactive environments, rather than a game-specific bot, as a step toward agents that operate across digital and physical worlds.
**Breakthrough (≤3 sentences):** The authors report that Gamer achieves generalization and efficiency comparable to skilled human players across several 3D open-world games and competitive results on conventional 2D game benchmarks (MCU, ViZDoom, OmniGameArena, GameWorld), evaluated with real-time (RT) scores against time-paused (TP) baselines. They evaluate on HSR side-quests ("Opportunity Makes the Thief Part I" with 30 milestones, "Bestial Ferocity" with 55 milestones) and a 40-instance, 7-type minigame suite.
**Tools & method (≤3 sentences):** Continued pretraining used roughly 2.4K hours of public gameplay data (VPT, D2E, OpenP2P) plus ~6.3B tokens of general vision-language data and additional HSR gameplay (85% gameplay/15% general mix); SFT drew on ~68K HSR sessions (~11K hours), filtered to ~3.2K sessions (~1K hours) for annotation, yielding ~261K operation-level, ~211K subgoal-level, and ~234K task-level samples. Training used distributed H200 clusters for CPT and A800 clusters for SFT, a 64-H200 Streaming-vLLM inference pool serving 32 parallel environments for RL (~14.6K verified online rollouts), and a GameScaling study consuming ~45K H200 GPU-hours across 120 configurations.
**Limitation (≤3 sentences):** The authors note that for distant, unseen games, additional continued-pretraining data does not produce sustained gains, and argue that longer tasks and more distant game worlds require task-conditioned supervision and online interaction. They also acknowledge the HSR evaluation tests new tasks within a familiar game rather than zero-shot transfer to an unseen game, and that their accuracy metric measures verified milestone progress rather than uninterrupted end-to-end quest completion.

---

## TelePhysica: Agentic Reconstruction of Physically Interactive Scenes
- **arXiv:** 2611.18078 · https://arxiv.org/abs/2611.18078
- **Submitted:** 2026-11-13
- **Authors:** Ruiqi Shu, Xufeng Zhan, Yuanzhi Liang, Haibin Huang, Chi Zhang, Xuelong Li
- **Qualifying affiliation(s):** China Telecom — Institute of Artificial Intelligence (TeleAI), all authors (Shu and Zhan completed the work as TeleAI interns; Li is corresponding author); FLAG: borderline
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** none (homepage https://interactive4d.vercel.app/ shown, but no code/weights/demo release stated for this work)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** TelePhysica is a closed-loop, agentic pipeline that reconstructs a physically simulatable 3D scene from a single photo and uses the resulting physics rollouts to condition video diffusion models. It targets two failure modes the authors identify: image-to-video diffusion models that entangle pixel synthesis with implicit, uncontrollable motion, and single-pass monocular 3D reconstruction that leaves depth/support underconstrained, causing objects to interpenetrate or collapse under gravity. The paper is explicitly labeled "Ongoing Work."
**Purpose (≤3 sentences):** The authors want a way to recover an executable, physically consistent scene from one uncalibrated image so that downstream video generation can be conditioned on genuine physical dynamics rather than implicit, uncontrollable motion priors, enabling mid-rollout intervention and counterfactual forces.
**Breakthrough (≤3 sentences):** The authors report that on a 100-scene benchmark, their closed-loop verification raises equilibrium-verified scene recovery from 0% (single-pass synthesis) to 81%. They also report that finite-element cloth simulation shows substantially larger corner displacement and out-of-plane pleating than rigid-plate proxies, and that conditioning video generation on simulated trajectories increases dynamic motion-mask overlap by 2-5x versus direct image-to-video baselines, while preserving motion direction under reversed forces where the baselines fail.
**Tools & method (≤3 sentences):** A vision-language coding agent generates visual meshes and declarative physics models from a single photo, verified by silhouette comparison against the input image and a zero-force gravity equilibrium test; the verified scene runs in a unified solver covering rigid bodies, articulated chains, cloth, and 3D elastic tetrahedral (soft-body) models. Simulated rollouts then condition pretrained video diffusion backbones (including Wan2.2-VACE at 1.3B and 14B scale, and a dual-reference MiniMax-H3 model) via Canny or RGB render control.
**Limitation (≤3 sentences):** The authors acknowledge that material parameters (mass density, Young's modulus, friction) are assigned from priors rather than identified online from visual feedback, leaving closed-loop physical parameter identification as future work. They also note only 81% of scenes reach equilibrium verification and only 49% complete the full simulated rollout, that the smaller 1.3B diffusion backbone shows weakened background appearance or texture distortion under control, and that the larger 14B backbone that fixes this needs about 2.1x the GPU memory (41.0 GB vs 19.4 GB).

---

# Near-misses
- 2611.18393 · WeatherDreamer: Learning a World Model from Multimodal Earth Observations · all authors affiliated with Zeus AI, Inc., a small startup not on the qualifying company list and not clearly comparable to the listed top-tier industry labs — no qualifying co-author
- 2611.18340 · DIRT: Depth-completed Image-based Rendering using Two-band Blending for Live Novel-view Synthesis · purely academic, all authors at Friedrich-Alexander-Universität Erlangen-Nürnberg, no industry co-author
- 2611.18267 · TetraCoder: Adaptive Tetrahedral Encoding for Neural Fields · purely academic, all authors at University of Trento, no industry co-author
- 2611.17957 · MacroGS: Macro-Pixel Shared Gaussian Primitives for Arbitrary-Scale Light Field Super-Resolution · purely academic, authors at Capital Normal University and National University of Singapore, no industry co-author
