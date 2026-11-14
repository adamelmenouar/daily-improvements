"""Bêta d'un portefeuille : moyenne pondérée des bêtas de ses lignes."""
import numpy as np


def portfolio_beta(weights, betas):
    return float(np.dot(np.asarray(weights, dtype=float), np.asarray(betas, dtype=float)))


def betas_from_returns(asset_returns, market_returns):
    """Bêta de chaque colonne de asset_returns (T, N) par rapport au marché."""
    a, m = np.asarray(asset_returns, dtype=float), np.asarray(market_returns, dtype=float)
    return np.array([np.cov(a[:, j], m, ddof=1)[0, 1] / m.var(ddof=1) for j in range(a.shape[1])])
