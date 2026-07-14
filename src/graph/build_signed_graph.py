import networkx as nx
import pandas as pd


def build_signed_graph(input_path):
    """
    Build a directed signed graph from processed CSV file.
    """

    df = pd.read_csv(input_path)

    G = nx.DiGraph()

    for _, row in df.iterrows():
        G.add_edge(
            row["source"],
            row["target"],
            sign=row["sign"],
            weight=row["weight"]
        )

    return G