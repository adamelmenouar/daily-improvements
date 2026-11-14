"""Couverture d'une position (spot) par un instrument liquide (futures)."""
import numpy as np


def min_variance_hedge_ratio(spot_returns, hedge_returns):
    """h* = cov(spot, hedge) / var(hedge)."""
    s, h = np.asarray(spot_returns, dtype=float), np.asarray(hedge_returns, dtype=float)
    return float(np.cov(s, h, ddof=1)[0, 1] / np.var(h, ddof=1))


def hedge_effectiveness(spot_returns, hedge_returns):
    """Part de variance éliminée = R² de la régression = corrélation au carré."""
    return float(np.corrcoef(spot_returns, hedge_returns)[0, 1] ** 2)
