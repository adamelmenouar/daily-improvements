"""Grecques d'un put européen, déduites de celles du call par la parité call-put."""
from math import exp
from pricing.greeks import call_delta
from pricing.theta_rho import call_rho, call_theta


def put_delta(s, k, t, r, sigma):
    return call_delta(s, k, t, r, sigma) - 1.0


def put_rho(s, k, t, r, sigma):
    return call_rho(s, k, t, r, sigma) - k * t * exp(-r * t)


def put_theta(s, k, t, r, sigma):
    return call_theta(s, k, t, r, sigma) + r * k * exp(-r * t)
