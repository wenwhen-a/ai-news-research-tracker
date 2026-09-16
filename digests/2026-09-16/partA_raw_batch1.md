---
## World Models for Embodied Intelligence: From Plausible to Controllable to Actionable
- **arXiv:** 2609.16697 · https://arxiv.org/abs/2609.16697
- **Submitted:** 2026-09-15 (v1)
- **Authors:** Nanjie Yao, Hao Wang, Chong Cheng, Zhikang Chen, Wenzhe Li, Jiafei Lyu, Li Shen, Peilin Zhao, Zongqing Lu, Gao Huang, Steven Hoi, Dacheng Tao, Deheng Ye
- **Qualifying affiliation(s):** Tencent — Jiafei Lyu; Alibaba Group — Steven Hoi, Dacheng Tao, Deheng Ye
- **Categories:** cs.RO; cs.AI
- **Open release:** none (project page only, no code/weights/demo stated) — https://3dagentworld.github.io/EmbodiedWM/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** This survey proposes a three-tier framework — Plausible, Controllable, Actionable — for organizing and evaluating world models used in embodied AI, tied to a 3×4 "grounding–improvement" matrix. It reviews applications across manipulation, navigation, locomotion, autonomous driving, and embodied learning.
**Purpose (≤3 sentences):** The authors aim to give the field a shared way to evaluate world models by what they contribute to downstream behavior rather than by visual realism alone.
**Breakthrough (≤3 sentences):** The authors report that a "Plausible" model preserves task-relevant temporal, geometric, or physical structure; a "Controllable" model additionally predicts how interventions alter that structure; and an "Actionable" model further translates predictions into measurable gains in planning, action, learning, evaluation, verification, recovery, or data selection.
**Tools & method (≤3 sentences):** The paper is a literature survey structured around this three-tier taxonomy and the 3×4 grounding–improvement matrix, covering manipulation, navigation, locomotion, and autonomous driving applications; it introduces no new model, dataset, or benchmark of its own.
**Limitation (≤3 sentences):** The authors identify open problems including persistent state drift, modeling causal action effects, decision utility under computational budget constraints, joint grounding, uncertainty calibration, and reproducibility of evaluation; no dedicated "Limitations" section is present.

---
## Beyond Gestures: Estimating Full Hand Pose and Contact Forces from Wrist-Worn Pressure Sensor Array
- **arXiv:** 2609.16518 · https://arxiv.org/abs/2609.16518
- **Submitted:** 2026-09-15 (v1)
- **Authors:** Svetoslav Kolev, Lingni Ma, Michael Goesele, Renzo De Nardi, Jakob Engel, Richard Newcombe
- **Qualifying affiliation(s):** Meta Reality Labs Research — all authors
- **Categories:** cs.HC; cs.RO
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents a wrist-worn device using flexible capacitive sensor arrays (no electrical skin contact required) paired with a recurrent neural network to recover continuous full-hand pose and distributed contact force. It is validated against optical motion-capture and tactile gloves across finger-motion and object-manipulation tasks.
**Purpose (≤3 sentences):** The authors aim to complement camera-based hand tracking (e.g. egocentric cameras) with a wearable that also reports contact force and keeps working when the hand is occluded from view.
**Breakthrough (≤3 sentences):** The authors report the pressure signatures from muscle contraction and tendon displacement at the wrist correlate with hand movement and interaction forces; measured performance is 4.6° mean finger-joint MAE for isolated motion and per-finger contact-force estimation at R²=0.57 across users, improving to R²=0.75 when conditioned on external pose information.
**Tools & method (≤3 sentences):** A recurrent neural network is trained on synchronized data from a wrist-worn flexible capacitive pressure-sensor array, optical motion-capture, and tactile gloves, across isolated finger motions and everyday object-manipulation tasks with four users.
**Limitation (≤3 sentences):** The authors state that intrinsic hand muscles are largely invisible from forearm sensors, limiting observability of thumb motion; cross-user generalization could not be established due to small cohort size and mixed hardware; and tactile-glove ground truth does not cover lateral, dorsal, and webbing surfaces, and per-taxel force accuracy is bounded by the reference system.

