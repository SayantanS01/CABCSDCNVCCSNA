import networkx as nx
import community as community_louvain
import pandas as pd


def detect_communities(G, output_path=None):
    """
    Detect communities using Louvain on undirected projection.
    """

    # Louvain requires undirected graph
    G_undirected = G.to_undirected()

    print("Running Louvain community detection...")

    partition = community_louvain.best_partition(G_undirected)

    # Attach community label to nodes
    for node, community_id in partition.items():
        G.nodes[node]["community"] = community_id

    if output_path:
        df = pd.DataFrame(partition.items(), columns=["node", "community"])
        df.to_csv(output_path, index=False)

    print("Community detection complete.")
    print("Total communities detected:", len(set(partition.values())))

    return G, partition