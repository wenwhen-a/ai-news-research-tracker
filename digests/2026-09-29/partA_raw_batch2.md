## Adaptive Latent Capacity for World Models
- **arXiv:** 2609.32921 · https://arxiv.org/abs/2609.32921
- **Submitted:** 2026-09-26
- **Authors:** Idan Achituve, Lior Dikstein, Idit Diamant, Arnon Netzer, Hai Victor Habi
- **Qualifying affiliation(s):** Arm Research, Israel (all authors); FLAG: borderline
- **Categories:** cs.LG
- **Open release:** none (no code/weights link found; only the arXiv listing itself)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents Adaptive LeWorldModel (ALeWM), a JEPA-based world model that learns to concentrate predictive information into compact prefixes of a wide latent space rather than using a fixed-width embedding. A new regularizer, MixSIGReg, biases variance toward earlier coordinate blocks so that a short prefix can still carry most of the useful signal for planning.
**Purpose (≤3 sentences):** Standard latent world models must choose between narrow embeddings (limited expressivity) and wide embeddings (costly, harder-to-plan-over) that spread information uniformly across coordinates. The authors want a representation that stays wide and expressive but lets planning operate on a much shorter, adaptively-sized prefix.
**Breakthrough (≤3 sentences):** The authors report that ALeWM "consistently achieves higher mean success rates than tuned fixed-width LeWM, with lower planning capacity on average," citing success-rate gains alongside an average 56% reduction in planning capacity across their benchmarks.
**Tools & method (≤3 sentences):** ALeWM combines a learned capacity network (predicting sequence-conditioned prefix-length distributions), the MixSIGReg regularizer, and a nested predictor trained with a straight-through Gumbel-Softmax estimator; it is evaluated on a synthetic damped-oscillator toy task and on TwoRoom, PushT, Reacher, and OGBench-Cube visual-control benchmarks using ViT-Tiny/ViT-Small encoders.
**Limitation (≤3 sentences):** The authors note the capacity network's behavior varies with initialization and random seed, the MixSIGReg prior depends on an arbitrary polynomial-degree choice, the Gumbel-Softmax gradient estimator is biased, and mixed-dataset training shows performance degradation.

