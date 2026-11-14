"""Moments partiels inférieurs (LPM) et ratio Kappa."""
import numpy as np


def lower_partial_moment(returns, order=2, target=0.0):
    r = np.asarray(returns, dtype=float)
    return float(np.mean(np.maximum(target - r, 0.0) ** order))


def kappa_ratio(returns, order=2, target=0.0):
    """(moyenne - cible) / LPM_n^(1/n). L'ordre 1 est le ratio Oméga moins 1, l'ordre 2 le ratio de Sortino."""
    r = np.asarray(returns, dtype=float)
    lpm = lower_partial_moment(r, order, target)
    return float("inf") if lpm == 0 else float((r.mean() - target) / lpm ** (1 / order))
