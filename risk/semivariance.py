"""Mesures de risque à la baisse."""
import numpy as np


def downside_deviation(returns, target=0.0):
    """Racine de la moyenne des carrés des écarts sous la cible."""
    r = np.asarray(returns, dtype=float)
    return float(np.sqrt(np.mean(np.minimum(r - target, 0.0) ** 2)))


def semivariance(returns):
    """Variance des seuls rendements inférieurs à la moyenne."""
    r = np.asarray(returns, dtype=float)
    return float(np.mean(np.minimum(r - r.mean(), 0.0) ** 2))
