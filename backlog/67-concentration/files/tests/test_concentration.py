from portfolio.concentration import herfindahl, effective_n


def test_equal_weights():
    assert abs(effective_n([0.25] * 4) - 4) < 1e-12


def test_single_position():
    assert herfindahl([1.0]) == 1.0 and effective_n([1.0]) == 1.0


def test_concentrated_book_has_fewer_effective_lines():
    assert effective_n([0.7, 0.1, 0.1, 0.1]) < 4
