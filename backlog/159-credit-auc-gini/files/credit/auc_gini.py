"""Qualité de classement d'un score de défaut."""
import numpy as np
from scipy.stats import rankdata


def auc(scores, defaulted):
    """Probabilité qu'un défaillant ait un score de risque plus élevé qu'un non-défaillant (Mann-Whitney)."""
    s, y = np.asarray(scores, dtype=float), np.asarray(defaulted, dtype=int)
    n1, n0 = (y == 1).sum(), (y == 0).sum()
    ranks = rankdata(s)
    return float((ranks[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def gini(scores, defaulted):
    return 2 * auc(scores, defaulted) - 1
