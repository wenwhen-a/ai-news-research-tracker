**[B03] GeForce Game Ready Driver — Path Tracing + DLSS 4.5 Ray Reconstruction in 007 First Light (plus day-one DLSS 4.5 in WARDOGS, Aniimo)**
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-09-15 (driver announced 2026-09-09; WARDOGS 2026-09-10; Aniimo 2026-09-16) · **New**
- **Surface:** Shipped games (GeForce Game Ready Driver + in-game updates)
- **Primary source:** <https://www.nvidia.com/en-us/geforce/news/wardogs-aniimo-007-first-light-path-tracing-geforce-game-ready-driver/>
- **Underlying research:** no traceable paper distinct from the already-tracked DLSS 4.5 Ray Reconstruction 2nd-gen transformer model — this is the same model rolling out to more games
- **Availability:** Free driver update via NVIDIA App/GeForce Experience; DLSS 4.5 features require GeForce RTX GPUs.

**What shipped:** NVIDIA shipped a Game Ready Driver adding full path tracing plus DLSS 4.5 Ray Reconstruction to the already-shipped game 007 First Light, alongside day-one DLSS 4.5 Super Resolution and Dynamic Multi Frame Generation in two newly released games, WARDOGS (early access) and Aniimo.
**What research it translates:** Same underlying DLSS 4.5 2nd-generation transformer Ray Reconstruction model already tracked from the 2026-08-25 Gamescom announcement; this entry documents its extension to path-traced lighting in a specific title rather than a new model.
**Practical significance:** NVIDIA states path tracing plus Ray Reconstruction improves lighting/reflection accuracy in 007 First Light; adoption in new day-one titles signals continuing developer uptake of the DLSS 4.5 stack.
**Engineering details:** Delivered via a standard GeForce Game Ready Driver plus in-game patches; NVIDIA Reflex is bundled in WARDOGS for latency reduction.
