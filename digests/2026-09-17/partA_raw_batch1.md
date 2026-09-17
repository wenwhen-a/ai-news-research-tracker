## PointZero: 3D Point Track Completion for Learning Transferable 3D Dynamics
- **arXiv:** 2609.19142 · https://arxiv.org/abs/2609.19142
- **Submitted:** 2026-09-16 (v1)
- **Authors:** Bardienus P. Duisterhof, Kaifeng Zhang, Adam Hung, Bowen Wen, Stan Birchfield, Yunzhu Li, Deva Ramanan, Jeffrey Ichnowski
- **Qualifying affiliation(s):** NVIDIA — Bowen Wen, Stan Birchfield (co-authors also at CMU and Columbia University)
- **Categories:** cs.CV; cs.RO
- **Open release:** code | dataset | weights (announced) — project page https://pointzero-wm.github.io; paper states "We release the dataset, checkpoints, and full training recipe"
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper studies "3D point track completion" — predicting future 3D trajectories of all observed points from a single RGB-D frame plus sparse partial 3D tracks — as a pre-training objective for learning 3D dynamics without robot action labels. The authors build PointZero, a transformer trained on a new 2.9M-frame synthetic dataset spanning deformable, articulated and rigid objects. They then post-train PointZero for action-conditioned dynamics prediction and imitation learning.

**Purpose (≤3 sentences):** Existing action-conditioned 3D dynamics methods require robot action labels, which excludes web video data from training. The authors aim to learn a transferable 3D dynamics prior that does not depend on robot action annotations, so it can eventually draw on broader (e.g., web) video sources.

**Breakthrough (≤3 sentences):** The authors report that PointZero "outperforms prior methods on the same data" for the pre-training objective, outperforms baselines on the recent PGND 3D dynamics benchmark when fine-tuned to condition on end-effector pose, and outperforms or matches baselines on 6 of 7 simulated and real-world robot manipulation tasks when fine-tuned to predict robot actions and 3D tracks.

**Tools & method (≤3 sentences):** PointZero is a transformer architecture trained via the 3D point track completion objective; the training data is a 2.9-million-frame synthetic dataset generated with NVIDIA FleX physics for deformable-object simulation. The authors also run an ablation training PointZero from scratch to separate the benefit of the architecture from the benefit of the pre-training objective and dataset.

**Limitation (≤3 sentences):** The authors state PointZero "remains limited by the coverage and realism of its pre-training data," which does not capture the full diversity of real-world materials, contact-rich hand-object interaction, cluttered scenes, or long-horizon dynamics. They also note the conditioning signals used (partial point tracks; end-effector pose) are relatively simple, and that downstream evaluations remain task-specific and relatively small-scale.

---

## Can MiniMax-H3 Reason About the Physical World? An Evaluation of Omni-Modal Generative Models
- **arXiv:** 2609.18323 · https://arxiv.org/abs/2609.18323
- **Submitted:** 2026-09-16 (v1)
- **Authors:** Haoyu Zhao, Zihao Zhao, Tianyu Deng, Ziqin Xu, Zihao Zhang, Xudong Wang, Jinxiang Guo, Chen Gao, Ziyi Ye, Yeying Jin, Jiaxi Gu, Zuxuan Wu, Shuicheng Yan
- **Qualifying affiliation(s):** Tencent — Yeying Jin (co-authors also at National University of Singapore and Fudan University)
- **Categories:** cs.CV
- **Open release:** code (benchmark/eval code) — https://github.com/gulucaptain/MiniMax-H3-Reason
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces an evaluation framework that tests whether the omni-modal generative model MiniMax-H3 can integrate complementary evidence spread across text, image, video, and audio modalities to reason about physical-world dynamics. It constructs implicit condition–prompt pairs (e.g., audio-image, prefix-video, audio-video) where each single modality alone gives only partial evidence of the underlying event. Across 517 evaluation instances, MiniMax-H3 achieves an overall success rate of 41.97%.

**Purpose (≤3 sentences):** The authors want to know whether multimodal alignment in an omni-modal model actually improves "world reasoning" — i.e., inferring latent event states and future dynamics — rather than just accepting heterogeneous inputs. They position the work as distinct from prior video-generation/world-model evaluations that use prompts closely matching target video content.

**Breakthrough (≤3 sentences):** The authors report Video-based Decision Reasoning as the strongest category (56.00% success) and Audio-based Disambiguation Reasoning as the weakest (27.40%), with an overall 41.97% success rate across four reasoning dimensions. They state this reveals "a substantial gap between omni-modal input support and effective physical-world reasoning," suggesting multimodal integration is not yet fully exploited by current omni-modal generative models.

**Tools & method (≤3 sentences):** The evaluation is built around four complementary scenarios of physical-world reasoning (implicit prompts with multiple frames, audio-image, prefix-videos, and audio-video inputs) applied to MiniMax-H3's shared latent audio-visual generation architecture. The authors release evaluation code on GitHub.

