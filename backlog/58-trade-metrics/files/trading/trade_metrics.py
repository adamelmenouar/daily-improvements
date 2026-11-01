"""Statistiques sur une liste de gains/pertes par transaction."""
import numpy as np


def hit_rate(pnls):
    p = np.asarray(pnls, dtype=float)
    return float((p > 0).mean())


def profit_factor(pnls):
    p = np.asarray(pnls, dtype=float)
    loss = -p[p < 0].sum()
    return float("inf") if loss == 0 else float(p[p > 0].sum() / loss)


def expectancy(pnls):
    """Gain moyen par transaction."""
    return float(np.mean(pnls))
