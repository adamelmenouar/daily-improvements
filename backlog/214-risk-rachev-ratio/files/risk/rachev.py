"""Ratio de Rachev : gain moyen dans la meilleure queue / perte moyenne dans la pire queue."""
import numpy as np


def rachev_ratio(returns, tail=0.05):
    r = np.sort(np.asarray(returns, dtype=float))
    k = max(int(len(r) * tail), 1)
    return float(r[-k:].mean() / abs(r[:k].mean()))
