#!/usr/bin/env python3

###
# Problem 55
# https://projecteuler.net/problem=55
# By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
###
# Solution: O(n) time | O(n) space
###

import cProfile

def problem_55(max, depth):
    lychrel = [i for i in range(1, max) if isLychrel(i, depth)]
    return len(lychrel), lychrel

def isLychrel(n, depth):
    lychrel = True
    for i in range(depth):
        m = int(str(n)[::-1])
        if n == m:
            lychrel = False
        else:
            n += m
    return lychrel

cProfile.run('print(problem_55(int(1e4), 50))')
