#!/usr/bin/env python3

###
# Problem 120
# https://projecteuler.net/problem=120
###

def p120(target):

    result       = 0
    sqremainder  = lambda p, n, psq: (pow(p + 1, n, psq) + pow(p - 1, n, psq)) % psq

    for p in range(3, int(target) + 1):
        maximum = 0
        for n in range(1, p + 1):
            r = sqremainder(p, n, p ** 2)
            if r > maximum:
                maximum = r
        result += maximum

    return result

print(p120(1e3))
