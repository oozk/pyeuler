#!/usr/bin/env python3

###
# Problem 57
# https://projecteuler.net/problem=57
###

def p057(n):
    numerator, denominator = 3, 2
    i, count = 1, 0
    while i < n:
        if len(str(numerator)) > len(str(denominator)): count += 1
        denominator, numerator = numerator + denominator, numerator + 2 * denominator
        i += 1
    return count

print(p057(1000))
