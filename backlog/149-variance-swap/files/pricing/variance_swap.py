"""Variance swap : échange de la variance réalisée contre un strike de variance."""
import numpy as np


def realized_variance(prices, periods=252):
    """Variance annualisée des rendements log (moyenne des carrés, sans centrage)."""
    r = np.diff(np.log(np.asarray(prices, dtype=float)))
    return float(np.mean(r**2) * periods)


def variance_swap_payoff(prices, strike_vol, vega_notional, periods=252):
    """Gain du receveur de variance réalisée. vega_notional : gain par point de volatilité (en %)."""
    var_notional = vega_notional / (2 * strike_vol * 100)
    return var_notional * (realized_variance(prices, periods) * 1e4 - (strike_vol * 100) ** 2)
