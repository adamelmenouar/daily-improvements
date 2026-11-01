"""Épisodes de drawdown : du sommet à la récupération."""
import numpy as np


def top_drawdowns(returns, n=3):
    """Liste des n pires épisodes : {'depth', 'start', 'trough', 'end'} (end = None si non récupéré)."""
    eq = np.cumprod(1 + np.asarray(returns, dtype=float))
    episodes, peak_i = [], 0
    trough_i = 0
    for i in range(1, len(eq)):
        if eq[i] >= eq[peak_i]:
            if trough_i > peak_i:
                episodes.append(dict(depth=float(eq[trough_i] / eq[peak_i] - 1), start=peak_i, trough=trough_i, end=i))
            peak_i, trough_i = i, i
        elif eq[i] < eq[trough_i] or trough_i == peak_i:
            trough_i = i
    if trough_i > peak_i:
        episodes.append(dict(depth=float(eq[trough_i] / eq[peak_i] - 1), start=peak_i, trough=trough_i, end=None))
    return sorted(episodes, key=lambda e: e["depth"])[:n]
