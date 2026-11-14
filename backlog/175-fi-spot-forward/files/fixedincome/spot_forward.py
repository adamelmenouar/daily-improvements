"""Taux zéro-coupon (capitalisation annuelle) <-> taux forward à un an."""


def forwards_from_spots(spots):
    """spots[i] = taux zéro à (i+1) ans. Retourne f_0 = spots[0] puis les forwards 1 an dans 1, 2, ... ans."""
    out = [spots[0]]
    for n in range(2, len(spots) + 1):
        out.append((1 + spots[n - 1]) ** n / (1 + spots[n - 2]) ** (n - 1) - 1)
    return out


def spots_from_forwards(forwards):
    out, growth = [], 1.0
    for n, f in enumerate(forwards, start=1):
        growth *= 1 + f
        out.append(growth ** (1 / n) - 1)
    return out
