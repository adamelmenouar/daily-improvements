"""Projection euclidienne de poids quelconques sur {w >= 0, somme = 1} (Duchi et al., 2008)."""
import numpy as np


def project_to_simplex(w):
    v = np.asarray(w, dtype=float)
    u = np.sort(v)[::-1]
    css = np.cumsum(u) - 1
    k = np.arange(1, len(v) + 1)
    rho = np.nonzero(u - css / k > 0)[0][-1]
    return np.maximum(v - css[rho] / (rho + 1), 0.0)
