import pandas as pd

def preprocess(input_path, output_path):
    """
    Preprocess raw signed network dataset into cleaned edge list.
    """

    # Read file (skip comment lines)
    df = pd.read_csv(
        input_path,
        sep=r"\s+",
        comment="#",
        header=None,
        names=["source", "target", "sign"]
    )

    # Remove self-loops
    df = df[df["source"] != df["target"]]

    # Add default weight
    df["weight"] = 1

    # Ensure sign is either +1 or -1
    df = df[df["sign"].isin([1, -1])]

    # Save processed file
    df.to_csv(output_path, index=False)

    return df