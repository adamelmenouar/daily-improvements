"""Relation 'triangle du crédit' : spread = probabilité de défaut x (1 - recouvrement)."""


def cds_spread(default_prob_annual, recovery=0.4):
    return default_prob_annual * (1 - recovery)


def implied_default_prob(spread, recovery=0.4):
    if recovery >= 1:
        raise ValueError("recovery doit être < 1")
    return spread / (1 - recovery)
