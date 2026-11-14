"""Règle du tick : hausse du prix = achat (+1), baisse = vente (-1), prix inchangé = signe précédent."""


def tick_rule(prices):
    signs, last = [], 1
    for i, p in enumerate(prices):
        if i > 0:
            if p > prices[i - 1]:
                last = 1
            elif p < prices[i - 1]:
                last = -1
        signs.append(last)
    return signs
