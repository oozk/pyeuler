#!/usr/bin/env python3

###
# Problem 23
# https://projecteuler.net/problem=23
###

def p23(n):
    divisors = lambda n: (d for d in range(1, n // 2 + 1) if n % d == 0)
    abundant = set(a for (a, b) in ((a, sum(divisors(a))) for a in range(n + 1)) if a < b)
    abundantsums = set(a + b for a in abundant for b in abundant if (a + b) < n)
    return n * (n - 1) // 2 - sum(abundantsums)

print(p23(28123))
