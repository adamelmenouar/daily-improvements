"""Ajustement quanto : une option payée dans une autre devise que son sous-jacent."""
from math import exp


def quanto_forward(spot, foreign_rate, t, sigma_asset, sigma_fx, correlation):
    """Prix à terme sous la mesure domestique : S * exp((r_étranger - rho * sigma_actif * sigma_change) * T).
    sigma_fx : volatilité du taux de change (devise domestique par unité de devise étrangère)."""
    return spot * exp((foreign_rate - correlation * sigma_asset * sigma_fx) * t)
