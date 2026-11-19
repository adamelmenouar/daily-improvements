"""Test ARCH-LM : la variance dépend-elle des chocs passés (volatility clustering) ?"""
import numpy as np
from scipy.stats import chi2


def arch_lm_test(returns, lags=5):
    """Retourne (LM, p-value). H0 : pas d'effet ARCH."""
    e2 = (np.asarray(returns, dtype=float) - np.mean(returns)) ** 2
    y = e2[lags:]
    X = np.column_stack([np.ones(len(y))] + [e2[lags - k:-k] for k in range(1, lags + 1)])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    r2 = 1 - resid.var() / y.var()
    lm = len(y) * r2
    return float(lm), float(1 - chi2.cdf(lm, df=lags))
