from pricing.barrier_mc import down_and_out_call
from pricing.black_scholes import bs_call


def test_never_more_expensive_than_the_vanilla_call():
    assert down_and_out_call(100, 100, 90, 1, 0.05, 0.2) < bs_call(100, 100, 1, 0.05, 0.2) + 0.3


def test_unreachable_barrier_is_close_to_vanilla():
    assert abs(down_and_out_call(100, 100, 1.0, 1, 0.05, 0.2) - bs_call(100, 100, 1, 0.05, 0.2)) < 0.5


def test_closer_barrier_means_cheaper_option():
    assert down_and_out_call(100, 100, 95, 1, 0.05, 0.2) < down_and_out_call(100, 100, 80, 1, 0.05, 0.2)
