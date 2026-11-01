"""Forward Rate Agreement : taux à terme implicite et règlement."""


def fra_rate(df_start, df_end, accrual):
    """Taux simple entre deux dates à partir de leurs facteurs d'actualisation."""
    return (df_start / df_end - 1) / accrual


def fra_settlement(notional, fra_rate_contract, reference_rate, accrual):
    """Règlement (actualisé à la date de début) pour l'acheteur du FRA qui paie le taux fixe contractuel."""
    return notional * (reference_rate - fra_rate_contract) * accrual / (1 + reference_rate * accrual)
