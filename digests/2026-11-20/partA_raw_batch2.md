## PRIO: Pre-trained Representation for Interactive Objects in 4D Worlds
- **arXiv:** 2611.25500 · https://arxiv.org/abs/2611.25500
- **Submitted:** 2026-11-19
- **Authors:** Shixun Huang, Lifu Wei, Yue Chang, Chen Geng, Heng Zhang, Jinhyung Ahn, Caoliwen Wang, Siyuan Chen, Donglai Xiang, Jiajun Wu, Peter Yichen Chen
- **Qualifying affiliation(s):** NVIDIA — Donglai Xiang
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PRIO is a pre-trained model that, given an object's static 3D geometry (mesh, point cloud, or 3D Gaussians), predicts an object-specific low-dimensional configuration space in a single forward pass. These coordinates drive Lagrangian-mechanics-based dynamics, so the object's motion follows physical laws and responds to user actions. Because the dynamics are linear in the predicted coordinates, they can be precomputed and simulated at interactive rates without further network inference.
**Purpose (≤3 sentences):** The authors note that reconstructed or generated 3D scenes typically contain only static objects that cannot move or deform realistically, limiting interactivity. PRIO aims to give arbitrary, unseen 3D objects a physically grounded, interactive representation without per-object training. It targets use cases such as real-to-sim transfer and robot manipulation.
**Breakthrough (≤3 sentences):** The authors report that PRIO generalizes to unseen shapes after being pre-trained on diverse 4D trajectories, and that it generates dynamics faster and follows user actions more faithfully than existing 4D generation methods. They demonstrate this across multiple 3D representations (meshes, point clouds, 3D Gaussians).
**Tools & method (≤3 sentences):** The method predicts a per-object configuration space in one forward pass, then simulates motion via Lagrangian mechanics parameterized by those coordinates, precomputing the (linear) dynamics so no further network inference is needed at run time. The authors demonstrate real-to-sim workflows and robot manipulation as applications.
**Limitation (≤3 sentences):** The accessible text does not state explicit limitations beyond what is implied by the method (restricted to the learned configuration-space formulation); none are asserted here beyond what is verifiable.

## SceneAnything: Agentic Reconstruction of Large-Scale Mesh Scenes from a Single Video
- **arXiv:** 2611.25340 · https://arxiv.org/abs/2611.25340
- **Submitted:** 2026-11-19
- **Authors:** Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Zahra Montazeri, Ravi Ramamoorthi, Milos Hasan
- **Qualifying affiliation(s):** NVIDIA — Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Milos Hasan
- **Categories:** cs.CV, cs.GR
- **Open release:** none found (authors state plans to release the harness, agent instructions, libraries, and scenes, but no link is given yet)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SceneAnything is an automated system that reconstructs editable, large-scale mesh scenes from a single real or generated video, and can also support text-to-scene creation when paired with a video generator. A software harness coordinates AI agents, pretrained vision models, and graphics tools, sharing camera, depth, and segmentation estimates to plan the environment and write parameterized Blender programs. On 100 test scenes, the authors report better original-view fidelity than direct-agent reconstruction and higher novel-view similarity than compared video-to-3D methods.
**Purpose (≤3 sentences):** The goal is to turn a single video into an editable, large-scale mesh scene usable in standard 3D/graphics pipelines, rather than an opaque implicit representation. The system also aims to complete unseen regions (marking them as inferred) and select an appropriate level of detail automatically.
**Breakthrough (≤3 sentences):** As the authors report, the agentic pipeline outperforms direct-agent reconstruction on original-view fidelity and outperforms compared video-to-3D baselines on novel-view similarity across 100 scenes. Accepted Blender programs are reused across scenes, which the authors frame as a form of programmatic knowledge accumulation.
**Tools & method (≤3 sentences):** Agents plan the environment using shared camera, depth, and segmentation estimates, then write parameterized Blender programs; revisions are checked both programmatically and visually before acceptance. The system fits lighting and motion and completes occluded/unseen regions, flagging them as inferred.
**Limitation (≤3 sentences):** The accessible text does not state explicit limitations beyond noting that unseen regions are inferred (not directly observed) and marked as such; code/data are not yet released, so independent reproduction is not currently possible.

