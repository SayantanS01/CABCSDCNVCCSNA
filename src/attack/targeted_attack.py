import pandas as pd
from src.evaluation.structural_metrics import compute_structural_metrics


def run_targeted_attack(G, ranked_nodes, max_k=5, output_path=None):

    results = []

    # Work on a single copy
    G_copy = G.copy()

    # --- NEW: Compute initial LCC before any removals ---
    initial_metrics = compute_structural_metrics(G_copy)
    initial_lcc = initial_metrics["lcc_size"]

    for k in range(1, max_k + 1):
        print(f"Removing top {k} nodes...")

        # Remove one new node
        node_to_remove = ranked_nodes[k - 1][0]
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