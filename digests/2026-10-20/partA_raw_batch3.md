## MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes
- **arXiv:** 2610.25345 · https://arxiv.org/abs/2610.25345
- **Submitted:** 2026-10-18
- **Authors:** Yifei Wang, Wei Tian, Wenhua Bao, Jia Zhou, Hanshi Wang, Fudong Ge, Jianhua Wu, Shuai Yuan, Zhipeng Zhang, Xingliang Liu, Xianming Zeng, Jianyun Xu, Bingzhao Gao
- **Qualifying affiliation(s):** Zaofu Intelligent Technology Co., Ltd. — Yifei Wang (internship), Wenhua Bao, and other co-authors; project leaders are drawn from this company per the paper's footnote. FLAG: borderline — Zaofu is a Shanghai L4 autonomous-driving/robotaxi joint venture (founded 2025 by Hello, Ant Group and CATL, reportedly >RMB 3B initial investment) and not on the explicit qualifying list.
- **Categories:** cs.CV
- **Open release:** none (no code/weights statement); project page at https://yfwang0824.github.io/mcsplat-project/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** MCSplat is a feed-forward 3D Gaussian Splatting method for reconstructing driving scenes from sparse surround-view camera images. It separates per-camera appearance (exposure, ISP, lighting) from geometry learning by building a shared canonical appearance space from depth-guided cross-camera correspondences. A multi-scale Bilateral Grid Transformer then recovers each camera's raw appearance so photometric supervision does not corrupt the learned geometry.

**Purpose (≤3 sentences):** The paper targets two failure modes of feed-forward driving-scene Gaussian splatting: cross-camera exposure/ISP/lighting differences being wrongly absorbed into scene geometry, and normal-based geometric supervision becoming unreliable near depth edges.

**Breakthrough (≤3 sentences):** The authors report that weighting surface self-supervision with a Fisher-information-based uncertainty estimated from photometric sensitivity improves cross-view depth consistency, surface-normal agreement, and reduces geometric artifacts. They report better reconstruction quality and generalization across driving datasets versus baselines; an ablation shows a geometry–photometry trade-off (removing the geometry loss raises raw-target PSNR to 30.76 dB but degrades geometry).

**Tools & method (≤3 sentences):** Evaluated on the Waymo Open Dataset and nuScenes; trained using 16 NVIDIA H20 GPUs. Because LiDAR is too sparse for dense normal ground truth, the authors use MoGe-2 predictions as pseudo-normal references.

**Limitation (≤3 sentences):** The authors state future work will explore stronger temporal appearance modeling and explicit modeling of ISP parameters. The paper's own ablation notes a geometry–photometry trade-off: removing the geometry loss improves raw-image PSNR but worsens geometric accuracy.

---

## Map2Vid: Embodied Navigation Video Generation with Human-Friendly Motion Control
- **arXiv:** 2610.25223 · https://arxiv.org/abs/2610.25223
- **Submitted:** 2026-10-18
- **Authors:** Yulin Dai, Yuqian Fu, Tianwen Qian, Zhen Xing, Bojia Zi, Xiaoling Wang
- **Qualifying affiliation(s):** Alibaba Group — Zhen Xing (Qwen Team, Alibaba Group, Hangzhou)
- **Categories:** cs.CV
- **Open release:** none (paper mentions only an examples directory in supplementary material; no stated code/weights release)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Map2Vid frames embodied-navigation video generation as turning a bird's-eye-view (BEV) map of a scene and intended route into an egocentric video, as an alternative to vague text prompts or low-level camera-trajectory controls. The authors built Map2Vid-100K, a dataset of about 117.8K navigation sequences (94.2K train / 23.6K eval, ~211.6 hours of video) across 61 indoor scenes, pairing egocentric video with BEV maps, camera trajectories, and language instructions. Their framework fuses multiple control signals with curriculum training that gradually reduces reliance on non-map inputs, so it works with full conditioning or the map alone.

**Purpose (≤3 sentences):** The authors argue existing navigation-video controls are poorly suited to embodied navigation: text prompts are spatially vague, and camera-trajectory control relies on low-level motion parameters that are not human-friendly.

