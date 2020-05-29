#!/usr/bin/env python3

###
# Problem 29
# https://projecteuler.net/problem=29
###

def p029(limit_a, limit_b):
  return len(set(a ** b for a in range(2, limit_a + 1) for b in range(2, limit_b +1)))

print(p029(100, 100))
