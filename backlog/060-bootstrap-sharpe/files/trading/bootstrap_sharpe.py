"""Incertitude sur le ratio de Sharpe par rééchantillonnage."""
import numpy as np


def _sharpe(r, periods):
    return np.sqrt(periods) * r.mean() / r.std(ddof=1)


def bootstrap_sharpe_ci(returns, n_boot=2000, level=0.95, periods=252, seed=0):
    """Retourne (borne basse, Sharpe observé, borne haute)."""
    r = np.asarray(returns, dtype=float)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(r), (n_boot, len(r)))
    boots = np.array([_sharpe(r[i], periods) for i in idx])
    lo, hi = np.quantile(boots, [(1 - level) / 2, 1 - (1 - level) / 2])
    return float(lo), float(_sharpe(r, periods)), float(hi)
