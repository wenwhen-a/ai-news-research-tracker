**[A09] Coda-DaVinci: Reimagining Video Generation with Code2Video**
- **arXiv:** 2611.26595 · <https://arxiv.org/abs/2611.26595>
- **Submitted:** 2026-11-19
- **Authors:** Yiyan Ji et al.
- **Qualifying affiliation(s):** Kuaishou — Yiyan Ji, Qixun Wang, Yang Shi, Yushuo Guan, Zihao Wang, Yuanxing Zhang, Pengfei Wan (listed under "KlingAI Research," Kuaishou's Kling AI research division)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** The paper studies Code2Video, where a coding agent builds a 3D proxy scene (in Blender) to guide video generation, and runs controlled experiments plus blinded human evaluation to see how proxy granularity, physics simulation, and prompting affect output quality.
**Purpose:** The authors argue video models still struggle with detailed instructions, state persistence across camera revisits, and physical plausibility, and that existing 3D-proxy pipelines don't adapt proxy detail or prompting to the task.
**Breakthrough:** The authors report Coda-DaVinci reaches a 91.42 checklist score and 11.08% WER on VTR (vs. 59.21% WER for direct generation), the highest reported scene-ID score (1.011) on R2M, and a 60.77 score on the World Models' Last Exam in Physics benchmark (second only to a Claude + Blender baseline at 65.52).
**Tools & method:** Coda-DaVinci routes tasks needing precise scene/motion control to 3D modeling and human-motion-centric tasks toward direct generation, uses coarse proxies for humans and medium-detail proxies for environments/objects, and has an agent inspect the rendered proxy to write prompts linking subjects to proxy entities.
**Limitation:** The authors report weaker motion naturalness and physical plausibility on VGIF-Bench (complex human/object motion), lower transition stability on LongAV-Compass, and weaker scene-setting adherence on WBench versus direct generation.
