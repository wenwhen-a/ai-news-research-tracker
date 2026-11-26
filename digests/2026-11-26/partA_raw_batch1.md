## AnyCam: Anything Can Represent Camera for Video Generation
- **arXiv:** 2611.34944 · https://arxiv.org/abs/2611.34944
- **Submitted:** 2026-11-25 (v1)
- **Authors:** Weijie Lyu, Zhixin Shu, Yuntian Ke, Ming-Hsuan Yang
- **Qualifying affiliation(s):** Adobe Research — Zhixin Shu (co-authors: Weijie Lyu and Ming-Hsuan Yang, UC Merced; Yuntian Ke, University of Pennsylvania)
- **Categories:** cs.CV
- **Open release:** demo — project page https://weijielyu.github.io/AnyCam and video https://youtu.be/vWr0S4sPfqw (no code/weights release found)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** AnyCam is a camera-controlled video generation method that represents the target camera trajectory with a reconstructed 3D anchor object rendered along that trajectory, rather than conditioning directly on camera parameters or explicit scene geometry. A video diffusion model then transfers the source video's content and dynamics onto the new viewpoint defined by the anchor's render. The authors also distill the model into AnyCam-AR, a streaming few-step generator for on-the-fly camera control.
**Purpose (≤3 sentences):** Prior camera-controlled video generation methods condition on explicit camera parameters or full scene geometry, which can be brittle or require expensive 3D reconstruction of the whole scene. The authors aim to control camera viewpoint in generated video using a lighter-weight single-object 3D anchor instead.
**Breakthrough (≤3 sentences):** The authors report that representing the camera via an anchor object reconstructed and rendered in 3D — rather than via explicit camera-parameter or full-scene-geometry conditioning — gives favorable camera control and visual quality compared with existing camera-controlled video generation and 3D reconstruction methods. They further distill this into AnyCam-AR, described as a streaming, few-step generator enabling on-the-fly camera control.
**Tools & method (≤3 sentences):** The pipeline reconstructs an anchor object in 3D, renders it along the desired camera trajectory, and uses a video diffusion model to transfer the source video's content/dynamics onto that rendered trajectory; AnyCam-AR is a distilled, few-step autoregressive variant for streaming use. Comparisons are made against existing camera-controlled video generation and 3D reconstruction baselines per the abstract.
**Limitation (≤3 sentences):** The method's camera control is mediated by a single reconstructed anchor object, which may limit applicability to scenes without a clear anchor object (observed, not stated). No code or model-weight release was found, only a project page and demo video.

---

## Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation
- **arXiv:** 2611.34907 · https://arxiv.org/abs/2611.34907
- **Submitted:** 2026-11-25 (v1)
- **Authors:** Shaoteng Liu, Shuai Yang, Wei Huang, Luozhou Wang, Song Han, Yukang Chen
- **Qualifying affiliation(s):** NVIDIA — Shuai Yang, Wei Huang, Luozhou Wang, Song Han, Yukang Chen (Song Han also lists MIT; Shaoteng Liu lists CUHK)
- **Categories:** cs.CV
- **Open release:** code — https://github.com/NVlabs/LongLive/tree/main/Agentic-LongLive ; project page https://nvlabs.github.io/LongLive/Agentic-LongLive/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents Agentic LongLive, an asynchronous memory system for real-time autoregressive video generators that keeps persistent text/image state for people, objects, and scenes across long generations. A memory agent runs on separate GPUs, reading only prompts revealed so far, and feeds memory into the generator without stalling output. On a new 25-story benchmark the authors report improved persistent-state accuracy, protagonist identity, and revisited-place consistency over the base generator, while still running faster than real time on an 8×B200 node.
**Purpose (≤3 sentences):** Long-form autoregressive video generation tends to lose track of characters, objects, and previously visited locations as the sequence grows. The authors aim to give a streaming video generator a working memory that can recall earlier state without interrupting the generation loop.
**Breakthrough (≤3 sentences):** The authors report the first real-time video generator with text-and-image memory managed by an LLM agent, decoupled onto separate GPUs so "the video never waits for memory and video errors are not written back." A small language model trained with reinforcement learning decides what to commit to memory.
**Tools & method (≤3 sentences):** Built on an autoregressive video generation backbone (LongLive) with an asynchronous agentic memory module and an RL-trained small LLM controller; evaluated on a newly introduced 25-story long-video benchmark. Reported throughput: faster-than-real-time generation on an 8×B200 GPU node.
**Limitation (≤3 sentences):** The memory agent only reads prompts already revealed and cannot revise generation after an error has occurred, since video output is never rolled back to match memory (acknowledged design trade-off in the abstract). The evaluation benchmark is newly introduced by the authors, so broader comparability to prior long-video memory methods is limited.

