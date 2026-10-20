**[A08] EmbodiedWorld-200K: Toward Embodied World Agents via Embodied-Planning Dataset and Interactive World Models**
- **arXiv:** 2610.25959 · <https://arxiv.org/abs/2610.25959>
- **Submitted:** 2026-10-19
- **Authors:** Xiaokun Feng, Junshu Tang, Zeyi Lin, Ling-Hao Chen, Shuai Shao, Qinglin Lu, Kaiqi Huang
- **Qualifying affiliation(s):** Tencent Hunyuan — Xiaokun Feng, Junshu Tang, Zeyi Lin, Ling-Hao Chen, Shuai Shao, Qinglin Lu, Kaiqi Huang (paper states the work was done during an internship at Tencent Hunyuan)
- **Categories:** cs.AI
- **Open release:** code | checkpoints | dataset (paper states "dataset, checkpoints, and code are said to be publicly released"; no specific link found in fetched text)
- **Shipped counterpart:** none found

**Summary:** The paper introduces "Embodied World Agents" (EWAs) and instantiates them as open-world embodied navigation planning.
**Purpose:** The authors argue existing embodied benchmarks are narrow (single scene, single robot, or single game) and that passive vision-language training lacks closed-loop perception-action ability.
**Breakthrough:** The authors report that SFT on their dataset raises a Qwen3-VL-4B baseline from TM 54.9/DirAcc 70.1/nDTW 67.1/NE 51.7 to TM 62.0/DirAcc 72.0/nDTW 83.6/NE 35.6 on their own held-out split, roughly matching Gemini-3.5 on DirAcc (72.0 vs 72.4).
**Tools & method:** Camera poses are recovered with VIPE; clips are segmented into "navigation-coherent segments" with a shared W/A/S/D action vocabulary; Qwen3.5-27B generates instructions.
**Limitation:** The fetched text's dedicated Limitations appendix was truncated, but visible section headers note "3D virtual games as proxies for the physical world" and "limited action granularity" as concerns.
