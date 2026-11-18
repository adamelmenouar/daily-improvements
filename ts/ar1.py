"""Modèle AR(1) : x_t = c + phi * x_{t-1} + bruit."""
import numpy as np


def fit_ar1(x):
    """Retourne (c, phi) estimés par moindres carrés."""
    a = np.asarray(x, dtype=float)
    phi, c = np.polyfit(a[:-1], a[1:], 1)
    return float(c), float(phi)


def forecast_ar1(x, steps=1):
    c, phi = fit_ar1(x)
    last = float(np.asarray(x, dtype=float)[-1])
    out = []
    for _ in range(steps):
        last = c + phi * last
        out.append(last)
    return np.array(out)
