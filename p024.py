#!/usr/bin/env python3

###
# Problem 24
# https://projecteuler.net/problem=24
###

from itertools import permutations, islice

def p25(n, k):
  pool = islice(permutations(list(range(n))), k-1, None)
  return "".join(str(x) for x in next(pool))

print(p25(10, 1000000))
