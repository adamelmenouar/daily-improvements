import pandas as pd
from utils.rebase import rebase


def test_series_starts_at_base():
    out = rebase(pd.Series([50.0, 55.0, 60.0]))
    assert out.iloc[0] == 100.0 and abs(out.iloc[-1] - 120.0) < 1e-12


def test_dataframe_columns_are_independent():
    df = pd.DataFrame({"a": [10.0, 20.0], "b": [200.0, 100.0]})
    out = rebase(df)
    assert out.iloc[0].tolist() == [100.0, 100.0] and out.iloc[1].tolist() == [200.0, 50.0]
