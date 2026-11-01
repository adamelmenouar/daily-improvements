"""Découpage chronologique : jamais de mélange aléatoire sur des séries temporelles."""


def time_split(n, train_fraction=0.7):
    """Retourne (indices d'entraînement, indices de test) : le test suit strictement l'entraînement."""
    if not 0 < train_fraction < 1:
        raise ValueError("train_fraction doit être dans ]0, 1[")
    cut = int(n * train_fraction)
    return range(0, cut), range(cut, n)
