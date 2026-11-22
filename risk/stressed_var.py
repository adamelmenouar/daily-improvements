"""VaR historique calculée sur la période la plus agitée de l'historique."""
import numpy as np


def stressed_var(returns, window=250, alpha=0.99):
    r = np.asarray(returns, dtype=float)
    vols = [r[i:i + window].std() for i in range(0, len(r) - window + 1)]
    i = int(np.argmax(vols))
    return float(-np.quantile(r[i:i + window], 1 - alpha))
