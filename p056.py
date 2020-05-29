#!/usr/bin/env python3

###
# Problem 56
# https://projecteuler.net/problem=56
###

def p056(n):
    digit_sum = lambda a, b : sum(int(y) for y in str(a ** b))
    return max(digit_sum(a, b) for a in range(n) for b in range(n))

print(p056(100))
