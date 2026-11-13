import pandas as pd
from trading.trailing_stop import trailing_stop_returns


def test_rising_prices_never_stopped():
    p = pd.Series([100 * 1.01**i for i in range(100)])
    assert (trailing_stop_returns(p, 0.05).dropna() - 0.01).abs().max() < 1e-12


def test_crash_is_partly_avoided():
    p = pd.Series([100, 110, 120, 100, 80, 60, 50], dtype=float)
    held = p.pct_change().add(1).prod() - 1
    stopped = trailing_stop_returns(p, 0.10).fillna(0).add(1).prod() - 1
    assert stopped > held
