**[A02] UNITE: Consolidating Embodied VLM Specialists via Shared-Anchor One-Bit Factorization**
- **arXiv:** 2611.20767 · <https://arxiv.org/abs/2611.20767>
- **Submitted:** 2026-11-16 (v1)
- **Authors:** Tao Tao et al.
- **Qualifying affiliation(s):** ACE Robotics, Shanghai — Tao Tao, Zhi Hou, Xiaogang Wang. FLAG: borderline — ACE Robotics (not on the explicit qualified-company list; standing unclear, kept per borderline rule). Other authors: Sichuan University, Nanyang Technological University, Sun Yat-sen University (Shenzhen).
- **Categories:** cs.LG (primary), cs.CV
- **Open release:** none (no GitHub/HuggingFace/project page found in abstract or HTML body)
- **Shipped counterpart:** none found

**Summary:** UNITE consolidates multiple fine-tuned vision-language-model (VLM) "specialists" — for visual grounding, spatial reasoning, navigation, and driving understanding — into a single compact mixture-of-experts model instead of deploying them separately or merging them into one conflict-prone dense model.
**Purpose:** The authors aim to avoid the storage cost of deploying many separate embodied VLM specialists while avoiding the capability loss and parameter conflicts that come from naively merging them into a single dense model.
**Breakthrough:** The authors report the full UNITE model occupies 20.3 GB — 1.16× the storage of one dense specialist and 59.6% below the uncompressed mixture-of-experts — while updating fewer than 0.6M router parameters (under 0.01% of the 8.8B active parameters), using only source weights with no calibration data.
**Tools & method:** UNITE represents the expert bank through a "shared-anchor one-bit factorization" — a shared floating-point anchor plus expert-specific, row-scaled binary deviations — optimized jointly via closed-form alternating updates with no calibration data, then adapts only token-level routing with the backbone and experts frozen.
