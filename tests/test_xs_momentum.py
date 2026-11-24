import numpy as np
import pandas as pd
from trading.xs_momentum import xs_momentum


def test_profits_when_winners_keep_winning():
    rng = np.random.default_rng(121)
    drift = np.linspace(-0.001, 0.001, 10)
    r = pd.DataFrame(rng.normal(drift, 0.005, (1500, 10)))
    assert xs_momentum(r, 60).iloc[100:].mean() > 0


def test_dollar_neutral_when_all_assets_move_together():
    r = pd.DataFrame(np.tile(np.random.default_rng(122).normal(0, 0.01, (300, 1)), (1, 6)))
    out = xs_momentum(r, 20)
    assert out.abs().max() < 1e-9
