"""Kelly pour un actif risqué à rendements gaussiens : f* = mu / sigma^2."""


def continuous_kelly(mu, sigma, rf=0.0):
    """Levier optimal (mu et sigma sur la même période). Peut dépasser 1 : prudence, utiliser une fraction."""
    if sigma <= 0:
        raise ValueError("sigma doit être > 0")
    return (mu - rf) / sigma**2
