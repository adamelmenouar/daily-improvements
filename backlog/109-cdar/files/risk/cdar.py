"""CDaR : drawdown moyen dans les pires (1 - alpha) % des cas."""
import numpy as np
from risk.drawdown import drawdown_series


def cdar(returns, alpha=0.95):
    """Valeur positive. Toujours comprise entre le quantile de drawdown et le drawdown maximal."""
    depth = -drawdown_series(returns)
    cutoff = np.quantile(depth, alpha)
    return float(depth[depth >= cutoff].mean())
