import pandas as pd
from trading.seasonality import weekday_mean_returns


def test_monday_effect_is_detected():
    idx = pd.bdate_range("2024-01-01", periods=100)
    r = pd.Series([0.01 if d.dayofweek == 0 else 0.0 for d in idx], index=idx)
    m = weekday_mean_returns(r)
    assert m.loc[0] == 0.01 and m.loc[1] == 0.0


def test_only_business_days_present():
    idx = pd.bdate_range("2024-01-01", periods=50)
    assert set(weekday_mean_returns(pd.Series(0.0, index=idx)).index) == {0, 1, 2, 3, 4}
