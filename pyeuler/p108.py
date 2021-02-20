#!/usr/bin/env python3

from sympy import divisor_count

def p108(l):
    k = 1
    while (divisor_count(k ** 2) + 1) / 2 < l: k += 1
    return k

print(p108(1000))
