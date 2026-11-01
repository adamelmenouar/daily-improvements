"""Ciblage de volatilité : ajuste l'exposition pour viser une volatilité annuelle constante."""
import numpy as np


def vol_target_returns(returns, target=0.10, window=20, max_leverage=3.0, periods=252):
    realised = returns.rolling(window).std() * np.sqrt(periods)
    leverage = (target / realised).clip(upper=max_leverage)
    return returns * leverage.shift(1)  # levier connu la veille
