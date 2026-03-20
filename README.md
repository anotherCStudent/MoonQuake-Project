# MoonQuake Project

MoonQuake is a web based interactive visualization built for the NASA Space Apps Challenge 2023. It displays lunar seismic events on a 3D Moon and lets you explore activity by filtering events by year and day.

## Demo

YouTube demo: https://www.youtube.com/watch?v=Pyb3ImDWBzQ

## What this project does

- Renders an interactive 3D Moon in the browser
- Plots moonquake style seismic events as pins on the globe
- Lets you filter events by:
  - Year (text input)
  - Day of year (slider)
- Includes a button to view the available dataset content in the UI

## Tech stack

- Python
- Django
- HTML, CSS, JavaScript
- Three.js (3D rendering)
- Papa Parse (CSV parsing in browser)
- pandas (server side CSV loading)

## Data

CSV files are stored here:

`myapp/static/data/`

Included datasets in this repo:

- `CombinedData.csv`
- `nakamura_1979_sm_locations.csv`
- `nakamura_1983_ai_arrivals.csv`
- `nakamura_1983_ai_locations.csv`
- `nakamura_1983_m_arrivals.csv`
- `nakamura_1983_sm_arrivals.csv`
- `nakamura_2005_dm_arrivals.csv`
- `nakamura_2005_dm_locations.csv`
- `weber_2011_dmq_s_picks.csv`

## Local setup

### Prerequisites

- Python 3.9 recommended
- pip

### Install and run

1. Clone the repo
2. Create and activate a virtual environment
3. Install dependencies
4. Run migrations
5. Start the server
