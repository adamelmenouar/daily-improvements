"""Test de Ljung-Box : y a-t-il de l'autocorrélation jusqu'au retard m ?"""
import numpy as np
from scipy.stats import chi2
from ts.acf import acf


def ljung_box(x, lags=10):
    """Retourne (statistique Q, p-value). H0 : pas d'autocorrélation."""
    n = len(x)
    rho = acf(x, lags)[1:]
    q = n * (n + 2) * np.sum(rho**2 / (n - np.arange(1, lags + 1)))
    return float(q), float(1 - chi2.cdf(q, df=lags))
