#!/usr/bin/env python3

###
# Problem 85
# https://projecteuler.net/problem=85
###

from math import ceil

def p085(target):
    pool = range(1, int(target ** 0.5) + 1)
    rectangles = ((m, n) for m in pool for n in pool)
    objective = lambda x: abs(target - (x[0] * (x[0] + 1) * x[1] * (x[1] + 1) // 4))
    m, n = min(rectangles, key=objective)
    return m * n

def count_rectangles(m, n):
    count = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            count += ceil(m / i) * ceil(n / j)
    return count

print(p085(2e6))
