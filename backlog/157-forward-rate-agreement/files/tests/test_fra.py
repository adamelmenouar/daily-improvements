from pricing.fra import fra_rate, fra_settlement


def test_flat_continuous_curve():
    from math import exp
    r = fra_rate(exp(-0.03 * 1), exp(-0.03 * 1.5), 0.5)
    assert abs(r - (exp(0.03 * 0.5) - 1) / 0.5) < 1e-12


def test_settlement_sign():
    assert fra_settlement(1e6, 0.03, 0.04, 0.5) > 0 > fra_settlement(1e6, 0.03, 0.02, 0.5)


def test_zero_when_rates_match():
    assert fra_settlement(1e6, 0.03, 0.03, 0.5) == 0.0
