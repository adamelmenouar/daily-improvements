"""Call européen par Monte Carlo (variables antithétiques)."""
import numpy as np


def mc_call(s, k, t, r, sigma, n=100_000, seed=0):
    """Retourne (prix, erreur standard)."""
    z = np.random.default_rng(seed).standard_normal(n)
    drift = (r - 0.5 * sigma**2) * t
    vol = sigma * np.sqrt(t)
    pay = 0.5 * (np.maximum(s * np.exp(drift + vol * z) - k, 0)
                 + np.maximum(s * np.exp(drift - vol * z) - k, 0))
    disc = np.exp(-r * t)
    return float(disc * pay.mean()), float(disc * pay.std(ddof=1) / np.sqrt(n))
