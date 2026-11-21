"""Backtest de l'Expected Shortfall : la perte moyenne en cas d'exception est-elle bien prévue ?"""
import numpy as np


def es_backtest_z1(returns, var_forecast, es_forecast):
    """Z1 = moyenne(-r / ES) - 1 sur les jours d'exception (perte > VaR). ~0 si l'ES est bien calibrée ;
    > 0 si l'ES sous-estime les pertes. Retourne nan s'il n'y a aucune exception."""
    r = np.asarray(returns, dtype=float)
    v = np.broadcast_to(np.asarray(var_forecast, dtype=float), r.shape)
    es = np.broadcast_to(np.asarray(es_forecast, dtype=float), r.shape)
    exc = -r > v
    if not exc.any():
        return float("nan")
    return float(np.mean(-r[exc] / es[exc]) - 1)
