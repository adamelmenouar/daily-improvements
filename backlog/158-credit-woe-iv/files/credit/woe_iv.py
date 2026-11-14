"""WoE / IV : pouvoir discriminant d'une variable catégorielle pour prédire le défaut."""
import numpy as np


def woe_iv(bins, defaulted, eps=0.5):
    """bins : catégorie de chaque emprunteur ; defaulted : 1 si défaut. Retourne ({catégorie: WoE}, IV).
    WoE = ln(part des bons / part des mauvais) ; eps évite les divisions par zéro."""
    b = np.asarray(bins)
    y = np.asarray(defaulted, dtype=int)
    goods, bads = (y == 0).sum(), (y == 1).sum()
    woe, iv = {}, 0.0
    for cat in np.unique(b):
        g = ((b == cat) & (y == 0)).sum() + eps
        d = ((b == cat) & (y == 1)).sum() + eps
        pg, pb = g / (goods + eps), d / (bads + eps)
        woe[cat] = float(np.log(pg / pb))
        iv += (pg - pb) * woe[cat]
    return woe, float(iv)
