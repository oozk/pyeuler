#!/usr/bin/env python3

###
# Problem 86
# https://projecteuler.net/problem=86
###

def p086(lim):

    a, count = 99, 1975    #2, 0

    while count < lim:
        for bc in range(3, 2 * a + 1):
            d = (a ** 2 + bc ** 2) ** .5
            if d - int(d) == 0: count += bc // 2 if bc <= a else (a - bc // 2) + 1
        a += 1

    return a

print(p086(1e6))