---
## DIDO: Distilling Interaction-Centric Dynamics into One-Step Denoising for World Action Models
- **arXiv:** 2609.15570 · https://arxiv.org/abs/2609.15570
- **Submitted:** 2026-09-14 (v1)
- **Authors:** Jing Lyu, Shuanghao Bai, Runze Xiao, Zhenyu Liao, Wenxing Tan, Zihan Tang, Ruochuan Shi, Cheng Peng, Yuheng Ji, Yihao Wang, Badong Chen, Pengwei Wang, Zhongyuan Wang, Xiaoguang Zhao
- **Qualifying affiliation(s):** Amazon — Zhenyu Liao
- **Categories:** cs.RO
- **Open release:** code — https://github.com/LoveJu1y/DIDO-WAM/ (project page: https://loveju1y.github.io/DIDO/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** DIDO distills the converged dynamics of a multi-step video-based World Action Model into a single denoising step to reduce closed-loop control latency in robotic manipulation. It combines distribution-matching distillation with interaction-centric visual reasoning tokens focused on the gripper and manipulated object.
**Purpose (≤3 sentences):** The authors target the added latency that iterative denoising in video generation models introduces for closed-loop robot control.
**Breakthrough (≤3 sentences):** The authors report that in one-step denoising, static background structure forms early while the gripper and manipulated object remain blurry after the first step, motivating their interaction-centric distillation approach; they report 99.0% success on LIBERO, 76.6% on LIBERO-Plus, and 92.0% on RoboTwin, with transfer to long-horizon and real-world manipulation tasks.
**Tools & method (≤3 sentences):** The method distills a robot-adapted four-step teacher into a one-step student using distribution matching plus interaction-centric representation guidance, leveraging a pretrained DINOv3 encoder for feature alignment; it is evaluated on LIBERO, LIBERO-Plus, RoboTwin, and real-world robot manipulation.
**Limitation (≤3 sentences):** The authors state that interaction-centric reasoning relies on bounding-box supervision for the gripper/object, which may be insufficient for multi-object interaction, deformable objects, or fine-grained contact geometry, and can be noisy under severe occlusion. They also note training requires three separate optimization phases (added complexity/cost), and the one-step model's predictive capability remains bounded by the quality of its four-step teacher.

---
## World-Action Models for Robot Learning and Control: A Survey
- **arXiv:** 2609.16074 · https://arxiv.org/abs/2609.16074
- **Submitted:** 2026-09-13 (v1)
- **Authors:** Zuxing Lu, Hongjia Zhai, Guanzhi Wang, Huajian Zeng, Jiaqi Yang, Jingyu Liu, Lei Cheng, Yuantai Zhang, Yuheng Qiu, Zezhou Cheng, Ivan Laptev, Danfei Xu, Benjamin Riviere, Giuseppe Loianno, Eric Xing, Xingxing Zuo
- **Qualifying affiliation(s):** Amazon (Amazon FAR) — Yuheng Qiu
- **Categories:** cs.RO; cs.CV
- **Open release:** none (project/awesome-list page only) — https://rcl-robotics.github.io/Awesome-World-Action-Models
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** This survey reviews World-Action Models (WAMs), which couple future-world prediction with executable action generation for robots, and relates them to conventional world models, model-based RL, and Vision-Language-Action policies. It organizes existing approaches by representation, transition modeling, action interfaces, architecture, training pipeline, and data modality.
**Purpose (≤3 sentences):** The authors aim to clarify how WAMs differ from and relate to adjacent paradigms (world models, model-based RL, VLA policies) and to organize the fast-growing literature via a shared taxonomy.
**Breakthrough (≤3 sentences):** The authors report identifying persistent open challenges across the surveyed literature: action alignment, spatial and multi-view consistency, memory for long-horizon tasks, and efficient inference for real-time operation, spanning manipulation, navigation, and autonomous-driving applications.
**Tools & method (≤3 sentences):** The paper is a literature survey and taxonomy; it curates and categorizes existing WAM approaches rather than introducing a new model, dataset, or benchmark.
**Limitation (≤3 sentences):** The authors state that action grounding, world-action factorization, spatial/multi-view consistency, long-horizon memory, neural simulation fidelity, and inference latency remain open problems in the field; no dedicated "Limitations" section is present.

