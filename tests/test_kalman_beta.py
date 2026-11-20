import numpy as np
from ts.kalman_beta import kalman_beta


def test_converges_to_constant_beta():
    rng = np.random.default_rng(101)
    x = rng.normal(size=2000)
    y = 1.5 * x + rng.normal(0, 0.1, 2000)
    assert abs(kalman_beta(y, x)[-1] - 1.5) < 0.05


def test_tracks_a_shift_in_beta():
    rng = np.random.default_rng(102)
    x = rng.normal(size=2000)
    true = np.where(np.arange(2000) < 1000, 1.0, 2.0)
    y = true * x + rng.normal(0, 0.1, 2000)
    b = kalman_beta(y, x, q=1e-3)
    assert abs(b[900] - 1.0) < 0.1 and abs(b[-1] - 2.0) < 0.1
