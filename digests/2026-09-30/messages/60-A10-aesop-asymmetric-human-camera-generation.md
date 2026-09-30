**[A10] AESOP: Asymmetric Human-Camera Generation with Translation-Intensity Control**
- **arXiv:** 2609.37229 · <https://arxiv.org/abs/2609.37229>
- **Submitted:** 2026-09-29 (v1)
- **Authors:** Jingzhong Lin, Zhanke Wang, Heng Li, Wenxiang Liu, Zhao Zhang, Kecheng Tang, Dongdong Xiang, Changbo Wang, Di Kang, Chunchao Guo, Linchao Bao, Gaoqi He
- **Qualifying affiliation(s):** Tencent — Di Kang, Chunchao Guo, Linchao Bao; Jingzhong Lin completed this work during a Tencent internship (other authors: East China Normal University, Peking University, Sun Yat-sen University)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** AESOP is a unified framework for both standalone camera-trajectory generation and joint human-camera generation, using an independent human-motion pathway plus a shared human-conditioned camera module.
**Purpose:** Camera generation and joint human-camera generation are usually treated as separate problems even though they share an asymmetric dependency (camera responds to human action, not vice versa).
**Breakthrough:** The authors report strong camera distributional and framing quality "in both tasks" on the PulpMotion dataset, plus effective control over translation intensity, achieved by constructing trajectory pairs that vary camera-translation magnitude while keeping human motion and camera text fixed.
**Tools & method:** An asymmetric architecture pairs an independent human-generation pathway with a shared, human-conditioned camera generator; an explicit translation-intensity condition is learned from constructed trajectory pairs.
**Limitation (≤3 sentences, authors' own):** The authors state that their sequence-level intensity condition limits control over individual events (rather than fine-grained, per-event control), and that reliance on complete human context plus offline sampling limits streaming/causal generation.
