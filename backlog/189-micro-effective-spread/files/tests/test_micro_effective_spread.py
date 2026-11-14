from microstructure.effective_spread import effective_spread


def test_trade_at_the_ask():
    assert abs(effective_spread(100.05, 100.0) - 0.001) < 1e-12


def test_trade_at_mid_is_free():
    assert effective_spread(100.0, 100.0) == 0.0


def test_symmetric_for_bid_and_ask():
    assert abs(effective_spread(99.95, 100.0) - effective_spread(100.05, 100.0)) < 1e-12
