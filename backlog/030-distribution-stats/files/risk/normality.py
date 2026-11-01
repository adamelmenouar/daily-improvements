"""Test de normalité des rendements."""
import numpy as np
from scipy.stats import chi2, skew, kurtosis


def jarque_bera(returns):
    """Retourne (statistique, p-value). H0 : les rendements sont gaussiens."""
    r = np.asarray(returns, dtype=float)
    n = len(r)
    jb = n / 6 * (skew(r) ** 2 + kurtosis(r) ** 2 / 4)
    return float(jb), float(1 - chi2.cdf(jb, df=2))
