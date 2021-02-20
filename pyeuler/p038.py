#!/usr/bin/env python3

###
# Problem 38
# https://projecteuler.net/problem=38
###

def p038():
    pandigital = lambda s : ''.join(sorted(s)) == '123456789'
    result = ""
    for n in range(2, 10):
        for i in range(1, 10 ** (9 // n)):
            s = ''.join(str(i * j) for j in range(1, n+1))
            if pandigital(s):
                result = max(result, s)

    print(result)

p038()
