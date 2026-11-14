import numpy as np
import pandas as pd
from trading.vol_regime import volatility_regime


def test_a_turbulent_period_is_flagged_high_vol():
    rng = np.random.default_rng(235)
    r = pd.Series(np.concatenate([rng.normal(0, 0.005, 500), rng.normal(0, 0.03, 100), rng.normal(0, 0.005, 200)]))
    reg = volatility_regime(r)
    assert reg.iloc[530:590].mean() > 0.9           # crise : quasi toujours en régime de forte volatilité
    assert reg.iloc[200:480].mean() < 0.65         # calme : environ la moitié des jours au-dessus de la médiane


def test_values_are_binary_or_nan_and_use_only_the_past():
    r = pd.Series(np.random.default_rng(236).normal(0, 0.01, 300))
    full, cut = volatility_regime(r), volatility_regime(r.iloc[:200])
    assert set(full.dropna().unique()) <= {0.0, 1.0}
    assert full.iloc[:200].fillna(-1).equals(cut.fillna(-1))
