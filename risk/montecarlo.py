"""VaR par simulation Monte Carlo."""
import numpy as np


def monte_carlo_var(mu, sigma, alpha=0.95, horizon=1, n_sims=100_000, seed=0):
    """VaR (perte positive) sur `horizon` jours pour des rendements log-normaux."""
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(n_sims)
    log_ret = (mu - 0.5 * sigma ** 2) * horizon + sigma * np.sqrt(horizon) * z
    pnl = np.expm1(log_ret)
    return float(-np.quantile(pnl, 1 - alpha))
