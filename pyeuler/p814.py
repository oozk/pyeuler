#!/usr/bin/env python3

from itertools import product
from sympy import factorint

def p814(n):

    P = ('0', '1', '2')
    r = 0
    R = {}
    for c in product(P, repeat=4*n):
        k = ''.join(c)
        i = k.count('01')
        if k[0] == '1' and k[-1] == '0':
            i += 1
        for j in range(2*n):
            if k[j] == '2' and k[j+2*n] == '2':
                i += 1

        try:
            R[i] += 1
        except:
            R[i]  = 1

    for r in R.keys():
        print(r, factorint(R[r]))

    # return K

for n in range(1, 11):
    print(n, p814(n))
