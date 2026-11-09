**[A03] Dynamic GPU Voxel Grids and Voxel-sequential Processing in NanoVDB**
- **arXiv:** 2611.08665 · <https://arxiv.org/abs/2611.08665>
- **Submitted:** 2026-11-05
- **Authors:** Eftychios Sifakis et al.
- **Qualifying affiliation(s):** NVIDIA — Francis Williams, Christopher Horvath, Rohan Sawhney, Mark Harris, Jonathan Swartz, Ken Museth (six of seven authors); Eftychios Sifakis is also affiliated with University of Wisconsin-Madison
- **Categories:** cs.GR (primary), cs.CV, cs.DC
- **Open release:** code (NanoVDB/VoxelBlockManager changes open-sourced in the Academy Software Foundation's OpenVDB repo: <https://github.com/AcademySoftwareFoundation/openvdb>; reconstruction code in <https://github.com/openvdb/fvdb-core>)
- **Shipped counterpart:** none found (NanoVDB is used inside NVIDIA Omniverse/OpenVDB tooling, but no dated product release tied to this paper's specific operators was found)

**Summary:** The paper extends NanoVDB, NVIDIA's GPU sparse-volume data structure, with dynamic topology operators (morphological dilation, grid merging, pruning, cross-resolution coarsening/refinement) that rebuild grids of hundreds of millions of voxels in milliseconds using bit-parallel algorithms, removing NanoVDB's prior read-only constraint.
**Purpose:** NanoVDB had been effectively read-only once built, limiting its use for workloads that need to dynamically rebuild or restructure sparse volumetric grids (e.g., 3D reconstruction, simulation, voxelization) at interactive rates.
**Breakthrough:** On a single 48 GB RTX 6000 Ada GPU, the authors report their mesh-voxelization method reaching about 9.88 billion active voxels at 0.001 voxel size on a 2.8-million-triangle test mesh, compared against OpenVDB's meshToUDF.
