"""Intensité de défaut constante déduite d'une probabilité de défaut cumulée."""
import math


def hazard_rate(cumulative_pd, horizon_years):
    if not 0 <= cumulative_pd < 1:
        raise ValueError("cumulative_pd doit être dans [0, 1[")
    return -math.log(1 - cumulative_pd) / horizon_years


def survival_probability(hazard, t):
    return math.exp(-hazard * t)


def default_probability(hazard, t):
    return 1 - survival_probability(hazard, t)
