import random
import pandas as pd
from src.evaluation.structural_metrics import compute_structural_metrics


def run_random_attack(G, max_k=20, output_path=None, seed=42):
    """
    Cumulative random node removal attack.
    """

    random.seed(seed)

    results = []

    # Work on copy
    G_copy = G.copy()

    # --- NEW: Compute initial LCC before removals ---
    initial_metrics = compute_structural_metrics(G_copy)
    initial_lcc = initial_metrics["lcc_size"]

    # Shuffle node list once
    nodes = list(G_copy.nodes())
    random.shuffle(nodes)

    for k in range(1, max_k + 1):
        print(f"[Random] Removing {k} nodes...")

        node_to_remove = nodes[k - 1]
        G_copy.remove_node(node_to_remove)

        metrics = compute_structural_metrics(G_copy)

        # --- NEW: Add percentage drop ---
        metrics["lcc_drop_percent"] = (
            (initial_lcc - metrics["lcc_size"]) / initial_lcc
        ) * 100

        metrics["k"] = k
        results.append(metrics)

    df_results = pd.DataFrame(results)

    if output_path:
        df_results.to_csv(output_path, index=False)

    return df_results