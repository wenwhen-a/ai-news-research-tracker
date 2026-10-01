## RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement
- **arXiv:** 2609.39045 · https://arxiv.org/abs/2609.39045
- **Submitted:** 2026-09-30
- **Authors:** Wenyi Wu et al. (Wenyi Wu, Minghao Fu, Jieyu You, Kun Zhou, Siqi Liu, Aayush Salvi, Yiheng Lin, Ce Zhang, Xiaohan Lan, Jiahui Zhu, Yujie Zhong, Qi She, Biwei Huang)
- **Qualifying affiliation(s):** ByteDance Inc. — Aayush Salvi, Yiheng Lin
- **Categories:** cs.CL, cs.GT, cs.LG, cs.MA
- **Open release:** code (https://github.com/WenyiWU0111/RSIGame), demo/dataset (https://huggingface.co/spaces/RSIGame/rsigame-page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** RSIGame is a framework for autonomous agentic game development that pairs a local explore-diagnose-improve loop with a global quality-monitoring loop to recursively self-improve LLM-generated games in the Godot and Phaser engines, evaluated on a new GameCraft-Bench benchmark (140 tasks across 15 game families).
**Purpose (≤3 sentences):** It addresses the problem that naive recursive self-improvement of LLM-based game generation converges to fragile, bug-ridden solutions that overfit to limited test cases rather than producing robust, playable games.
**Breakthrough (≤3 sentences):** The authors report that a fine-tuned Qwen3.8-27B model combined with RSIGame reaches a 61.38 overall score on Godot (vs. 37.07 for the unassisted baseline), exceeding one-shot GPT-5.5's 50.26, while reducing generation tokens by up to 1,111x versus baseline; comparable gains (50.24 vs. GPT-5.5's 49.44) are reported on Phaser.
**Tools & method (≤3 sentences):** A local loop (Controller, Explorer, Editor, Verifier) maintains an evolving issue checklist, while a global loop tracks the best checkpoint and detects convergence after 3 consecutive checkpoints without improvement; the base model is further fine-tuned via supervised learning on roughly 2,200 generation, planning, and verified-improvement traces.
**Limitation (≤3 sentences):** The authors state their evaluation rubric (Mechanics, Depth, Visuals, Art) does not fully capture originality, narrative quality, long-term player engagement, or subjective enjoyment, and that experiments targeted "relatively compact games" within practical agent budgets.

## No Corners Cut: State-Grounded Transitions for Mid-Stream Prompt Switches in Video Generation
- **arXiv:** 2609.38691 · https://arxiv.org/abs/2609.38691
- **Submitted:** 2026-09-30
- **Authors:** Zejing Rao, Ketong Ren, Xiaoqiang Liu, Yiping Meng, Guoxin Zhang, Fan Tang
- **Qualifying affiliation(s):** Kuaishou (Kling AI) — Xiaoqiang Liu, Yiping Meng, Guoxin Zhang
- **Categories:** cs.CV
- **Open release:** none found (no code/weights/demo link in the paper)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper proposes a training-free VLM planner plus a distillation technique (SpanDMD) to prevent "corner cutting" — implausible shortcuts — when streaming video generators must respond to mid-stream prompt switches, evaluated on a new OpenTrans-360 benchmark of 1,800 prompt switches.
**Purpose (≤3 sentences):** It addresses the problem that existing streaming video generation systems keep visual smoothness during prompt changes but produce semantically incoherent transitions, such as object duplication, invalid physical interactions, or abrupt state jumps.
**Breakthrough (≤3 sentences):** The authors report an overall score of 0.887 on OpenTrans-360 versus 0.866 for the strongest baseline, ranking first on all 8 transition metrics, and a user-study preference rate above 50% against all 12 baselines tested.
**Tools & method (≤3 sentences):** State-Grounded Segue Planning uses a VLM (JoyAI-VL-Interaction) to generate intermediate "segue prompts" through a Transition Dependency Schema (Terminate, Release, Align, Entry roles); SpanDMD distills a frozen Wan2.1-T2V-14B teacher into a Wan2.1-T2V-1.3B student while restricting each prompt's gradient contribution to its assigned temporal span.
**Limitation (≤3 sentences):** The authors state the method lacks explicit modeling of physical prerequisites (e.g., support conditions), relies only on the single latest frame which limits motion history, and that there is a training-inference gap because planner training data is text-only while inference is visually grounded.

