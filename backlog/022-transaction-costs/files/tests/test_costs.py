import pandas as pd
from trading.costs import net_returns


def test_constant_position_pays_only_entry_cost():
    g = pd.Series([0.01] * 5)
    pos = pd.Series([1.0] * 5)
    n = net_returns(g, pos, cost_rate=0.001)
    assert abs(n.iloc[0] - 0.009) < 1e-12
    assert (n.iloc[1:] == 0.01).all()


def test_zero_cost_changes_nothing():
    g = pd.Series([0.01, -0.02, 0.03])
    pos = pd.Series([1.0, 0.0, 1.0])
    assert (net_returns(g, pos, 0.0) == g).all()
