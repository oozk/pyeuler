#!/usr/bin/env python3
###
# Problem 32
# https://projecteuler.net/problem=32
# Pandigital products
###
def p032():
    pandigits = [str(i) for i in range(1, 10)]
    pandigital = lambda p, m: sorted(str(p) + str(m) + str(p // m)) == pandigits
    products = range(1, 10000)
    multipliers = lambda p: (m for m in range(1, int(p ** 0.5) + 1) if p % m == 0)
    return sum(set(p for p in products for m in multipliers(p) if pandigital(p, m)))

print(p032())
