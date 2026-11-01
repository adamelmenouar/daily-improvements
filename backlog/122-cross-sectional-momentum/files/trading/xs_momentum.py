"""Momentum en coupe transversale : long les meilleurs actifs passés, short les pires."""
import pandas as pd


def xs_momentum(returns, lookback=60, quantile=0.3):
    """returns : DataFrame (dates x actifs). Rendement quotidien du portefeuille long/short à poids égaux."""
    past = (1 + returns).rolling(lookback).apply(lambda x: x.prod(), raw=True) - 1
    rank = past.rank(axis=1, pct=True).shift(1)  # information de la veille seulement
    long_ = (rank >= 1 - quantile).astype(float)
    short = (rank <= quantile).astype(float)
    w = long_.div(long_.sum(axis=1), axis=0).fillna(0) - short.div(short.sum(axis=1), axis=0).fillna(0)
    return (w * returns).sum(axis=1)
