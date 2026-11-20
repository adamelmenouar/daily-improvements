"""Lissage exponentiel simple."""
import numpy as np


def simple_exponential_smoothing(x, alpha=0.3):
    """Série lissée ; la dernière valeur est aussi la prévision à un pas."""
    if not 0 < alpha <= 1:
        raise ValueError("alpha doit être dans ]0, 1]")
    a = np.asarray(x, dtype=float)
    out = np.empty_like(a)
    out[0] = a[0]
    for t in range(1, len(a)):
        out[t] = alpha * a[t] + (1 - alpha) * out[t - 1]
    return out
