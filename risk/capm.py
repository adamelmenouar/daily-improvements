"""Bêta et alpha d'un actif par rapport à un indice (rendements périodiques)."""
import numpy as np


def beta(asset, market):
    a, m = np.asarray(asset, dtype=float), np.asarray(market, dtype=float)
    return float(np.cov(a, m, ddof=1)[0, 1] / np.var(m, ddof=1))


def alpha(asset, market, periods=252):
    """Alpha annualisé (rendement moyen non expliqué par le bêta)."""
    a, m = np.asarray(asset, dtype=float), np.asarray(market, dtype=float)
    return float((a.mean() - beta(a, m) * m.mean()) * periods)
