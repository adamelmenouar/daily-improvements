"""Ichimoku Kinko Hyo (sans la ligne Chikou, qui utilise le futur)."""
import pandas as pd


def _mid(high, low, window):
    return (high.rolling(window).max() + low.rolling(window).min()) / 2


def ichimoku(high, low, tenkan=9, kijun=26, senkou_b=52):
    """Retourne un DataFrame : tenkan, kijun, senkou_a et senkou_b (nuage décalé de `kijun` périodes vers l'avant)."""
    t, k = _mid(high, low, tenkan), _mid(high, low, kijun)
    return pd.DataFrame({
        "tenkan": t,
        "kijun": k,
        "senkou_a": ((t + k) / 2).shift(kijun),
        "senkou_b": _mid(high, low, senkou_b).shift(kijun),
    })
