"""Moindres carrés ordinaires avec inférence classique."""
import numpy as np


def ols(X, y):
    """Retourne (coefficients avec intercept en premier, erreurs-types, t-stats, R²)."""
    x = np.column_stack([np.ones(len(X)), np.asarray(X, dtype=float)])
    y = np.asarray(y, dtype=float)
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    resid = y - x @ beta
    sigma2 = resid @ resid / (len(y) - x.shape[1])
    se = np.sqrt(np.diag(sigma2 * np.linalg.inv(x.T @ x)))
    return beta, se, beta / se, float(1 - resid.var() / y.var())
