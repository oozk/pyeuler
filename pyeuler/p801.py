#!/usr/bin/env python3

from sympy import factorint
def p801(n):
    result = 0

    for x in range(1, n**2-n+1):
        for y in range(1, n**2-n+1):
            if pow(x, y, n) == pow(y, x, n):
                # print(x, y, pow(x, y, n))
                result += 1

    return result

for n in [3, 5, 7, 11, 13]:
    print(factorint(p801(n)))
