import pandas as pd


def compute_attack_score(G, alpha=0.30, beta=0.30, gamma=0.25, delta=0.15, output_path=None):

    scores = {}

    # collect feature values
    degrees = [G.nodes[n].get("degree", 0) for n in G.nodes()]
    betweenness = [G.nodes[n].get("betweenness", 0) for n in G.nodes()]
    bridges = [G.nodes[n].get("bridge_score", 0) for n in G.nodes()]
    polarity = [G.nodes[n].get("signed_polarity", 0) for n in G.nodes()]

    # normalization denominators
    max_degree = max(degrees) if max(degrees) > 0 else 1
    max_between = max(betweenness) if max(betweenness) > 0 else 1
    max_bridge = max(bridges) if max(bridges) > 0 else 1
    max_polarity = max(polarity) if max(polarity) > 0 else 1

    for node in G.nodes():

        d = G.nodes[node].get("degree", 0) / max_degree
        b = G.nodes[node].get("betweenness", 0) / max_between
        br = G.nodes[node].get("bridge_score", 0) / max_bridge
        p = G.nodes[node].get("signed_polarity", 0) / max_polarity

        score = alpha*d + beta*b + gamma*br + delta*p

        scores[node] = score

    ranked_nodes = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    if output_path:
        df = pd.DataFrame(ranked_nodes, columns=["node", "attack_score"])
        df.to_csv(output_path, index=False)

    return ranked_nodes