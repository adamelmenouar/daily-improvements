import numpy as np
from ts.arch_lm import arch_lm_test


def test_iid_returns_not_rejected():
    assert arch_lm_test(np.random.default_rng(95).normal(0, 0.01, 5000))[1] > 0.01


def test_arch_process_is_detected():
    rng = np.random.default_rng(95)
    r = np.zeros(5000)
    for t in range(1, 5000):
        r[t] = np.sqrt(1e-5 + 0.6 * r[t - 1] ** 2) * rng.normal()
    assert arch_lm_test(r)[1] < 1e-6
