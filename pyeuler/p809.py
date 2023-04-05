#!/usr/bin/env python3

from fractions import Fraction
from math import ceil

def p809(n, d):

    def f(x):
        if x > 0 and x == int(x):
            print('1', x)
            return x
        elif x < 1:
            print('2', x)
            return f(Fraction(1, 1 - x))
        else:
            print('3', x)
            return f(Fraction(1, ceil(x) - x) - 1 + f(x-1))


    return f(Fraction(n, d))

print(p809(3, 2))
