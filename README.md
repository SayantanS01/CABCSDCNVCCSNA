# Signed Graph Attack Project

This project focuses on analyzing signed networks (like the Epinions dataset) and evaluating their structural robustness against various network attack strategies. It computes different influence metrics and measures how removing critical nodes impacts the Largest Connected Component (LCC).

## Features

- **Signed Network Preprocessing**: Cleans and constructs a signed graph from raw edge lists.
- **Influence & Centrality Analysis**: Computes degree centrality, betweenness centrality, signed polarity, and bridge scores.
- **Community Detection**: Uses the Signed Louvain algorithm to partition the network.
- **Network Attacks**: Simulates targeted attacks based on:
  - Random selection
  - Degree centrality
  - Betweenness centrality
  - Proposed model scoring (based on a combination of metrics)
- **Evaluation & Visualization**: Generates tables and comparison plots showing the drop in the Largest Connected Component (LCC) and overall network fragmentation.

## Project Structure

```
├── data/
│   ├── raw/               # Raw dataset files (e.g., soc-sign-epinions.txt)
│   ├── processed/         # Cleaned and processed graph data
│   └── results/           # Output metrics, tables (CSV), and comparison plots (PNG)
├── src/
│   ├── attack/            # Attack strategy implementations
│   ├── community/         # Community detection and bridge analysis
│   ├── evaluation/        # Structural metrics and disruption plotting
│   ├── graph/             # Graph construction logic
│   ├── influence/         # Centrality and influence scoring
│   ├── preprocessing/     # Dataset parsing and preparation
│   └── main.py            # Main entry point to run the pipeline
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Installation

1. Ensure you have Python installed.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Place your raw dataset (e.g., `soc-sign-epinions.txt`) inside `data/raw/`.
2. Run the main pipeline script from the root directory:

```bash
python src/main.py
```

This script will process the graph, perform centrality analysis and community detection, execute the attack strategies, and output CSV tables and comparison plots into the `data/results/` directory.
