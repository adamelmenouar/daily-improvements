"""Nombre de périodes par an selon la fréquence des données."""
import math

PERIODS_PER_YEAR = {"D": 252, "W": 52, "M": 12, "Q": 4, "Y": 1}


def periods_per_year(freq):
    try:
        return PERIODS_PER_YEAR[freq.upper()]
    except KeyError:
        raise ValueError(f"fréquence inconnue : {freq!r}") from None


def scale_volatility(vol, from_freq, to_freq):
    """Convertit une volatilité d'une fréquence à une autre (racine du temps)."""
    return vol * math.sqrt(periods_per_year(from_freq) / periods_per_year(to_freq))
