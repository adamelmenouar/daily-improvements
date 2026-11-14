import pandas as pd
from ml.features import market_features
from trading.backtest.ma_crossover import simulate_prices


def test_expected_columns():
    f = market_features(simulate_prices(100), (5, 10))
    assert list(f.columns) == ["ret_5", "vol_5", "mom_5", "ret_10", "vol_10", "mom_10"]


def test_no_lookahead():
    p = simulate_prices(200)
    full, cut = market_features(p), market_features(p.iloc[:150])
    assert full.iloc[:150].equals(cut) or ((full.iloc[:150] - cut).abs().max().max() < 1e-12)


def test_leading_values_are_nan():
    assert market_features(simulate_prices(100), (20,)).iloc[:19].isna().all().all()
