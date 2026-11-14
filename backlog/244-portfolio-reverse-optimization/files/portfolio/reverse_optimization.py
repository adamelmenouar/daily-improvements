"""Rendements d'équilibre implicites : ceux pour lesquels les poids de marché seraient optimaux."""
import numpy as np


def implied_returns(market_weights, cov, risk_aversion=3.0):
    """pi = lambda * Sigma @ w_marché."""
    return risk_aversion * np.asarray(cov, dtype=float) @ np.asarray(market_weights, dtype=float)
