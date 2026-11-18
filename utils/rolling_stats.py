"""Statistiques glissantes (séries pandas)."""


def rolling_zscore(series, window=20):
    return (series - series.rolling(window).mean()) / series.rolling(window).std()


def rolling_skew(series, window=60):
    return series.rolling(window).skew()
