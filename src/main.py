import pandas as pd
from src.preprocessing.prepare_dataset import preprocess
from src.graph.build_signed_graph import build_signed_graph
from src.influence.centrality_analysis import compute_centrality
from src.influence.attack_score import compute_attack_score
from src.attack.targeted_attack import run_targeted_attack
from src.attack.random_attack import run_random_attack
from src.evaluation.plot_disruption import plot_comparison
from src.community.signed_louvain import detect_communities
from src.community.bridge_analysis import compute_bridge_scores
from src.influence.signed_polarity import compute_signed_polarity
from src.influence.degree_ranking import rank_by_degree
from src.influence.betweenness_ranking import rank_by_betweenness
from src.evaluation.plot_disruption import plot_all_comparisons
from src.evaluation.plot_disruption import plot_lcc_drop
if __name__ == "__main__":

    raw_path = "data/raw/soc-sign-epinions.txt"
    processed_path = "data/processed/signed_edges.csv"

    # Step 1: Preprocess
    df = preprocess(raw_path, processed_path)

    print("Preprocessing complete.")
    print("Total edges after cleaning:", len(df))
    print("Positive edges:", (df["sign"] == 1).sum())
    print("Negative edges:", (df["sign"] == -1).sum())

    # Step 2: Build Graph
    G = build_signed_graph(processed_path)

    print("\nGraph successfully built.")
    print("Number of nodes:", G.number_of_nodes())
    print("Number of edges:", G.number_of_edges())

    # Step 3: Centrality
    G = compute_centrality(G, k_sample=200)
    print("Centrality computation complete.")
    
    # Baseline rankings
    degree_ranking = rank_by_degree(G)
    betweenness_ranking = rank_by_betweenness(G)
    
    # Step 4: Community Detection
    G, partition = detect_communities(
        G,
        output_path="data/results/community_assignments.csv"
    )

    # Compute Bridge Scores
    G = compute_bridge_scores(G)
    
    G = compute_signed_polarity(G)
    # Step 4: Compute Attack Score
    ranking = compute_attack_score(
    G,
    alpha=0.30,
    beta=0.30,
    gamma=0.25,
    delta=0.15,
    output_path="data/results/attack_ranking.csv"
    )

    print("Attack score computed.")
    print("Top 5 influential nodes:")
    for node, score in ranking[:5]:
        print(node, score)

    # Step 5: Targeted Attack
    results = run_targeted_attack(
        G,
        ranking,
        max_k=20,
        output_path="data/results/disruption_metrics.csv"
    )

    print("\nTargeted attack completed.")
    
    # Degree attack
    degree_results = run_targeted_attack(
        G,
        degree_ranking,
        max_k=20,
        output_path="data/results/degree_attack_metrics.csv"
    )

    print("\nDegree attack completed.")
    
    # Betweenness attack
    betweenness_results = run_targeted_attack(
        G,
        betweenness_ranking,
        max_k=20,
        output_path="data/results/betweenness_attack_metrics.csv"
    )

    print("\nBetweenness attack completed.")

    # Step 6: Random Attack
    random_results = run_random_attack(
        G,
        max_k=20,
        output_path="data/results/random_disruption_metrics.csv"
    )

    print("\nRandom attack completed.")

    # Step 7: Plot comparison
    plot_all_comparisons(
    results,
    random_results,
    degree_results,
    betweenness_results,
    output_path="data/results/full_attack_comparison.png"
    )
    
    # --- Create comparison table ---
    comparison_df = results.copy()

    comparison_df = comparison_df.rename(columns={
        "lcc_size": "targeted_lcc",
        "fragmentation": "targeted_fragmentation",
        "lcc_drop_percent": "targeted_drop_percent"
    })

    comparison_df["random_lcc"] = random_results["lcc_size"]
    comparison_df["random_fragmentation"] = random_results["fragmentation"]
    comparison_df["random_drop_percent"] = random_results["lcc_drop_percent"]

    # Improvement difference
    comparison_df["improvement_percent"] = (
        comparison_df["targeted_drop_percent"]
        - comparison_df["random_drop_percent"]
    )

    comparison_df.to_csv("data/results/comparison_table.csv", index=False)

    print("\nComparison table saved.")
    
    plot_lcc_drop(
        results,
        random_results,
        degree_results,
        betweenness_results,
        output_path="data/results/lcc_drop_comparison.png"
    )
    
    # --- Average Improvement Table ---

    avg_proposed = results["lcc_drop_percent"].mean()
    avg_degree = degree_results["lcc_drop_percent"].mean()
    avg_between = betweenness_results["lcc_drop_percent"].mean()
    avg_random = random_results["lcc_drop_percent"].mean()

    summary_df = pd.DataFrame({
        "Method": [
            "Random Attack",
            "Betweenness Attack",
            "Degree Attack",
            "Proposed Model"
        ],
        "Average LCC Drop (%)": [
            avg_random,
            avg_between,
            avg_degree,
            avg_proposed
        ]
    })

    summary_df.to_csv("data/results/average_performance_table.csv", index=False)

    print("\nAverage performance table saved.")