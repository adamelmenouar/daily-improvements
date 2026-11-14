"""Rééquilibrer seulement en partie pour limiter les coûts de transaction."""
import numpy as np


def partial_rebalance(weights, target, max_turnover):
    """Rotation = moitié de la somme des |écarts|. Au-delà du plafond, on avance proportionnellement vers la cible."""
    w, t = np.asarray(weights, dtype=float), np.asarray(target, dtype=float)
    turnover = 0.5 * np.abs(t - w).sum()
    if turnover <= max_turnover:
        return t
    return w + (max_turnover / turnover) * (t - w)
