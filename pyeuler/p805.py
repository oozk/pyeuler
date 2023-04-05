#!/usr/bin/env python3

from math import gcd

def p805(N):

    for u in range(1, N+1):
        for v in range(u+1, N+1):
            if gcd(u, v) == 1:
                print(u, v, v**3 / u**3)

p805(200)
