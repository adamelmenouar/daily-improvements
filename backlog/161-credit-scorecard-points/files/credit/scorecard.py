"""Échelle de score : base_score points pour des cotes base_odds contre 1, +pdo points chaque fois que les cotes doublent."""
import math


def score_from_pd(pd_, base_score=600, base_odds=50, pdo=20):
    factor = pdo / math.log(2)
    offset = base_score - factor * math.log(base_odds)
    return offset + factor * math.log((1 - pd_) / pd_)
