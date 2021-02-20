#!/usr/bin/env python3

###
# Problem 4
# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
###
# Solution: O(n^2) time | O(1) space
###
import cProfile
from math import ceil

def largest_palindrome_product(start, finish):
    pool = ((i * j, i, j) for i in reversed(range(int(ceil(start / 11)) * 11, finish, 11)) for j in reversed(range(start, finish)))
    # return max(x[0] for x in pool if str(x[0]) == str(x[0])[::-1])
    max  = (0, 0, 0)
    for x in pool:
        if max[0] < x[0] and str(x[0]) == str(x[0])[::-1]:
            max = x
    return max

cProfile.run('print(largest_palindrome_product(100, 1000))')