## VideoRNG: Relightable Neural Gaussians from Generative Video Models
- **arXiv:** 2611.25338 · https://arxiv.org/abs/2611.25338
- **Submitted:** 2026-11-19
- **Authors:** Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Ravi Ramamoorthi, Zahra Montazeri, Miloš Hašan
- **Qualifying affiliation(s):** NVIDIA — Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Zahra Montazeri, Miloš Hašan
- **Categories:** cs.CV, cs.GR
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** VideoRNG creates relightable 3D assets from a text prompt or single image in two stages: a fine-tuned video diffusion model first generates an RGBA turntable video under known pose, camera, and lighting, and a feed-forward reconstruction model then maps latent frames from selected views into millions of anisotropic 3D Gaussians with learned appearance features. A shared directional decoder and a stochastic ray tracer render these "ray-traced Relightable Neural Gaussians" (rtRNG) under novel viewpoints and lighting. The authors report generating fine-structured assets such as fur, feathers, and spider webs that can be interactively rendered, relit, and placed into scenes.
**Purpose (≤3 sentences):** The authors argue that realistic 3D assets, especially those with fine geometry or complex light transport, are hard to express with standard meshes and physically based materials, and that existing Gaussian-splatting generators typically bake in fixed lighting. VideoRNG aims to generate relightable Gaussian-based assets directly from generative video models instead.
**Breakthrough (≤3 sentences):** The authors report that their method can produce assets with fine, hard-to-model structures (fur, feathers, webs) that remain relightable and interactively renderable, which they attribute to the combination of video-diffusion generation with a Gaussian-based relightable representation. They introduce depth-anchored appearance training, foreground token selection, and cost-aware distributed sampling to preserve detail and keep training tractable at scale.
**Tools & method (≤3 sentences):** Stage one fine-tunes a video diffusion model to produce an RGBA turntable video under known pose/camera/lighting; stage two feed-forward reconstructs latent frames from selected views into anisotropic 3D Gaussians with learned appearance features, rendered via a shared directional decoder and a stochastic ray tracer. Training assets are sourced from the TexVerse dataset.
**Limitation (≤3 sentences):** The accessible text does not state an explicit limitations section; no code, weights, or demo release statement was found in the portion of the paper reviewed.

## WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation
- **arXiv:** 2611.25251 · https://arxiv.org/abs/2611.25251
- **Submitted:** 2026-11-18
- **Authors:** Qianzhong Chen, Muyuan Lin, Yuyin Sun, Mac Schwager, Cheng-Hao Kuo, Roberto Martín-Martín
- **Qualifying affiliation(s):** Amazon — listed in the paper's affiliation block; a footnote states "Work done during an internship at Amazon."; FLAG: borderline topic (robotics-focused)
- **Categories:** cs.RO
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** WEVO post-trains a whole-body humanoid vision-language-action (VLA) policy inside an action-conditioned video world model, avoiding unsafe exploration directly on the humanoid robot. Simulated manipulation/locomotion play data first improves the world model's predictions of contact dynamics and viewpoint changes; a VLA trained on synthetic demonstrations then runs 20 autonomous real-robot rollouts per task to align the world model with real deployment observations. The VLA, a whole-body controller, and the video world model together form a closed-loop RL environment with dense progress rewards.
**Purpose (≤3 sentences):** The authors note that reinforcement learning can push VLA policies beyond imitation learning, but exploring directly on a humanoid is unsafe, and RL trained purely in simulation can exploit sim-to-real gaps. WEVO aims to get RL's benefits while avoiding both problems by optimizing policies inside a deployment-aligned video world model.
**Breakthrough (≤3 sentences):** As the authors report, across three real-robot tasks, RL inside the video world model raised mean success from 23.3% (initial) to 75.0%, compared with 48.3% for RL performed directly on the real robot. They also report that play data improved every evaluated world-model metric and downstream policy success.
**Tools & method (≤3 sentences):** The pipeline combines simulation-based play data (for broad coverage and policy initialization), a video world model refined by real-robot rollouts (for deployment alignment), and closed-loop RL with dense progress rewards over the VLA, whole-body controller, and world model jointly. Evaluation uses a real humanoid robot across three manipulation/locomotion tasks.
**Limitation (≤3 sentences):** The accessible text does not state an explicit limitations section beyond the paper's own framing of the problem (unsafe real-world exploration, sim-to-real gap); this is a robotics loco-manipulation paper without a game/3D-content angle.

