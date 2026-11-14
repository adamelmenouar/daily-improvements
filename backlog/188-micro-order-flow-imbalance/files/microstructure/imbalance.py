"""Déséquilibre acheteur/vendeur, entre -1 (que des ventes) et +1 (que des achats)."""


def order_flow_imbalance(buy_volume, sell_volume):
    total = buy_volume + sell_volume
    if total == 0:
        return 0.0
    return (buy_volume - sell_volume) / total
