"""K-fold purgé : retire du train les observations trop proches du test (fuite d'information)."""
import numpy as np


def purged_kfold_splits(n, n_splits=5, purge=5, embargo=5):
    """Génère (indices train, indices test). `purge` observations avant et `embargo` après chaque bloc test
    sont exclues de l'entraînement (les étiquettes recouvrent plusieurs périodes)."""
    folds = np.array_split(np.arange(n), n_splits)
    for test in folds:
        lo, hi = test[0], test[-1]
        mask = np.ones(n, dtype=bool)
        mask[max(lo - purge, 0): min(hi + embargo + 1, n)] = False
        yield np.nonzero(mask)[0], test
