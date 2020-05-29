#!/usr/bin/env python3

###
# Problem 40
# https://projecteuler.net/problem=40
###

from functools import reduce
import operator

def p040():
  champernowne = "".join(str(x) for x in range(1, int(1e6)))
  return reduce(operator.mul, (int(champernowne[10 ** x - 1]) for x in range(0, 7)))

print(p040())
