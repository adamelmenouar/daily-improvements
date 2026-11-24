"""Points pivots classiques calculés à partir de la séance précédente."""


def pivot_points(high, low, close):
    p = (high + low + close) / 3
    return {
        "S2": p - (high - low), "S1": 2 * p - high, "P": p,
        "R1": 2 * p - low, "R2": p + (high - low),
    }
