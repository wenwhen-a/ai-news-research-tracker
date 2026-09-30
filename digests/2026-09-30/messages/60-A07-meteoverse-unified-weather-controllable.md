**[A07] MeteoVerse: Unified Weather-Controllable Video World Model**
- **arXiv:** 2609.36810 · <https://arxiv.org/abs/2609.36810>
- **Submitted:** 2026-09-29
- **Authors:** Renlong Wu et al.
- **Qualifying affiliation(s):** Huawei — Xiaoxiao Sheng, Tianyu Huang; other authors from Harbin Institute of Technology. FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none (project page only: <https://meteoverse.github.io/>; no code or weights release stated in the fetched text)
- **Shipped counterpart:** none found

**Summary:** MeteoVerse is a video world model that generates future video conditioned on scene description, weather instruction, and camera path, explicitly modeling weather transitions (preserving, introducing, or removing rain/snow/fog with intensity control) rather than leaving them implicit.
**Purpose:** The authors argue real-world scene evolution depends on environmental/weather conditions as well as viewpoint and object dynamics, and that prior video world models entangle weather inference with scene dynamics, making controllable weather generation unreliable.
**Breakthrough:** The authors report large gains over baselines on their own weather-controllable video benchmark: weather introduction alignment of 61.00 versus 29.00 for the best baseline (VerseCrafter), and weather removal alignment of 89.00 versus 38.00 for LingBot-World, while weather-preservation scores remain competitive (86.70 vs. 86.56).
**Tools & method:** The pipeline includes a new MeteoVerse dataset of over 50,000 real-world weather video clips with pseudo-paired "sunny" counterparts, disentangled scene/weather descriptions, intensity annotations, and camera trajectories, supporting four training-pair types (preservation/introduction/removal).
