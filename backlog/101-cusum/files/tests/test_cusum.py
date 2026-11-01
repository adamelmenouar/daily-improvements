import numpy as np
from ts.cusum import cusum_alarm


def test_no_alarm_without_shift():
    assert cusum_alarm(np.random.default_rng(103).normal(size=1000), h=10) is None


def test_alarm_shortly_after_a_shift():
    rng = np.random.default_rng(104)
    x = np.concatenate([rng.normal(0, 1, 300), rng.normal(2, 1, 300)])
    t = cusum_alarm(x, h=8)
    assert t is not None and 300 <= t < 330
