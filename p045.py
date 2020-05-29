#!/usr/bin/env python3

###
# Problem 45
# https://projecteuler.net/problem=45
###

def p045(i, j, k):
    T = lambda n : n * (n + 1) // 2
    P = lambda n : n * (3 * n - 1) // 2
    H = lambda n : n * (2 * n - 1)
    while True:
        t, p, h = T(i), P(j), H(k)
        minimum = min(t, p, h)
        if minimum == max(t, p, h):
            return t
        if minimum == t: i += 1
        if minimum == p: j += 1
        if minimum == h: k += 1

print(p045(286, 165, 143))
