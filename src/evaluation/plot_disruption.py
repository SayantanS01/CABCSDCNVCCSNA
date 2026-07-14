import matplotlib.pyplot as plt


def plot_comparison(targeted_df, random_df, output_path=None):

    plt.figure(figsize=(8, 5))

    plt.plot(targeted_df["k"], targeted_df["lcc_size"],
             marker="o", label="Targeted Attack")

    plt.plot(random_df["k"], random_df["lcc_size"],
             marker="x", label="Random Attack")

    plt.xlabel("Number of Nodes Removed (k)")
    plt.ylabel("Largest Connected Component Size")
    plt.title("Targeted vs Random Attack Disruption")
    plt.legend()
    plt.grid(True)

    if output_path:
        plt.savefig(output_path)

    plt.show()


# NEW FUNCTION FOR FULL EXPERIMENT
def plot_all_comparisons(proposed_df, random_df, degree_df, betweenness_df, output_path=None):

    plt.figure(figsize=(9, 6))

    plt.plot(proposed_df["k"], proposed_df["lcc_size"],
             marker="o", label="Proposed Model")

    plt.plot(degree_df["k"], degree_df["lcc_size"],
             marker="s", label="Degree Attack")

    plt.plot(betweenness_df["k"], betweenness_df["lcc_size"],
             marker="^", label="Betweenness Attack")

    plt.plot(random_df["k"], random_df["lcc_size"],
             marker="x", label="Random Attack")

    plt.xlabel("Number of Nodes Removed (k)")
    plt.ylabel("Largest Connected Component Size")
    plt.title("Comparison of Attack Strategies")

    plt.legend()
    plt.grid(True)

    if output_path:
        plt.savefig(output_path)

    plt.show()
    
def plot_lcc_drop(proposed_df, random_df, degree_df, betweenness_df, output_path=None):

    plt.figure(figsize=(9,6))

    plt.plot(proposed_df["k"], proposed_df["lcc_drop_percent"],
             marker="o", label="Proposed Model")

    plt.plot(degree_df["k"], degree_df["lcc_drop_percent"],
             marker="s", label="Degree Attack")

    plt.plot(betweenness_df["k"], betweenness_df["lcc_drop_percent"],
             marker="^", label="Betweenness Attack")

    plt.plot(random_df["k"], random_df["lcc_drop_percent"],
             marker="x", label="Random Attack")

    plt.xlabel("Number of Nodes Removed (k)")
    plt.ylabel("LCC Drop (%)")
    plt.title("Network Collapse Comparison (Normalized)")
    plt.legend()
    plt.grid(True)

    if output_path:
        plt.savefig(output_path)

    plt.show()