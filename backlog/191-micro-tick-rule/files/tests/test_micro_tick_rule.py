from microstructure.tick_rule import tick_rule


def test_known_sequence():
    assert tick_rule([10.0, 10.1, 10.1, 10.0, 10.0, 10.2]) == [1, 1, 1, -1, -1, 1]


def test_constant_prices_keep_the_initial_sign():
    assert tick_rule([5.0] * 4) == [1, 1, 1, 1]
