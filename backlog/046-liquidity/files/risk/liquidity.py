"""Mesures de liquidité."""
import numpy as np


def amihud_illiquidity(returns, dollar_volume):
    """Moyenne de |rendement| / volume en valeur. Plus c'est grand, moins c'est liquide."""
    r = np.asarray(returns, dtype=float)
    v = np.asarray(dollar_volume, dtype=float)
    return float(np.mean(np.abs(r) / v))


def half_spread_cost(bid, ask):
    """Coût relatif d'un aller simple au mid : (ask - bid) / (ask + bid)."""
    return (ask - bid) / (ask + bid)
