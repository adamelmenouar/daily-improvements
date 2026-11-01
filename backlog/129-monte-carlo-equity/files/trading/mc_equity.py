"""Rééchantillonnage des transactions pour estimer la distribution des drawdowns."""
import numpy as np
from risk.drawdown import max_drawdown


def simulate_max_drawdowns(trade_returns, n_paths=2000, seed=0):
    """Pour chaque scénario, tire les transactions avec remise dans un ordre aléatoire."""
    t = np.asarray(trade_returns, dtype=float)
    rng = np.random.default_rng(seed)
    return np.array([max_drawdown(rng.choice(t, len(t))) for _ in range(n_paths)])
