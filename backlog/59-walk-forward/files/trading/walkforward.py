"""Découpage walk-forward : entraîner sur le passé, tester sur la période suivante."""


def walk_forward_splits(n, train_size, test_size):
    """Génère des paires (indices d'entraînement, indices de test) sans chevauchement ni fuite du futur."""
    start = 0
    while start + train_size + test_size <= n:
        train = range(start, start + train_size)
        test = range(start + train_size, start + train_size + test_size)
        yield train, test
        start += test_size
