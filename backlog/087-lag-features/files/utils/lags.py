"""Variables retardées pour les modèles prédictifs (sans fuite du futur)."""
import pandas as pd


def make_lags(series, lags):
    """DataFrame avec les colonnes lag_k = valeur de k périodes plus tôt."""
    return pd.DataFrame({f"lag_{k}": series.shift(k) for k in lags})
