"""Optimisation rééchantillonnée : moyenne de portefeuilles optimaux sur des rendements espérés bruités."""
import numpy as np
from portfolio.tangency import tangency_weights


def resampled_tangency(mu, cov, n_obs, rf=0.0, n_sims=500, seed=0):
    """Tire mu ~ N(mu_estimé, cov / n_obs), calcule le portefeuille tangent de chaque tirage, puis les moyenne."""
    mu, cov = np.asarray(mu, dtype=float), np.asarray(cov, dtype=float)
    rng = np.random.default_rng(seed)
    draws = rng.multivariate_normal(mu, cov / n_obs, n_sims)
    return np.mean([tangency_weights(m, cov, rf) for m in draws], axis=0)
