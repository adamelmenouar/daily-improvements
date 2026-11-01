"""Conversions usuelles entre types de rendements."""
import numpy as np


def to_log(simple_returns):
    return np.log1p(np.asarray(simple_returns, dtype=float))


def to_simple(log_returns):
    return np.expm1(np.asarray(log_returns, dtype=float))


def cumulative_return(returns):
    return float(np.prod(1 + np.asarray(returns, dtype=float)) - 1)


def annualize_return(returns, periods=252):
    r = np.asarray(returns, dtype=float)
    return float(np.prod(1 + r) ** (periods / len(r)) - 1)


def annualize_vol(returns, periods=252):
    return float(np.std(np.asarray(returns, dtype=float), ddof=1) * np.sqrt(periods))
