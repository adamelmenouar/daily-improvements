import numpy as np
from portfolio.target_vol import scale_to_target_vol

COV = np.array([[0.04, 0.006], [0.006, 0.09]])


def test_hits_the_target():
    w = scale_to_target_vol([0.5, 0.5], COV, 0.12)
    assert abs(np.sqrt(w @ COV @ w) - 0.12) < 1e-12


def test_keeps_relative_proportions():
    w = scale_to_target_vol([0.7, 0.3], COV, 0.05)
    assert abs(w[0] / w[1] - 7 / 3) < 1e-12
