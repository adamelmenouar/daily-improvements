"""Test d'indépendance des exceptions de VaR (clusters d'exceptions)."""
import numpy as np
from scipy.special import xlogy
from scipy.stats import chi2


def christoffersen_independence(exceptions):
    """exceptions : suite de 0/1. Retourne (LR, p-value). H0 : les exceptions sont indépendantes."""
    e = np.asarray(exceptions, dtype=int)
    a, b = e[:-1], e[1:]
    n00 = int(((a == 0) & (b == 0)).sum())
    n01 = int(((a == 0) & (b == 1)).sum())
    n10 = int(((a == 1) & (b == 0)).sum())
    n11 = int(((a == 1) & (b == 1)).sum())
    pi01 = n01 / max(n00 + n01, 1)
    pi11 = n11 / max(n10 + n11, 1)
    pi = (n01 + n11) / (n00 + n01 + n10 + n11)
    ll0 = xlogy(n00 + n10, 1 - pi) + xlogy(n01 + n11, pi)
    ll1 = (xlogy(n00, 1 - pi01) + xlogy(n01, pi01)
           + xlogy(n10, 1 - pi11) + xlogy(n11, pi11))
    lr = float(max(-2 * (ll0 - ll1), 0.0))
    return lr, float(1 - chi2.cdf(lr, df=1))
