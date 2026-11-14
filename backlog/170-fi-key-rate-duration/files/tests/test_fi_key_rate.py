import numpy as np
from fixedincome.key_rate import key_rate_durations, _price

CF = [(1, 5.0), (2, 5.0), (3, 5.0), (4, 5.0), (5, 105.0)]
NODES, RATES = [1, 2, 3, 4, 5], [0.02, 0.025, 0.03, 0.033, 0.035]


def test_sum_equals_parallel_shift_duration():
    krd = key_rate_durations(CF, NODES, RATES)
    h = 1e-4
    p0 = _price(CF, np.array(NODES, float), np.array(RATES))
    parallel = -(_price(CF, np.array(NODES, float), np.array(RATES) + h)
                 - _price(CF, np.array(NODES, float), np.array(RATES) - h)) / (2 * h * p0)
    assert abs(krd.sum() - parallel) < 1e-6


def test_biggest_exposure_is_at_the_maturity_of_the_big_cash_flow():
    assert key_rate_durations(CF, NODES, RATES).argmax() == 4


def test_zero_coupon_only_sensitive_to_its_own_node():
    krd = key_rate_durations([(3, 100.0)], NODES, RATES)
    assert abs(krd[2] - 3 / (1 + 0.03)) < 1e-3 and abs(krd[[0, 1, 3, 4]]).max() < 1e-9
