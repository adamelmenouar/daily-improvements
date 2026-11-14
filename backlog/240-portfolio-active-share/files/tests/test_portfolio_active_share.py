from portfolio.active_share import active_share


def test_index_fund_has_zero_active_share():
    assert active_share([0.5, 0.3, 0.2], [0.5, 0.3, 0.2]) == 0.0


def test_fully_different_portfolio_has_active_share_one():
    assert active_share([1.0, 0.0], [0.0, 1.0]) == 1.0


def test_known_value():
    assert abs(active_share([0.6, 0.4, 0.0], [0.4, 0.3, 0.3]) - 0.3) < 1e-12
