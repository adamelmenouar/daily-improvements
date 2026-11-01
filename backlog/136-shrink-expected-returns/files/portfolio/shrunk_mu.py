"""Les rendements espérés estimés sont très bruités : on les rapproche de leur moyenne globale."""
import numpy as np


def shrink_expected_returns(mu, delta=0.5):
    """delta = 0 : inchangé ; delta = 1 : tous égaux à la moyenne (l'optimiseur ne parie plus sur eux)."""
    if not 0 <= delta <= 1:
        raise ValueError("delta doit être dans [0, 1]")
    m = np.asarray(mu, dtype=float)
    return (1 - delta) * m + delta * m.mean()
