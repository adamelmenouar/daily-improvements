from pricing.caplet import caplet, floorlet

ARGS = dict(vol=0.25, expiry=1.0, accrual=0.5, discount_factor=0.97)


def test_cap_floor_parity():
    f, k = 0.035, 0.03
    lhs = caplet(f, k, **ARGS) - floorlet(f, k, **ARGS)
    assert abs(lhs - 0.5 * 0.97 * (f - k)) < 1e-12


def test_higher_volatility_raises_both():
    lo, hi = dict(ARGS, vol=0.15), dict(ARGS, vol=0.40)
    assert caplet(0.03, 0.03, **hi) > caplet(0.03, 0.03, **lo)
    assert floorlet(0.03, 0.03, **hi) > floorlet(0.03, 0.03, **lo)


def test_at_the_money_caplet_equals_floorlet():
    assert abs(caplet(0.03, 0.03, **ARGS) - floorlet(0.03, 0.03, **ARGS)) < 1e-12
