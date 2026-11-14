from math import exp
from pricing.quanto import quanto_forward


def test_uncorrelated_asset_has_the_plain_forward():
    assert abs(quanto_forward(100, 0.02, 1.0, 0.2, 0.1, 0.0) - 100 * exp(0.02)) < 1e-12


def test_positive_correlation_lowers_the_quanto_forward():
    assert quanto_forward(100, 0.02, 1.0, 0.2, 0.1, 0.5) < quanto_forward(100, 0.02, 1.0, 0.2, 0.1, 0.0)


def test_negative_correlation_raises_it():
    assert quanto_forward(100, 0.02, 1.0, 0.2, 0.1, -0.5) > quanto_forward(100, 0.02, 1.0, 0.2, 0.1, 0.0)
