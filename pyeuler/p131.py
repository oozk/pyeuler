#!/usr/bin/env python3

def p131(N):

    check  = lambda n: n%2!=0 and all(n%k for k in range(3, int(n**.5)+1, 2))

    r, i   = 0, 0
    while True:
        i += 1
        d  = (i + 1)**3 - i**3
        if d > N: break
        if check(d): r += 1

    return r

print(p131(1e6))
