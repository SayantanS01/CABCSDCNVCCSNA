import networkx as nx

def compute_structural_metrics(G):
    """
    Lightweight structural metrics (optimized for large graphs).
    """

    total_nodes = G.number_of_nodes()

    if total_nodes == 0:
        return {
            "lcc_size": 0,
            "num_components": 0,
            "fragmentation": 1.0
        }

    G_undirected = G.to_undirected()

    components_generator = nx.connected_components(G_undirected)

    num_components = 0
    max_size = 0

    for comp in components_generator:
        num_components += 1
        comp_size = len(comp)

        if comp_size > max_size:
            max_size = comp_size

    # Fragmentation index
    fragmentation = 1 - (max_size / total_nodes)

    return {
        "lcc_size": max_size,
        "num_components": num_components,
        "fragmentation": fragmentation
    }