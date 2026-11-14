"""Structure par terme de volatilité : on interpole la variance totale sigma^2 * T, pas la volatilité."""
import numpy as np


def implied_vol_at(t, maturities, vols):
    m, v = np.asarray(maturities, dtype=float), np.asarray(vols, dtype=float)
    total = v**2 * m
    return float(np.sqrt(np.interp(t, m, total) / t))


def has_calendar_arbitrage(maturities, vols):
    """Vrai si la variance totale décroît avec la maturité (impossible sans arbitrage)."""
    total = np.asarray(vols, dtype=float) ** 2 * np.asarray(maturities, dtype=float)
    return bool((np.diff(total) < 0).any())
