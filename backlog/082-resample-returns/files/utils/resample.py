"""Passage de rendements journaliers à hebdomadaires / mensuels (série pandas indexée par dates)."""


def compound_returns(returns, rule="W"):
    """Compose les rendements sur chaque période ('W' semaine, 'ME' mois, ...)."""
    return (1 + returns).resample(rule).prod() - 1
