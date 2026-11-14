"""Barres de volume : une nouvelle barre à chaque fois qu'un volume seuil est échangé."""


def volume_bars(prices, volumes, threshold):
    """Retourne une liste de (ouverture, plus haut, plus bas, clôture, volume)."""
    bars, o, h, l, vol = [], None, None, None, 0.0
    for p, v in zip(prices, volumes):
        o = p if o is None else o
        h = p if h is None else max(h, p)
        l = p if l is None else min(l, p)
        vol += v
        if vol >= threshold:
            bars.append((o, h, l, p, vol))
            o, h, l, vol = None, None, None, 0.0
    return bars
