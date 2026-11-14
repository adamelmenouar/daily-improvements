import pytest
from credit.hazard import hazard_rate, survival_probability, default_probability


def test_round_trip_at_the_calibration_horizon():
    h = hazard_rate(0.10, 5)
    assert abs(default_probability(h, 5) - 0.10) < 1e-12


def test_survival_decreases_with_time():
    h = hazard_rate(0.05, 1)
    assert survival_probability(h, 3) < survival_probability(h, 1) < 1


def test_invalid_probability():
    with pytest.raises(ValueError):
        hazard_rate(1.0, 1)
