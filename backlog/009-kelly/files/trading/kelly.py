"""Critère de Kelly."""


def kelly_fraction(win_prob, win_loss_ratio):
    """Fraction du capital à miser : f* = p - (1 - p) / b. Négative = ne pas jouer."""
    if not 0 <= win_prob <= 1:
        raise ValueError("win_prob doit être dans [0, 1]")
    if win_loss_ratio <= 0:
        raise ValueError("win_loss_ratio doit être > 0")
    return win_prob - (1 - win_prob) / win_loss_ratio


def half_kelly(win_prob, win_loss_ratio):
    """Version prudente : la moitié de Kelly, bornée à [0, 1]."""
    return min(1.0, max(0.0, 0.5 * kelly_fraction(win_prob, win_loss_ratio)))
