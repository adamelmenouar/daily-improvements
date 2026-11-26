"""Risque de ruine d'une stratégie à gains et pertes égaux (approximation classique)."""


def risk_of_ruin(win_prob, units):
    """Probabilité de perdre `units` mises avant tout gain net. Vaut 1 sans avantage statistique."""
    if not 0 <= win_prob <= 1:
        raise ValueError("win_prob doit être dans [0, 1]")
    edge = 2 * win_prob - 1
    if edge <= 0:
        return 1.0
    return ((1 - edge) / (1 + edge)) ** units
