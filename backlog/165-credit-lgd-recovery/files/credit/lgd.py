"""LGD = 1 - valeur actuelle des recouvrements / exposition au défaut."""


def lgd_from_recoveries(ead, recoveries, discount_rate=0.05):
    """recoveries : liste de (délai en années, montant récupéré). Borné à [0, 1]."""
    if ead <= 0:
        raise ValueError("ead doit être > 0")
    pv = sum(amount / (1 + discount_rate) ** t for t, amount in recoveries)
    return min(max(1 - pv / ead, 0.0), 1.0)
