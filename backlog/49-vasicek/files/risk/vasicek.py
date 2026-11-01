"""Modèle à un facteur de Vasicek (base des exigences de fonds propres de Bâle)."""
from math import sqrt
from scipy.stats import norm


def vasicek_loss_quantile(pd_, rho, lgd=0.45, confidence=0.999):
    """Taux de perte du portefeuille dépassé avec probabilité 1 - confidence."""
    cond_pd = norm.cdf((norm.ppf(pd_) + sqrt(rho) * norm.ppf(confidence)) / sqrt(1 - rho))
    return float(lgd * cond_pd)
