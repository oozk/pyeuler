#!/usr/bin/env python3

from sympy import nextprime, isprime

def p808(N):

    L = []
    s = 0
    while len(L) < N:
        s = nextprime(s)
        p = s ** 2
        q = int(str(p)[::-1])
        r = q ** .5
        if p != q and r == int(r) and isprime(int(r)):
            L += [p]

    return sum(L)


def p808_2(N):

    def isPrime(n):
        return n % 2 != 0 and all(n % x != 0 for x in range(3, int(n**.5)+1, 2))

    def base4(n):
        r = 0
        k = 0
        while n > 0:
            r  += (n % 4) * 10**k
            k  += 1
            n //= 4
        return r

    def nextbase4prime(n):
        while True:
            n += 1
            p  = base4(n)
            if isPrime(p):
                return p, n

    L = []
    i = 0
    while len(L) < N:
        s, i = nextbase4prime(i)
        p    = s ** 2
        q    = int(str(p)[::-1])
        r    = q ** .5
        if p != q and r == int(r) and isPrime(int(r)):
            L += [p]

    return sum(L)

print(p808_2(50))
