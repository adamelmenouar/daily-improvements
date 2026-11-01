"""Effet de levier financé par emprunt."""


def levered_return(portfolio_return, leverage, borrow_rate):
    """Rendement sur fonds propres : L * r - (L - 1) * taux d'emprunt (même période)."""
    if leverage < 1:
        raise ValueError("leverage doit être >= 1")
    return leverage * portfolio_return - (leverage - 1) * borrow_rate
