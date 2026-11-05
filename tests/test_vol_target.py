import numpy as np
import pandas as pd
from trading.vol_target import vol_target_returns

R = pd.Series(np.random.default_rng(23).normal(0, 0.01, 3000))


def test_realised_vol_close_to_target():
    out = vol_target_returns(R, target=0.10).dropna()
    assert abs(out.std() * np.sqrt(252) - 0.10) < 0.02


def test_leverage_cap_is_respected():
    calm = pd.Series(np.random.default_rng(24).normal(0, 0.0005, 500))
    out = vol_target_returns(calm, target=0.10, max_leverage=2.0).dropna()
    assert (out.abs() <= 2.0 * calm.abs().max() + 1e-12).all()
