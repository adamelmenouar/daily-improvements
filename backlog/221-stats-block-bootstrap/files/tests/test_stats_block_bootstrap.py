import numpy as np
from stats.block_bootstrap import block_bootstrap_mean_ci


def _ar(phi, n=1000, seed=220):
    rng = np.random.default_rng(seed)
    x = np.zeros(n)
    for t in range(1, n):
        x[t] = phi * x[t - 1] + rng.normal()
    return x


def test_interval_contains_the_estimate():
    lo, m, hi = block_bootstrap_mean_ci(_ar(0.5))
    assert lo < m < hi


def test_wider_than_the_iid_bootstrap_when_data_is_autocorrelated():
    x = _ar(0.7)
    w_block = np.subtract(*block_bootstrap_mean_ci(x, block=20)[::2][::-1])
    w_iid = np.subtract(*block_bootstrap_mean_ci(x, block=1)[::2][::-1])
    assert abs(w_block) > abs(w_iid)


def test_reproducible():
    x = _ar(0.3)
    assert block_bootstrap_mean_ci(x, seed=2) == block_bootstrap_mean_ci(x, seed=2)
