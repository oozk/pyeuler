#!/usr/bin/env python3

from math import factorial

def p493():

    n_choose_r   = lambda n, r: factorial(n) / factorial(r) / factorial(n-r)
    return round(7 * (1 - n_choose_r(60, 20) / n_choose_r(70, 20)), 9)

print(p493())