**Breakthrough (≤3 sentences):** The authors report that BEV-map control is a viable direction for navigation video generation across several tested foundation generation models, with curriculum training letting the model run on map-only input at inference. In zero-shot cross-scene and Sim2Real settings, geometric/trajectory control held up better than visual quality, which degraded sharply.

**Tools & method (≤3 sentences):** Benchmark built by replaying R2R trajectories in the Habitat simulator over Matterport3D scenes; evaluated with large DiT-based video generation backbones. The dataset (Map2Vid-100K) pairs BEV maps, camera trajectories, and language instructions with egocentric video.

**Limitation (≤3 sentences):** The authors state their conclusions are "limited to a simulation-based benchmark rather than real-world deployment," and that the dataset covers only static indoor layouts without dynamic obstacles or human-agent interaction. They also note precise orientation at sharp turns and translational stability remain challenging, with observed under/over-rotation and translation drift, plus substantial compute overhead from the large DiT backbones.

---

## Latent World Models Should Plan with Distances Along the Latent Manifold
- **arXiv:** 2610.25013 · https://arxiv.org/abs/2610.25013
- **Submitted:** 2026-10-18
- **Authors:** Zunzhi You, Linwei Tao, Siyu Xu, Yunke Wang, Chang Xu
- **Qualifying affiliation(s):** Apple — Linwei Tao (Machine Learning Research, Apple, in addition to University of Sydney)
- **Categories:** cs.LG (cross-listed cs.RO)
- **Open release:** code · https://github.com/youzunzhi/ngc-latent-manifold
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper studies latent world models (e.g., LeWM) that plan by picking action sequences whose predicted latent is closest to a goal latent under Euclidean (L2) distance. The authors find L2 cost only works well near the goal; farther away it creates misleading low-cost regions that trap planners even though the latents still encode the true physical state. They propose the Neighborhood Graph Cost (NGC), which measures shortest-path distance over a mutual nearest-neighbor graph built from training latents, used only as the terminal planning cost with no retraining required.

**Purpose (≤3 sentences):** The goal is to fix long-horizon planning failures in latent world models caused by treating the latent space as globally Euclidean when it instead sits on a curved, low-dimensional manifold.

**Breakthrough (≤3 sentences):** The authors report NGC improves LeWM's planning success on all four tested benchmarks and nearly solves TwoRoom and Reacher; at the farthest goal offsets tested it reaches 95% and 100% success versus 27% and 81% for the L2 baseline. NGC requires no retraining of the world model, only a different terminal cost at planning time.

**Tools & method (≤3 sentences):** Evaluated on four benchmarks: TwoRoom, Reacher, Cube, and PushT, built on the LeWM latent world model. NGC builds a mutual nearest-neighbor graph over training-set latents and computes shortest-path (graph) distance as the terminal cost.

**Limitation (≤3 sentences):** The authors state NGC still falls short on the contact-rich Cube and PushT tasks even with an oracle predictor, because nearby physical states (e.g., a gripper near contact) can respond very differently to the same action, and contact introduces asymmetric transitions an undirected graph cannot express. They also note generalization to goals or environments outside the graph's coverage "remains untested."

---

## SwitchSplat: Learning Discrete Object States from Casually Captured Scenes
- **arXiv:** 2610.24812 · https://arxiv.org/abs/2610.24812
- **Submitted:** 2026-10-17
- **Authors:** Yizheng Xie, Yalda Foroutan, George Shramko, Daniel Rebain, Shrisudhan Govindarajan, Andrea Tagliasacchi
- **Qualifying affiliation(s):** Wayve Labs (Vancouver) — Daniel Rebain, Shrisudhan Govindarajan, Andrea Tagliasacchi. FLAG: borderline — Wayve is a UK autonomous-driving software company (backed by $1B+ rounds from NVIDIA, Microsoft and SoftBank) not on the explicit qualifying list, though comparable in standing.
- **Categories:** cs.CV (cross-listed cs.GR)
- **Open release:** none found for code/dataset; project page at https://switchsplat.github.io
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SwitchSplat extends 3D Gaussian Splatting to casually captured scenes containing discrete object-state interactions (e.g., opening a door, toggling a switch), which standard static 3DGS and time-conditioned 4DGS methods can't model without tying state to a specific recorded timestamp. It decomposes the scene into a shared static base plus per-object "slots," each modeling one interactable object's on/off states, with a differentiable Gaussian-to-slot assignment learned directly from video without manual annotation. At inference, users can recombine slot states and render from any viewpoint, including unseen state combinations.