## Infer3D: Inverse Generative Modeling Enables Robust 3D Reconstruction
- **arXiv:** 2611.25061 · https://arxiv.org/abs/2611.25061
- **Submitted:** 2026-11-18
- **Authors:** Amani Kiruga, Mark Hamilton, Joshua B. Tenenbaum, William T. Freeman, Vincent Sitzmann, Yilun Du, Ayush Tewari
- **Qualifying affiliation(s):** Google DeepMind — Mark Hamilton
- **Categories:** cs.CV, cs.LG, cs.RO
- **Open release:** none found (project website listed: amanikiruga.github.io/infer3d-site; no code/weights release statement found)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Infer3D reframes monocular 3D reconstruction as inverse generative modeling: instead of a feedforward network mapping an image directly to 3D, it searches the latent space of a 2D generative prior (StyleGAN2 or a Diffusion Autoencoder) plus camera/sensor parameters. The search is guided by a frozen 3D "lifting" network (Splatter Image or CATSplat) and a 3D Gaussian Splatting renderer, constraining results to a valid, multi-view-consistent 3D manifold and avoiding degenerate flat outputs. An adaptive inference strategy spends more test-time compute on ambiguous out-of-distribution (OOD) inputs and processes in-distribution inputs efficiently.
**Purpose (≤3 sentences):** The authors motivate the work by noting humans can infer 3D structure even from unfamiliar viewpoints via top-down generative reasoning, whereas state-of-the-art feedforward 3D reconstruction networks degrade on out-of-distribution scenes. Infer3D aims to make monocular 3D reconstruction more robust to OOD viewpoints and object categories.
**Breakthrough (≤3 sentences):** The authors report Infer3D achieves better OOD reconstruction accuracy than feedforward networks trained on equal or larger datasets, with examples including 18.46 dB vs. 15.73 dB PSNR (Splatter Image) on CO3D Hydrants under OOD viewpoint shift, and 20.29 dB vs. 14.30–15.23 dB on ShapeNet Cars under OOD rotation. On real car captures, they report a mean Chamfer Distance of 0.131 versus 0.219 (Splatter Image) and 0.491 (BRFI).
**Tools & method (≤3 sentences):** The method optimizes latents of a frozen 2D generative prior (StyleGAN2/DiffAE) against a frozen 3D lifter and a Gaussian-splatting renderer, and uses initial reconstruction error as an OOD signal to route only suspicious inputs to the costlier optimization loop. Real-world evaluation relies on pseudo-ground-truth masks from Segment Anything 2.
**Limitation (≤3 sentences):** The authors report that optimization alone is less accurate than the feedforward lifter on in-distribution data (by about 0.9–2.7 dB depending on dataset), and that reconstruction sharpness is capped by the generative prior, with lighter backbones (StyleGAN2, DiffAE) missing high-frequency detail. Full optimization takes about 2.8 minutes per sample (about 1.2 minutes with early stopping), and heavier diffusion backbones could improve quality but at higher compute cost.

# Near-misses
- 2611.25134 · GEMS: Generation and Experience Memory for Subgoal-Guided Long-Horizon World Model Planning · no industry-affiliated author ("Meta" lead was a false match on the "Meta-World" benchmark name; verified affiliations are University of Minnesota, Twin Cities and Cisco)
- 2611.24171 · Efficient World-Model Planning via Physics-Guided Search Distillation · off-topic: autonomous-driving trajectory planning (NAVSIM benchmark), not 3D content/world models for games/character animation/game engines; affiliations are Yanshan University, Xiaomi Corporation, KAIST, Tsinghua University, and Beijing Automotive Technology Center Co., Ltd. (Xiaomi borderline, not confirmed top-tier, and topic gate fails regardless)
- 2611.23890 · EVA-RSI: Recursive Self-Improvement of Video Evaluators for Judging Temporal Quality · off-topic: generic video-generation quality evaluator/metric, not specifically tied to 3D content, world models, character animation, or game engines, despite confirmed Roblox affiliation (Yu Yuan, Ruizhou Ding, Shaoheng Fang, Zhuo Chen)
- 2611.23825 · Learning Martial Arts Motion Skills for Animating Opponents in VR Sparring Games · no industry-affiliated author ("Meta" lead was a false match on "Meta Quest," the VR hardware used; verified affiliations are Arizona State University and Rice University)
- 2611.23416 · OCLDA-GS: Object-Centric Local Deformation-Aware Gaussian Streaming · no industry-affiliated author ("Google" lead was a false match on the "Google Immersive" dataset name; verified affiliations are University of Southern Mississippi and University of Utah)
