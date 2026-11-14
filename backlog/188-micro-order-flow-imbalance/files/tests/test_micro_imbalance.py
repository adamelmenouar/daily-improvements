from microstructure.imbalance import order_flow_imbalance


def test_bounds_and_balance():
    assert order_flow_imbalance(100, 0) == 1.0 and order_flow_imbalance(0, 100) == -1.0
    assert order_flow_imbalance(50, 50) == 0.0


def test_known_value():
    assert abs(order_flow_imbalance(300, 100) - 0.5) < 1e-12


def test_no_trades_is_neutral():
    assert order_flow_imbalance(0, 0) == 0.0
