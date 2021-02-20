#!/usr/bin/env python3

###
# Problem 104
# https://projecteuler.net/problem=104
###

def p104():
    pandigital = lambda x : ''.join(sorted(str(x)[:9])) == ''.join(sorted(str(x)[-9:])) == '123456789'
    f1, f2, k = 1, 1, 2
    while True:
        f1, f2 = f2, f2 + f1
        k += 1
        if pandigital(f2):
            return k


print(p104())
