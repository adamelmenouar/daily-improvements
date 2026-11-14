"""Triple barrière (López de Prado) : +1 si le profit est touché d'abord, -1 si le stop, 0 si l'horizon expire."""


def triple_barrier_label(prices, start, take_profit, stop_loss, horizon):
    """take_profit et stop_loss sont des fractions positives du prix d'entrée."""
    entry = prices[start]
    for i in range(start + 1, min(start + horizon, len(prices) - 1) + 1):
        r = prices[i] / entry - 1
        if r >= take_profit:
            return 1
        if r <= -stop_loss:
            return -1
    return 0
