#!/usr/bin/env python3

###
# Problem 25
# https://projecteuler.net/problem=25
###

def p025(n):
  n1, n2 = 1, 1
  r  = 2
  while len(str(n2)) < n:
      n1, n2 = n2, n2 + n1
      r += 1
  else:
      return r

print(p025(1000))
