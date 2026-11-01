import numpy as np
from risk.christoffersen import christoffersen_independence


def test_independent_exceptions_not_rejected():
    e = np.random.default_rng(35).random(3000) < 0.05
    assert christoffersen_independence(e)[1] > 0.01


def test_clustered_exceptions_rejected():
    e = np.zeros(1000, dtype=int)
    for start in (100, 300, 500, 700, 900):
        e[start:start + 10] = 1
    assert christoffersen_independence(e)[1] < 0.001
