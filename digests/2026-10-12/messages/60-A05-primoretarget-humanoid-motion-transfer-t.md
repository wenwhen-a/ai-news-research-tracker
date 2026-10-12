**[A05] PriMoRetarget: Humanoid Motion Transfer Through Prioritized Motion Retargeting**
- **arXiv:** 2610.12642 · <https://arxiv.org/abs/2610.12642>
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Nicholas Ioannidis et al.
- **Qualifying affiliation(s):** NVIDIA — Xue Bin Peng (also affiliated with Simon Fraser University and the Alberta Machine Intelligence Institute)
- **Categories:** cs.RO (primary), cs.GR
- **Open release:** none yet — project page <https://nickioan.github.io/primoretarget-page/>; the authors state code and retargeted motion data "will be publicly released upon publication"
- **Shipped counterpart:** none found

**Summary:** PriMoRetarget is a framework for retargeting human motion onto humanoid robots, covering single-character motion, human-object manipulation, and human-human interaction.
**Purpose:** The authors aim to produce retargeted robot motion that better preserves task-relevant contacts and interactions than weighted-objective retargeting methods, and that yields reference trajectories which are easier for downstream controllers to track.
**Breakthrough:** The authors report that, evaluated across four datasets spanning single-character, character-object, and character-character motion, PriMoRetarget better preserves task-relevant interactions and produces trajectories that are easier for controllers to track than widely used retargeting methods (compared against PHC, GMR, and OmniRetarget).
**Tools & method:** The method is evaluated on LAFAN1 (single-character), OMOMO (character-object), Inter-X (character-character), and a 35-minute in-house collaborative-manipulation dataset; downstream RL tracking policies follow a DeepMimic/PPO setup on a simulated Unitree G1, with runtime benchmarked on an NVIDIA RTX 5090 and real deployment on a Unitree G1 robot (plus generalization tests on Deep Robotics DR02, Unitree H1-2, and Booster T1).
