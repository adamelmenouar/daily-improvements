"""Spread effectif estimé à partir de la covariance sérielle des variations de prix (Roll, 1984)."""
import numpy as np


def roll_spread(prices):
    """2 * sqrt(-cov(dp_t, dp_{t-1})) ; nan si la covariance est positive (hypothèse du modèle violée)."""
    dp = np.diff(np.asarray(prices, dtype=float))
    cov = np.cov(dp[1:], dp[:-1], ddof=1)[0, 1]
    return float(2 * np.sqrt(-cov)) if cov < 0 else float("nan")
