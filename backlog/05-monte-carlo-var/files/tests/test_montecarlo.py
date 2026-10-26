from risk.montecarlo import monte_carlo_var


def test_longer_horizon_means_more_risk():
    assert monte_carlo_var(0.0, 0.01, horizon=10) > monte_carlo_var(0.0, 0.01, horizon=1)


def test_higher_confidence_means_more_risk():
    assert monte_carlo_var(0.0, 0.01, alpha=0.99) > monte_carlo_var(0.0, 0.01, alpha=0.95)


def test_reproducible():
    assert monte_carlo_var(0.0, 0.01) == monte_carlo_var(0.0, 0.01)
