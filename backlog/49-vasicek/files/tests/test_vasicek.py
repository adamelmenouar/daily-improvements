from risk.vasicek import vasicek_loss_quantile


def test_zero_correlation_gives_expected_loss():
    assert abs(vasicek_loss_quantile(0.02, 1e-12, lgd=0.45) - 0.02 * 0.45) < 1e-6


def test_more_correlation_more_tail_loss():
    assert vasicek_loss_quantile(0.02, 0.2) > vasicek_loss_quantile(0.02, 0.05)


def test_higher_confidence_more_loss():
    assert vasicek_loss_quantile(0.02, 0.15, confidence=0.999) > vasicek_loss_quantile(0.02, 0.15, confidence=0.95)
