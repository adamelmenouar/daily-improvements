"""Ratios de performance ajustés du risque (rendements périodiques)."""
import numpy as np


def sortino(returns, periods=252, target=0.0):
    """Comme Sharpe mais ne pénalise que la volatilité à la baisse."""
    r = np.asarray(returns, dtype=float)
    downside = np.minimum(r - target, 0.0)
    dd = np.sqrt((downside ** 2).mean())
    if dd == 0:
        return float("inf")
    return float(np.sqrt(periods) * (r.mean() - target) / dd)


def calmar(returns, periods=252):
    """Rendement annualisé divisé par la valeur absolue du drawdown maximal."""
    from risk.drawdown import max_drawdown

    r = np.asarray(returns, dtype=float)
    ann = (1 + r).prod() ** (periods / len(r)) - 1
    mdd = abs(max_drawdown(r))
    return float("inf") if mdd == 0 else float(ann / mdd)
