import numpy as np
from pricing.strategies import straddle_pnl, straddle_breakevens, bull_call_spread_pnl


def test_straddle_loses_premium_at_the_money():
    assert straddle_pnl(100, 100, 4, 3) == -7


def test_straddle_is_zero_at_breakevens():
    lo, hi = straddle_breakevens(100, 4, 3)
    assert np.allclose(straddle_pnl([lo, hi], 100, 4, 3), 0)


def test_bull_spread_profit_is_capped():
    assert bull_call_spread_pnl(200, 100, 110, 4) == 6
    assert bull_call_spread_pnl(50, 100, 110, 4) == -4
