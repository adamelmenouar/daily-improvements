from execution.arrival import arrival_slippage_bps


def test_buy_above_mid_is_positive_slippage():
    assert abs(arrival_slippage_bps(100.0, 100.05, "buy") - 5.0) < 1e-9


def test_sell_above_mid_is_negative_slippage():
    assert arrival_slippage_bps(100.0, 100.05, "sell") < 0


def test_fill_at_mid_has_no_slippage():
    assert arrival_slippage_bps(50.0, 50.0) == 0.0
