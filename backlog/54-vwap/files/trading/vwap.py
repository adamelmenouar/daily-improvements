"""Prix moyen pondéré par les volumes."""


def vwap(price, volume):
    """VWAP cumulé depuis le début de la série."""
    return (price * volume).cumsum() / volume.cumsum()
