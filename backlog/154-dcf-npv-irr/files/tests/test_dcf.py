from pricing.dcf import npv, irr, payback_period

CF = [-1000, 300, 400, 500, 200]


def test_npv_at_zero_rate_is_the_sum():
    assert npv(0.0, CF) == 400.0


def test_npv_is_zero_at_the_irr():
    assert abs(npv(irr(CF), CF)) < 1e-6


def test_higher_discount_rate_lowers_npv():
    assert npv(0.15, CF) < npv(0.05, CF)


def test_payback():
    assert payback_period(CF) == 3 and payback_period([-100, 10, 10]) is None