---

## WorldExpand: Building Coherent 3D Worlds via Sparse Joint Panoramic Expansion
- **arXiv:** 2611.34810 · https://arxiv.org/abs/2611.34810
- **Submitted:** 2026-11-25 (v1)
- **Authors:** Yuyang Yin, Chenjie Cao, Xuhui Zuo, Yuning Gong, Pengfei Wang, Junta Wu, Zhenwei Wang, Yao Zhao, Tengfei Wang, Yunchao Wei, Chunchao Guo
- **Qualifying affiliation(s):** Tencent Hunyuan — all authors are listed under joint affiliation with Beijing Jiaotong University and Tencent Hunyuan in the paper's author block
- **Categories:** cs.CV
- **Open release:** demo — project page https://yuyangyin.github.io/WorldExpand_web/ (no code repository found)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** WorldExpand builds complete 3D worlds from a single panorama by generating a sparse set of complementary, high-resolution panoramas instead of a dense sequential video. A coverage-guided view-selection module picks informative viewpoints, and a joint panoramic diffusion model uses Gaussian-splatting-based geometric warps to synthesize four pose-grounded, cross-view-consistent panoramas at once. The authors report recovered content behind occluders, improved novel-view synthesis and 3D reconstruction, and faster runtime than the prior state-of-the-art panoramic-video method.
**Purpose (≤3 sentences):** A single panorama leaves most of a 3D scene unobserved, and prior panoramic-video expansion methods generate many redundant sequential frames, accumulate errors over long camera trajectories, and can produce directionally inconsistent results. The authors aim to expand a single panorama into a coherent, fully covered 3D world more efficiently and consistently.
**Breakthrough (≤3 sentences):** The authors report that formulating expansion as sparse, jointly generated panoramas (rather than dense sequential frames) reduces redundancy and error accumulation while improving cross-view consistency. A global-local attention schedule is used to keep the joint multi-panorama generation computationally tractable.
**Tools & method (≤3 sentences):** The method combines a coverage-guided view-selection module, a joint panoramic diffusion model conditioned on Gaussian-splatting-based geometric warps, and a global-local attention schedule for efficiency. The authors evaluate novel-view synthesis and 3D reconstruction quality and generalization to in-the-wild scenes.
**Limitation (≤3 sentences):** The paper does not report a code release, only a project page, limiting independent reproduction. The abstract's quantitative comparisons are against a single prior panoramic-video baseline, per the paraphrased abstract.

---

