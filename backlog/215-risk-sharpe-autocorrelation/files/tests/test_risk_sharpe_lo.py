import numpy as np
from risk.sharpe_lo import annualization_factor, adjusted_annual_sharpe


def _ar(phi, n=20_000, seed=209):
    rng = np.random.default_rng(seed)
    r = np.zeros(n)
    for t in range(1, n):
        r[t] = phi * r[t - 1] + rng.normal()
    return r


def test_iid_returns_give_the_square_root_rule():
    assert abs(annualization_factor(_ar(0.0), 12) - 12**0.5) < 0.1


def test_positive_autocorrelation_reduces_the_factor():
    assert annualization_factor(_ar(0.4), 12) < annualization_factor(_ar(0.0), 12)


def test_adjusted_sharpe_is_finite():
    assert np.isfinite(adjusted_annual_sharpe(_ar(0.2) + 0.05))
