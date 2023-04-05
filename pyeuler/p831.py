#!/usr/bin/env python3

from math import comb, lcm
from numpy import polyfit, polyval
from fractions import Fraction
from sympy import Symbol, lambdify

def p831(m,  digits):
    def base(n, r):
        res = []
        while n: res+=[str(n % r)]; n//=r
        return ''.join(res[::-1])
        
    def g7(n):
        res = 0
        for j in range(n+1):
            for i in range(j+1):
                res += pow(-1, j-i) * comb(n, j) * comb(j, i) * comb(j+5+6*i, j+5)
        return res//pow(7, n)
    
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
        Y = [g7(x) for x in X]
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
    
    C    = poly_fit(100, 3, 10)
    f, d = f_gen(C)
    return base(7**m * f(m) // d, 7)[:digits]

print(p831(142857, 10))