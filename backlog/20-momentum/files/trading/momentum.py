"""Momentum de série temporelle (long si le rendement passé est positif)."""
import numpy as np


def momentum_strategy(prices, lookback=60):
    signal = np.sign(prices.pct_change(lookback)).clip(lower=0)  # long / flat
    return prices.pct_change() * signal.shift(1)
