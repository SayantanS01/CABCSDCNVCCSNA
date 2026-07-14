# Signed Graph Attack Project: Robustness and Vulnerability Analysis

## Abstract / Overview

The **Signed Graph Attack Project** is a comprehensive Python framework designed to analyze the structural robustness of signed social networks (e.g., the Epinions dataset). In signed networks, edges carry positive (trust/friendship) or negative (distrust/enmity) weights. This project evaluates how removing highly influential nodes disrupts the network structure, specifically by measuring the drop in the **Largest Connected Component (LCC)** and the increase in overall network fragmentation.

The core contribution of this project is a **Proposed Attack Score**, which combines multiple structural and influence metrics (Degree, Betweenness, Bridge Score, and Signed Polarity) to identify the most critical nodes. The project then simulates network attacks by sequentially removing these nodes and compares the disruption against baseline attack strategies (Random, Degree-based, and Betweenness-based).

---

## 🔬 Theoretical Background & Metrics

To identify the most critical nodes for a targeted attack, the system computes several centrality and influence metrics:

1. **Degree Centrality**: The basic measure of a node's connectivity (total number of incoming and outgoing edges). Highly connected nodes are naturally prime targets.
2. **Betweenness Centrality**: Measures how often a node acts as a bridge along the shortest path between two other nodes. Removing nodes with high betweenness fragments the network quickly.
3. **Bridge Score (Community-aware)**: The network is first partitioned into communities using a **Signed Louvain** algorithm. The bridge score is calculated as the ratio of inter-community edges to the node's total degree, scaled by its normalized degree centrality. Nodes with high bridge scores are critical links *between* different distinct communities.
4. **Signed Influence Polarity (SIP)**: Specific to signed networks, this metric captures the proportion of negative outgoing edges a node has relative to its total outgoing edges (`negative_out_edges / total_out_edges`).
5. **Proposed Attack Score**: A weighted linear combination of the above normalized metrics. It assigns an overarching vulnerability score to each node:
   `Attack Score = (α * Degree) + (β * Betweenness) + (γ * Bridge Score) + (δ * SIP)`
   *(Default weights: α=0.30, β=0.30, γ=0.25, δ=0.15)*

---

## ⚙️ Project Pipeline & Modules

The project is structured into modular components located in the `src/` directory:

- **`preprocessing/`**: Cleans the raw `soc-sign-epinions.txt` dataset and constructs a structured edge list.
- **`graph/`**: Uses `NetworkX` to construct the signed directed graph from the processed edge list.
- **`community/`**: Implements the Signed Louvain community detection algorithm and computes bridge scores based on the resulting partitions.
- **`influence/`**: Calculates Degree, Betweenness, Signed Polarity, and the final combined Proposed Attack Score.
- **`attack/`**: Simulates the node removal process (Targeted vs. Random). It recalculates structural metrics at each step `k`.
- **`evaluation/`**: Computes the drop in LCC size (both absolute and percentage) and generates comparative visualizations using `matplotlib`.

---

## 📊 Evaluation & Simulation

The attack simulation works by ranking all nodes based on a specific metric and removing the top `k` nodes iteratively. The project simulates four distinct attack strategies:
1. **Proposed Model Attack**: Removes nodes ranked by the custom Attack Score.
2. **Degree Attack**: Removes nodes ranked purely by degree centrality.
3. **Betweenness Attack**: Removes nodes ranked purely by betweenness centrality.
4. **Random Attack**: Removes nodes at random (acts as a baseline).

For each step `k`, the system measures the **LCC Drop Percentage**:
`LCC Drop (%) = ((Initial LCC Size - Current LCC Size) / Initial LCC Size) * 100`

---

## 📁 Directory Structure

```text
├── data/
│   ├── raw/               # Raw dataset files (e.g., soc-sign-epinions.txt)
│   ├── processed/         # Cleaned and processed graph data
│   └── results/           # Output metrics, tables (CSV), and comparison plots (PNG)
├── src/
│   ├── attack/            # Attack simulations (Targeted, Random)
│   ├── community/         # Signed Louvain detection, bridge score computation
│   ├── evaluation/        # LCC tracking and plot generation
│   ├── graph/             # NetworkX graph construction
│   ├── influence/         # Computation of centrality and attack scores
│   ├── preprocessing/     # Dataset parsing and cleaning scripts
│   └── main.py            # Main execution pipeline
├── requirements.txt       # Python dependencies (pandas, networkx, matplotlib, python-louvain)
└── README.md              # Project documentation
```

---

## 🚀 Setup & Installation

1. Ensure you have **Python 3.8+** installed.
2. Clone the repository and navigate into the root directory.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

*(Dependencies: `pandas`, `networkx`, `matplotlib`, `python-louvain`)*

## 💻 Usage Instructions

1. **Add Data**: Ensure your raw dataset (e.g., `soc-sign-epinions.txt`) is placed inside the `data/raw/` directory.
2. **Run Pipeline**: Execute the main script from the project root:

```bash
python src/main.py
```

3. **Results Output**: The script will output the progress to the console. Once completed, navigate to `data/results/` to view:
   - `attack_ranking.csv`: Full list of nodes ranked by the proposed attack score.
   - `*_attack_metrics.csv`: Structural metrics recorded at each node removal step for every attack type.
   - `comparison_table.csv` / `average_performance_table.csv`: Aggregated performance metrics.
   - `lcc_drop_comparison.png` / `full_attack_comparison.png`: Visual line charts comparing the disruption caused by each attack strategy.
