"""Exposant de Hurst par mise à l'échelle des écarts : std(x[t+lag] - x[t]) ~ lag^H.

H ~ 0.5 : marche aléatoire ; H < 0.5 : retour à la moyenne ; H > 0.5 : tendance.
"""
import numpy as np


def hurst_exponent(series, max_lag=20):
    x = np.asarray(series, dtype=float)
    lags = np.arange(2, max_lag)
    tau = [np.std(x[lag:] - x[:-lag]) for lag in lags]
    return float(np.polyfit(np.log(lags), np.log(tau), 1)[0])
