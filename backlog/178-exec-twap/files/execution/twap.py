"""TWAP : découper un ordre en tranches égales dans le temps."""


def twap_schedule(total_quantity, n_slices):
    """Quantités entières par tranche ; le reste est réparti sur les premières. La somme est exacte."""
    if n_slices <= 0:
        raise ValueError("n_slices doit être > 0")
    base, rest = divmod(int(total_quantity), n_slices)
    return [base + (1 if i < rest else 0) for i in range(n_slices)]
