"""Micro-prix : prix milieu tiré vers le côté le moins fourni du carnet."""


def microprice(bid, ask, bid_size, ask_size):
    return (bid * ask_size + ask * bid_size) / (bid_size + ask_size)
