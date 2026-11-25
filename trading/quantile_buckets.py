"""Rendement moyen futur par quantile de signal : un bon signal est monotone."""
import numpy as np
import pandas as pd


def bucket_returns(signal, forward_returns, q=5):
    """Index 0 = quantile le plus bas du signal, q-1 = le plus haut."""
    df = pd.DataFrame({"s": np.asarray(signal, dtype=float), "r": np.asarray(forward_returns, dtype=float)})
    df["bucket"] = pd.qcut(df["s"], q, labels=False, duplicates="drop")
    return df.groupby("bucket")["r"].mean()
