import numpy as np
import pytest
from portfolio.shrunk_mu import shrink_expected_returns

MU = [0.02, 0.08, 0.05]


def test_extremes():
    assert np.allclose(shrink_expected_returns(MU, 0), MU)
    assert np.allclose(shrink_expected_returns(MU, 1), [0.05] * 3)


def test_mean_is_preserved_and_spread_shrinks():
    out = shrink_expected_returns(MU, 0.4)
    assert abs(out.mean() - np.mean(MU)) < 1e-12 and out.std() < np.std(MU)


def test_invalid_delta():
    with pytest.raises(ValueError):
        shrink_expected_returns(MU, 1.5)