**Limitation (≤3 sentences):** The authors state the overall reasoning performance "remains limited" despite complementary multimodal evidence being available, and note this is only an initial evaluation set they plan to "continuously expand and refine ... with more diverse physical-world scenarios, modality combinations, and reasoning requirements." They also state they still need to develop a more reliable automated evaluation framework for assessing reasoning outcomes.

---

## Zing-0.5: Toward Playable Worlds with Real-Time Joint Action and Text Control
- **arXiv:** 2609.17909 · https://arxiv.org/abs/2609.17909
- **Submitted:** 2026-09-15 (v1)
- **Authors:** Mingyang Chen, Shengdong Chen, Xiaoxiao Fu, Bosheng Gong, Haoyuan Guo, Bowen Li, Jiawen Li, Kejun Li, Tianpeng Li, Yin Liu, Haoze Sun, Zeyang Tian, Meng Wang, Xinmiao Wu, Jiangqiao Yan, Zining Zhao
- **Qualifying affiliation(s):** SeedLeap.ai (all authors) — FLAG: borderline (company not on the core qualifying list; standing unverified)
- **Categories:** cs.CV; cs.LG
- **Open release:** weights | code — https://huggingface.co/seedleap/zing-0.5, https://github.com/seedleap/zing-world-model, https://github.com/seedleap/Zing-SGLang; project page https://zing.loopit.me/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents Zing-0.5, a 5B-parameter autoregressive world model built for "playability," letting users explore generated worlds and influence unfolding events via joint keyboard and real-time text control. It combines unified action/text conditioning, event-scale supervision via distillation from a segment-level teacher, and low-cost real-time streaming generation. It reports an overall score of 81.0 and a consistency score of 88.5 on 158 WBench Navigation cases, running at 24 FPS.

**Purpose (≤3 sentences):** The authors aim to build an interactive world model where users can both navigate and cause persistent event changes through natural-language instructions, rather than navigation-only control. They frame this as a step toward genuinely "playable" generated worlds rather than passive video generation.

**Breakthrough (≤3 sentences):** The authors report three technical contributions: unified action-and-text conditioning learned jointly with magnitude-aware keyboard inputs and temporally aligned text instructions; event-scale supervision using distribution-matching distillation from a segment-level teacher to a block-level causal student; and four-step generation with context-preserving streaming enabling 832×480 real-time inference at 24 FPS at an estimated $0.009 per stream-minute server cost. They report an overall WBench Navigation score of 81.0 and consistency score of 88.5, and demonstrate a text-directed event change occurring mid-navigation without restarting generation.

**Tools & method (≤3 sentences):** Zing-0.5 is a 5B autoregressive world model trained with jointly annotated action-and-text video data, using a segment-level teacher model distilled into a block-level causal student via distribution-matching distillation. The authors release model weights, inference code, and a "Zing-SGLang" serving implementation for real-time deployment.

**Limitation (≤3 sentences):** In their discussion, the authors state that "visual history does not fully specify world state" — meaning the model cannot always keep track of state changes purely from what has been visually shown — and that "persistent worlds need architectural support" beyond current capacity and context length to reliably retain and update facts across viewpoint and instruction changes. They call for future evaluation to test whether users can make a change, leave it, and later see its consequences persist, implying current persistence is not fully reliable.

---

## PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM
- **arXiv:** 2609.17387 · https://arxiv.org/abs/2609.17387
- **Submitted:** 2026-09-15 (v1)
- **Authors:** Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang
- **Qualifying affiliation(s):** Ant Group — Hao Shi (dual-affiliated with Zhejiang University) — FLAG: borderline
- **Categories:** cs.CV
- **Open release:** code (announced, no link live yet) — paper states "The source code will be made publicly available"
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents PanoGS-SLAM, described as the first dense SLAM system for panoramic cameras built on 3D Gaussian Splatting. It performs differentiable rendering and pose optimization directly in the spherical domain to get omnidirectional photometric constraints, using a sphere-consistent photometric loss and a depth-guided Gaussian initialization strategy. On the PALVIO and SynPano benchmarks it reports consistently outperforming geometric and GS-based baselines in tracking accuracy and rendering quality.

**Purpose (≤3 sentences):** Prior 3DGS-based SLAM methods are designed for narrow-FoV pinhole cameras, where limited angular coverage weakens pose observability and destabilizes photometric optimization under rapid motion or large viewpoint changes. The authors aim to exploit panoramic (360°) cameras' wide field of view for more stable tracking and mapping.

**Breakthrough (≤3 sentences):** The authors report that PanoGS-SLAM "consistently outperforms geometric and GS-based baselines in tracking accuracy and rendering quality" on the PALVIO and SynPano benchmarks while achieving fast front-end convergence and real-time performance. They also report a controlled field-of-view experiment showing a "clear monotonic improvement in optimization conditioning and convergence stability as angular coverage increases," directly linking sensing geometry to optimization quality.

