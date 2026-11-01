"""Coût des fonds propres et coût moyen pondéré du capital."""


def cost_of_equity(rf, beta, market_risk_premium):
    """CAPM : rf + beta * prime de risque du marché."""
    return rf + beta * market_risk_premium


def wacc(equity, debt, cost_equity, cost_debt, tax_rate):
    """Coût moyen pondéré du capital, dette après économie d'impôt."""
    total = equity + debt
    return equity / total * cost_equity + debt / total * cost_debt * (1 - tax_rate)
