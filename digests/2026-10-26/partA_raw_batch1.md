## CompMVR: Compression-Aware Multi-View Restoration Using Diffusion Models for Geometrically Consistent 3D Reconstruction
- **arXiv:** 2610.32800 · https://arxiv.org/abs/2610.32800
- **Submitted:** 23 October 2026 (v1)
- **Authors:** Dong-hwi Kim, Chaewon Moon, Hojun Song, Dongbeom Kim, Junyeong Jang, Aro Kim, Gahyeon Kim, Heejung Choi, Jehee Kim, Gianella Cravioto, Sohyun Lee, Gyeongjin Choi, EunHye Jeong, Soo Ye Kim, Jaehyup Lee, Sang-hyo Park
- **Qualifying affiliation(s):** Adobe — Soo Ye Kim (Adobe Research, USA; corresponding author). Remaining authors are affiliated with Kyungpook National University, Republic of Korea.
- **Categories:** cs.CV
- **Open release:** code (project page states code and data are available: https://mchaewon.github.io/CompMVR-project-page/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper identifies compression-induced cross-view geometric inconsistency as a failure mode in multi-view 3D reconstruction, where lossy compression disrupts feature matching and correspondence across views. It proposes CompMVR, a compression-aware multi-view diffusion framework that jointly restores compressed views while preserving cross-view consistency using learned compression priors and cross-view correspondence. The authors also construct compressed-view datasets for evaluation.
**Purpose (≤3 sentences):** Lossy compression of multi-view imagery introduces view-dependent artifacts that break geometric consistency across views, degrading downstream 3D tasks such as camera pose estimation and novel view synthesis. Prior restoration methods were not designed to preserve this cross-view consistency.
**Breakthrough (≤3 sentences):** The authors report consistent gains in restoration quality and downstream 3D reconstruction performance across multiple datasets, codecs, and compression levels compared to baseline restoration approaches. The paper is accepted as a SIGGRAPH Asia 2026 technical paper.
**Tools & method (≤3 sentences):** The method is a diffusion-based multi-view restoration framework combining learned compression priors with cross-view correspondence; the authors built new compressed-view datasets to evaluate it. No specific hardware/compute details were extracted.
**Limitation (≤3 sentences):** Not stated by the authors (not surfaced in the available abstract/summary text).

## Past as State, Present as Attention: Persistent-State Blockwise Flow Matching for Long-Horizon Co-Speech Motion Generation
- **arXiv:** 2610.32373 · https://arxiv.org/abs/2610.32373
- **Submitted:** 23 October 2026 (v1)
- **Authors:** Yi Liu, Xiangyue Zhang, Jianfang Li, Jia Ma, Yisheng He, Jianqiang Ren
- **Qualifying affiliation(s):** Alibaba Group — Jianfang Li (corresponding author), Yisheng He, Jianqiang Ren, and Yi Liu (listed with a dual Tongji University / Alibaba Group affiliation). Xiangyue Zhang is affiliated with The University of Tokyo; Jia Ma with Tongji University.
- **Categories:** cs.CV (primary); cs.GR; cs.MM
- **Open release:** none found (no code/project link located on the abstract or HTML page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper tackles long-horizon co-speech motion generation, where existing segment-by-segment methods either drift (short recent-frame conditioning) or become costly and hard to train (ever-growing explicit histories). The authors propose PASPA, built on the principle that past motion carries a slowly-changing style that can be compactly summarized while the current segment needs detailed, fast-dynamics modeling. PASPA summarizes history in an inter-block persistent state and models the current segment via intra-block bidirectional self-attention within a blockwise flow-matching framework.
**Purpose (≤3 sentences):** Long-duration co-speech motion generation must remain temporally coherent and stylistically consistent, but existing segment-based generation approaches either drift over time or require expensive, hard-to-learn long explicit histories.
**Breakthrough (≤3 sentences):** The authors report state-of-the-art FGD (Fréchet Gesture Distance) on public benchmarks along with improved style preservation over long sequences compared to prior methods. The paper is noted as accepted at NeurIPS 2026.
**Tools & method (≤3 sentences):** The method uses blockwise flow matching with multi-block supervision for training on variable-length histories, prefill-decode state caching for efficient rollout, and hybrid classifier-free guidance for history and speech conditioning.
**Limitation (≤3 sentences):** Not stated by the authors (not surfaced in the available abstract/summary text).

## Easy-3Dfy: Object-Level Geometric Composition for Single-Image 3D Scene Construction
- **arXiv:** 2610.32250 · https://arxiv.org/abs/2610.32250
- **Submitted:** 23 October 2026 (v1)
- **Authors:** Ziang Zhang, Wenyou Yi, Zehan Wang, Jiachen Xu, Xintong Han, Chunchao Guo, Zhou Zhao
- **Qualifying affiliation(s):** Tencent — Jiachen Xu, Xintong Han, Chunchao Guo (and Ziang Zhang, Zehan Wang hold dual Zhejiang University / Tencent affiliations). Wenyou Yi and Zhou Zhao are affiliated with Zhejiang University.
- **Categories:** cs.CV, cs.AI
- **Open release:** none found (no code/project link located on the abstract or HTML page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses single-image 3D scene construction, noting that existing end-to-end methods (e.g., SAM-3Dfy) can reconstruct 3D assets and layouts but struggle with fine scene geometry and asset quality. The authors propose Easy-3Dfy, a workflow that separates object generation from scene layout estimation so each sub-problem can use a specialized model, with an RPF-based aligner matching object-local meshes to partial scene pointmaps to recover object placement.
**Purpose (≤3 sentences):** Single-image 3D scene reconstruction needs both high-quality individual object geometry and accurate scene-level spatial layout, which end-to-end methods trade off against each other.
**Breakthrough (≤3 sentences):** The authors report that Easy-3Dfy outperforms SAM-3Dfy on several geometric metrics on the Scene-Maker and 3D-FUTURE200 benchmarks, without requiring complete scene-level supervision.
**Tools & method (≤3 sentences):** The method decouples object generation (via a dedicated 3D object generator) from scene layout estimation, then uses an RPF-based alignment procedure to fit object meshes into partial scene pointmaps; evaluated on Scene-Maker and 3D-FUTURE200.
**Limitation (≤3 sentences):** Not stated by the authors (not surfaced in the available abstract/summary text).

# Near-misses
- 2610.32978 · SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning · no HTML version found (404 at both /html/2610.32978 and /html/2610.32978v1), affiliation unverifiable; authors (Yuhan Liu, Lianhui Qin, Shenji Wan) appear academic (Lianhui Qin is UCSD faculty)
- 2610.32977 · UniAction: Unified Action Conditioning for World Models · academic-only, all four authors (Bowen Xue, Zizhang Li, Hong-Xing Yu, Jiajun Wu) affiliated with Stanford University, no industry co-author confirmed
- 2610.32414 · When Does Dynamics Randomization Test Context Inference? · off-topic: generic RL/meta-learning methodology on context inference and dynamics randomization, not tied to 3D/world-model applications per the gate; also no industry (Microsoft) affiliation confirmed
- 2610.32230 · Towards Effective and Transferable Physical Camouflage against Multi-View BEV-based 3D Perception in Autonomous Driving · off-topic: autonomous-driving adversarial-camouflage/perception security, explicitly excluded by the gate
- 2610.32177 · Ψ-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model · academic-only, all eight authors (Khai Loong Aw, Klemen Kotar, Baihan Zhang, Yifan Liu, Lilian Chen, Atlas Kazemian, Rahul Venkatesh, Daniel Yamins) affiliated with Stanford University, no industry (Google) co-author confirmed
- 2610.32075 · RADIANT: Object-Centric Feed-Forward Global Illumination · academic-only, all five authors (Sarah Zhang, Zhiyang Dou, Minghao Guo, Benjamin Tod Jones, Wojciech Matusik) affiliated with MIT CSAIL, no industry (ByteDance) co-author confirmed
- 2610.31801 · KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations · off-topic: robot-demonstration segmentation is robotics manipulation/imitation-learning tooling, not 3D/world-model/character-animation/game-engine per the gate
