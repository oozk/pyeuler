#!/usr/bin/env pypy3
import cProfile
from sympy import divisors
def p834(N):
    def S(n):
        k = n*(n-1)
        return [x-n if x >= n else k//x-n for x in divisors(k//(k&-k))] 
    def T(n):
        k = n*(n-1)
        return sum(x-n if x >= n else k//x-n for x in divisors(k//(k&-k)))
    
    return sum(T(n) for n in range(3, N+1))

def p834_2(N):
    divs     = [[1, n] for n in range(2, N+1)]
    for p in range(3, N+1, 2):
        for n in range(p, N+1, p):
            for k in divs[n]:
                d = k*p
                if d > n: break
                if n%d == 0 and d not in divs[n]:
                    divs[n] += [d]

    result = 0
    q      = [1]
    for n in range(3, N+1):
        k = n*(n-1)
        for p in divs[n]:
            for q in divs[n-1]:
                d = p*q          
                result += d-n if d >= n else k//d-n

    return result

cProfile.run('print(p834(100))')
cProfile.run('print(p834(1234567))')
# cProfile.run('print(p834_2(1234567))')

def p834_0(n, L):
    def S(n, L):
        f = lambda n, m: (m+1)*(2*n+m)//2
        m = 1
        while m <= L:
            if f(n, m) % (n+m) == 0:
                yield m
            m += 1
    print(list(S(n, L)))

