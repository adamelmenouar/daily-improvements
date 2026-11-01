"""Taille de position à risque fixe par transaction."""


def fixed_fractional_size(capital, risk_fraction, entry, stop):
    """Nombre d'unités telles qu'une exécution du stop coûte `risk_fraction` du capital."""
    risk_per_unit = abs(entry - stop)
    if risk_per_unit == 0:
        raise ValueError("entry et stop doivent différer")
    return capital * risk_fraction / risk_per_unit
