"""Smile de volatilité : sigma(K) = a + b * m + c * m^2 avec m = ln(K / F)."""
import numpy as np


def fit_smile(strikes, vols, forward):
    m = np.log(np.asarray(strikes, dtype=float) / forward)
    c, b, a = np.polyfit(m, np.asarray(vols, dtype=float), 2)
    return float(a), float(b), float(c)


def smile_vol(strike, forward, coefficients):
    a, b, c = coefficients
    m = np.log(strike / forward)
    return a + b * m + c * m**2
