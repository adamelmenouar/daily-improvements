"""Sensibilité d'une obligation à chaque point de la courbe zéro-coupon."""
import numpy as np


def _price(cash_flows, nodes, rates):
    return sum(cf / (1 + np.interp(t, nodes, rates)) ** t for t, cf in cash_flows)


def key_rate_durations(cash_flows, nodes, rates, bump=1e-4):
    """cash_flows : liste de (échéance en années, flux). Une valeur par noeud ; leur somme ~ duration effective."""
    nodes, rates = np.asarray(nodes, dtype=float), np.asarray(rates, dtype=float)
    p0 = _price(cash_flows, nodes, rates)
    out = []
    for i in range(len(nodes)):
        up, down = rates.copy(), rates.copy()
        up[i] += bump
        down[i] -= bump
        out.append(-(_price(cash_flows, nodes, up) - _price(cash_flows, nodes, down)) / (2 * bump * p0))
    return np.array(out)
