#!/usr/bin/env python3

from math import comb, lcm, factorial
from numpy import polyfit, polyval
from fractions import Fraction
from sympy import Symbol, lambdify, factorint, isprime

def p830(m,  digits):
        
    def S(n):
        r = 0
        for k in range(n+1):
            r += comb(n, k) * k**n
        return r #// pow(2, n - bin(n//2).count('1'))
    
    def f_gen(coeff):
        denom = lcm(*[x.denominator for x in coeff])
        n = Symbol('n')
        f = sum(int(denom*coeff[k]) * n**k for k in range(len(coeff)))
        return lambdify(n, f), denom

    def f_eval(coeff, L):
        err  = 0
        f, d = f_gen(coeff)
        for x in range(L+1):
            err += (f(x)//d - g7(x))**2
        return err    
    
    def poly_fit(L, min_deg, max_deg):
        X = list(range(L+1))
        Y = [S(x) for x in X]
        F = set()
        print(Y)
        for y in Y:
            print(factorint(y))
            F |= {k for k in factorint(y).keys()}
        print(sorted(F))
        best    = float('inf')
        Coeff   = []
        for deg in range(min_deg, max_deg):
            try:
                c = [Fraction(x).limit_denominator() for x in polyfit(X, Y, deg)]
                if c[0].numerator == 0: continue
            except:
                continue
            error = f_eval(c, 100)
            if error < best:
                Coeff   = c[::-1]
        return Coeff
    
    C    = poly_fit(30, 3, 30)
    print(C)
    f, d = f_gen(C)
    return 

# p830(100, 83**3 * 89**3 * 97**3)
# M = 83**3 * 89**3 * 97**3


def p830_0(N, M):

    def S(n):
        r = 0
        for k in range(n+1):
            r += comb(n, k) * k**n
        return r
    b = 1
    d = 1
    for n in range(3, N+1):
        # F = factorint(S(n))
        # p = 3
        # try:
        #     k = F[p]
        # except:
        #     k = 0
        # a = S(n) - n
        # e = a/b
        # print(n, e, e-d, a)
        print(n, S(n) % M)
        # d = e
        # b = a

p830_0(2000, 83**3 * 89**3 * 97**3)