---
## GeomVLA: Unifying Scene, Motion, and Action in 3D
- **arXiv:** 2609.13812 · https://arxiv.org/abs/2609.13812
- **Submitted:** 2026-09-12 (v1)
- **Authors:** Ziyin Xiong, Nikos Gkanatsios, Moritz Reuss, Katerina Fragkiadaki
- **Qualifying affiliation(s):** NVIDIA — Moritz Reuss
- **Categories:** cs.RO
- **Open release:** none (project page only, no code/weights/demo stated) — https://ziyin-xiong.github.io/geomvla.io/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GeomVLA is a Vision-Language-Action model that unifies perception, latent scene-motion prediction, and action generation within a shared robot-centric 3D coordinate frame. It lifts pretrained VLM features into spatially grounded 3D tokens and uses a 3D Scene Trajectory Denoiser to predict how scene points will move.
**Purpose (≤3 sentences):** The authors aim to ground VLA policies in explicit 3D geometry and motion so that action generation can be conditioned on predicted scene dynamics rather than raw 2D image features alone.
**Breakthrough (≤3 sentences):** The authors report state-of-the-art results on the CALVIN benchmark and competitive performance on LIBERO and RoboTwin2.0, achieved without large-scale robot-action pretraining, and demonstrate real-world manipulation across eight tasks (accepted to CoRL 2026).
**Tools & method (≤3 sentences):** The method lifts pretrained vision-language features into 3D using depth and camera calibration, trains a 3D Scene Trajectory Denoiser with SpatialTrackerV2 pseudo-labels via a motion-weighted rectified-flow objective, and conditions action generation on geometry-aware attention over these motion features.
**Limitation (≤3 sentences):** The authors state accuracy depends on precise camera calibration, with depth or extrinsic-calibration errors degrading geometric representations especially in real-world settings. They also note the model is trained only on benchmark demonstrations without large-scale robot-action pretraining or cross-embodiment data, and reasons through latent geometric trajectories rather than explicit language-based reasoning, limiting hierarchical task decomposition.

---
## Spheriverse: 3D Scene Understanding from Spherical Observations in the Wild
- **arXiv:** 2609.09012 · https://arxiv.org/abs/2609.09012
- **Submitted:** 2026-09-08 (v1)
- **Authors:** Fei Teng, Sheng Wu, Mengfei Duan, Guoqiang Zhao, Junhui Ma, Kai Luo, Siyu Li, Hao Shi, Zhiyong Li, Kailun Yang
- **Qualifying affiliation(s):** FLAG: borderline — Ant Group — Hao Shi (Ant Group is an Alibaba-affiliated fintech spinoff, not Alibaba itself; other co-authors are affiliated with Hunan University and Zhejiang University of Science and Technology/Zhejiang University)
- **Categories:** cs.CV; cs.RO; eess.IV
- **Open release:** code (stated "will be available") — link not yet live per paper text; dataset/benchmark also to be released
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces Spheriverse, a real-world dataset of 64,400 temporally aligned spherical image–LiDAR pairs across 644 sequences, and SphereOcc, a framework for 3D occupancy prediction, semantic mapping, and object detection from spherical (360°) observations. It benchmarks over 30 existing methods on the new dataset.
**Purpose (≤3 sentences):** The authors aim to bridge the "cross-space representation gap" between angular spherical imagery and the Cartesian voxel space used for dense 3D scene understanding, which existing perspective-camera-focused methods do not address.
**Breakthrough (≤3 sentences):** The authors report SphereOcc achieves 13.91% mIoU and 24.65% GeoIoU on occupancy prediction, versus 12.21% mIoU (TPVFormer) and 22.55% GeoIoU (SurroundOcc) from the strongest prior methods — relative gains of 13.9% and 9.3% — and ranks first across all five scene categories in their benchmark.
**Tools & method (≤3 sentences):** SphereOcc uses Cartesian–Spherical Representation Remodeling (CSRR) to align Cartesian voxel features with spherical range–azimuth geometry, and Spherical Evidence Re-querying (SER) to retrieve semantic evidence via the range–height–azimuth mapping induced by spherical imaging; evaluation uses a 360°-horizontal/136.7°-vertical camera rig with a 128-beam LiDAR.
**Limitation (≤3 sentences):** The paper does not include a dedicated "Limitations" section, but discusses (as acknowledged challenges) vehicle camouflage, semantic ambiguity in rural environments, low-light degradation, lens contamination, and complex multi-level structures across the full spherical field of view.

# Near-misses
- 2609.16679 · AI for Games in the Foundation Model Era · academic-only — all authors affiliated with National University of Singapore / Nanyang Technological University; Tencent, Ubisoft, and Roblox appear only as cited game products/prior work (e.g. "Roblox Cube", "Ubisoft Teammates"), not as author affiliations.
- 2609.16684 · MEgoVista: Multi-view Ego-aware Motion Estimation for Metric 4D Hands and Head in the Wild · academic-only — authors are affiliated with Northwestern Polytechnical University, Xi'an Jiaotong University, and Maniformer (a startup not on the qualified-company list); Apple appears only in a citation ("manipulation using Apple Vision Pro"), not as an author affiliation.
- 2609.12614 · ProClosure: Hierarchical Room-Object Assignment using Progressive Boundary Closure from Monocular Video · academic-only — all four authors are affiliated with Clarity Lab, Department of CSE, IIT Jodhpur; no ByteDance or other qualifying affiliation found anywhere in the HTML (author block, footnotes, or acknowledgments).
