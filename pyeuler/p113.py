#!/usr/bin/env python3

from scipy.special import comb

def p113(N):
    return comb(N+9, 9, exact=True) + comb(N+10, 10, exact=True) - 10*N - 2

print(p113(100))