**Tools & method (≤3 sentences):** The method performs differentiable rendering and pose optimization directly in the spherical domain rather than projecting to pinhole views, introducing (1) a sphere-consistent photometric loss that compensates for equirectangular-projection area distortion, and (2) a depth-guided Gaussian initialization strategy for newly observed regions. It is evaluated on the real-world PALVIO benchmark and the synthetic SynPano benchmark.

**Limitation (≤3 sentences):** The authors note that even with panoramic input, differentiable photometric pose estimation has a fundamental limitation: the optimization landscape depends heavily on the spatial/angular distribution of image gradients, and under narrower FoV settings gradients concentrate within a narrow viewing cone, weakening rotational observability. They also identify a second issue during incremental mapping, where newly observed regions initially lack sufficient Gaussian support and geometric constraints, which can destabilize tracking.

---

## DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming
- **arXiv:** 2609.17230 · https://arxiv.org/abs/2609.17230
- **Submitted:** 2026-09-15 (v1)
- **Authors:** Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu
- **Qualifying affiliation(s):** Intel Labs — Sainan Liu (co-authors listed with University of Bonn/Almetra, V3DEO, and Cauth AI affiliations)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** DecoGS is a method for efficient online training of 3D Gaussians from streaming video, targeting free-viewpoint video (FVV) streaming. Instead of updating every Gaussian every frame, it selectively optimizes only spatiotemporal regions showing motion or photometric change, reducing redundant updates that cause flicker and drift in static regions. On the N3DV and MeetRoom benchmarks it reports 34.55 dB and 31.60 dB PSNR respectively, at 261 FPS rendering, with 70x lower temporal flicker than the best prior method.

**Purpose (≤3 sentences):** Streaming 3D reconstruction needs both speed and temporal fidelity, but existing methods undermine this by indiscriminately updating every Gaussian every frame even in static regions. The authors aim to eliminate this redundant computation to enable faster, higher-fidelity, and more temporally stable free-viewpoint video streaming.

**Breakthrough (≤3 sentences):** The authors report DecoGS achieves 34.55 dB PSNR on N3DV and 31.60 dB PSNR on MeetRoom, "outperforming all streaming and offline baselines," while rendering at 261 FPS and achieving 70x lower temporal flicker than the best prior method, without requiring large-scale pretraining. This is attributed to an adaptive mechanism that focuses optimization only on regions with detected motion or photometric change.

**Tools & method (≤3 sentences):** DecoGS integrates region-aware Gaussian management via gradient gating and efficient visibility filtering to maintain temporal coherence and a compact memory footprint. It is evaluated on the N3DV and MeetRoom free-viewpoint video datasets.

**Limitation (≤3 sentences):** The authors state that current change detection could be extended with semantic or foundation-model cues for more intent-aware dynamic-region detection, since the current approach relies on heuristics that don't distinguish transient objects from persistent background. They also note that DecoGS, like all existing online FVV methods, assumes fixed, synchronized, and calibrated cameras, and that robustness to camera drift or exposure changes remains an open problem.

---

# Near-misses
- 2609.18442 · Risk-Aware World Modeling with Flow-Guided Occupancy Evolution for Selective Trajectory Planning in Automated Driving · purely academic (RWTH Aachen, Monash University, TU Munich), no industry co-author; screen match "NVIDIA" not confirmed in author affiliations
- 2609.18465 · GeoCond: A Conditioning-Aware Reliability Adapter for Feed-Forward 3D Reconstruction · purely academic (CSIRO Australia, Monash University), no industry co-author; screen match "ByteDance" not confirmed in author affiliations
- 2609.18406 · Prosthesis-Aware 3D Human Pose Estimation: A Dataset and Benchmark for RSP Users · off-topic: medical/assistive-technology application (prosthesis-specific pose estimation for accessibility/biomechanics), not a 3D-reconstruction/animation/game-industry contribution, despite a genuine Sony Computer Science Laboratories co-author (Ken Endo)
- 2609.18034 · IRIS: Implicit Rendering Matters for Pose-Free Novel View Synthesis · no HTML version available on arXiv, affiliation unverifiable
- 2603.23983 · SafeFlow: Real-Time Text-Driven Humanoid Whole-Body Control via Physics-Guided Rectified Flow and Selective Safety Gating · out of window — true v1 was submitted 2026-03-25 (arXiv ID 2603.xxxxx); only a v2 revision landed on 2026-09-15, so the paper's actual submission predates the 30-day tracking window
- 2609.17525 · You Shall Not Pass into Ring-0! A User Privacy-Friendly Anti-Cheat Architecture for Personal Computers · off-topic: cybersecurity/virtualization systems architecture for anti-cheat (cs.CR), not 3D/character-animation/game-engine research, despite a genuine Microsoft Research co-author (Sangho Lee)
- 2604.11082 · RefGlitch-Bench: A Benchmark for Reference-based Gameplay Glitch Detection with Vision-Language Models · out of window — true v1 was submitted 2026-04-13 (arXiv ID 2604.xxxxx); only a v2 revision landed on 2026-09-15, so the paper's actual submission predates the 30-day tracking window
