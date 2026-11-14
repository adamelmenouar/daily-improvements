import numpy as np
from credit.woe_iv import woe_iv


def test_informative_variable_has_high_iv():
    rng = np.random.default_rng(158)
    bins = rng.integers(0, 3, 6000)
    pd_ = np.array([0.02, 0.10, 0.30])[bins]
    y = rng.random(6000) < pd_
    woe, iv = woe_iv(bins, y)
    assert iv > 0.3 and woe[0] > woe[1] > woe[2]


def test_uninformative_variable_has_near_zero_iv():
    rng = np.random.default_rng(159)
    assert woe_iv(rng.integers(0, 4, 8000), rng.random(8000) < 0.1)[1] < 0.02
