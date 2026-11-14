from microstructure.microprice import microprice


def test_balanced_book_gives_the_mid():
    assert microprice(100.0, 100.2, 500, 500) == 100.1


def test_big_bid_pushes_the_price_toward_the_ask():
    assert microprice(100.0, 100.2, 900, 100) > 100.1


def test_stays_within_the_spread():
    assert 100.0 <= microprice(100.0, 100.2, 10, 1000) <= 100.2
