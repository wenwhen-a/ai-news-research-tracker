**[A04] DIDO: Distilling Interaction-Centric Dynamics into One-Step Denoising for World Action Models**
- **arXiv:** 2609.15570 · <https://arxiv.org/abs/2609.15570>
- **Submitted:** 2026-09-14 (v1)
- **Authors:** Jing Lyu, Shuanghao Bai, Runze Xiao, Zhenyu Liao, Wenxing Tan, Zihan Tang, Ruochuan Shi, Cheng Peng, Yuheng Ji, Yihao Wang, Badong Chen, Pengwei Wang, Zhongyuan Wang, Xiaoguang Zhao
- **Qualifying affiliation(s):** Amazon — Zhenyu Liao
- **Categories:** cs.RO
- **Open release:** code — <https://github.com/LoveJu1y/DIDO-WAM/> (project page: <https://loveju1y.github.io/DIDO/)>
- **Shipped counterpart:** none found

**Summary:** DIDO distills the converged dynamics of a multi-step video-based World Action Model into a single denoising step to reduce closed-loop control latency in robotic manipulation.
**Purpose:** The authors target the added latency that iterative denoising in video generation models introduces for closed-loop robot control.
**Breakthrough:** The authors report that in one-step denoising, static background structure forms early while the gripper and manipulated object remain blurry after the first step, motivating their interaction-centric distillation approach; they report 99.0% success on LIBERO, 76.6% on LIBERO-Plus, and 92.0% on RoboTwin, with transfer to long-horizon and real-world manipulation tasks.
**Tools & method:** The method distills a robot-adapted four-step teacher into a one-step student using distribution matching plus interaction-centric representation guidance, leveraging a pretrained DINOv3 encoder for feature alignment; it is evaluated on LIBERO, LIBERO-Plus, RoboTwin, and real-world robot manipulation.
**Limitation:** The authors state that interaction-centric reasoning relies on bounding-box supervision for the gripper/object, which may be insufficient for multi-object interaction, deformable objects, or fine-grained contact geometry, and can be noisy under severe occlusion.
