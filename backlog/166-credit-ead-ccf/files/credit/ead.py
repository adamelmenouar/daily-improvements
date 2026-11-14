"""Exposition au défaut d'une ligne de crédit : montant tiré + CCF x montant non tiré."""


def exposure_at_default(drawn, limit, ccf=0.5):
    if not 0 <= ccf <= 1:
        raise ValueError("ccf doit être dans [0, 1]")
    if drawn > limit:
        raise ValueError("drawn ne peut pas dépasser limit")
    return drawn + ccf * (limit - drawn)
