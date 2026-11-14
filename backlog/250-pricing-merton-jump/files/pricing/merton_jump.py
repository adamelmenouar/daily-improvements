"""Call européen dans le modèle à sauts de Merton (1976) : série de prix de Black-Scholes pondérés par Poisson."""
from math import exp, sqrt
from scipy.stats import poisson
from pricing.black_scholes import bs_call


def merton_jump_call(s, k, t, r, sigma, lam, mu_j, delta_j, n_terms=60):
    """lam : intensité des sauts par an ; les log-sauts suivent N(mu_j, delta_j^2)."""
    kappa = exp(mu_j + 0.5 * delta_j**2) - 1
    lam_p = lam * (1 + kappa)
    price = 0.0
    for n in range(n_terms):
        sigma_n = sqrt(sigma**2 + n * delta_j**2 / t)
        r_n = r - lam * kappa + n * (mu_j + 0.5 * delta_j**2) / t
        price += poisson.pmf(n, lam_p * t) * bs_call(s, k, t, r_n, sigma_n)
    return float(price)
