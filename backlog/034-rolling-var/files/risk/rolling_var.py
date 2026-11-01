"""VaR historique sur fenêtre glissante (série pandas)."""


def rolling_var(returns, window=250, alpha=0.95):
    """Perte (positive) dépassée avec probabilité 1 - alpha, estimée sur les `window` derniers jours."""
    return -returns.rolling(window).quantile(1 - alpha)
