"""Régression d'un portefeuille sur des facteurs de risque."""
import numpy as np


def factor_betas(portfolio_returns, factor_returns):
    """Retourne (alpha par période, bêtas, R²). factor_returns : (T, K)."""
    y = np.asarray(portfolio_returns, dtype=float)
    x = np.column_stack([np.ones(len(y)), np.asarray(factor_returns, dtype=float)])
    coef, *_ = np.linalg.lstsq(x, y, rcond=None)
    resid = y - x @ coef
    r2 = 1 - resid.var() / y.var()
    return float(coef[0]), coef[1:], float(r2)
