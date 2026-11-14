from pricing.black_scholes import bs_call
from pricing.merton_jump import merton_jump_call


def test_no_jumps_gives_black_scholes():
    assert abs(merton_jump_call(100, 100, 1, 0.05, 0.2, 0.0, -0.1, 0.2) - bs_call(100, 100, 1, 0.05, 0.2)) < 1e-9


def test_jumps_raise_the_price_of_far_out_of_the_money_calls():
    # mu_j = -delta^2 / 2 : sauts de moyenne nulle, ils n'ajoutent que de la variance
    jump = merton_jump_call(100, 140, 0.5, 0.03, 0.2, 1.0, -0.045, 0.3)
    assert jump > bs_call(100, 140, 0.5, 0.03, 0.2)


def test_price_is_within_no_arbitrage_bounds():
    p = merton_jump_call(100, 100, 1, 0.03, 0.2, 0.5, -0.1, 0.25)
    assert 0 < p < 100
