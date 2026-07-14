def compute_bridge_scores(G):
    """
    Compute bridge ratio for each node.
    Bridge ratio = inter-community edges / total degree
    """

    print("Computing bridge scores...")

    for node in G.nodes():
        node_comm = G.nodes[node]["community"]
        total_degree = G.degree(node)

        if total_degree == 0:
            G.nodes[node]["bridge_score"] = 0
            continue

        cross_edges = 0

        for neighbor in G.neighbors(node):
            if G.nodes[neighbor]["community"] != node_comm:
                cross_edges += 1

        # Bridge ratio
        bridge_ratio = cross_edges / total_degree

        # Multiply by normalized degree centrality
        degree_cent = G.nodes[node].get("degree", 0)

        # Final scaled bridge effect
        G.nodes[node]["bridge_score"] = bridge_ratio * degree_cent

    print("Bridge score computation complete.")
    return G