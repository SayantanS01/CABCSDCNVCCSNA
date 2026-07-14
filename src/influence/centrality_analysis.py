import networkx as nx


def compute_centrality(G, k_sample=200):
    """
    Compute degree and approximate betweenness centrality.
    """

    print("\nComputing degree centrality...")
    degree = nx.degree_centrality(G)

    print("Computing approximate betweenness centrality...")
    betweenness = nx.betweenness_centrality(
        G,
        k=k_sample,        # number of sampled nodes
        normalized=True,
        seed=42
    )

    # Attach as node attributes
    for node in G.nodes():
        G.nodes[node]["degree"] = degree.get(node, 0)
        G.nodes[node]["betweenness"] = betweenness.get(node, 0)

    return G