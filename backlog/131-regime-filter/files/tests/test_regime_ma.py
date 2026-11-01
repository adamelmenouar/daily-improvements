import pandas as pd
from trading.regime_ma import regime_filtered_returns


def test_no_exposure_in_a_falling_market():
    p = pd.Series([200 * 0.99**i for i in range(400)])
    assert regime_filtered_returns(p, 50).fillna(0).abs().sum() == 0


def test_no_exposure_before_the_window_is_full():
    p = pd.Series([100 * 1.01**i for i in range(300)])
    assert regime_filtered_returns(p, 100).iloc[:100].fillna(0).abs().sum() == 0


def test_full_exposure_in_a_steady_uptrend():
    p = pd.Series([100 * 1.01**i for i in range(300)])
    assert (regime_filtered_returns(p, 50).iloc[60:] - 0.01).abs().max() < 1e-12
