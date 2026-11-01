"""Coûts de transaction."""


def net_returns(gross_returns, positions, cost_rate=0.0005):
    """Rendements nets : on retire cost_rate * |variation de position| à chaque date.

    positions : position tenue pendant la période (déjà alignée sur gross_returns).
    """
    turnover = positions.diff().abs().fillna(positions.abs())
    return gross_returns - cost_rate * turnover
