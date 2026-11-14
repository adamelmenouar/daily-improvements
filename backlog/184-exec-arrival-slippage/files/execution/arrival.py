"""Slippage par rapport au prix milieu à l'arrivée de l'ordre."""


def arrival_slippage_bps(arrival_mid, avg_fill_price, side="buy"):
    sign = 1.0 if side == "buy" else -1.0
    return sign * (avg_fill_price - arrival_mid) / arrival_mid * 1e4
