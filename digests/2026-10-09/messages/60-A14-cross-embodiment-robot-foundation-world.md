**[A14] Cross-Embodiment Robot Foundation World Models with Latent Actions**
- **arXiv:** 2610.10846 · <https://arxiv.org/abs/2610.10846>
- **Submitted:** 2026-10-07 (v1)
- **Authors:** Huang Huang et al.
- **Qualifying affiliation(s):** Meta FAIR Robotics — Arjun Majumdar, Elie Aljalbout, Tushar Nagarajan, Tsung-Yen Yang, Akshara Rai, Michael Rabbat, Tingfan Wu, Franziska Meier, and (partly) Huang Huang and Sriram Yenamandra (flag: the author block credits each as "work partially done while at Meta FAIR Robotics," a past/in-progress note rather than a stated current affiliation; kept and flagged per the borderline-affiliation rule rather than silently dropped). Other authors (current): Stanford University (Li Fei-Fei, Jiajun Wu, and others).
- **Categories:** cs.RO
- **Open release:** none stated in the abstract
- **Shipped counterpart:** none found

**Summary:** The paper introduces LAC-WM, a robot world model that uses a learned latent action space shared across different robot embodiments, and compares it against EAC-WM, which conditions on explicit motion labels.
**Purpose:** To test whether a learned latent action representation transfers across robot embodiments better than conditioning on explicit motion labels.
**Breakthrough (≤3 sentences, attributed):** The authors report LAC-WM improves downstream performance by up to 46.7% on dexterous manipulation and 11.7% on a modified LIBERO benchmark versus EAC-WM, and that LAC-WM's performance improves as the number of pretraining embodiments grows while EAC-WM's declines.
**Tools & method:** Evaluated on dexterous manipulation tasks and a modified LIBERO benchmark, directly comparing latent-action conditioning (LAC-WM) against explicit-motion-label conditioning (EAC-WM) for cross-embodiment world models.
**Limitation:** Not stated in the available abstract text beyond the EAC-WM comparison itself.
