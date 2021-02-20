#!/usr/bin/env python3

from scipy.special import binom
import numpy as np

def p744_s(n, p):
    result = np.longouble(0.0)

    for k in range(n):
        result += binom(n + k - 1, k) * ((p**n) * ((1-p)**k) + (p**k) * ((1-p)**n))* (n - k + 1) / (2 * n + 1)
    return round(result, 10)

def p744_l(n, p):
    return round(((n + 1)/(2*n + 1) -  n * (p**n - p) / ((2*n + 1) * (p-1))), 10)

print('%.10f' % p744_s(6, 1/2))
print('%.10f' % p744_s(10, 3/7))
print('%.10f' % p744_l(1e4, 0.3))
print('%.10f' % p744_l(1e11, 0.4999))