## ProDyGS: Dynamic Gaussian Splatting from a Single Static Monocular Camera
- **arXiv:** 2609.32711 · https://arxiv.org/abs/2609.32711
- **Submitted:** 2026-09-26
- **Authors:** Ugo Leone Cavalcanti, Fabio Tosi, Matteo Poggi, Andrea Conti, Vladimir Zlokolica, Valerio Cambareri, Stefano Mattoccia
- **Qualifying affiliation(s):** Sony (Sony Depthsensing Solutions, Brussels) — Andrea Conti, Vladimir Zlokolica, Valerio Cambareri
- **Categories:** cs.CV
- **Open release:** none confirmed (project page only: https://prodygs.github.io; no code/weights link stated)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ProDyGS reconstructs dynamic 3D Gaussian Splatting scenes from video captured by a single static (non-moving) monocular camera, a setting where prior dynamic-view-synthesis methods fail due to a complete absence of multi-view geometric cues. It synthesizes proxy multi-view supervision from monocular depth to make this possible.
**Purpose (≤3 sentences):** Dynamic view synthesis normally needs multi-camera rigs or significant camera motion to supply the geometric constraints needed for reconstruction. The authors target the harder case of footage from one fixed camera, where "the complete absence of multi-view geometry guidance causes existing DVS frameworks to fail."
**Breakthrough (≤3 sentences):** The authors report state-of-the-art results on the DyNeRF benchmark using only monocular depth as external supervision, with reported average metrics of PSNR 26.64 / SSIM 0.8806 / LPIPS 0.1110 versus the prior best (MoDGS) at PSNR 22.64 / SSIM 0.8042 / LPIPS 0.1545.
**Tools & method (≤3 sentences):** The pipeline uses Depth Pro for initial depth estimation plus neural refinement and optical-flow-based temporal consistency, generates synthetic proxy viewpoints via lightweight 3D Gaussian Splatting, and trains a spatio-temporal HexPlane deformation network to warp canonical Gaussians; it is trained and evaluated on the DyNeRF dataset (6 scenes, 18-20 synchronized cameras) plus the Light Field Video dataset, on a single NVIDIA RTX 5090 GPU (~3 hours, 40k steps).
**Limitation (≤3 sentences):** The paper does not explicitly enumerate limitations in the fetched text; the evaluation protocol depends on COLMAP pose alignment for benchmarking, and overall quality is tied to the reliability of the monocular depth estimator used.

## HapticWorld: an Interactive World Simulator with Real-time Torque Feedback
- **arXiv:** 2609.31924 · https://arxiv.org/abs/2609.31924
- **Submitted:** 2026-09-25
- **Authors:** Shaoting Peng, Litian Liang, Yixuan Wang, Ming Yang, Katherine Driggs-Campbell, Mark Cutkosky, James Jingxi Xu
- **Qualifying affiliation(s):** NVIDIA — Yixuan Wang
- **Categories:** cs.RO
- **Open release:** none confirmed (project page only: https://haptic-world.github.io/; no code/weights link stated)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** HapticWorld extends a learned interactive video-based world simulator with a lightweight torque-prediction head so that an operator collecting robot manipulation demonstrations gets real-time force/torque feedback during teleoperation, not just visuals. Policies trained on the simulator's synthetic demonstrations approach real-robot-data performance.
**Purpose (≤3 sentences):** Contact-rich manipulation needs force sensing that vision alone cannot supply, but real-robot force data collection is hardware-bound, physics simulators mis-model contact forces, and prior learned world simulators are vision-only. The authors want a world model that predicts and renders torque feedback in real time to make synthetic data collection more efficient and realistic.
**Breakthrough (≤3 sentences):** The authors report a 1.6x average improvement in data-collection throughput with haptic feedback, torque-prediction RMSE of 0.26-0.38 N·m (3.5-4.8% normalized error), and real-world policy success of 54/60 trials — close to the 56/60 real-data upper bound and far above the 19/60 vision-only baseline.
**Tools & method (≤3 sentences):** A torque-prediction head (181K parameters, 0.5% of model size) reads intermediate features from an action-conditioned consistency-model visual backbone (built on the "Interactive World Simulator") and is jointly trained with the visual dynamics loss; data collection used bilateral teleoperation via an OpenArm 1 leader device across three tasks (microwave opening, whiteboard wiping, box pivoting), with training on 8 NVIDIA A100 GPUs over ~2 days and policies trained with ACT (Action Chunking with Transformers).
**Limitation (≤3 sentences):** The authors state the system only handles slow, smooth interactions — fast events like impacts or slips are not crisply predicted/rendered at the 10 Hz rendering rate — and it requires fresh per-task play data plus its haptic fidelity depends entirely on the accuracy of the learned visual dynamics model.

## MVAgent: Multi-Agent Video Generation via Consistent Condition Construction and Shot-Level Policy Optimization
- **arXiv:** 2609.30609 · https://arxiv.org/abs/2609.30609
- **Submitted:** 2026-09-24
- **Authors:** Xiangyu Kong, Wenjie Zhou, Fengping Tian, Lihua Fang, Haoqin Sun, Chenyang Lyu, Longyue Wang, Weihua Luo
- **Qualifying affiliation(s):** Alibaba Group — Wenjie Zhou, Fengping Tian, Lihua Fang, Haoqin Sun, Chenyang Lyu, Longyue Wang, Weihua Luo
- **Categories:** cs.CV
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** MVAgent is a multi-agent pipeline for generating multi-shot videos that keep characters, spatial layout, and camera angles consistent across shots, built on top of a frozen video generator. It uses typed conditioning agents plus a new shot-level reinforcement-learning algorithm to optimize output quality.
**Purpose (≤3 sentences):** When each shot is a separate call to a frozen text-to-video generator, "repeated text does not determine appearance, layout or state," so multi-shot narratives lose character and scene consistency. The authors want to recast cross-shot consistency as a condition-construction problem rather than requiring a new generator.
**Breakthrough (≤3 sentences):** The authors report the highest cross-shot Global Consistency score among compared methods (0.5689 vs. 0.5571 for ViMax) and a 61.39% human preference win rate on cross-scene consistency against ViMax, on their new ViMax-Bench benchmark, with an average narrative-quality score of 4.19/5.0.
**Tools & method (≤3 sentences):** The pipeline chains a Spatial Grounding agent (camera-view anchoring from traversal clips), an Observer and Transition agent (continuity memory of shot endings), and an Orchestrator that composes conditions for the frozen generator, optimized with a new "Trunk-GDPO" reinforcement-learning algorithm that compares shot-level rather than episode-level candidates; experiments use Veo 3.1 as the generator, Gemini 3 Pro as VLM, and GPT-5.4/Qwen3-32B as LLMs, evaluated on ViMax-Bench (35 stories) and NarrativeQA (50 novels).
**Limitation (≤3 sentences):** The authors report their lowest score is on the faithfulness metric (2.64/5.0), attributed to a lack of novel retrieval, and note that performance margins over ablated variants shrink as more conditioning components are added, suggesting diminishing returns.

## TrackEverything: Long Horizon Dense Tracking via De-Duplicating 3D Scene Representations
- **arXiv:** 2609.30222 · https://arxiv.org/abs/2609.30222
- **Submitted:** 2026-09-24
- **Authors:** Ayush Jain, Sreeharsha Paruchuri, Ishita Gupta, Fan Zhang, Tanner Schmidt, Jakob Engel, Katerina Fragkiadaki, Adam W. Harley
- **Qualifying affiliation(s):** Meta — Fan Zhang, Tanner Schmidt, Jakob Engel, Adam W. Harley
- **Categories:** cs.CV, cs.AI, cs.RO
- **Open release:** none confirmed (project page only: https://trackeverything.github.io/; no code/weights link stated)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** TrackEverything is a 3D point tracker that represents video as persistent 3D scene tracks in world coordinates so that tracking cost is decoupled from video length, letting it track all visible points across full videos rather than only sparse query points or short clips. It claims to be the first 3D tracker able to track all visible points across videos over 1000 frames within 40 GB of GPU memory.
**Purpose (≤3 sentences):** Existing point trackers force a tradeoff: track sparse query points over long videos, or track dense points only in short clips, because dense long-horizon tracking is memory-prohibitive. The authors want a method that tracks all visible points over arbitrarily long videos within fixed memory.
**Breakthrough (≤3 sentences):** The authors report their method is "the first 3D tracker capable of tracking all visible points across videos exceeding 1000 frames within 40 GB of GPU memory," outperforms open-source all-frame dense 3D trackers "by more than 20% APD" on short clips, and remains competitive with sparse trackers on long sequences despite tracking orders of magnitude more points.
**Tools & method (≤3 sentences):** The method combines voxelization-based de-duplication (merging co-located tracks at sliding-window boundaries), an endpoint-then-trajectory decomposition (endpoint refiner plus a trajectory refiner limited to dynamic points), and "3D WAFT," a 3D extension of warp-aligned feature transforms replacing costly 4D correlation volumes; it is trained on Kubric, PointOdyssey, and Dynamic Replica and evaluated on TAPVid-3D, PointOdyssey, and Dynamic Replica, using 8 L40S-46GB GPUs for training and a single L40S for inference.
**Limitation (≤3 sentences):** The authors note memory still grows during perpetual exploration requiring a spatial cache eviction strategy for hour-long trajectories, the method relies on external geometry (pointmap quality), voxelization via mean-pooling can permanently and irreversibly merge distinct surfaces, and broader pretraining data or larger models could further improve real-world dynamics handling.

## WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation
- **arXiv:** 2609.30221 · https://arxiv.org/abs/2609.30221
- **Submitted:** 2026-09-24
- **Authors:** Yubo Zhu, Yawen Shao, Ziyun Dai, Zixun Fang, Kai Zhu, Siyang Sun, Haolan Xue, Chuxin Wang, Tingyu Weng, Jingming Luo, Chen Shi, Lianghua Huang, Yufeng Ai, Yuzheng Wang, Wenyuan Zhang, Yu Shang, Yuxiang Bao, Zoubin Bi, Jie Xiao, Jinbo Xing, Jiaxing Zhao, Chongyang Zhong, Hengjian Chen, Chenwei Xie, Akide Liu, Zhehan Kan, Yu Liu, Wei Zhai, Sheng Zhong, Wei Tong
- **Qualifying affiliation(s):** Alibaba Group (Wan Team) — multiple co-authors
- **Categories:** cs.CV
- **Open release:** none confirmed (project page only: https://wan-pe.github.io/; no code/weights link stated)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** WanPE is a large (reported ~397B-parameter) prompt-enhancement model that plans cinematic elements — actions, camera trajectories, lighting, and sound — for text-to-video generation, rather than just elaborating captions descriptively. It is trained on 1.05 million real videos and evaluated with a new benchmark, WanPEval.
**Purpose (≤3 sentences):** As text-to-video generators now handle multi-shot, tens-of-seconds outputs, prompt enhancement needs to orchestrate cinematic planning (shots, camera moves, audio) rather than merely add descriptive detail, while still preserving the user's original request throughout the sequence.
**Breakthrough (≤3 sentences):** The authors report their video-grounded reverse-construction supervision beats forward rewriting by 10.37 points, their Semantic-Consistency GRPO (SC-GRPO) improves semantic consistency by 18.6-23.3 points across model scales, and enhanced prompts improve human preference by 50.86 points over raw prompts at 30-second generation lengths.
**Tools & method (≤3 sentences):** The approach derives supervision by reverse-constructing user requests (via LLM) from cinematic conditions mined from 1.05M real videos, then applies SC-GRPO, a nine-dimensional reward function penalizing omissions, alterations, incorrect bindings, and temporal inconsistencies; training used 512 GPUs, and evaluation used the new WanPEval benchmark (249 requests, ~11K expert pairwise assessments from 60 film professionals).
**Limitation (≤3 sentences):** The authors note WanPEval is relatively small (249 requests) for comprehensive benchmarking, transferability depends on adapting output format to the downstream generator, and SC-GRPO's reliance on LLM-based reward evaluation introduces potential assessment bias.

## Latent evolving World Action Model
- **arXiv:** 2609.27455 · https://arxiv.org/abs/2609.27455
- **Submitted:** 2026-09-23
- **Authors:** Xueji Fang, Boqiang Duan, Hua Wu, Jingdong Wang, Guo-Jun Qi
- **Qualifying affiliation(s):** Baidu Inc. — Hua Wu
- **Categories:** cs.CV, cs.RO
- **Open release:** code (https://github.com/XuejiFang/LeWAM) | weights (https://huggingface.co/XuejiFang/LeWAM)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces LeWAM, a World Action Model that replaces large video-diffusion backbones with JEPA-derived predictive embeddings for robot action generation, arguing these support action generation better than compressed VAE latents. It adds an offline preference-refinement stage, DemoDPO, that derives preference supervision directly from demonstrations.
**Purpose (≤3 sentences):** Existing World Action Models built on video-diffusion latents (VAE-compressed) are inefficient and poorly suited to direct action generation, while imitation learning alone cannot distinguish subtly superior from inferior actions even though small deviations cause task failures.
**Breakthrough (≤3 sentences):** The authors report that with only 0.4B trainable parameters, LeWAM achieves a 92.28% average success rate on the RoboTwin 2.0 benchmark, that DemoDPO raises success from 90.69% to 92.28%, and that frozen I-JEPA-Huge embeddings outperform V-JEPA2-Huge and Wan2.2 VAE latents in their encoder comparison.
**Tools & method (≤3 sentences):** LeWAM uses frozen I-JEPA embeddings with AdaFuse adaptive multi-layer fusion as visual input, a single predictor jointly handling action generation (via flow matching) and future embedding prediction, and DemoDPO for offline preference refinement without extra environment interaction; it was trained on RoboTwin 2.0 (50 tasks, 2,500 clean + 25,000 randomized demonstrations) using 16 NVIDIA H800 GPUs, plus real-world validation on an AgileX dual Piper robot across three bimanual tasks.
**Limitation (≤3 sentences):** The authors state their linear-Gaussian VAE analysis is "an analyzable instance, not a model of the pretrained Wan2.2 VAE," i.e., the theoretical framework applies to controlled settings and may not generalize to all scenarios.

## GAE: Learning a Geometry-Native Latent Space for 3D-Consistent World Generation
- **arXiv:** 2609.24981 · https://arxiv.org/abs/2609.24981
- **Submitted:** 2026-09-21
- **Authors:** Jiahao Lu, Minghao Yin, Wenbo Hu, Hengyu Liu, Wang Zhao, Sai-Kit Yeung, Ying Shan, Yuan Liu
- **Qualifying affiliation(s):** Tencent (ARC Lab, Tencent IEG) — Minghao Yin, Wenbo Hu, Wang Zhao, Ying Shan
- **Categories:** cs.CV
- **Open release:** none confirmed (project page only: https://jiah-cloud.github.io/GAE.github.io/; no code/weights link stated)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GAE (Geometry-Native Autoencoder) is a latent representation for video/scene generation that is decodable to appearance, depth, cameras, and point maps, aiming to give generative models a geometry-aware latent space instead of a purely appearance-focused one. The authors argue this shared representation improves 3D consistency in generated content.
**Purpose (≤3 sentences):** Visual generators often fail to maintain 3D consistency across viewpoints because they operate on appearance-centric latents while perception models use geometry-rich representations; the authors argue "perception and generation should instead share a geometry-native latent space."
**Breakthrough (≤3 sentences):** The authors report that using GAE latents reduces FVD by 12.7% on RealEstate10K and 23.1% on DL3DV, and roughly halves camera-trajectory error versus the strongest competing latent, while GAE-64 achieves 0.0034 ATE on RealEstate10K (a 52.8% improvement) and a 0.1208 MEt3R score.
**Tools & method (≤3 sentences):** GAE is trained in two stages: a codec stage that compresses frozen DA3 geometry-foundation-model features (four hierarchical levels, 3,072 raw channels) into a compact 64-128 channel latent decodable to RGB and geometry, followed by a flow-training stage that trains conditional flow matching for generation tasks in that latent space; it is evaluated on RealEstate10K and DL3DV at 256² (held-out 64-scene pool, 9 views/scene) and with 81-view rollouts at 672x378 in qualitative demos.
**Limitation (≤3 sentences):** The paper does not provide explicit failure-case discussion beyond ablation trade-offs (per the fetched excerpt); the work focuses on indoor/scene datasets and its applicability to other domains is not stated.

## Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene Reconstruction
- **arXiv:** 2609.23796 · https://arxiv.org/abs/2609.23796
- **Submitted:** 2026-09-20
- **Authors:** Yang-Tian Sun, Tianjia Liu, Zehuan Huang, Yi-Hua Huang, Xiaoyang Lyu, Ziyi Yang, Zi-Xin Zou, Yuan-Chen Guo, Yan-Pei Cao, Xiaojuan Qi
- **Qualifying affiliation(s):** VAST — co-authors (paper's affiliation footnote lists "The University of Hong Kong" and "VAST"; per-author numeric mapping not resolved from the rendered HTML); FLAG: borderline
- **Categories:** cs.CV, cs.GR
- **Open release:** none confirmed (project page https://sunyangtian.github.io/Mira-Scene-web/ now redirects to https://vast-ai-research.github.io/eden-page/?p=mira-scene; no code/weights link found in the paper text itself)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Mira-Scene reconstructs compositional 3D scenes from a single image by replacing sparse object-pose regression with dense, pixel-aligned correspondence recovery via a "Canonical Coordinate Map." A multimodal diffusion transformer jointly generates object geometry and these coordinate maps, which are then used to assemble the full scene.
**Purpose (≤3 sentences):** Single-image compositional 3D scene reconstruction requires placing high-fidelity 3D objects into a coherent scene layout, but existing sparse-pose-regression approaches to layout are hard to learn and generalize poorly given limited scene-level supervision.
**Breakthrough (≤3 sentences):** The authors report relative gains of 39.8% in 3D-IoU (0.520 → 0.727) and 16.5% in 2D-IoU (0.672 → 0.783) over SAM3D on the BlendSwap benchmark, while maintaining competitive object geometry (Chamfer Distance 0.021) with substantially less training data.
**Tools & method (≤3 sentences):** The method introduces a Canonical Coordinate Map (mapping visible object pixels to a bounded canonical surface space) alongside a Point Cloud Map, generated jointly with object geometry by a multimodal diffusion transformer with separate expert streams and shared attention, then assembles the scene via RANSAC-based geometric alignment on the dense correspondences; training uses object-level pretraining on 60K Objaverse assets (1M rendered views) followed by scene-level fine-tuning on 20K 3D-FRONT views, evaluated on BlendSwap and 3D-Future Scene.
**Limitation (≤3 sentences):** The authors state detailed limitations are discussed in an appendix; from the main text, 3D-IoU drops to 0.635 under 60%+ occlusion, and the method depends on accurate monocular geometry (Point Cloud Map quality) and on instance mask availability.

# Near-misses
- 2609.32761 · From Feed-Forward to Flow: Unifying Reconstruction and Generation Is Easier Than You Think · no industry author (all authors Peking University)
- 2609.32692 · World Agent: Can Language Models Keep a World Running? · no industry author (Sun Yat-sen University, South China University of Technology, Peng Cheng Laboratory, X-Era AI Lab — all academic/government)
- 2609.32175 · OneFixer: High-Quality and Consistent One-Step Autoregressive 3DGS Refinement for Driving Scenes · off-topic (autonomous-driving-only; authors from 42dot and Hyundai Motor Company, neither a tracked or comparable graphics/world-model/game lab)
- 2609.21400 · A Scene Language Model for Open-Vocabulary Scene Mapping (SceneLM) · off-topic (VLM-based textual SLAM/scene-graph mapping for robot navigation, not 3D graphics/generative world-model/character-animation/game-engine work, despite an NVIDIA co-author)
- 2609.18077 · vidax: A Unified JAX Framework for Video Generative Models on Accelerator Meshes · no industry author (sole author, MIT)
