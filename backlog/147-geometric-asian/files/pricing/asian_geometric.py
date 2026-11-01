"""Call asiatique à moyenne géométrique continue (Kemna-Vorst)."""
from math import exp, log, sqrt
from scipy.stats import norm


def geometric_asian_call(s, k, t, r, sigma):
    sig_g = sigma / sqrt(3)
    fwd = s * exp(0.5 * t * (r - sigma**2 / 6))      # espérance de la moyenne géométrique
    d1 = (log(fwd / k) + 0.5 * sig_g**2 * t) / (sig_g * sqrt(t))
    return exp(-r * t) * (fwd * norm.cdf(d1) - k * norm.cdf(d1 - sig_g * sqrt(t)))
