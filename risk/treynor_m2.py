"""Ratios de performance ajustés du risque de marché."""
import numpy as np
from risk.capm import beta


def treynor_ratio(returns, market, rf=0.0, periods=252):
    """Excès de rendement annualisé par unité de bêta."""
    r, m = np.asarray(returns, dtype=float), np.asarray(market, dtype=float)
    return float((r.mean() - rf / periods) * periods / beta(r, m))


def modigliani_m2(returns, market, rf=0.0, periods=252):
    """Rendement annualisé qu'aurait le portefeuille s'il avait la volatilité du marché."""
    r, m = np.asarray(returns, dtype=float), np.asarray(market, dtype=float)
    sharpe = (r.mean() - rf / periods) / r.std(ddof=1)
    return float(rf + sharpe * np.sqrt(periods) * m.std(ddof=1) * np.sqrt(periods))
