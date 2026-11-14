"""Taux nominal, taux réel et inflation anticipée (relation de Fisher exacte)."""


def real_rate(nominal, inflation):
    return (1 + nominal) / (1 + inflation) - 1


def breakeven_inflation(nominal, real):
    """Inflation qui rend équivalents une obligation nominale et une obligation indexée."""
    return (1 + nominal) / (1 + real) - 1
