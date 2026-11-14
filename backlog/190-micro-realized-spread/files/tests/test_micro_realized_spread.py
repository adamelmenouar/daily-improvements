from microstructure.realized_spread import realized_spread


def test_no_price_move_after_trade_gives_full_spread():
    assert abs(realized_spread(100.05, 100.0, 100.0, +1) - 0.001) < 1e-12


def test_informed_buyer_moves_price_up_and_erodes_the_spread():
    assert realized_spread(100.05, 100.05, 100.0, +1) == 0.0


def test_sell_side_mirror():
    assert abs(realized_spread(99.95, 100.0, 100.0, -1) - 0.001) < 1e-12
