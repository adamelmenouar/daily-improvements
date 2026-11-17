"""Écrêtage des valeurs extrêmes."""
import numpy as np


def winsorize(x, lower=0.01, upper=0.99):
    """Ramène les valeurs sous le quantile `lower` / au-dessus du quantile `upper` à ces quantiles."""
    if not 0 <= lower < upper <= 1:
        raise ValueError("il faut 0 <= lower < upper <= 1")
    a = np.asarray(x, dtype=float)
    lo, hi = np.quantile(a, [lower, upper])
    return np.clip(a, lo, hi)
