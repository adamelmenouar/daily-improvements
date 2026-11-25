import numpy as np
from trading.quantile_buckets import bucket_returns


def test_informative_signal_gives_monotone_buckets():
    rng = np.random.default_rng(123)
    s = rng.normal(size=20_000)
    out = bucket_returns(s, 0.01 * s + rng.normal(0, 0.01, 20_000), 5)
    assert len(out) == 5 and (np.diff(out.values) > 0).all()


def test_useless_signal_has_flat_buckets():
    rng = np.random.default_rng(124)
    out = bucket_returns(rng.normal(size=20_000), rng.normal(0, 0.01, 20_000), 5)
    assert out.max() - out.min() < 0.0008
