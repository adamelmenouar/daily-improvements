"""Mise à l'échelle d'une VaR journalière."""
import math


def scale_var(var_1d, days):
    """Règle de la racine du temps : valable si les rendements sont i.i.d. et centrés."""
    if days <= 0:
        raise ValueError("days doit être > 0")
    return var_1d * math.sqrt(days)
