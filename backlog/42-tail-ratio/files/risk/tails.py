"""Asymétrie des extrêmes et rapport gains / pertes."""
import numpy as np


def tail_ratio(returns, q=0.05):
    """|quantile haut (1-q)| / |quantile bas (q)|. > 1 : queue droite plus grosse."""
    r = np.asarray(returns, dtype=float)
    return float(abs(np.quantile(r, 1 - q)) / abs(np.quantile(r, q)))


def gain_to_pain(returns):
    """Somme des rendements / somme des pertes en valeur absolue."""
    r = np.asarray(returns, dtype=float)
    pain = -r[r < 0].sum()
    return float("inf") if pain == 0 else float(r.sum() / pain)
