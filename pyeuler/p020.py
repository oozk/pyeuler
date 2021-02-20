#!/usr/bin/env python3

###
# Problem 20
# https://projecteuler.net/problem=20
# ###
# Solution: O(n) time | O(1) space
###

from math import factorial

def problem_20(n):
    values = str(factorial(n))
    return sum(int(x) for x in values)

print(problem_20(100))
