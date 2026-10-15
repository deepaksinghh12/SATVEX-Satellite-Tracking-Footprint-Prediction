# 🛰️ SAT-VEX — Satellite Tracking & Footprint Prediction

**An independently extended satellite-tracking module originating from a Smart India Hackathon (SIH) 2025 winning solution.**

SAT-VEX explores satellite position estimation, orbit propagation from Two-Line Element (TLE) data, and ground-footprint visualization. It combines orbital-mechanics workflows with an interactive 3D globe and experimental machine-learning-assisted correction.

<p align="left">
  <a href="https://github.com/deepaksinghh12/Satvex">Source Code</a> ·
  <a href="https://github.com/deepaksinghh12/Satvex/issues">Report an Issue</a> ·
  <a href="https://www.linkedin.com/in/deepaksinghh12/">Connect on LinkedIn</a>
</p>

> **Deployment status:** Deployment is planned. A live demo link will be added after the application is deployed and verified.

---

## Contents

- [Overview](#overview)
- [Key capabilities](#key-capabilities)
- [Architecture and workflow](#architecture-and-workflow)
- [Technology stack](#technology-stack)
- [Repository structure](#repository-structure)
- [Run locally](#run-locally)
- [Data sources and accuracy](#data-sources-and-accuracy)
- [Screenshots](#screenshots)
- [Roadmap](#roadmap)
- [SIH 2025 background](#sih-2025-background)
- [Responsible interpretation](#responsible-interpretation)
- [Contributing](#contributing)
- [Author](#author)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Overview

Satellite tracking depends on orbital data, propagation models, timestamps, and clear visualization. SAT-VEX brings these pieces together in a web application intended to help users inspect satellite positions and explore predicted ground tracks and footprints.

The project began as the satellite-tracking and visualization module of a **Smart India Hackathon (SIH) 2025 winning solution**. This repository represents the module independently extended and maintained as SAT-VEX; it should not be interpreted as the complete original SIH solution.

## Key capabilities

### 🌍 Interactive 3D Earth

- Explore satellite positions and paths on a CesiumJS-powered globe.
- Visualize orbital movement in a geographic context.
- Use the interface to inspect satellite-tracking data.

### 📡 TLE-based orbit propagation

- Work with Two-Line Element (TLE) sets used to describe satellite orbits.
- Support satellite records associated with NORAD catalog identifiers.
- Explore time-based position calculations using the propagation workflow implemented in the project.

> TLEs become less representative of a satellite's current orbit as they age. Results depend on the freshness and quality of the orbital elements.

### 📐 Ground-track and footprint visualization

- Visualize predicted satellite ground tracks and estimated ground footprints.
- Explore the geographic area associated with a satellite's position and configured footprint calculations.
- Provide a foundation for further coverage-analysis features.

### 🤖 Experimental ML-assisted correction

- Includes work toward machine-learning-assisted correction of propagated positions.
- Intended to investigate whether learned corrections can reduce prediction error under evaluated conditions.
- Actual improvements depend on the model, training data, evaluation method, and orbital scenario; no accuracy improvement is guaranteed without measured results.

### ⏱️ Time-aware position exploration

- Explore satellite positions at selected times where supported by the application workflow.
- Investigate historical or future positions within the limits of the available TLE data and propagation implementation.

## Architecture and workflow

```mermaid
flowchart TD
    U[User] --> UI[Web interface]
    UI --> G[CesiumJS 3D globe]
    UI --> B[Python application/backend]
    B --> T[TLE and satellite catalog data]
    T --> P[Orbit propagation]
    P --> F[Ground-track and footprint calculations]
    P --> M[Experimental ML correction]
    F --> R[Position and coverage results]
    M --> R
    R --> UI
```

This is a conceptual view of the project's main responsibilities. The exact request flow and available endpoints are defined by the current implementation in the repository.

## Technology stack

| Area | Technologies |
|---|---|
| Backend and data workflows | Python |
| Interactive globe | CesiumJS |
| Frontend | HTML, CSS, JavaScript |
| Orbital input data | Two-Line Element (TLE) sets |
| Orbit propagation | SGP4-based workflow where configured |
| ML experimentation | Python |

## Repository structure

```text
Satvex/
├── .github/workflows/       # GitHub Actions workflows
├── config/                  # Application configuration
├── satTrack/                # Satellite-tracking application/module
├── static/                  # Static assets
├── templates/               # HTML templates
├── tools/                   # Data utilities and helper scripts
├── Dockerfile
├── docker-entrypoint.sh
├── requirements.txt
├── manage.py
├── SATELLITE_DATA_API_GUIDE.md
└── README.md
```

The repository also contains scripts for fetching, updating, inspecting, and validating satellite records. Review each script before running it, particularly those that write to data files or call external APIs.

## Run locally

### Prerequisites

- Python version compatible with the dependencies in `requirements.txt`
- Git
- Network access for any configured external data source
- Docker, if you prefer to use the included container configuration

### 1. Clone the repository

```bash
git clone https://github.com/deepaksinghh12/Satvex.git
cd Satvex
```

### 2. Create and activate a virtual environment

**Windows PowerShell**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure and start the application

Inspect the repository configuration and `SATELLITE_DATA_API_GUIDE.md` for required environment variables, external API setup, and the supported startup command.

For a Django-based setup, the usual development command is:

```bash
python manage.py runserver
```

If the repository uses a custom entry point or additional setup steps, follow those instructions instead. Keep API keys and private credentials in environment variables; never commit secrets to the repository.

### 5. Optional: run with Docker

The repository includes a `Dockerfile` and `docker-entrypoint.sh`. Review their expected configuration and build requirements before running:

```bash
docker build -t satvex .
docker run --rm -p 8000:8000 satvex
```

The container port and required environment variables must match the actual application configuration. If the container does not listen on port `8000`, adjust the mapping based on the Dockerfile and startup logs.

## Data sources and accuracy

SAT-VEX relies on orbital element data and the calculations implemented in the repository.

- **TLE freshness matters:** predictions can degrade as orbital elements age, especially for satellites affected by atmospheric drag or maneuvers.
- **Propagation assumptions matter:** calculated positions are estimates, not direct measurements.
- **ML results require evaluation:** compare predictions against a documented reference dataset and report the error metric, time horizon, and sample size before claiming improved accuracy.
- **External providers may change:** availability, rate limits, and data formats depend on the configured sources.

For external data setup, consult [`SATELLITE_DATA_API_GUIDE.md`](SATELLITE_DATA_API_GUIDE.md).

## Screenshots

Screenshots and a live demonstration will be added after deployment and verification.

<!-- Suggested screenshots:
1. SAT-VEX landing page
2. 3D globe with selected satellites
3. Satellite details and orbit path
4. Ground-track or footprint visualization
5. Time-based position exploration
-->

## Roadmap

These items describe possible next steps, not necessarily features already completed.

- [ ] Deploy the application and verify the public URL.
- [ ] Add screenshots and a short walkthrough.
- [ ] Document supported satellite-data sources and refresh cadence.
- [ ] Add reproducible orbit-propagation tests using known reference cases.
- [ ] Evaluate ML correction against a baseline and publish measured results.
- [ ] Add clearer stale-data indicators and error states.
- [ ] Document API endpoints, configuration, and operational limits.
- [ ] Improve accessibility and mobile usability.

## SIH 2025 background

SAT-VEX originated as the satellite-tracking and visualization module of a **Smart India Hackathon (SIH) 2025 winning solution** focused on satellite tracking and space-weather activity forecasting, including coronal mass ejections (CMEs) and geomagnetic storms.

This repository contains the independently extended SAT-VEX module. It is not presented as the entire hackathon solution, and the original team contribution should be distinguished from the work maintained in this repository.

## Responsible interpretation

SAT-VEX is a research and visualization project. Its output should not be treated as authoritative operational space-situational-awareness data.

- Do not rely on estimated positions or footprints alone for safety-critical or operational decisions.
- Check the timestamp and source of the orbital elements used for each result.
- Treat machine-learning corrections as experimental unless validated against suitable reference data.
- Confirm critical orbital information using trusted sources and appropriate domain expertise.

## Contributing

Suggestions, issue reports, and focused pull requests are welcome.

1. Open an issue describing the problem or proposed improvement.
2. Include reproduction steps, relevant logs, and expected behavior.
3. For changes to orbital calculations, include tests or reference cases where possible.
4. Do not commit secrets, private data, or unlicensed datasets.

## Author

**Deepak Singh** — Full-Stack Developer

- GitHub: [@deepaksinghh12](https://github.com/deepaksinghh12)
- LinkedIn: [Deepak Singh](https://www.linkedin.com/in/deepaksinghh12/)
- Portfolio: [deepaksinghdev.in](https://deepaksinghdev.in)

## Acknowledgements

SAT-VEX originated from work on a Smart India Hackathon 2025 winning solution. Credit for the original hackathon work belongs to the participating team; this repository documents the independently maintained SAT-VEX module.

---

<p align="center">
  <strong>Built as an independent extension of a Smart India Hackathon 2025 winning solution.</strong>
  <br />
  <sub>Deployment link and project screenshots will be added after they are live and verified.</sub>
</p>

## License

This repository includes an Apache-2.0 license. See [`LICENSE`](LICENSE) for the full terms.
