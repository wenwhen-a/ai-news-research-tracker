## OneLA: Learning Many Worlds from Latent Actions
- **arXiv:** 2610.20160 · https://arxiv.org/abs/2610.20160
- **Submitted:** 2026-10-14
- **Authors:** Ziyu Zhu, Zhaoxu Sun, Fan Jiang, Chiyu Wang, Junfeng Ni, Mu Xu
- **Qualifying affiliation(s):** Alibaba Group — Ziyu Zhu, Zhaoxu Sun, Fan Jiang, Chiyu Wang, Mu Xu (all AMAP, Alibaba Group); Junfeng Ni (AMAP, Alibaba Group, with internship work also credited to Tsinghua University)
- **Categories:** cs.CV
- **Open release:** none stated on the abstract/HTML page
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** OneLA learns continuous latent actions from unlabeled videos spanning games, navigation, driving, and robotics, using a shared orthonormal motion dictionary and a single predictive objective rather than task-specific designs or cross-domain alignment losses. The latent actions act as a shared control interface for world models, with lightweight adapters mapping native control commands into that space. A shared Wan2.2-TI2V-5B diffusion transformer is trained to jointly predict video and latent actions.
**Purpose (≤3 sentences):** The authors motivate the work by noting that "learning shared latent actions across domains remains challenging," since prior latent-action methods tend to require domain-specific alignment tricks. OneLA aims to provide one latent-action space usable across many different "worlds" (games, navigation, driving, robotics) to control world models generically.
**Breakthrough (≤3 sentences):** The authors report a 24.8% reduction in action cycle-transfer rotation error (and 15.5% for translation) over the strongest baseline (OLaF), and a 20.5% improvement in Human Preference Score v3 (HPSv3) for real-scene generation in a joint-training comparison. They also report linear-probe macro-F1 improvements of 5.30 points on a Game benchmark and 5.63 points on AgiBot over OLaF, plus the highest nuScenes PSNR (16.13) and SSIM (0.625) among evaluated methods.
**Tools & method (≤3 sentences):** The method uses an orthonormal motion dictionary built via QR factorization, combined with KL and sparsity regularization and a reconstruction objective, to learn domain-general latent actions from video. Lightweight MLP adapters map native control signals (game inputs, navigation commands, driving controls, robot actions) into this shared latent space. Evaluation spans Game, AgiBot, MIND (cross-view), and nuScenes benchmarks.
**Limitation (≤3 sentences):** No explicit limitations section was surfaced in the fetched content; the paper is an empirical benchmark/method paper and the reported gains are relative to specific baselines (e.g., OLaF) rather than absolute task success in deployed systems.

