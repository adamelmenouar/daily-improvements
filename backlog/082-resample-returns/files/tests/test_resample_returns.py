import pandas as pd
from utils.resample import compound_returns


def test_two_weeks_of_one_percent():
    idx = pd.bdate_range("2024-01-01", periods=10)  # lundi -> vendredi x 2
    out = compound_returns(pd.Series(0.01, index=idx), "W")
    assert len(out) == 2 and abs(out.iloc[0] - (1.01**5 - 1)) < 1e-12


def test_compounding_preserves_total_return():
    idx = pd.bdate_range("2024-01-01", periods=40)
    r = pd.Series(0.002, index=idx)
    assert abs((1 + compound_returns(r, "W")).prod() - (1 + r).prod()) < 1e-12
