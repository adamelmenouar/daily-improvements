from pricing.vol_term_structure import implied_vol_at, has_calendar_arbitrage

M, V = [0.25, 1.0, 2.0], [0.30, 0.25, 0.22]


def test_flat_term_structure_stays_flat():
    assert abs(implied_vol_at(0.7, [0.25, 1.0, 2.0], [0.2, 0.2, 0.2]) - 0.2) < 1e-12


def test_exact_at_the_nodes():
    assert abs(implied_vol_at(1.0, M, V) - 0.25) < 1e-12


def test_interpolated_value_lies_between_neighbors():
    assert 0.22 < implied_vol_at(1.5, M, V) < 0.25


def test_calendar_arbitrage_detection():
    assert not has_calendar_arbitrage(M, V)
    assert has_calendar_arbitrage([1.0, 2.0], [0.40, 0.20])
