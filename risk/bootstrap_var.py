"""Incertitude d'une VaR historique par rééchantillonnage."""
import numpy as np


def bootstrap_var_ci(returns, alpha=0.95, n_boot=2000, level=0.95, seed=0):
    """Retourne (borne basse, VaR observée, borne haute)."""
    r = np.asarray(returns, dtype=float)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(r), (n_boot, len(r)))
    boots = -np.quantile(r[idx], 1 - alpha, axis=1)
    lo, hi = np.quantile(boots, [(1 - level) / 2, 1 - (1 - level) / 2])
    return float(lo), float(-np.quantile(r, 1 - alpha)), float(hi)
