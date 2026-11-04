from trading.backtest.ma_crossover import simulate_prices
from trading.bollinger import bollinger_bands, bollinger_strategy


def test_band_ordering():
    lo, mid, up = bollinger_bands(simulate_prices(300))
    ok = lo.notna()
    assert (lo[ok] <= mid[ok]).all() and (mid[ok] <= up[ok]).all()


def test_strategy_same_length():
    p = simulate_prices(300)
    assert len(bollinger_strategy(p)) == len(p)
