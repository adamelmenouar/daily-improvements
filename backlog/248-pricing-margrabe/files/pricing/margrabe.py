"""Option d'échange : droit de recevoir l'actif 1 contre l'actif 2 (payoff max(S1 - S2, 0))."""
from math import log, sqrt
from scipy.stats import norm


def margrabe_exchange(s1, s2, t, sigma1, sigma2, rho):
    """Aucun taux n'intervient : le numéraire est l'actif 2."""
    sigma = sqrt(sigma1**2 + sigma2**2 - 2 * rho * sigma1 * sigma2)
    d1 = (log(s1 / s2) + 0.5 * sigma**2 * t) / (sigma * sqrt(t))
    return s1 * norm.cdf(d1) - s2 * norm.cdf(d1 - sigma * sqrt(t))
