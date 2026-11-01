"""Saisonnalité par jour de la semaine (série pandas indexée par dates)."""


def weekday_mean_returns(returns):
    """Rendement moyen du lundi (0) au dimanche (6)."""
    return returns.groupby(returns.index.dayofweek).mean()
