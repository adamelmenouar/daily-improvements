"""Immunisation classique : l'actif couvre un passif si valeur actuelle et duration sont égales."""


def is_immunized(asset_pv, asset_duration, liability_pv, liability_duration, tol=0.05):
    """Valeur actuelle de l'actif >= celle du passif, et durations égales à `tol` an près."""
    return asset_pv >= liability_pv and abs(asset_duration - liability_duration) <= tol


def duration_gap(asset_pv, asset_duration, liability_pv, liability_duration):
    """Écart de duration pondéré par la taille de bilan : D_A - (L / A) * D_L."""
    return asset_duration - liability_pv / asset_pv * liability_duration
