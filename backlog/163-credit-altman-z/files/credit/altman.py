"""Z-score d'Altman (1968) pour entreprises industrielles cotées."""


def altman_z(working_capital, retained_earnings, ebit, market_equity, sales, total_assets, total_liabilities):
    x1, x2, x3 = working_capital / total_assets, retained_earnings / total_assets, ebit / total_assets
    x4, x5 = market_equity / total_liabilities, sales / total_assets
    return 1.2 * x1 + 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 1.0 * x5


def altman_zone(z):
    """'safe' au-dessus de 2.99, 'distress' sous 1.81, sinon 'grey'."""
    return "safe" if z > 2.99 else "distress" if z < 1.81 else "grey"
