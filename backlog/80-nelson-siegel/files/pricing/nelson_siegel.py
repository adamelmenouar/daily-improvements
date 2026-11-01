"""Courbe de taux paramétrique de Nelson-Siegel."""
import numpy as np


def nelson_siegel(t, beta0, beta1, beta2, tau):
    """beta0 : niveau long terme, beta1 : pente, beta2 : courbure, tau : échelle de temps."""
    t = np.asarray(t, dtype=float)
    x = t / tau
    loading = (1 - np.exp(-x)) / x
    return beta0 + beta1 * loading + beta2 * (loading - np.exp(-x))
