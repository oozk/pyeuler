#!/usr/bin/env python3

###
# Problem 21
# https://projecteuler.net/problem=21
###

from sympy import divisors

def p21(n):
  pool = ((a, sum(divisors(a)[:-1])) for a in range(n))
  return sum(a for (a, b) in pool if a < n and b < n and a != b and sum(divisors(b)[:-1]) == a)

print(p21(10000))
