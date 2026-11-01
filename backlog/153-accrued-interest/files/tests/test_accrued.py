from pricing.accrued import accrued_interest, dirty_price, clean_price


def test_accrued_at_the_start_and_end_of_the_period():
    assert accrued_interest(100, 0.06, 0, 182) == 0.0
    assert abs(accrued_interest(100, 0.06, 182, 182) - 3.0) < 1e-12


def test_half_a_period_accrues_half_a_coupon():
    assert abs(accrued_interest(100, 0.05, 91, 182) - 1.25) < 1e-12


def test_clean_dirty_round_trip():
    assert clean_price(dirty_price(99.5, 1.2), 1.2) == 99.5
