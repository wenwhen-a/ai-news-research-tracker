## LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation
- **arXiv:** 2610.40495 · https://arxiv.org/abs/2610.40495
- **Submitted:** 29 October 2026
- **Authors:** Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan, Alessandro Burzio, Sherwin Bahmani, Jiahui Huang, Stefan Roth, Shengyu Huang, Qunjie Zhou, Laura Leal-Taixé
- **Qualifying affiliation(s):** NVIDIA — Oliver Hahn, Stefan Roth (also Sherwin Bahmani, work done while at NVIDIA)
- **Categories:** cs.CV
- **Open release:** none (project page only: https://research.nvidia.com/labs/sil/projects/lucidlyra)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** LucidLyra is a feed-forward model that reconstructs a 3D scene as Gaussians while jointly predicting open-vocabulary semantics and class-agnostic instance groupings, all in a single pass from video-diffusion latents. It distills a camera-controlled video diffusion model and frozen 2D vision foundation models into one network, requiring no manual 3D annotation, multi-view capture, or per-scene optimization. The authors also show early results extending it to dynamic scenes from monocular video.
**Purpose (≤3 sentences):** The goal is to make generatively reconstructed 3D scenes directly queryable for semantics and object instances, rather than requiring a separate per-scene 3DGS segmentation step bolted onto generative reconstruction.
**Breakthrough (≤3 sentences):** The authors report that LucidLyra outperforms baselines that combine existing 3DGS segmentation methods with generative reconstruction, while preserving the base reconstruction quality of the underlying "Lyra" system. They also report it supports novel-view rendering, open-vocabulary segmentation, and object grouping without per-scene optimization, plus applications in 3D scene editing, 3D asset mining, and physical-AI simulation.
**Tools & method (≤3 sentences):** The method distills knowledge from a camera-controlled video diffusion model (which supplies both latents and training data) and frozen 2D vision foundation models into a single feed-forward Gaussian decoder that jointly predicts geometry, appearance, semantics, and instance cues.
**Limitation (≤3 sentences):** The authors do not name a specific limitation explicitly; instead they frame remaining work as scaling the approach with accelerated video generation and larger-scale joint training for generation and scene understanding.

## Wizard: Manipulate Any World in Real Time via Agentic Control
- **arXiv:** 2610.40339 · https://arxiv.org/abs/2610.40339
- **Submitted:** 29 October 2026
- **Authors:** Yuzhe Wu, Zijun Lin, Yeying Jin
- **Qualifying affiliation(s):** Tencent — Yuzhe Wu, Zijun Lin, Yeying Jin
- **Categories:** cs.CV
- **Open release:** none (project page only: https://wyzardwu.github.io/wizard)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Wizard is an agentic game world model that gives real-time, precise control over character motion in generated game worlds. It generalizes zero-shot to new scenes, characters, and actions, conditioning video generation on skeleton and geometry information as intermediate representations. An agentic framework tracks and updates game state alongside an adaptive masking mechanism.
**Purpose (≤3 sentences):** The authors aim to overcome existing game/world models' limited control flexibility and generalization, where action-conditioned models restrict players to predefined action sets and prompt-conditioned models struggle with instructions unseen during training.
**Breakthrough (≤3 sentences):** The authors report that Wizard demonstrates strong zero-shot generalization to unseen characters, scenes, and motions, letting players create and manipulate customized game worlds. They built a supporting dataset of 750 scenes and 178 characters to enable this generalization.
**Tools & method (≤3 sentences):** The method uses skeleton and geometry information as intermediate representations to condition video generation, combined with an adaptive masking mechanism and an agentic framework that maintains and updates explicit game state separate from the visual generation process.
**Limitation (≤3 sentences):** The authors state that Wizard's reliance on a motion library makes it difficult to find compatible motions for characters with uncommon body structures, and that consistency between scene proxies and generated video may decline over longer rollouts.

## RFW-A: Agentic Procedural Generation of 400K Articulated Assets over 500 Categories
- **arXiv:** 2610.40333 · https://arxiv.org/abs/2610.40333
- **Submitted:** 29 October 2026
- **Authors:** Yuanbo Lyu, Changjian Pan, Saining Zhang, Yi Yang, Peishuo Li, Zhiheng Li, Jialu Liu, Junhao Chen, Jiawei Weng, Yupeng Gao, Weiqing Xiao, Wenyi Li, Jiarui Guo, Rui Zhang, Jingrun Du, Weiyi Lin, Zenan Meng, Hu Wei, Lin Qu, Zongzheng Zhang, Hao Zhao, Chaojian Li
- **Qualifying affiliation(s):** Alibaba Group — Yuanbo Lyu, Yi Yang, Jiawei Weng, Weiyi Lin, Lin Qu, Zenan Meng, Hu Wei (corresponding authors' contact emails use @alibaba-inc.com), plus Wenyi Li, Jiarui Guo, Rui Zhang, Jingrun Du (dual Alibaba/Tsinghua)
- **Categories:** cs.CV
- **Open release:** none (project page only: https://brain-labbb.github.io/RFW_A_web/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** RFW-A combines agentic program synthesis with procedural generation: agents build reusable, category-level generator programs from existing articulated-asset code, test and refine them across sampled configurations, then produce assets procedurally without further model calls. Using this, the authors built RFW-A-400K, a dataset of over 400,000 sim-ready articulated assets spanning more than 500 categories. The premise is that assets within a category can share construction logic despite variation in structure and appearance.
**Purpose (≤3 sentences):** The goal is to make large-scale construction of high-quality articulated 3D assets for embodied perception, simulation, and manipulation far cheaper than manual annotation, procedural modeling, or per-asset agentic reasoning.
**Breakthrough (≤3 sentences):** The authors report an average generator-authoring cost of $10.62, dropping to about $0.05 per asset once amortized over 200 assets per category, while maintaining high structural and kinematic validity and stable execution across physics simulators. They also report that training on the dataset improves part-level articulation estimation on both seen and unseen categories, and that simulation-trained policies transfer zero-shot to real articulated objects.
**Tools & method (≤3 sentences):** Agents synthesize and refine category-level generator programs from sampled configurations, after which assets are produced procedurally without further model calls; the resulting RFW-A-400K dataset is validated for structural/kinematic correctness and simulator stability.
**Limitation (≤3 sentences):** The authors state that diversity remains limited by the source components and category blueprints, so expanding coverage requires extending those sources; they also note that validation covers only sampled configurations and motion states, leaving the full configuration space untested, and that broader multi-category studies are needed to quantify cost savings.

## PhysAg3D: Bridging 3D Generative and Agentic Models for High-Fidelity and Physically-Interactive Assets
- **arXiv:** 2610.39924 · https://arxiv.org/abs/2610.39924
- **Submitted:** 29 October 2026
- **Authors:** Bi'an Du, Fanpeng Meng, Jiemin Fang, Chen Yang, Pufan Li, Daizong Liu, Qi Tian, Wei Hu
- **Qualifying affiliation(s):** Huawei — Fanpeng Meng, Jiemin Fang, Chen Yang, Qi Tian (also Guangdong Laboratory of Artificial Intelligence and Digital Economy); FLAG: borderline (Huawei is not on the core tracked list but is a comparable top-tier industry lab)
- **Categories:** cs.CV
- **Open release:** none (project page only: http://supra-3d.github.io/PhysAg3D)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PhysAg3D couples 3D generative models with agentic reasoning and tool use to turn a single image into an interactive 3D asset. A vision-language agent infers semantic parts, candidate interactions, and physical priors, while a 3D generator produces a textured whole-object mesh, with a hierarchical interaction representation guiding construction of parts, joints, deformable regions, and surface bindings. The framework supports both rigid articulation and compliant (soft) deformation.
**Purpose (≤3 sentences):** The goal is high-fidelity, physically-interactive 3D asset creation from a single image, bridging the gap between purely generative 3D reconstruction (visually faithful but not interactive) and agentic/procedural approaches (interactive but often lower visual fidelity).
**Breakthrough (≤3 sentences):** The authors report that feedback-based refinement, carried out within a fixed budget, and surface preservation together support appearance fidelity and plausible interactions, validated with evaluations on real photographs and external benchmarks plus ablations on bounded refinement and source-surface preservation.
**Tools & method (≤3 sentences):** A vision-language agent infers semantic parts, candidate interactions, and physical priors from an image; a 3D generative model produces a textured mesh; a hierarchical interaction representation (parts, joints, deformable regions, surface bindings) then guides iterative, budget-bounded refinement.
**Limitation (≤3 sentences):** The authors state that recovering hidden structure and material properties remains a limitation of their approach.

## Aligning Misaligned Benchmarks for Single-View Novel View Synthesis
- **arXiv:** 2610.38349 · https://arxiv.org/abs/2610.38349
- **Submitted:** 28 October 2026
- **Authors:** Yang-Che Tseng, Erqun Dong, Jeong-gi Kwak, Gopal Sharma, Shakiba Kheradmand, Stephan Garbin, Hossam Isack, Kwang Moo Yi
- **Qualifying affiliation(s):** Google — Stephan Garbin, Hossam Isack
- **Categories:** cs.CV, cs.AI
- **Open release:** none (no project page, code, or demo link found on the abstract page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The authors argue that single-view novel-view-synthesis methods are hard to compare fairly because each method's output must first be pose-aligned to ground truth, and common test-time pose optimization is ill-posed, leaving methods evaluated at arbitrary local optima. They propose aligning 3D reconstructions using standard 2D-to-2D and 2D-to-3D image matching instead, and evaluating only within regions co-visible between predicted and ground-truth views. Under this corrected evaluation, explicit 3D Gaussian methods reach state-of-the-art results.
**Purpose (≤3 sentences):** The goal is to standardize evaluation for single-view novel view synthesis by removing the confound of ill-posed test-time pose optimization, so method comparisons reflect actual reconstruction quality rather than alignment artifacts.
**Breakthrough (≤3 sentences):** The authors report that, under their corrected alignment and co-visible-region evaluation, explicit 3D Gaussian methods achieve state-of-the-art results. They also report a simple baseline — an off-the-shelf video generator combined with a feed-forward geometry estimator — performs comparably to methods trained specifically for this task, without any task-specific training.
**Tools & method (≤3 sentences):** The method replaces test-time pose optimization with traditional 2D-to-2D and 2D-to-3D image matching to align 3D reconstructions to ground truth, then restricts evaluation metrics to the co-visible regions between views.
**Limitation (≤3 sentences):** The authors state that while their findings could apply to other novel-view-synthesis settings, such as few-shot or dynamic novel view synthesis, they have not yet explored those extensions.

## ETA-Motion: Efficient Topology-Agnostic Motion Diffusion via Sparse Joint Learning
- **arXiv:** 2610.38259 · https://arxiv.org/abs/2610.38259
- **Submitted:** 28 October 2026
- **Authors:** Seoyoung Hwang, Tae-Kyun Kim
- **Qualifying affiliation(s):** Samsung Electronics — Seoyoung Hwang (dual KAIST/Samsung Electronics); FLAG: borderline (Samsung is not on the core tracked list but is a comparable top-tier industry lab)
- **Categories:** cs.CV
- **Open release:** none (project page only: https://sy-hwang.github.io/eta-motion-page/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ETA-Motion generates motion for characters with arbitrary, varying skeletons by training a motion generator on only a compact subset of joints rather than all joints. It adds semantic joint embeddings that combine textual and visual cues, plus topology-aware training objectives, so the model learns from sparse skeletal data but can generate full-skeleton motion at inference. The paper is accepted to WACV 2027.
**Purpose (≤3 sentences):** The goal is efficient, topology-agnostic motion generation that generalizes across characters with different skeleton structures and joint semantics, without the computational overhead of modeling every joint densely.
**Breakthrough (≤3 sentences):** The authors report that dense full-joint modeling in prior topology-agnostic approaches incurs substantial computational overhead and pushes the model to learn topology-specific details that do not transfer; their sparse-joint approach instead reports better results than existing topology-agnostic baselines, with improved efficiency and generalization to unseen motions and topologies.
**Tools & method (≤3 sentences):** The method combines a visual joint embedding (computed from rigged-mesh vertex features) with textual joint-name cues to build semantic joint embeddings, and pairs these with topology-aware training objectives so training on sparse joint subsets still yields full-skeleton generation at inference.
**Limitation (≤3 sentences):** The authors note that asset-provided joint names are often noisy, incomplete, or inconsistent across rigs, which makes establishing accurate correspondence from textual cues alone difficult — motivating their added visual joint embedding.

## METATRON: A Promptable Whole-Body Execution Layer for Humanoids
- **arXiv:** 2610.38027 · https://arxiv.org/abs/2610.38027
- **Submitted:** 27 October 2026
- **Authors:** Chen Tessler, Yifeng Jiang, Alec Otto, Yi Shi, Umar Iqbal, Gal Chechik, Xue Bin Peng
- **Qualifying affiliation(s):** NVIDIA — Chen Tessler, Yifeng Jiang, Yi Shi, Umar Iqbal, Gal Chechik, Xue Bin Peng (Alec Otto, Dollhouse Robotics, interned at NVIDIA)
- **Categories:** cs.RO, cs.AI
- **Open release:** none (project page only: https://research.nvidia.com/labs/par/projects/metatron/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Metatron is a humanoid control system built on a frozen, generative whole-body base policy plus a programmable skill layer on top. The policy accepts "prompts" combining timed body-part targets, velocity commands, and style cues, while skills are ordinary code that coding agents can refine directly from motion data, without task-specific policy retraining. The system is demonstrated on a physical Unitree G1 humanoid robot.
**Purpose (≤3 sentences):** The goal is a reusable, promptable execution layer for humanoid whole-body control that lets new skills be authored and refined as code on top of a single frozen motion policy, instead of retraining a policy for every new task.
**Breakthrough (≤3 sentences):** The authors report physical-robot tests covering walking, recovery, teleoperated object pickup, and sitting, with higher reaching success and push robustness than the reference-tracking baselines they compared against. They also report that push-recovery performance degrades sharply under strong perturbations, with all tested methods falling below 10% success at 600–800 N forces.
**Tools & method (≤3 sentences):** A frozen generative whole-body base policy is driven by prompts combining timed body-part targets, velocity commands, and style cues; skills built on top are authored as ordinary code that coding agents can refine from motion-capture data without retraining the underlying policy.
**Limitation (≤3 sentences):** The authors state that Metatron's motion repertoire depends on training coverage, so underspecified goals or incidental style cues can produce unintended motions (e.g., abruptly commanding 2 m/s from rest often triggers a front roll), and that all tested methods, including theirs, fall below 10% success under strong (600–800 N) pushes.

## GOFish: Full Field-of-View Gaussian Splatting and Mesh Extraction
- **arXiv:** 2610.37818 · https://arxiv.org/abs/2610.37818
- **Submitted:** 27 October 2026
- **Authors:** Allen Tu, Meher Gitika Karumuri, Shifan Zhu, Hailing Wang, Yen-Liang Lin, David Held, Matthias Zwicker, Tom Goldstein
- **Qualifying affiliation(s):** Amazon — Allen Tu, Meher Gitika Karumuri, Shifan Zhu, Hailing Wang, Yen-Liang Lin, David Held (per PDF affiliation superscript "1 = Amazon"; most likely as an internship collaboration, since other authors hold University of Maryland/Northeastern/CMU affiliations)
- **Categories:** cs.CV, cs.GR, cs.RO
- **Open release:** none (project page only: https://3dgofish.github.io/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GOFish is the first 3D Gaussian Splatting surface reconstruction method that trains directly on fisheye images, rasterizing fields of view beyond 180° and extracting an aligned mesh from the same scene. It introduces calibrated densification to recover surfaces across the full field of view, plus Calibrated Mip Filtering and Wide-Angle Appearance Modeling to keep pixel blur and lens falloff out of the reconstructed scene and mesh. The output is framed as a LiDAR-free, simulation-ready digital twin that renders in real time and provides collision geometry.
**Purpose (≤3 sentences):** The goal is to build simulation-ready digital twins directly from wide-FoV fisheye cameras (used by robots, autonomous vehicles, and consumer 360° cameras) without requiring LiDAR, since prior fisheye Gaussian Splatting methods cap out at 180° and don't produce meshes, while Gaussian surface-reconstruction methods assume pinhole images.
**Breakthrough (≤3 sentences):** The authors report PSNR improvements over the best prior method of 2.28 dB and 1.97 dB on the 200° FIORD and 205° FullCircle benchmarks respectively, and the highest mesh F-score on FIORD and the main ScanNet++ set. In a component study, full field-of-view rasterization alone left F-score at 0.139, with calibrated densification and Calibrated Mip Filtering together accounting for 3.6 of GOFish's 4.0 dB total gain within the baseline's 160° range.
**Tools & method (≤3 sentences):** The method combines calibrated densification, Calibrated Mip Filtering, and Wide-Angle Appearance Modeling on top of 3D Gaussian Splatting, trained directly on calibrated fisheye images, and extracts a mesh aligned to the reconstructed Gaussian scene; it is evaluated on the FIORD, FullCircle, and ScanNet++ benchmarks.
**Limitation (≤3 sentences):** The authors state that GOFish inherits opacity-field limitations from prior work: taking the minimum across views can misplace reflective surfaces or carve thin structures, sparse observations can leave holes or cause mesh overfill, and full-FoV coverage cannot recover information lost to sparse sampling or rim attenuation.

# Near-misses
- 2610.39639 · Where Do Vision Language Models Fail at 3D Reasoning? · affiliations confirmed via rendered PDF logos are Novel (startup), University of Toronto, Vector Institute, Hong Kong Polytechnic University, Texas A&M, Carnegie Mellon, Salesforce, Stanford, and Oxford — none on the tracked list or clearly comparable in this domain (Salesforce is enterprise software, not a tracked 3D/graphics/gaming lab)
- 2610.39528 · PRIME W0: Physical Priors from World Models for Embodied Manipulation · affiliations are "Lumos SZ Lab Team," "Lumos Robotics," Tsinghua, CUHK, NTU — Lumos is not a tracked company or a clearly comparable top-tier lab
- 2610.39076 · Tactus: Tactile & Pose Sensing Glove for Natural Dexterity Data Collection · genuine Meta Reality Labs Research affiliation confirmed, but off-topic: this is robotics hardware/data-collection tooling for manipulation research, not 3D, world models, character animation, or game engines
- 2610.39038 · LightGenBench: A Benchmark for 3D Emission Generation · only affiliation found is Simon Fraser University (academic only), no industry affiliation in the HTML author block
- 2610.38980 · Context Compaction for World Models · sole author affiliated with Boston University and AllSpice Inc.; neither is a tracked company or a comparable top-tier industry lab
- 2610.37891 · When More Planning Hurts: Learned Planners for World Models · sole author is an independent researcher, no industry affiliation found
- 2610.32554 · HGWM: Hierarchical Graph-Guided World Model for Zero-Shot Object Navigation via Graph Matching · authors affiliated with Tsinghua University and Peking University only, no industry affiliation found in the HTML author block
