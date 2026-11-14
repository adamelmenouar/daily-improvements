"""Corrections de p-values contrôlant le risque d'au moins un faux positif sur plusieurs tests."""
import numpy as np


def bonferroni(pvalues):
    p = np.asarray(pvalues, dtype=float)
    return np.minimum(p * len(p), 1.0)


def holm(pvalues):
    """Holm descendant : jamais moins puissant que Bonferroni."""
    p = np.asarray(pvalues, dtype=float)
    order = np.argsort(p)
    adj = np.empty_like(p)
    running = 0.0
    for rank, i in enumerate(order):
        running = max(running, (len(p) - rank) * p[i])
        adj[i] = min(running, 1.0)
    return adj