**Purpose (≤3 sentences):** The goal is to let 3D Gaussian Splatting represent scenes with discrete interactable object states from ordinary casual video capture, rather than only replaying the exact recorded state sequence as 4DGS does.

**Breakthrough (≤3 sentences):** The authors report SwitchSplat outperforms static and dynamic (4DGS-style) baselines on a new casual-capture dataset and can render state combinations that were never observed together during capture. The method assumes binary object states and single-operator, one-free-hand capture.

**Tools & method (≤3 sentences):** Uses a VLM to seed the number of interactable slots and approximate interaction timing, with per-part geometry learned via a differentiable Gaussian-to-slot assignment. Evaluated on a new custom casual-capture dataset (indoor and outdoor scenes); outdoor evaluation excludes dynamic background regions (foliage, sky, street activity) from some metrics.

**Limitation (≤3 sentences):** The authors state the method assumes binary (not continuous or multi-valued) object states and single-operator capture, and that "fully unsupervised discovery of both the number and timing of interactions from raw video remains an open problem" since slot count/timing are VLM-seeded. The work is scoped to novel-view synthesis; combining it with physics or generative priors for scene editing/simulation is left to future work.

---

# Near-misses
- 2610.25261 · GOFusion: Real-Time Gaussian-Occupancy Submap Fusion for Fisher-Informed Autonomous Robot Navigation · no qualifying industry co-author — all authors are at TU Munich, ETH Zurich, University of Toronto/Vector Institute; Huawei Technologies appears only in the Acknowledgments as a funder, not in the author affiliation block.
- 2610.25245 · GeoV2V: Geometry-Grounded Video Diffusion Model for Driving Scene Generation · no qualifying industry co-author — all authors are at Shanghai Jiao Tong University; one author's listed affiliation (Shanghai Pudong Development Bank) is explicitly footnoted as "work done while at" SJTU, and a bank is not a relevant qualifying company regardless.
- 2610.25068 · Localization and Neural Splatting on the Edge: An FPGA Scene Memory for Robots · no qualifying industry co-author — all four authors are at University of Georgia; AMD/Xilinx appears only as the hardware platform (Kria KR260), not an author affiliation.
- 2610.24965 · Meta Inverse Prompting for Video Generative Models · no qualifying industry co-author — both authors are at Korea University; "Meta" in the title refers to meta-learning, not Meta the company.
- 2610.24869 · SpriteStage: Long Horizon Animation Generation via Progressive Scene Programming and Replay · no qualifying industry co-author — authors are at Beijing Institute of Technology and University of Auckland; no Tencent affiliation found.
- 2610.24534 · Structured Latent Dynamics for Long-Horizon Embodied World Models · no qualifying industry co-author found — the only institution confirmed in the (partially garbled) author/affiliation block is Tsinghua University; NVIDIA appears only as a cited third-party model (Cosmos-Predict2.5-2B), not an author affiliation, and no corroborating source could be found for an NVIDIA affiliation.
- 2610.24177 · Self-Improving Video-to-Action Models · no qualifying industry co-author — all four authors are at MIT (CSAIL), with @mit.edu emails; no Google affiliation found.
- 2610.23953 · Functionalizing AI-Generated 3D Shapes via Interior Geometry Construction · no qualifying industry co-author — all authors are at Singapore University of Technology and Design / Singapore Institute of Technology; Tencent appears only in a citation of the Hunyuan3D tool, not as an author affiliation.

Verification note: each of the 12 candidates was checked against its arXiv abstract page (title, authors, v1 date, categories, withdrawal status) and its arXiv HTML version (author/affiliation block, abstract, and — for the 4 items written up in full — limitations/conclusion sections and code/release statements). All 12 HTML versions were accessible (no "affiliation unverifiable" cases). All v1 dates fall within the 30-day window (2026-09-20 to 2026-10-20). Double-verification pass completed for the 4 qualifying/borderline entries above.
