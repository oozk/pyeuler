#!/usr/bin/env python3

###
# Problem 16
# https://projecteuler.net/problem=16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
# ###
# Solution: O(2**n) time | O(1) space
###
def problem_16(n):
    return sum(int(i) for i in str(2 ** n))

print(problem_16(1000))
