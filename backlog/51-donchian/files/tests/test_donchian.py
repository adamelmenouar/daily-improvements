from trading.backtest.ma_crossover import simulate_prices
from trading.donchian import donchian_channel, donchian_strategy


def test_channel_ordering():
    lo, hi = donchian_channel(simulate_prices(300))
    ok = lo.notna()
    assert (lo[ok] <= hi[ok]).all()


def test_strategy_same_length():
    p = simulate_prices(300)
    assert len(donchian_strategy(p)) == len(p)
