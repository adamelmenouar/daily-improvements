"""Écart de performance par rapport à un benchmark."""
import numpy as np


def tracking_error(returns, benchmark, periods=252):
    d = np.asarray(returns, dtype=float) - np.asarray(benchmark, dtype=float)
    return float(d.std(ddof=1) * np.sqrt(periods))


def information_ratio(returns, benchmark, periods=252):
    d = np.asarray(returns, dtype=float) - np.asarray(benchmark, dtype=float)
    te = d.std(ddof=1)
    return float("nan") if te == 0 else float(d.mean() / te * np.sqrt(periods))
