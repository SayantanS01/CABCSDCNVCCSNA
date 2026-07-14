def rank_by_degree(G):
    """
    Rank nodes purely by degree centrality.
    """

    scores = {}

    for node in G.nodes():
        degree = G.nodes[node].get("degree", 0)
        scores[node] = degree

    ranked_nodes = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return ranked_nodes