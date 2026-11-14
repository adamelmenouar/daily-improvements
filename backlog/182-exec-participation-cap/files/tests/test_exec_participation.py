import numpy as np
from execution.participation import capped_schedule


def test_cap_is_respected():
    ex, left = capped_schedule([500, 500], [1000, 10_000], 0.10)
    assert np.allclose(ex, [100, 500]) and abs(left - 400) < 1e-9


def test_no_cap_binding_executes_everything():
    ex, left = capped_schedule([10, 20], [1000, 1000], 0.5)
    assert np.allclose(ex, [10, 20]) and left == 0.0
