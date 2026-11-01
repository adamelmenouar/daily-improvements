"""Test de Dickey-Fuller simple (sans retards, avec constante).

Statistique t de b dans : dx_t = a + b * x_{t-1} + e. Seuil critique à 5 % : environ -2.86.
"""
import numpy as np

CRITICAL_5PCT = -2.86


def adf_statistic(x):
    a = np.asarray(x, dtype=float)
    y, lag = np.diff(a), a[:-1]
    X = np.column_stack([np.ones(len(lag)), lag])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    sigma2 = resid @ resid / (len(y) - 2)
    se_b = np.sqrt(sigma2 * np.linalg.inv(X.T @ X)[1, 1])
    return float(beta[1] / se_b)


def is_stationary(x, critical=CRITICAL_5PCT):
    return adf_statistic(x) < critical
