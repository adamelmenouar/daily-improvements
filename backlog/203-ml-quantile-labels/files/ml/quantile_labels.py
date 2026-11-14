"""Transforme des rendements futurs en classes (0 = pires, n_classes - 1 = meilleurs)."""
import numpy as np


def quantile_labels(forward_returns, n_classes=3):
    r = np.asarray(forward_returns, dtype=float)
    edges = np.quantile(r, np.linspace(0, 1, n_classes + 1)[1:-1])
    return np.searchsorted(edges, r, side="right")
