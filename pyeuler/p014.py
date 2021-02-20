#!/usr/bin/env python3

###
# Problem 14
# https://projecteuler.net/problem=14
# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
# ###
# Solution: O(n^2) time | O(1) space
###

import cProfile

def problem_14(N):
    best = (0, 0)
    start = max(9, int(N * 0.7) - int(N * 0.7) % 10 - 1)
    for n in range(start, int(N), 10):
        m = countCollatzSequence(n)
        if best[1] < m:
            best = (n, m)
    return best

def countCollatzSequence(n):
    count = 0
    while n > 1:
        count += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    else:
        count += 1
    return count

def getCollatzSequence(n):
    while n > 1:
        yield n
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    else:
        yield n

cProfile.run('print(problem_14(1e6))')
