**[A01] ReactWorld: Structuring Interaction Responses for Embodied Video Generation**
- **arXiv:** 2611.06120 · <https://arxiv.org/abs/2611.06120>
- **Submitted:** 2026-11-04
- **Authors:** Hanwei Liu et al.
- **Qualifying affiliation(s):** Huawei Technologies Co., Ltd. — Hanwei Liu, Huijia Zhang, Hanzhang Wang, Linjie Hu, Bin Xiao, Xuan Zhou, Dong Zhang (remaining authors: Tongji University / Zhejiang University, per paper's author block)
- **Categories:** cs.CV (primary), cs.RO
- **Open release:** none (project page only, no code/weights found) — <https://metaengine-world.github.io/ReactWorld/>
- **Shipped counterpart:** none found

**Summary:** Embodied video world models can predict scene changes from robot actions, but the paper argues generated object responses may not match task intent or contact dynamics.
**Purpose:** The authors target embodied video generation where object/environment reactions to a robot's actions must be physically and semantically plausible, not just visually coherent.
**Breakthrough:** The authors report an average score of 77.51 on RBench, 3.29 points above the PhysisForcing baseline with gains in all nine categories, and a Domain score of 86.98 and average of 81.87 on EZS-Bench.
**Tools & method:** The method is built on a frozen Wan2.2-I2V-A14B backbone, fine-tuned with rank-32 video LoRA (AdamW, lr 1e-5, effective batch size 32) on 8 H100 GPUs in BF16, using about 500K clips from AgiBot, RoVid-X, and internet robot videos; Qwen3-VL and SAM3/CoWTracker are used for role annotation and object/trajectory extraction, and Qwen3-VL/Qwen2.5-VL serve as RBench/EZS-Bench evaluators.
**Limitation:** The authors state that "ReactWorld currently anticipates interactions using a 2D response representation," leaving 3D interaction relations unmodeled, and name exploring temporally consistent 3D motion representations as future work.
