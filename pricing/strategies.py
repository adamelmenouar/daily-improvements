"""Profits à l'échéance de stratégies d'options (primes incluses), par unité."""
import numpy as np


def straddle_pnl(spot_at_expiry, strike, call_premium, put_premium):
    s = np.asarray(spot_at_expiry, dtype=float)
    return np.abs(s - strike) - (call_premium + put_premium)


def straddle_breakevens(strike, call_premium, put_premium):
    total = call_premium + put_premium
    return strike - total, strike + total


def bull_call_spread_pnl(spot_at_expiry, k_low, k_high, net_debit):
    s = np.asarray(spot_at_expiry, dtype=float)
    return np.minimum(np.maximum(s - k_low, 0), k_high - k_low) - net_debit
