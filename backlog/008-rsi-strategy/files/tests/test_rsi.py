from trading.backtest.ma_crossover import simulate_prices
from trading.rsi import rsi, rsi_strategy


def test_rsi_bounds():
    r = rsi(simulate_prices(500)).dropna()
    assert ((r >= 0) & (r <= 100)).all()


def test_strategy_same_length():
    p = simulate_prices(300)
    assert len(rsi_strategy(p)) == len(p)
