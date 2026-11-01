"""Corrélation de rang entre un signal et le rendement futur."""
from scipy.stats import spearmanr


def information_coefficient(signal, forward_returns):
    """Spearman entre signal(t) et rendement(t+1). Un IC de 0.05 est déjà considéré comme bon."""
    return float(spearmanr(signal, forward_returns)[0])
