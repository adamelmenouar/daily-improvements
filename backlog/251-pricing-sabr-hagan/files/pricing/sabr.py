"""Volatilité implicite lognormale du modèle SABR (Hagan et al., 2002)."""
from math import log, sqrt


def sabr_vol(f, k, t, alpha, beta, rho, nu):
    one_b = 1 - beta
    if abs(f - k) < 1e-12 * f:
        fk = f**one_b
        corr = 1 + (one_b**2 / 24 * alpha**2 / f ** (2 * one_b) + rho * beta * nu * alpha / (4 * fk)
                    + (2 - 3 * rho**2) * nu**2 / 24) * t
        return alpha / fk * corr
    logfk = log(f / k)
    fk = (f * k) ** (one_b / 2)
    z = nu / alpha * fk * logfk
    x = log((sqrt(1 - 2 * rho * z + z**2) + z - rho) / (1 - rho))
    denom = fk * (1 + one_b**2 / 24 * logfk**2 + one_b**4 / 1920 * logfk**4)
    corr = 1 + (one_b**2 / 24 * alpha**2 / fk**2 + rho * beta * nu * alpha / (4 * fk) + (2 - 3 * rho**2) * nu**2 / 24) * t
    return alpha / denom * (z / x) * corr
