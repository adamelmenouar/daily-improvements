import numpy as np
from portfolio.hrp import hrp_weights

COV = np.array([[0.04, 0.018, 0.0, 0.0],
                [0.018, 0.09, 0.0, 0.0],
                [0.0, 0.0, 0.16, 0.05],
                [0.0, 0.0, 0.05, 0.25]])


def test_weights_are_a_valid_allocation():
    w = hrp_weights(COV)
    assert abs(w.sum() - 1) < 1e-12 and (w > 0).all()


def test_least_volatile_asset_gets_the_biggest_weight():
    assert hrp_weights(COV).argmax() == 0


def test_identical_assets_get_equal_weights():
    w = hrp_weights(np.eye(4) * 0.04)
    assert np.allclose(w, 0.25)
