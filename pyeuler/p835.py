#!/usr/bin/env python3

from sympy import GF, N
from numpy import array, matmul, polyfit
from numpy.linalg import matrix_power
from math import floor, log

def p835(k, m, f):

    #case1 (a, b, c=b+1)
    n       = 5*pow(10, k//2-1, m)-1 
    result  = GF(m)((n+1)*(n+2)*(4*n+3)//3)

    #case2 (a, b=a+1, c)
    # a, b    = p835_lf()
    # p       = floor(a*(k-1)+b)

    g = (k * log(10) + log(2 * (2**.5)))/log(1 + (2**.5)) - 1
    print(g)
    hf = floor(N(g, 1000))
    print(hf)
    if hf % 2 == 1:
        p = int(floor((hf+1)/2))
    else:
        p = int(floor(hf/2))
 
    T       = array([[GF(m)(0),  GF(m)(1), GF(m)(0)], 
                     [GF(m)(-1), GF(m)(6), GF(m)(2)], 
                     [GF(m)(0),  GF(m)(0), GF(m)(1)]])
    A       = array([0, 2, 1])
    T       = matrix_power(T, p+f)
    result += matmul(T, A)[1]

    #remove case1 n=0, case2 n=0 and case2 n=1
    result -= 12+2+2 
    return result

def p835_lf():
    a, b = (2, 0), (1.2, 1)
    i    = 2
    X, Y = [], []
    while b[1] <= 5*10**5:
        if a[1] == b[1]:
            c  = 6*b[0] - a[0]
            d  = b[1]
            if c >= 10:
                c  /= 10
                d  += 1
        else:
            c  = 60*b[0] - a[0]
            d  = b[1]
            if floor(log(c, 10)) >= floor(log(b[0]*10, 10)):
                c /= pow(10, floor(log(c, 10)))
            if floor(log(60*b[0] - a[0], 10)) > floor(log(b[0]*10, 10)):    
                d += 1
        i    += 1
        a, b  = b, (c, d)
        if i > 300000:
            Y += [i]
            X += [d]
    S = polyfit(X, Y, 1)
    return S

print(p835(10**10, 1234567891, -1))


# import sympy


# expon = sympy.Pow(10, 10)
# g = (expon * sympy.log(10) + sympy.log(2 * sympy.sqrt(2)))/sympy.log(1 + sympy.sqrt(2)) - 1
# hf = sympy.floor(sympy.N(g, 1000))

# if hf % 2 == 1:
#     h = int(sympy.floor((hf+1)/2))
# else:
#     h = int(sympy.floor(hf/2))

# print(h, hf)