## Neural Rendering Compiler: Generative Video Models as Programmable Renderers
- **arXiv:** 2611.34680 · https://arxiv.org/abs/2611.34680
- **Submitted:** 2026-11-25 (v1)
- **Authors:** Yuxia Zhu, Xinglong Xu, Hao Liang, Linzhuang Sun, Caijun Jia, Qifeng Cai, Jincen Luo, Lei Li, Alden Cai, Asher Qin, Wentao Zhang, Cheng Tan
- **Qualifying affiliation(s):** Tencent (listed as one of three institutional affiliations — Peking University, University of Chinese Academy of Sciences, Tencent — in the paper's affiliation block; the arXiv HTML rendering did not preserve which individual authors map to which numbered affiliation, so exact author-to-Tencent mapping could not be confirmed, only that Tencent is a genuine listed affiliation for the author group)
- **Categories:** cs.CV (primary), cs.CL
- **Open release:** code — https://github.com/OpenRaiser/NeurCo ; project page https://openraiser.github.io/NeurCo
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces the Neural Rendering Compiler (NeurCo), which probes frozen video generation models to learn which semantic requirements each model can reliably satisfy, then compiles a model-agnostic user intent (objects, constraints, events, cameras) into model-specific execution strategies. The authors also introduce VComBench, a 380-task compositional benchmark spanning text-to-video, image-to-video, and reference-to-video generation. They report NeurCo raises requirement satisfaction from 46.8% to 52.3% on Wan and from 66.5% to 69.3% on MiniMax H3, with further gains when combined with prompt enhancers.
**Purpose (≤3 sentences):** Video generation models vary in which compositional/semantic requirements (object identity, event order, camera behavior) they can reliably honor, and users have no systematic way to know which requirements a given model can satisfy or how to phrase intent accordingly. The authors aim to treat video generators as "programmable renderers" that can be compiled against per-model capability manuals.
**Breakthrough (≤3 sentences):** The authors report that probing a frozen model to build a capability manual, then rewriting or recompiling unreliable requirements rather than always keeping the original instruction verbatim, measurably raises requirement satisfaction on two different backbones (Wan, MiniMax H3). They state further gains are observed when NeurCo is combined with prompt enhancers, including on Seedance 2.5.
**Tools & method (≤3 sentences):** The method represents user intent in a model-agnostic schema of objects, constraints, events, and cameras, compiles it per-backbone, and is evaluated on the authors' new VComBench (312... [benchmark detail per abstract: 380 compositional tasks across text-to-video, image-to-video, and reference-to-video). Backbones tested include Wan, MiniMax H3, and Seedance 2.5.
**Limitation (≤3 sentences):** Gains are backbone-dependent and vary substantially in magnitude (46.8%→52.3% vs. 66.5%→69.3%), indicating the compiler's benefit depends on the underlying model's existing reliability, per the authors' reported numbers. The benchmark (VComBench) is newly introduced by the same authors, so independent validation is pending.

---

## ProxyGenBench: Benchmarking Proxy-Guided Video Generation
- **arXiv:** 2611.34457 · https://arxiv.org/abs/2611.34457
- **Submitted:** 2026-11-25 (v1)
- **Authors:** Zhenchen Tang, Haolin Lu, Songlin Yang, Xiaotong Zhao, Ran Zhang, Bo Peng, Shuai Li, Haotian Fan, Haobin Zhong, Yanni Zhang, Songlian Li, Ning Zhang, Xun Gao, Alan Zhao, Jing Dong
- **Qualifying affiliation(s):** Tencent — Xiaotong Zhao, Ran Zhang, Shuai Li, Haotian Fan, Haobin Zhong, Yanni Zhang, Songlian Li, Ning Zhang, Xun Gao, Alan Zhao (affiliation #4 in the paper's institution list)
- **Categories:** cs.CV, cs.AI
- **Open release:** demo — project page https://2kxx.github.io/ProxyGenBench/ (no code/dataset download link found)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ProxyGenBench is a benchmark for proxy-guided video generation, where structural proxies such as animated 3D blockouts guide a video generator's layout, motion, camera behavior, and event order. It contains 312 evaluation cases across 60 scenes and three scene tasks, varying proxy fidelity, text detail, and multimodal inputs, and evaluates five video generators with case-specific checklists. The authors report that proxies improve spatiotemporal control but more proxy detail can reduce completion quality, and strong structural adherence does not guarantee correct binding of text/image/audio conditions to entities and events.
**Purpose (≤3 sentences):** Structural proxies (e.g., 3D blockouts) are a promising way to control video generation layout and motion, but their effect on output quality and condition-binding was not previously benchmarked systematically. The authors aim to quantify the trade-offs of proxy-guided generation across varying proxy detail and modality combinations.
**Breakthrough (≤3 sentences):** The authors report a benchmark-level finding that more detailed structural proxies can paradoxically reduce completion quality, and that adherence to proxy structure does not guarantee correct text/image/audio-to-entity binding — a nuance not previously isolated, per the abstract.
**Tools & method (≤3 sentences):** The benchmark comprises 312 cases from 60 scenes across three scene tasks, with case-specific evaluation checklists, and evaluates five existing video generation models (including MiniMax-H3, per the paper's references). Proxy fidelity, text detail, and multimodal input variations are the controlled variables.
**Limitation (≤3 sentences):** As a benchmark paper, it evaluates existing third-party generators rather than proposing a new generation method, so findings are bounded by the five models tested. No code or dataset release was found on the project page at the time of review.

---

## Most of the Way There: Turning a Strong Video Prior into an Action-Conditioned World Model
- **arXiv:** 2611.34435 · https://arxiv.org/abs/2611.34435
- **Submitted:** 2026-11-25 (v1)
- **Authors:** Zanyi Wang, Xia Chen, Liu Liu, Xianglong Guo, Dengyang Jiang, Haodong Li, Tingyang Xiao, Wenhao Hu, Zhizhong Su
- **Qualifying affiliation(s):** Horizon Robotics — Xia Chen, Liu Liu, Tingyang Xiao, Zhizhong Su (also Zanyi Wang, UC San Diego/Horizon Robotics); FLAG: borderline (Horizon Robotics is a Chinese autonomous-driving/robotics chip and AI company; comparability to the core qualified-company list is a judgment call)
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** demo — project page https://xmz111.github.io/Dianjing/ (no code release found)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents Dianjing, which adapts a strong pretrained video foundation model (MiniMax H3, 33B parameters) into an action-conditioned world model for robotics with minimal added training. It freezes the backbone, trains only 0.34% of parameters, concentrates training at high-noise levels where motion/layout are determined, and adds native history conditioning, using about 65 hours of robot video from two embodiments. On the WorldOracle benchmark the authors report best results on four of five tracks and second place on AgiBot-Long.
**Purpose (≤3 sentences):** Video generators produce visually plausible futures but do not guarantee those futures reflect the physical effects of specific robot actions. The authors aim to convert an existing strong video prior into a usable action-conditioned world model for robot policy evaluation without extensive retraining.
**Breakthrough (≤3 sentences):** The authors report that a pretrained video prior is already "most of the way" to a working world model, and that lightweight action grounding — training only 0.34% of parameters — can close the remaining gap. They find via ablation that how training compute is distributed across diffusion noise levels matters more than the specific mechanism used to inject actions into the network.
**Tools & method (≤3 sentences):** Built by fine-tuning a frozen MiniMax H3 (33B) video backbone with unified action conditioning, noise-level-concentrated training, and native history conditioning; trained on roughly 65 hours of robot video spanning two robot embodiments. Evaluated on the WorldOracle benchmark against prior action-conditioned world models.
**Limitation (≤3 sentences):** The model ranked second (not first) on the AgiBot-Long track, per the authors' own reported results, indicating the approach does not uniformly dominate across all benchmark tracks. Training data is limited to about 65 hours across only two robot embodiments, which may bound generalization to other robot platforms.

---

## PostMesh: Self-Rewarded Preference Post-Training for Flow-Based Artist Mesh Generation
- **arXiv:** 2611.34319 · https://arxiv.org/abs/2611.34319
- **Submitted:** 2026-11-25 (v1)
- **Authors:** Gihyun Kwon
- **Qualifying affiliation(s):** Amazon — Gihyun Kwon (note: the paper's author-notes footnote states "Work done outside Amazon," so this may not represent Amazon-sponsored research; included per the listed affiliation but flagged for this caveat)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PostMesh is presented as the first post-training method for diffusion/flow-based artist mesh generators, which are much faster than autoregressive mesh generators but previously produced lower artist-quality output. It requires no artist-made ground truth: the generator trains on its own samples, scored by a reward comparing output to the dense input mesh, via a proposed "artistic mesh reward" and a multi-negative flow preference optimization method. After a short LoRA post-training step, the authors report PostMesh matches or beats slower autoregressive generators on most artist-mesh quality metrics and in a blind VLM preference test, at a fraction of the runtime.
**Purpose (≤3 sentences):** Autoregressive artist-mesh generators produce accurate, artist-style quad meshes but take tens to hundreds of seconds per mesh, while faster diffusion/flow-based generators sacrifice mesh quality. The author aims to close that quality gap for fast flow-based generators without requiring artist-labeled ground-truth training data.
**Breakthrough (≤3 sentences):** The author reports this is the first post-training approach for flow-based artist mesh generation that uses self-generated samples and a self-computed reward rather than artist ground truth, via a new "artistic mesh reward" and "multi-negative flow preference optimization."
**Tools & method (≤3 sentences):** The method uses a flow-based mesh generator fine-tuned with LoRA, a reward model comparing generated mesh output to the dense input geometry, and multi-negative flow preference optimization to propagate the reward signal; evaluation includes artist-mesh quality metrics and a blind VLM preference test against autoregressive baselines.
**Limitation (≤3 sentences):** The paper has a single author and no stated large-scale compute or dataset details beyond the self-rewarded training loop, per the available abstract/affiliation data. No code, weights, or project page release was found.

---

## Rehearse in 3D, Render in 2D: Physically Consistent and Editable Robot World Models
- **arXiv:** 2611.34288 · https://arxiv.org/abs/2611.34288
- **Submitted:** 2026-11-25 (v1)
- **Authors:** Guangyu Liu, Hanzhang Wang, Huijia Zhang, Hanbei Zhan, Linjie Hu, Bin Xiao, Xuan Zhou, Dong Zhang, Hanwei Liu
- **Qualifying affiliation(s):** Huawei Technologies Ltd. (listed among three affiliations — Tongji University, Huawei Technologies Ltd., Zhejiang University — exact per-author mapping not resolved in the HTML render); FLAG: borderline (Huawei's comparability to the core qualified-company list is a judgment call per the tracker's borderline-company guidance)
- **Categories:** cs.RO (primary), cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces RehearsalWorld, an editable robot world model built on "3D Interaction Rehearsal": a pretrained 3D point-flow motion prior is refined to preserve scene stability, object structure, and grasp attachments, then projected into geometric conditioning for a fine-tuned video generator. Because physical response is separated from visual synthesis, material properties and camera viewpoints can be edited independently. On real DROID grasping sequences, the authors report a 79%–84% reduction in gripper-relative offset versus PointWorld, with video prediction results of 23.92 dB PSNR and an FVD of 149.
**Purpose (≤3 sentences):** Existing robot world models couple physical dynamics and visual rendering tightly, making it hard to edit scene materials or camera viewpoint independently of the simulated physics. The authors aim to build a world model that rehearses interactions in 3D (for physical consistency) while rendering output in 2D (for editability).
**Breakthrough (≤3 sentences):** The authors report that decoupling a 3D point-flow-based physical rehearsal stage from a 2D video-rendering stage allows independent editing of material properties and camera viewpoint while preserving physical consistency — and quantify this with a 79%–84% gripper-relative-offset reduction over PointWorld on real DROID data.
**Tools & method (≤3 sentences):** The method combines a pretrained 3D point-flow model (motion prior) refined for scene/object/grasp stability, geometric conditioning derived from the refined rehearsal, and a fine-tuned video generator for 2D rendering; evaluated on real DROID robot grasping sequences using PSNR (23.92 dB) and FVD (149).
**Limitation (≤3 sentences):** Comparisons are reported against a single named baseline (PointWorld); broader baseline coverage is not described in the abstract. No code or project-page release was found, limiting independent verification of the reported numbers.

# Near-misses
- 2611.34932 · MERLoc: Robust Robot Localization in Dynamic Environments with Pose-Based Retrieval over 3D Gaussian Splatting References · off-topic (core contribution is robot localization/SLAM-style pose retrieval in dynamic environments; 3D Gaussian Splatting is used only as a pre-built map representation, with no 3D-content, world-model, character-animation, or game-engine angle). Note: affiliation (Disney Research, Switzerland, with ETH Zurich) would likely have qualified as a comparable top-tier industry lab if the paper were on-topic.
- 2611.34509 · Long-Horizon Planning with Latent World Models via Graph Anchors · no qualifying industry co-author, purely academic (University of Dhaka, Adelaide University, University of Oxford only)

Verification note: all 7 included papers above, plus the 2 near-misses, were checked against both the arXiv abstract page (title, authors, v1 date, categories, withdrawal status — none withdrawn) and the arXiv HTML page (author affiliation block, project/code links) as of 2026-11-26.
