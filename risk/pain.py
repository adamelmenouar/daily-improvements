"""Pain Index : drawdown moyen sur toute la période (plus doux que l'Ulcer Index)."""
import numpy as np
from risk.drawdown import drawdown_series
from utils.returns import annualize_return


def pain_index(returns):
    return float(-drawdown_series(returns).mean())


def pain_ratio(returns, periods=252):
    p = pain_index(returns)
    return float("inf") if p == 0 else float(annualize_return(returns, periods) / p)
