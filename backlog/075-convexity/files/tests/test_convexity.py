from pricing.bond import bond_price, modified_duration
from pricing.convexity import bond_convexity


def test_positive():
    assert bond_convexity(100, 0.05, 0.05, 10) > 0


def test_convexity_improves_price_approximation():
    args = (100, 0.05, 0.05, 10)
    p0, dy = bond_price(*args), 0.01
    exact = bond_price(100, 0.05, 0.06, 10)
    first = p0 * (1 - modified_duration(*args) * dy)
    second = first + 0.5 * bond_convexity(*args) * dy**2 * p0
    assert abs(exact - second) < abs(exact - first)
