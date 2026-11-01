from risk.cva import cva


def test_no_default_risk_means_no_cva():
    assert cva([100, 100], [0, 0], [0.99, 0.98]) == 0.0


def test_full_recovery_means_no_cva():
    assert cva([100, 100], [0.01, 0.02], [0.99, 0.98], recovery=1.0) == 0.0


def test_known_value():
    assert abs(cva([100], [0.02], [0.95], recovery=0.4) - 0.6 * 100 * 0.02 * 0.95) < 1e-12


def test_more_exposure_more_cva():
    assert cva([200], [0.02], [0.95]) > cva([100], [0.02], [0.95])
