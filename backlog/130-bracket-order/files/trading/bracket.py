"""Ordre bracket : sortie au stop ou à l'objectif, selon ce qui est touché en premier."""


def simulate_bracket(prices, entry_index, stop_pct, target_pct):
    """Position longue. Retourne (indice de sortie, rendement). Sans touche, sortie au dernier prix."""
    entry = prices[entry_index]
    for i in range(entry_index + 1, len(prices)):
        r = prices[i] / entry - 1
        if r <= -stop_pct:
            return i, -stop_pct
        if r >= target_pct:
            return i, target_pct
    return len(prices) - 1, prices[-1] / entry - 1
