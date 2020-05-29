#!/usr/bin/env python3

###
# Problem 94
# https://projecteuler.net/problem=94
###

from math import gcd

def p094(limit):
    pool = range(1, int((limit // 3) ** 0.5), 2)
    triangles = (t for p in pool for t in pythagorean(p) if sum(t) < limit)
    return sum(sum(t) for t in triangles)

def pythagorean(s):
    for t in range(s-2, 0, -2):
        if gcd(s, t) == 1:
            a = s * t
            b = (s * s - t * t) // 2
            c = (s * s + t * t) // 2
            # yield (a, b, c)
            if abs(2 * a - c) == 1: yield (c, c, 2 * a)
            if abs(2 * b - c) == 1: yield (c, c, 2 * b)

print(p094(1e9))
