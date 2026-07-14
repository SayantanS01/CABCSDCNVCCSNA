def compute_signed_polarity(G):
    """
    Compute signed influence polarity for each node.
    SIP = negative_degree / total_degree
    """

    print("Computing signed polarity scores...")

    for node in G.nodes():

        pos = 0
        neg = 0

        for _, _, data in G.out_edges(node, data=True):

            if data["sign"] == 1:
                pos += 1
            else:
                neg += 1

        total = pos + neg

        if total == 0:
            sip = 0
        else:
            sip = neg / total

        G.nodes[node]["sip"] = sip

    print("Signed polarity computation complete.")

    return G