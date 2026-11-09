**[B03] NVIDIA Cosmos — new simulation checkpoints (Transfer-Auto, Sim-Auto, Sim-Transfer, Sim-Bimanual, Cosmos3-H-Embodied-Nano, Cosmos3-H-Dreams) via Cosmos NIM**
- **Company:** NVIDIA — flagged: use-case is robotics/autonomous-vehicle/surgical simulation, not games; included under the "world models" topic per the skill's tracked-topic list, not the games-specific product surfaces.
- **Status:** GA · **Released:** 2026-11-02 · **New**
- **Surface:** cloud API / SDK (Cosmos NIM microservice container; also runnable via build.nvidia.com trial and Hugging Face weights)
- **Primary source:** <https://developer.nvidia.com/blog/build-world-models-for-interactive-simulation-with-nvidia-cosmos/>
- **Underlying research:** arXiv:2503.14492, "Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control" (NVIDIA) — matches the "Transfer" family of checkpoints named in the post; NVIDIA also links its own technical report at research.nvidia.com/labs/cosmos-lab/cosmos-simulation/technical-report.pdf.
- **Availability:** Downloadable/runnable today via the `nvcr.io/nim/nvidia/cosmos3:2.0.0` NIM container (no invitation), trial on build.nvidia.com, and checkpoints/weights on Hugging Face; NVIDIA Open Model License for the models, separate NVIDIA software license for the NIM container.

**What shipped:** NVIDIA released new Cosmos 3 simulation recipes and checkpoints — Transfer-Auto and Sim-Auto for autonomous-vehicle simulation, Sim-Transfer and Sim-Bimanual for robotics, and Cosmos3-H-Embodied-Nano / Cosmos3-H-Dreams for surgical scenarios — alongside guidance for running them as containerized Cosmos NIM microservices.
**What research it translates:** NVIDIA's own technical report underlies the release; the "Transfer" checkpoints align with the previously published Cosmos-Transfer1 paper (arXiv:2503.14492) on conditional world generation with adaptive multimodal (segmentation/depth/edge) control for Sim2Real transfer.
