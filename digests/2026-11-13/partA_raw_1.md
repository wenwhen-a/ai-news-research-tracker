## Back to Pixels: Lifting Latent Video Diffusion into Pixel Space
- **arXiv:** 2611.17336 · https://arxiv.org/abs/2611.17336
- **Submitted:** 2026-11-12
- **Authors:** Yanke Song, Shuo Chen, Chris Rockwell, Guande He, Nan Liu, Desai Xie, Tianpei Gu, Yong-Hyun Park, Aryan V S, Dennis Yuren Menn, Ming-Hsuan Yang, Xun Huang
- **Qualifying affiliation(s):** Roblox (listed affiliation block; other listed affiliations are UC Merced, UPenn, UT Austin)
- **Categories:** cs.CV
- **Open release:** none (project page only: https://chenshuo20.github.io/PixVid/; no explicit code/weights statement)
- **Shipped counterpart:** none found (Roblox-affiliated; no named shipping product claimed in the paper)

**Summary (≤3 sentences):** The paper presents PixVid, which adapts a pretrained latent video diffusion model (Wan2.1-14B) to generate video directly in pixel space instead of a compressed VAE latent space. It replaces the VAE with a pixel patch embedding plus a causal convolutional "detailer" head, predicts clean video rather than velocity, and distills a causal, frame-by-frame variant for interactive use.
**Purpose (≤3 sentences):** Latent compression in standard video diffusion models limits high-resolution generation, frame-level control, and response latency, which matters for interactive/world-model-style applications. The authors aim to remove that bottleneck while keeping diffusion-transformer architecture and training recipes.
**Breakthrough (≤3 sentences):** The authors report VBench totals of 84.78 (480p) and 85.09 (960p) for PixVid versus 84.05 for Wan2.1 and 83.72 for PixelUMM, and a human study where PixVid won all pairwise comparisons against baselines on 100 Movie Gen prompts. For interactive use, they report median control-to-screen latency dropping from 495 ms to 34 ms versus a SolarWM baseline, with throughput of 29.4 fps and comparable FVD (51.1 vs 53.8).
**Tools & method (≤3 sentences):** Training used roughly 6.4M Wan2.1-generated clips (convergence ~1.3M clips, ~44K B200 GPU-hours), on NVIDIA B200 GPUs with batch size 64 across 64 GPUs. Editing experiments used ~79K training clips and 1,000 held-out clips, evaluated with VBench, Movie Gen Video Bench, and FVD/FVMD/LPIPS metrics.
**Limitation (≤3 sentences):** Without temporal compression, PixVid processes ~3.9x as many tokens per second as Wan2.1 at 480×832, raising cost for short low-resolution clips. Camera rotation/translation drift over long rollouts is worse than the latent baseline, and pixel-color sensitivity to sampler precision is flagged as unresolved.

## Neural Render Proxies for Interactive and Differentiable Lighting
- **arXiv:** 2611.17185 · https://arxiv.org/abs/2611.17185
- **Submitted:** 2026-11-12
- **Authors:** Sergio Sancho, Alexander Rath, Marco Manzi, Pascal Chang, Amit H. Bermano, Derek Nowrouzezahrai, Markus Gross, Marios Papas
- **Qualifying affiliation(s):** Disney Research|Studios — Sergio Sancho, Alexander Rath, Marco Manzi, Pascal Chang, Amit H. Bermano, Markus Gross, Marios Papas (all list affiliation 2); FLAG: borderline (Disney not on the explicit qualifying list but is a comparable top-tier entertainment/graphics industry lab)
- **Categories:** cs.GR (primary), cs.CV
- **Open release:** none stated (paper names third-party tools it builds on — PyTorch, tiny-cuda-nn, Triton, Mitsuba 3, Disney's Hyperion renderer — but does not say its own code/weights/demo will be released)
- **Shipped counterpart:** none found (Hyperion is Disney's existing production renderer, used as an evaluation baseline/testbed, not claimed as a new shipped feature)

**Summary (≤3 sentences):** The paper introduces a method for interactive, differentiable relighting of static scenes (fixed camera, fixed materials) by decoupling path sampling from emission computation. A light-agnostic pass caches path vertices/throughput once, and a small scene-specific MLP maps light parameters to pixel contributions at 30–60 Hz.
**Purpose (≤3 sentences):** Production lighting iteration normally requires re-rendering with slow, often non-differentiable offline renderers, taking minutes to hours per frame. The authors aim to make relighting both fast and differentiable for artist iteration and light optimization.
**Breakthrough (≤3 sentences):** The authors report the method outperforms image-based baselines by 2.8 dB (PSNR) at 1024 training images, with a best ablation configuration reaching 41.07 dB PSNR. Tens of GB of cached path data compress to a few MB of network weights, with inference per-pixel costs of 0.83–31.21 ms depending on network size (5.6–13.3 MB).
**Tools & method (≤3 sentences):** Path data for a 960×402, 512-spp production scene took ~30 minutes to render (14–28 GB RAM); standard training took ~1 hour for 100k iterations on an NVIDIA RTX 5090 (32 GB), with path rendering on 32 threads of an Intel Xeon Gold 6342. Light optimization was benchmarked against Mitsuba 3 and ZeroGrads over 50 runs on Cornell Box, Bedroom, and Kitchen scenes.
**Limitation (≤3 sentences):** Only simple, few-parameter light types (sphere and quad lights) work well; textured or arbitrary-shape lights are left to future work. Light transport is baked in after training (no non-physical attenuation/exclusivity edits), occluded/narrow regions can be under-sampled without next-event estimation, and training is memory-bound since all path data is preloaded.

## PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models
- **arXiv:** 2611.16748 · https://arxiv.org/abs/2611.16748
- **Submitted:** 2026-11-12
- **Authors:** Yuxuan Chen, Xiaojie Li, Hao Chen, Juncheng Ma, Kewei Zhang, Zhongjing Du, Guoqiang Wei, Fangfang Wang, Zhen Dong, Zhiyang Dou, Liming Zhao, Yan Zeng, Jianwei Zhang, Daquan Zhou, et al.
- **Qualifying affiliation(s):** ByteDance Seed (listed among the paper's affiliations; exact per-author mapping not recoverable from the HTML, affiliation fields were blank — other listed affiliations: Peking University, UC Santa Barbara, MIT, Universität Hamburg, Hangzhou Normal University)
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** code + dataset — github.com/DAGroup-PKU/PhysLoop; authors say they release the 100K-video PhysLoop-100K set, PhysLoop-Gen/PhysLoop-Repair eval sets, and "generation tools" (no model weights mentioned)
- **Shipped counterpart:** none found (uses third-party models Seedance 2.5, GPT-6 Astra, Claude Opus 5 as components, not claimed as a new shipped product)

**Summary (≤3 sentences):** PhysLoop is a harness in which an LLM agent writes a physics task/scene program that Unreal Engine (with Taichi/Genesis support) simulates, a verifier checks the simulated result, and a video model (Seedance 2.5 by default) renders appearance on top — building a training/repair pipeline for physically-grounded video generation. Failures are revised by the agent within a budget of up to five generation calls per task.
**Purpose (≤3 sentences):** Video generation models often produce visually realistic but physically implausible motion. The authors aim to use LLMs' physics knowledge, grounded via simulation, to both generate physically-correct training data and repair physical errors in existing generated videos, as a step toward recursive self-improvement of video models.
**Breakthrough (≤3 sentences):** The authors report 85% task success on PhysLoop-Gen (100 generation tasks) versus 73% for standalone Seedance 2.5, and 86% success on PhysLoop-Repair (50 repair tasks) versus 19.33% for the best standalone baseline. On Physics-IQ Verified (66 cases), PhysLoop scores 52.06 vs 48.07 for standalone Seedance 2.5, though human-rated visual realism is lower for PhysLoop (3.72 vs 4.29).
**Tools & method (≤3 sentences):** Simulation ran on a Mac mini (Apple M4, 10-core, 16 GB) with Unreal Engine 5.7, producing 1080p/24fps output after appearance refinement; combined generation time is estimated at 7–12 minutes per task. PhysLoop-100K comprises 100K accepted videos drawn from 2.5K physical events.
**Limitation (≤3 sentences):** Results depend on simulator/asset/verification coverage, and reconstructing unobserved geometry/materials/initial states requires assumptions. Appearance refinement can introduce new errors and local repair may not suffice when later events change; the full recursive self-improvement loop is not yet demonstrated, and human-rating coverage in the pilot is incomplete.

## Rethinking Actions: Continuity-Aware Priors for World-Model Planning
- **arXiv:** 2611.16645 · https://arxiv.org/abs/2611.16645
- **Submitted:** 2026-11-12
- **Authors:** Shaobo Yang, Zichen Ai, Ziyang Ma, Qian Yang, Bin Fang
- **Qualifying affiliation(s):** Alibaba Group — Qian Yang; (other authors are at Beijing University of Posts and Telecommunications; Bin Fang's affiliation is ambiguous in the HTML, with an Ant Group email domain visible — FLAG: borderline on that one author only, but Qian Yang/Alibaba alone satisfies the gate)
- **Categories:** cs.RO (primary), cs.LG
- **Open release:** code — github.com/oliverstack-byte/LG-DKGP (no weights/demo statement)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper studies whether action proposals that better respect the temporal continuity of expert action sequences improve goal-directed planning with learned visual world models. It proposes LG-DKGP, a locality-gated deep-kernel Gaussian-process action prior that seeds planning search near a continuity-aware predicted trajectory rather than from scratch.
**Purpose (≤3 sentences):** Standard planning with visual world models (e.g., via CEM-style sampling) often proposes actions that ignore how real/expert action sequences evolve smoothly over time, hurting planning efficiency and success. The authors aim to inject that continuity structure as a prior to improve goal-directed planning.
**Breakthrough (≤3 sentences):** The authors report LG-DKGP reaches 87.07% macro success across five environments (PushT, OGBench Cube, LIBERO Caddy, LIBERO Scene2, RoboTwin), versus 71.03% for INTACT, 61.66% for PRISM, and 58.66% for LeWM (averaged over five seeds). It loses only on the Scene2 task, where INTACT (77.53%) narrowly beats LG-DKGP (76.96%).
**Tools & method (≤3 sentences):** LG-DKGP combines recent and longer-range executed action history via gated attention to predict a neural continuation mean, adds a temporal Gaussian-process residual, and uses CEM search seeded around that mean with a scale derived from expert action increments; a frozen world model scores goal progress during search. Hardware details were in an appendix section not fully retrieved.
**Limitation (≤3 sentences):** The value of history-only versus visually-conditioned proposals is task-dependent (history-only wins on three of five tasks). The prior is tuned for 25-action continuations, with success dropping for goals 30–50 steps ahead across all environments, and the authors note transition-feature MMD and raw GP variance are both weak, task-dependent predictors of planning failure.

# Near-misses
- 2611.17324 · K2V: Generative Keyframing For Physically Plausible Video Generation · no qualifying industry affiliation (University of Cambridge + Toyota Motor Europe; Toyota is automotive, not on the list or clearly comparable; NVIDIA mentioned only as an academic GPU-grant funder, not a co-author affiliation)
- 2611.17160 · XBot-Omni: An Omni-Modal Model for Embodied Understanding and Interaction · no qualifying affiliation (all 13 authors at AGIBOT X-Lab, not on the list and not clearly comparable top-tier) and off-topic: humanoid-robot embodied interaction/dialogue, not character animation or games
- 2611.17142 · FORGE: Force-Aware Multi-Granularity Control for Efficient Humanoid Loco-Manipulation · no qualifying industry affiliation (Shanghai AI Laboratory/Tsinghua/Zhejiang/SJTU/CUHK, all academic) and off-topic: humanoid robot loco-manipulation hardware control, not character animation or games
- 2611.16897 · TokenStream: Multi-Subject Personalized Video Generation with Token-wise LoRA and Guided Attention · qualifying affiliation present (Qualcomm AI Research) but off-topic: general multi-subject video personalization, not 3D/world-model/character-animation/game-engine work
- 2611.16422 · BlinkMimic: Training a Humanoid Motion Tracker in Minutes on a Single GPU · single author, no institutional affiliation given (no qualifying affiliation) and off-topic: pure simulated humanoid-robot locomotion/whole-body control, not character animation or games despite using the LAFAN1 animation dataset as motion source
