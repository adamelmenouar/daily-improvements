"""Ratios rendement / drawdowns, calculés sur les n pires épisodes de baisse."""
import numpy as np
from risk.drawdown_table import top_drawdowns
from utils.returns import annualize_return


def sterling_ratio(returns, n=5, periods=252):
    """Rendement annualisé / moyenne des profondeurs (en valeur absolue) des n pires drawdowns."""
    dd = [abs(e["depth"]) for e in top_drawdowns(returns, n)]
    return float("inf") if not dd else float(annualize_return(returns, periods) / np.mean(dd))


def burke_ratio(returns, n=5, periods=252):
    """Rendement annualisé / racine de la somme des carrés des n pires drawdowns."""
    dd = np.array([abs(e["depth"]) for e in top_drawdowns(returns, n)])
    return float("inf") if len(dd) == 0 else float(annualize_return(returns, periods) / np.sqrt((dd**2).sum()))
