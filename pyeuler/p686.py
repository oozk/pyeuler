#!/usr/bin/env python3

from math import floor
import decimal

def p686(L1, L2, n):
    decimal.getcontext().prec = 20
    b2    = decimal.Decimal(2).ln()
    lower = decimal.Decimal(L1).ln() / b2
    upper = decimal.Decimal(L2).ln() / b2
    step  = decimal.Decimal(10).ln() / b2

    exp, cnt = 0, 0
    while cnt < n:
        exp += 1
        if floor(exp * step + lower) < floor(exp * step + upper):
            cnt += 1

    return floor(exp * step + upper)

print(p686(1.2, 1.3, 1))
print(p686(1.2, 1.3, 2))
print(p686(1.23, 1.24, 45))
print(p686(1.23, 1.24, 678910))
