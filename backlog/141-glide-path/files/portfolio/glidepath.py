"""Part d'actions décroissant linéairement avec l'âge (fonds à échéance)."""


def equity_weight(age, start_age=25, retire_age=65, start_weight=0.9, end_weight=0.3):
    if retire_age <= start_age:
        raise ValueError("retire_age doit être > start_age")
    x = min(max((age - start_age) / (retire_age - start_age), 0.0), 1.0)
    return start_weight + x * (end_weight - start_weight)
