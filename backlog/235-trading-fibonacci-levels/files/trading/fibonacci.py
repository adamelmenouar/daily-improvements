"""Niveaux de retracement de Fibonacci d'un mouvement entre un plus bas et un plus haut."""

RATIOS = (0.236, 0.382, 0.5, 0.618, 0.786)


def fibonacci_retracements(swing_high, swing_low, uptrend=True):
    """Tendance haussière : retracements mesurés à partir du plus haut vers le bas ; baissière : du plus bas vers le haut."""
    if swing_high <= swing_low:
        raise ValueError("swing_high doit être > swing_low")
    span = swing_high - swing_low
    if uptrend:
        return {r: swing_high - r * span for r in RATIOS}
    return {r: swing_low + r * span for r in RATIOS}
