"""Implementation shortfall : coût d'exécution par rapport au prix au moment de la décision."""
import numpy as np


def implementation_shortfall_bps(decision_price, fill_prices, fill_quantities, side="buy"):
    """Coût en points de base du prix moyen d'exécution vs prix de décision (positif = coûteux)."""
    p, q = np.asarray(fill_prices, dtype=float), np.asarray(fill_quantities, dtype=float)
    avg = (p * q).sum() / q.sum()
    sign = 1.0 if side == "buy" else -1.0
    return float(sign * (avg - decision_price) / decision_price * 1e4)
