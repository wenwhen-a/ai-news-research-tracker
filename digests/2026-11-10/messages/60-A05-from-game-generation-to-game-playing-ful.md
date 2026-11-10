**[A05] From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models**
- **arXiv:** 2611.11136 · <https://arxiv.org/abs/2611.11136>
- **Submitted:** 2026-11-08
- **Authors:** Changran Liu, Qi Wu, Wenchao Ma, Sharon X. Huang, Haomiao Jiang
- **Qualifying affiliation(s):** Roblox — Changran Liu, Qi Wu, Haomiao Jiang
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** The paper presents a framework that uses an LLM-powered coding agent to automatically build game environments, tasks, and scripted expert players from natural-language skill descriptions, which then generate keyboard-and-mouse demonstrations without any human gameplay data.
**Purpose:** The authors target the bottleneck of collecting human gameplay demonstrations for training game-playing VLA agents, aiming to fully automate both environment/task generation and the expert demonstrations used to train such agents.
**Breakthrough:** The authors report a fully automated pipeline that goes from natural-language skill descriptions to generated game environments, scripted expert players, and synthetic demonstrations, removing the need for human gameplay data entirely.
**Tools & method:** The pipeline uses an LLM coding agent to author environments/tasks and scripted "expert" players in Roblox (via Luau scripting and the Rojo build system) and Minecraft; it trains a 4B vision-language-action model (Script2Play) via behavior cloning on 150.3 hours of generated keyboard-and-mouse demonstration data.
**Limitation:** Not stated by the authors in the abstract or main text reviewed.
