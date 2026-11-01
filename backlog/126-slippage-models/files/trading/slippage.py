"""Coûts d'exécution."""
import math


def fixed_bps_cost(notional, bps=2.0):
    """Coût forfaitaire en points de base du montant échangé."""
    return abs(notional) * bps / 1e4


def square_root_impact(order_size, daily_volume, daily_vol, k=1.0):
    """Impact relatif en racine : k * sigma * sqrt(ordre / volume journalier)."""
    if daily_volume <= 0:
        raise ValueError("daily_volume doit être > 0")
    return k * daily_vol * math.sqrt(abs(order_size) / daily_volume)
