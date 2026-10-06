## InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation
- **arXiv:** 2610.06850 · https://arxiv.org/abs/2610.06850
- **Submitted:** 2026-10-05
- **Authors:** Yucheng Zhang, Sirui Xu, Jinhong Li, Liuyu Bian, Anatulya Nandi, Derek Zhang, Xiangchen Liu, Xueting Li, Umar Iqbal, Yu-Xiong Wang, Liang-Yan Gui
- **Qualifying affiliation(s):** NVIDIA — Yucheng Zhang, Sirui Xu, Jinhong Li, Liuyu Bian, Anatulya Nandi, Derek Zhang, Xiangchen Liu, Xueting Li, Umar Iqbal, Yu-Xiong Wang, Liang-Yan Gui (all authors listed with dual University of Illinois Urbana-Champaign / NVIDIA affiliation in the paper header)
- **Categories:** cs.RO, cs.CV, cs.GR
- **Open release:** demo/project page (https://sirui-xu.github.io/InterMimicGen) | code — none confirmed
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents InterMimicGen, a framework that retargets motion-captured human-object interaction data to humanoid robots with dexterous hands, trains a physics-based tracking policy in simulation, and uses an iterative "self-evolving" augmentation loop to expand the motion dataset while keeping only variants whose simulated execution completes the task.
**Purpose (≤3 sentences):** Humanoid loco-manipulation research is limited by scarce, diverse, physically executable human-object interaction references; the authors aim to scale usable training data for whole-body dexterous manipulation without manual re-collection.
**Breakthrough (≤3 sentences):** The authors report that the self-evolution loop grows the verified reference library by up to 150.5× by round 5 in a bimanual Inspire-hand setting and 146.4× in grasping scenarios, with retargeting achieving 5.62 cm MPJPE and 83.45% hand-contact preservation, and policies that transfer to physical robot execution.
**Tools & method (≤3 sentences):** The method consolidates human-object interaction mocap datasets (16,059 motions from public datasets), retargets them to a humanoid platform with dexterous hands, and combines physics-based RL tracking in simulation with an iterative perturb-finetune-filter augmentation loop.
**Limitation (≤3 sentences):** The authors state the loop "densifies coverage around each demonstration without creating new task semantics," and that iterative selection may favor easier objects or compound reference errors.

## Real-time Rendering of Pre-integrated Neural Emitters
- **arXiv:** 2610.06762 · https://arxiv.org/abs/2610.06762
- **Submitted:** 2026-10-05
- **Authors:** Arno Coomans, Floor Verhoeven, Edoardo A. Dominici, Markus Steinberger
- **Qualifying affiliation(s):** Huawei Technologies — Floor Verhoeven, Edoardo A. Dominici, Markus Steinberger (FLAG: borderline)
- **Categories:** cs.GR
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces Neural Emission Fields (NEF), a neural field that precomputes direct illumination in the volume around a light emitter, conditioned on position, normal, view direction and material, so that rendering requires only a single network evaluation per shading point instead of runtime integration.
**Purpose (≤3 sentences):** Real-time integration of illumination from complex-shaped, textured or deforming light emitters is computationally expensive; the authors aim to move that integration offline into a reusable, transformable lighting asset.
**Breakthrough (≤3 sentences):** The authors report diffuse NEF evaluation in 1.2 ms and glossy NEF evaluation in 2.5 ms at 1920×1080 on an RTX 4090, inherently handling internal reflections, self-occlusion, spatially-varying emission and mesh deformation "at zero additional runtime cost," with training times from 1 minute (simple planar emitters) to 3 hours (complex interreflections).
**Tools & method (≤3 sentences):** NEF uses a dual-architecture neural network trained in the emitter's local coordinate frame, evaluated on scenes including Sponza, Bistro, Cornell Box and custom emitter geometries (Pierced Sphere, Dragon mesh, Lattice Box, Whiteroom, Living Room) against LTC and ReSTIR DI baselines using FLIP and relative MSE metrics, on an RTX 4090.
**Limitation (≤3 sentences):** The authors state NEF only captures the unoccluded emission field (requiring extra shadow rays for scene occlusion), degrades as surface roughness approaches mirror-like specularity, scales linearly with the number of emitters (N independent NEFs per scene), and requires retraining for arbitrary independent light motion.

## MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion Transformers
- **arXiv:** 2610.06801 · https://arxiv.org/abs/2610.06801
- **Submitted:** 2026-10-05
- **Authors:** Jiarui Chen, Zeqiang Lai, Jiangshan Wang, Ziheng Ouyang, Ye Huang, Xiangyu Yue, Cewu Lu, Chunchao Guo
- **Qualifying affiliation(s):** Tencent (Tencent Hunyuan / "Tencent HY") — Jiarui Chen, Zeqiang Lai, Jiangshan Wang, Ziheng Ouyang
- **Categories:** cs.CV, cs.AI
- **Open release:** demo/project page (https://dodododddo.github.io/mcsparse-project-page/) | code — none confirmed
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper proposes MC-Sparse (Meta-Cached Sparse Attention), a training-free sparse-attention framework for diffusion transformers that combines tile-aligned query grouping, token-level key-value selection, and temporal reuse of selections and residuals across denoising steps.
**Purpose (≤3 sentences):** Existing sparse-attention methods for diffusion transformers degrade generation quality due to token-grouping constraints, inaccurate interaction selection, and lost attention contributions from discarded tokens; the authors aim to close this dense-sparse quality gap without retraining.
**Breakthrough (≤3 sentences):** The authors report a 1.80× denoising speedup on Minimax-H3-Base and a 2.32× speedup on 3D asset generation (an internal model, HY3D-Internal), both with negligible quality loss, validated using PSNR, SSIM, LPIPS, VBench scores, Chamfer distance and volumetric IoU/F1 metrics.
**Tools & method (≤3 sentences):** The method is evaluated on Minimax-H3-Base (768p), HunyuanVideo-13B (720p), Wan2.1 (720p) and HY3D-Internal using Penguin Benchmark and VBench prompt sets (50 samples per task, 345-frame videos), on a single Hopper GPU for most models and 8 Hopper GPUs with Ulysses sequence parallelism for Minimax-H3-Base.
**Limitation (≤3 sentences):** Not stated beyond the three quality-degradation sources (token-grouping constraints, selection inaccuracy, lost discarded-token contributions) that the method is designed to address.

## SteadySplats: Resampling of Low-Variance Gaussians for High-Fidelity Stochastic Rendering
- **arXiv:** 2610.05576 · https://arxiv.org/abs/2610.05576
- **Submitted:** 2026-10-04
- **Authors:** Felix Windisch, Thomas Köhler, Lukas Radl, Chris Wyman, Georgios Kopanas, Bernhard Kerbl, Markus Steinberger
- **Qualifying affiliation(s):** NVIDIA — Chris Wyman; Google DeepMind — Georgios Kopanas
- **Categories:** cs.CV, cs.GR
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper proposes SteadySplats, a method for high-fidelity stochastic order-independent-transparency rendering of 3D Gaussian Splatting scenes, combining a training-time color-variance regularizer with inference-time history-based spatial resampling and temporal resampling for camera-motion coherence.
**Purpose (≤3 sentences):** Stochastic rendering of 3DGS avoids expensive global depth sorting but previously produced high noise at low sample counts; the authors aim to make 1-sample-per-pixel stochastic rendering practical and visually close to sorted 3DGS.
**Breakthrough (≤3 sentences):** The authors report a 13 dB PSNR increase in quality over previous stochastic methods at 1 sample per pixel, with convergence approaching sorted-3DGS rendering quality, evaluated on Mip-NeRF 360 (7 scenes, 21 camera trajectories, 3,152 frames) using PSNR/SSIM/LPIPS and a temporal PSNR metric.
**Tools & method (≤3 sentences):** The approach is built on a custom Vulkan-based renderer and a standard 3DGS optimization pipeline, measured on an RTX 5090 GPU.
**Limitation (≤3 sentences):** The authors state the variance-reducing loss dilutes photometric loss and slightly lowers peak quality for fully converged models, spatial resampling adds buffer-management and neighbor-sampling overhead, and the spatial-reuse transmittance approximation (limited to K prior samples) sacrifices strict unbiasedness for faster convergence.

## FLEX-WAM: Flexible Block-Causal World-Action Models for Long-Horizon Imagination and Planning
- **arXiv:** 2610.05483 · https://arxiv.org/abs/2610.05483
- **Submitted:** 2026-10-04
- **Authors:** R. Khorrambakht, Joseph Amigo, Félix Lebel, Leon Seetoo, Jean Ponce, Zhenzhen Li, Ludovic Righetti
- **Qualifying affiliation(s):** NVIDIA — Zhenzhen Li
- **Categories:** cs.RO, cs.AI
- **Open release:** none confirmed (authors state code/checkpoints "will be released upon acceptance")
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** FLEX-WAM is a flexible block-causal world-action model that predicts action-conditioned futures, generates feasible actions, and supports planning in imagination, while handling variable-length context and stable long multi-step autoregressive rollouts.
**Purpose (≤3 sentences):** Existing world/action models struggle to jointly serve as both policy and outcome predictor over long horizons without losing action responsiveness; the authors address this with gradient balancing and a "Forward-Dynamics elasticity" training mechanism.
**Breakthrough (≤3 sentences):** The authors report stable long-horizon imagination and planning performance across simulated tasks (LIBERO, OGBench 4×4 visual puzzles) and real-robot tasks (PushT, Unitree G1 play data, OpenArm), with training on 8 NVIDIA H100 GPUs for ~150k steps (about 4 days) and inference on up to 4 NVIDIA RTX6000 Pro MaxQ cards.
**Tools & method (≤3 sentences):** The model is evaluated on LIBERO simulation, 4 hours of real-world PushT play data, OGBench visual puzzles, Unitree G1 play data, and OpenArm real-robot counterfactual-detection tasks.
**Limitation (≤3 sentences):** The authors state that executing imagined plans in the real world and using detected mismatches for continual model improvement remain future work; OGBench puzzle success was measured only in imagination (not real-world execution); and text conditioning was excluded because it competes with action information for predicting futures.

## CleanMDM: Clean Motion Diffusion Model for Multimodal Motion Cleanup
- **arXiv:** 2610.05411 · https://arxiv.org/abs/2610.05411
- **Submitted:** 2026-10-04
- **Authors:** Zhe Li, Shicheng Wang, Bowen Cai, Huan Fu
- **Qualifying affiliation(s):** Alibaba — Bowen Cai, Huan Fu
- **Categories:** cs.CV
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** CleanMDM is a unified Clean Motion Diffusion Model that formulates motion-capture cleanup — removing jitter, missing segments, drift and contact artifacts — as masked conditional generation, accepting combinations of noisy 3D motion, sparse 2D/3D keyframes and text as plug-and-play conditions.
**Purpose (≤3 sentences):** Motion capture data typically contains imperfections that require manual animator cleanup; the authors aim to unify cleanup and controllable generation in one multimodal framework instead of treating them as separate tools.
**Breakthrough (≤3 sentences):** The authors report that a Latent Motion Quality Discriminator and Mesh-Aware Contact Projection improve kinematic accuracy and physical realism, with superior performance against baselines (StableMotion, ACMDM, CondMDI, GenMo) on MPJPE, foot-skating ratio, acceleration error, penetration frequency/distance, jitter, FID and diversity, and show text and 2D-keyframe conditions providing effective controllable guidance.
**Tools & method (≤3 sentences):** The model is trained on AMASS and a filtered ~28K-clip subset of MotionLLaMA, evaluated on synthetic corruptions and real-world datasets (IDEA400, HuMMan, KungFu, HAA500), using 22 NVIDIA H20 GPUs (batch size 128, ~16 hours for 600 epochs) for training and 1 NVIDIA V100 for testing.
**Limitation (≤3 sentences):** The authors state evaluation relies on controlled corruption and a simplified ground model during Mesh-Aware Contact Projection, with future work planned on more realistic video-mocap degradations, stronger learned contact priors, and additional control modalities.

## Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation
- **arXiv:** 2610.05608 · https://arxiv.org/abs/2610.05608
- **Submitted:** 2026-10-04
- **Authors:** Team Kandinsky, Julia Agafonova, Bulat Akhmatov, Mikhail Aksyutin, Grigorii Alekseenko, Anastasia Aliaskina, Olga Androsova, Vladimir Arkhipkin, Anna Averchenkova, Alexander Belykh, Serafima Bocharova, Sofiya Bogakovskaya, Anton Bukashkin, Mark Bulygin, Kirill Buzygin, Irina Cheremnykh, Kirill Chernyshev, Mikhail Chernyshov, Vladimir Chernyy, David Chikovani, Georgy Daniltsev, Denis Dimitrov, Anna Dmitrienko, Vladimir Dokholyan, Sergey Emelyanov, Dmitry Ermilov, Georgii Fedorov, Polina Gavrilova, Nikolai Gerasimenko, Aleksandr Gordeev, Andrey Inozemtsev, Andrei Ivaniuta, Alexander Ivanov, Mikhail Karaev, Anastasiia Kargapoltseva, Ivan Kirillov, Nikita Kiselev, Valeria Kobenko, Yury Kolabushin, Denis Koposov, Anatoly Korobov, Vladimir Korviakov, Kirill Kozlov, Denis Krzhivokolskiy, Konstantin Kuklev, Alexander Kunitsyn, Sergey Kuzin, Vladislav Lakhtionov, Alexey Letunovskiy, Maxim Litvinov, Alexander Lyulkov, Georgy Makarov, Kirill Malakhov, Egor Malykh, Mikhail Mamaev, Dmitrii Mikhailov, Polina Mikhailova, Ivan Mikheev, Elizaveta Muromtseva, Nikolai Nazarkin, Tatiana Nikulina, Lev Novitskiy, Stanislav Onuchin, Nikita Osterov, Denis Parkhomenko, Anatoliy Parpara, Vladimir Polovnikov, Konstantin Reznikov, Azat Saginbaev, Nikita Samsonov, Alexander Sentsov, Nikita Shaimov, Artem Sherstyuk, Andrey Shutkin, Egor Silvestrov, Bulat Suleimanov, Matvey Suprunov, Sergey Taranov, Irina Tolstykh, Tatiana Trofimuk, Ilya Trushkin, Aleksandra Tsybina, Olga Varlashina, Viacheslav Vasilev, Ilya Vasiliev, Eugeny Vilisov, Sergey Yakubson, Konstantin Zakharov
- **Qualifying affiliation(s):** Sber (FLAG: borderline) — "Team Kandinsky" contributors are identified in the paper as Sber's Kandinsky Lab, with Cloud.ru (Sber-affiliated cloud infrastructure) also named; individual per-author institution tags were not resolvable from the retrieved text beyond the group-level attribution
- **Categories:** cs.CV, cs.AI, cs.LG, cs.MM
- **Open release:** code (https://github.com/kandinskylab/kandinsky-6) | weights (https://huggingface.co/collections/kandinskylab/kandinsky-60-diffusers) | demo/project page (https://kandinskylab.ai)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Kandinsky 6.0 Video introduces two diffusion foundation models — Lite (3B parameters) and Pro (29B parameters) — for synchronized video and audio generation, producing 5-second clips with synchronized 44 kHz audio including lip-sync across multiple generation modes.
**Purpose (≤3 sentences):** The authors aim to provide an open foundation model family that jointly generates visually and acoustically synchronized video, rather than video and audio as separate, unsynchronized outputs.
**Breakthrough (≤3 sentences):** The authors report that the Pro model outperforms its predecessor and performs competitively against comparable systems, built on a dual-stream CrossDiT architecture connecting a pretrained video stream and a newly trained audio stream via bidirectional cross-attention, trained through pretraining, fine-tuning, reinforcement-learning optimization and distillation stages.
**Tools & method (≤3 sentences):** The model family was developed by Sber's Kandinsky Lab team with infrastructure support from Cloud.ru; the authors release model weights, source code, and a diffusers integration under the MIT license.
**Limitation (≤3 sentences):** Not stated beyond the architecture/training description in the retrieved text.

# Near-misses
- 2610.06594 · VGGT-Bridge: Beyond Sequential Pose Graphs via Coarse-Stride Skip Edges · no industry author (all affiliations academic: Korea Advanced Institute of Science and Technology, KAIST)
- 2610.06472 · MaRO-GS: Mask-Robust Object-Centric Gaussian Splatting from Inconsistent Multi-view Masks · no industry author (all affiliations academic: Kyungpook National University)
- 2610.05739 · HLA-WM: Hybrid Linear Attention for Long-Horizon Video World Models · no industry author (all affiliations academic: Monash University, University of Adelaide, Zhejiang University)
