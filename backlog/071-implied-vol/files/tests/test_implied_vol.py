import pytest
from pricing.black_scholes import bs_call
from pricing.implied_vol import implied_vol_call


@pytest.mark.parametrize("sigma", [0.1, 0.25, 0.6])
def test_round_trip(sigma):
    p = bs_call(100, 105, 0.5, 0.03, sigma)
    assert abs(implied_vol_call(p, 100, 105, 0.5, 0.03) - sigma) < 1e-6


def test_impossible_price_rejected():
    with pytest.raises(ValueError):
        implied_vol_call(0.0, 100, 100, 1, 0.05)
