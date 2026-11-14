"""Découpage d'un gros ordre en tranches de taille affichée fixe."""


def iceberg_slices(total_quantity, display_quantity):
    if display_quantity <= 0:
        raise ValueError("display_quantity doit être > 0")
    full, rest = divmod(int(total_quantity), int(display_quantity))
    return [int(display_quantity)] * full + ([rest] if rest else [])
