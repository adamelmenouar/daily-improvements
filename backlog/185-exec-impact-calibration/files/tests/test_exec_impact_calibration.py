import numpy as np
from execution.impact_calibration import calibrate_impact_coefficient


def test_recovers_the_true_coefficient():
    rng = np.random.default_rng(170)
    sig = rng.uniform(0.01, 0.03, 500)
    q = rng.uniform(1e3, 5e4, 500)
    v = rng.uniform(1e6, 5e6, 500)
    cost = 0.8 * sig * np.sqrt(q / v) + rng.normal(0, 1e-5, 500)
    assert abs(calibrate_impact_coefficient(cost, sig, q, v) - 0.8) < 0.05


def test_exact_data_gives_exact_coefficient():
    s, q, v = np.array([0.02, 0.01]), np.array([1e4, 4e4]), np.array([1e6, 1e6])
    assert abs(calibrate_impact_coefficient(1.5 * s * np.sqrt(q / v), s, q, v) - 1.5) < 1e-12
