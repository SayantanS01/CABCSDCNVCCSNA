def rank_by_betweenness(G):
    """
    Rank nodes purely by betweenness centrality.
    """

    scores = {}

    for node in G.nodes():
        betweenness = G.nodes[node].get("betweenness", 0)
        scores[node] = betweenness

    ranked_nodes = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return ranked_nodes