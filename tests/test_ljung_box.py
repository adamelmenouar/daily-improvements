import numpy as np
from ts.ljung_box import ljung_box


def test_white_noise_not_rejected():
    assert ljung_box(np.random.default_rng(93).normal(size=3000))[1] > 0.01


def test_autocorrelated_series_rejected():
    rng = np.random.default_rng(93)
    x = np.zeros(3000)
    for t in range(1, 3000):
        x[t] = 0.5 * x[t - 1] + rng.normal()
    assert ljung_box(x)[1] < 1e-6
