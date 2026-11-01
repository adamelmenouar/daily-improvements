import pandas as pd
from utils.lags import make_lags


def test_known_values():
    out = make_lags(pd.Series([1, 2, 3, 4]), [1, 2])
    assert out["lag_1"].tolist()[1:] == [1, 2, 3]
    assert out["lag_2"].tolist()[2:] == [1, 2]


def test_no_future_leak():
    out = make_lags(pd.Series(range(10)), [1])
    assert (out["lag_1"].dropna() < pd.Series(range(10))[1:]).all()
