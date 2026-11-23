"""VaR ajustée de la liquidité : VaR + coût de liquidation au spread."""


def liquidity_adjusted_var(var, half_spread):
    """Tout en proportion de la valeur du portefeuille : VaR + demi-spread relatif."""
    if var < 0 or half_spread < 0:
        raise ValueError("var et half_spread doivent être >= 0")
    return var + half_spread
