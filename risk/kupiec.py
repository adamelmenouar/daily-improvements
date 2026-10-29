"""Test de Kupiec (proportion d'exceptions) pour le backtest d'une VaR."""
import numpy as np
from scipy.stats import chi2


def kupiec_test(returns, var_forecasts, alpha=0.95):
    """Retourne (n_exceptions, statistique LR, p-value). H0 : taux d'exception = 1 - alpha.

    var_forecasts : VaR positives (pertes) prévues pour chaque date.
    """
    r = np.asarray(returns, dtype=float)
    v = np.broadcast_to(np.asarray(var_forecasts, dtype=float), r.shape)
    n = len(r)
    x = int((r < -v).sum())
    p = 1 - alpha
    if x == 0:
        lr = -2 * n * np.log(1 - p)
    elif x == n:
        lr = -2 * n * np.log(p)
    else:
        phat = x / n
        lr = -2 * (
            (n - x) * np.log(1 - p) + x * np.log(p)
            - (n - x) * np.log(1 - phat) - x * np.log(phat)
        )
    return x, float(lr), float(1 - chi2.cdf(lr, df=1))
