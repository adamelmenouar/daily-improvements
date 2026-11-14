"""Lambda de Kyle : variation de prix par unité de volume signé (acheteur - vendeur)."""
import numpy as np


def kyle_lambda(price_changes, signed_volume):
    x, y = np.asarray(signed_volume, dtype=float), np.asarray(price_changes, dtype=float)
    return float(np.polyfit(x, y, 1)[0])
