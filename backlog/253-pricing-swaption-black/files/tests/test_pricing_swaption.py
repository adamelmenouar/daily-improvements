from pricing.swaption import payer_swaption, receiver_swaption


def test_payer_receiver_parity_gives_the_forward_swap_value():
    s, k, a = 0.035, 0.03, 4.5
    assert abs(payer_swaption(s, k, 0.3, 2.0, a) - receiver_swaption(s, k, 0.3, 2.0, a) - a * (s - k)) < 1e-12


def test_at_the_money_payer_equals_receiver():
    assert abs(payer_swaption(0.03, 0.03, 0.3, 1.0, 4.0) - receiver_swaption(0.03, 0.03, 0.3, 1.0, 4.0)) < 1e-12


def test_longer_expiry_is_worth_more():
    assert payer_swaption(0.03, 0.03, 0.3, 5.0, 4.0) > payer_swaption(0.03, 0.03, 0.3, 1.0, 4.0)
