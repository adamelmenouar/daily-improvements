"""Capture haussière / baissière par rapport à un benchmark."""
import numpy as np


def up_capture(returns, benchmark):
    r, b = np.asarray(returns, dtype=float), np.asarray(benchmark, dtype=float)
    up = b > 0
    return float(r[up].mean() / b[up].mean())


def down_capture(returns, benchmark):
    r, b = np.asarray(returns, dtype=float), np.asarray(benchmark, dtype=float)
    dn = b < 0
    return float(r[dn].mean() / b[dn].mean())