## What Matters for World Modeling in Vision-Language-Action Models?
- **arXiv:** 2610.19825 · https://arxiv.org/abs/2610.19825
- **Submitted:** 2026-10-14
- **Authors:** Qisen Ma, Yixiang Chen, Yuan Xu, Peiyan Li, Jiabing Yang, Kai Wang, Jianhua Yang, Jianlou Si, Jun Huang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang
- **Qualifying affiliation(s):** Alibaba Group — Jianlou Si, Jun Huang
- **Categories:** cs.RO (primary), cross-listed cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** This is a controlled empirical study of how to integrate world models into Vision-Language-Action (VLA) robot policies so they predict future dynamics instead of only mapping observations to actions. The authors group prior approaches into four paradigms (Implicit Future Alignment, Explicit Future Query, MoT Future Expert, External World Predictor), implement each in one unified framework, and test several frozen world-representation encoders (DINOv3, SigLIP, ImageVAE, WanVAE, VGGT, V-JEPA 2.1) on two policy backbones. Evaluation covers in-domain, out-of-domain, long-horizon, dynamic, few-shot, and real-world robot settings.
**Purpose (≤3 sentences):** Prior work conflates world representation choice, integration strategy, and policy backbone, making it unclear which design choices actually matter for world modeling in VLAs. The paper isolates these factors to give practical guidance on building world-model-augmented robot policies.
**Breakthrough (≤3 sentences):** The authors report that 2D semantic representations give consistent gains across paradigms, that no single paradigm wins everywhere though the decoupled MoT Future Expert is competitive overall (especially out-of-domain), and that world modeling outperforms action-only baselines, with the largest gains on long-horizon and dynamic tasks. On LIBERO-Plus (OOD), WM-MoT raises the average from a 71.8% baseline to 76.2%; on real-world tasks, all world-modeling paradigms raise the 45.0% baseline average to 56.3–73.8%.
**Tools & method (≤3 sentences):** The unified framework evaluates world-model paradigms on Qwen3-VL-2B with a cross-DiT action expert and on π0.5, using benchmarks including LIBERO, LIBERO-Plus, RoboTwin 2.0, DOMINO, and four real-world robot tasks. Frozen encoders (DINOv3, SigLIP, ImageVAE, WanVAE, VGGT, V-JEPA 2.1) supply the world representations compared across paradigms.
**Limitation (≤3 sentences):** The study reports that gains are paradigm- and setting-dependent (e.g., WM-Align improves in-domain LIBERO but drops performance on π0.5/RoboTwin's Clean2Random setting from 46.4% to 41.0%), indicating no universally best configuration. No other explicit limitations were surfaced in the fetched content.

## StateCraft: Augmenting Video World Models with Abstract-State Reasoning
- **arXiv:** 2610.19795 · https://arxiv.org/abs/2610.19795
- **Submitted:** 2026-10-14
- **Authors:** Lorenzo Venturoli, Nedko Savov, Xi Wang, Marc Pollefeys, Luc Van Gool
- **Qualifying affiliation(s):** Microsoft — listed among the paper's affiliations (INSAIT/Sofia University, ETH Zurich, University of Ulm, TUM MCML, Microsoft); the HTML page does not print an explicit per-author marker mapping, but Microsoft appears in the affiliation block for this author list
- **Categories:** cs.CV (primary); cs.AI; cs.LG
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** StateCraft decouples a persistent, updatable "abstract state" from the visual state in a video world model, so that actions can change parts of the world that are not currently visible on screen. It pairs a language model (which predicts state transitions and updates a graph of views/elements) with a video diffusion model that renders frames conditioned on that predicted state. The authors also build an automated data collection pipeline and a benchmark covering generation quality, memory, and controllability.
**Purpose (≤3 sentences):** Standard video world models struggle to track changes to parts of a scene that fall outside the current camera view, since they condition only on visible history. StateCraft aims to give video world models a persistent, editable internal state so off-screen changes are remembered and reflected correctly when revisited.
**Breakthrough (≤3 sentences):** The authors report revisit self-consistency staying near 0.9 SSIM over up to 512 actions versus about 0.5–0.6 for baselines, and a 10.29 dB PSNR gain from state conditioning on their CF++ backbone. They also report direct state edits are followed in 81% of cases (98% for category changes on re-entry), and a proof-of-concept 3D experiment (changing lighting in an unobserved room) reaches 0.864 illumination-classification AUC versus 0.542 without state conditioning.
**Tools & method (≤3 sentences):** A vision-language model predicts state transitions from incoming actions and updates a graph of views and elements; a video diffusion model generates frames conditioned on this predicted state, the action, and visual history. Probes trained on the video model's activations decide when the language model needs to refresh the state, letting the gate skip 40.8% of language-model calls at a 0.57 dB PSNR cost.
**Limitation (≤3 sentences):** The authors report that inserting new elements onto an empty background is markedly weaker (48% success) than other controllability edits (up to 98%). The 3D extension is explicitly described as only a "proof-of-concept" limited to a lighting-change scenario in a single room.

## Holi-Spatial 360: Generative Reconstruction from Sparse Panoramas for Spatial Rendering and Intelligence
- **arXiv:** 2610.19502 · https://arxiv.org/abs/2610.19502
- **Submitted:** 2026-10-14
- **Authors:** Yuanyuan Gao, Zhirui Liu, Yuning Gong, Yifei Liu, Yifan Zhan, Kuixuan Jiao, Xiaolong Zhou, Yifan Yang, Hongjie Zhang, Xue Yang, Dan Xu, Zhihang Zhong
- **Qualifying affiliation(s):** Tencent — Yuning Gong
- **Categories:** cs.CV
- **Open release:** none stated (a dataset/benchmark, Holi360, is introduced but no explicit release link was found on the page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Holi-Spatial 360 turns sparse real-estate panoramas of multi-room homes into annotated, photorealistic 3D environments, addressing the shortage of large-scale, semantically labeled indoor 3D data that typically requires costly LiDAR capture. It builds a 3D Gaussian Splatting (3DGS) representation via correspondence-guided geometric optimization, then uses image and video generative priors to restore appearance and complete camera trajectories. An automated pipeline combining 3D grounding with VLM-based verification produces the resulting Holi360 dataset and a spatial-understanding benchmark.
**Purpose (≤3 sentences):** Existing indoor 3D datasets are mostly room-scale and depend on expensive LiDAR scanning, limiting data available for training spatially aware vision-language models. The authors aim to generate large-scale, multi-room, annotated 3DGS scenes directly from cheap, sparse panorama photos instead.
**Breakthrough (≤3 sentences):** The authors report the Holi360 dataset contains over 1K multi-room 3DGS scenes, more than 100K instance annotations, and 2M spatial question-answer pairs. They report novel-view synthesis PSNR of 22.58 versus 19.68 for plain 3DGS, geometry F@2cm of 0.2617 versus 0.2207 for DA3, and that fine-tuning Qwen3.5-4B on Holi360 raises spatial classification macro accuracy from 46.77% to 85.25% while cutting numerical MAE from 0.9767 m to 0.3898 m.
**Tools & method (≤3 sentences):** A frozen feed-forward reconstruction model supplies cross-view correspondences that anchor the initial 3DGS optimization from sparse panoramas; fine-tuned image and video generative models fill in missing views along completed camera trajectories, distilled back into the scene. A VLM plus a "Boxer" model produce verified 3D object instances, grounding labels, and spatial QA pairs for the released benchmark.
**Limitation (≤3 sentences):** No explicit limitations section was surfaced in the fetched content; the method still depends on generative priors to "hallucinate" unseen appearance/geometry from sparse panorama inputs, which is an inherent approximation rather than ground-truth capture.

# Near-misses
- 2610.20609 · SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving · no industry co-author — all academic (UC Irvine, UC San Diego, University of Cincinnati, National University of Singapore); on-topic (driving world model) but fails the affiliation gate.
- 2610.20579 · PingpongDuo: Agile Humanoid Table Tennis Doubles with Safe Team Coordination · off-topic: this is humanoid-robot sim-to-real motor control/team coordination (table tennis), not a learned world model, 3D-content, character-animation, or game-engine paper, despite one author (Jingbo Wang) being NVIDIA-affiliated and other authors from The University of Hong Kong, Shanghai Innovation Institute, and Archon Robotics.
- 2610.20571 · Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation · no industry co-author — all academic (Zhejiang University, Monash University, BAIR/UC Berkeley, Adelaide University).
- 2610.20089 · When Pairwise Preferences Cycle: A Reliability-Anchored Preference Walk for Video GRPO · off-topic: this is a preference-aggregation/RL-training method for video generation models (addressing cyclic pairwise preferences in GRPO), not a 3D, world-model, animation, or game-engine paper; affiliations are University of Science and Technology of China and Huawei Noah's Ark Lab (FLAG: borderline — Huawei, but dropped on topic grounds).
- 2610.19623 · MagicGarment: Benchmarking Single-Image Standalone 3D Garment Reconstruction · no industry co-author — all academic (Wuhan Textile University, McGill University).
- 2610.19519 · Revisiting Triplet Contrastive Learning for 3D Shape Understanding · no industry co-author — all academic/research-institute (Xiamen University, Shanghai AI Lab); Shanghai AI Lab is a research institute, not an industry company on or comparable to the qualifying list.