## EPIC: Epipolar-Consistent 360° Immersive Stereo Video Generation
- **arXiv:** 2609.38689 · https://arxiv.org/abs/2609.38689
- **Submitted:** 2026-09-30
- **Authors:** Debabrata Mandal, Dongdong Fu, Jonathon Miller, William Villareal, Xi Peng, Praneeth Chakravarthula
- **Qualifying affiliation(s):** Dolby Laboratories — Dongdong Fu, Jonathon Miller, William Villareal; FLAG: borderline (Dolby is not on the tracker's explicit company list but is a comparable top-tier industry research lab directly relevant to this paper's immersive-media topic). Note: the arXiv HTML render also contained anomalous placeholder entries not present on the abs page (including a spurious "Microsoft Research" affiliation attached to an implausible name); these do not match the verified author list from arxiv.org/abs/2609.38689 and were disregarded as unreliable/likely-injected content, so "Microsoft" as the original lead is NOT substantiated.
- **Categories:** cs.CV, cs.HC
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** EPIC is a three-stage pipeline — training-free stereo generation via spherical depth warping and diffusion inpainting, preference optimization using a new Panoramic Epipolar Geometry Score (PEGS), and a viewing-refinement stage with 4K upsampling — for generating geometrically consistent 360° stereoscopic video.
**Purpose (≤3 sentences):** It addresses the lack of geometric consistency in current video generation models, which handle panoramic and stereo generation separately, producing stereo and temporal artifacts the authors say are highly disruptive for headset viewing.
**Breakthrough (≤3 sentences):** The authors report that DPO refinement using their PEGS metric reduces stereo inconsistency from 3.121 to 2.640 milliradians, and that their method yields a 2.6% inconsistent-correspondence rate versus 8.2% for the DissolveStereo baseline.
**Tools & method (≤3 sentences):** Spherical depth warping with diffusion inpainting produces training-free stereo views; PEGS, a pose-free metric scoring epipolar constraint violations on the viewing sphere, drives rank-64 LoRA preference optimization (Adam, lr 5e-6) on a frozen Wan2.1-1.3B backbone with a PanoWan adapter.
**Limitation (≤3 sentences):** The authors state the method's rigid-scene assumption prevents scoring dynamic content without discarding moving objects, and that combining stereo and temporal consistency ("diagonal axis") showed no improvement, which they identify as remaining headroom.

## Eulerian Motion Reconstruction for Water Scenery
- **arXiv:** 2609.38622 · https://arxiv.org/abs/2609.38622
- **Submitted:** 2026-09-29
- **Authors:** Chuhan Chen et al. (Chuhan Chen, Yen-Chi Cheng, Ayush Saraf, Rajvi Shah, Tuotuo Li, Johannes Kopf, Chen Gao, Hung-Yu Tseng, Deva Ramanan, Matthew O'Toole, Changil Kim)
- **Qualifying affiliation(s):** Meta — Ayush Saraf, Rajvi Shah, Tuotuo Li, Johannes Kopf, Chen Gao, Hung-Yu Tseng, Changil Kim
- **Categories:** cs.CV
- **Open release:** demo (project page: sally-chen.github.io/eulersplats/); no code or weights found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper reconstructs a loopable 4D representation of water scenes from monocular video by combining canonical 3D Gaussian splats, a static 3D Eulerian velocity field, and a time-varying residual deformation field, with Gaussians advected via forward Euler integration and cyclically reborn with staggered start times.
**Purpose (≤3 sentences):** It addresses the gap that existing 4D reconstruction methods assume persistent objects and struggle with water, where particles continuously flow in and out of view rather than persisting across frames.
**Breakthrough (≤3 sentences):** The authors report PSNR 23.05 / SSIM 0.716 / LPIPS 0.315 on a 7-scene custom water-capture benchmark, outperforming baselines (AmbGS, 4DGS, MoSca, MoVieS) on FID/KID/FVD, and state their method was preferred in 97.6% of user-study judgments.
**Tools & method (≤3 sentences):** The system is initialized from optical flow and jointly optimized with rendering losses; a separate inference-time propagation algorithm is reported to run 3-4x faster than training-time propagation; training used 8 NVIDIA A6000 GPUs for about 8 hours per scene on a custom 7-scene, ~5,250-frame water capture dataset.
**Limitation (≤3 sentences):** The authors state the method fails on large water surfaces with reflections (lakes, rivers, oceans), that the static Eulerian field cannot represent time-varying stochastic motion, and that it requires accurate depth initialization from static reconstruction.

# Near-misses
- 2609.39235 · The Planning Limits of Latent World Models · no qualifying industry co-author (all authors University of Melbourne; "Meta" lead appears to stem from the paper's use of Meta's V-JEPA 2 model, not author affiliation)
- 2609.39195 · Uruqi: Learning Spatial Cognition from Visual Experience · no qualifying industry co-author (all authors Beijing University of Posts and Telecommunications / Tsinghua University, purely academic)
- 2609.39101 · Beyond Prediction: Steering VLM Agents with Retrospective World Modeling · affiliation unverifiable (no HTML version — https://arxiv.org/html/2609.39101 and /v1 both return 404)
- 2609.38978 · PARK: Accurate Block Retrieval for Sparse Attention in Video Diffusion Transformers · no qualifying industry co-author (all 5 authors South China University of Technology; no Tencent affiliation found)
- 2609.38285 · GaugeVLM: Structuring Spatial Supervision with Measured Geometric Interventions · no qualifying industry co-author (authors from CASIA/UCAS, National University of Singapore, CUHK; no ByteDance affiliation found)
