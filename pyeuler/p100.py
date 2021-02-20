#!/usr/bin/env python3

import sympy as sy

def p100(target):

    # OEIS A046090
    # a(n) = 7*a(n-1) - 7*a(n-2) + a(n-3) - Harvey P. Dale, Apr 13 2012
    totals    = [1, 4, 21, 120]
    while totals[-1] < target: totals += [7 * totals[-1] - 7 * totals[-2] + totals[-3]]

    total     = sy.Symbol('t', integer=True)
    blue      = sy.Symbol('b', integer=True)
    red       = sy.Symbol('r', integer=True)
    eq1       = sy.Eq(total - blue - red, 0)
    eq2       = sy.Eq(total * (total -1) - 2 * blue * (blue - 1), 0)
    solutions = list(sy.solve((eq1, eq2), (blue, red)))
    funcblue  = [[sy.lambdify([total], f) for f in s] for s in solutions]

    sample    = [21, 15, 6]
    test      = lambda func, sample: all((sample[1] == func[0](sample[0]),
                                          sample[2] == func[1](sample[0])))
    shortlist = lambda func, sample: [f for f in func if test(f, sample)]
    funcblue  = shortlist(funcblue, sample)
    f         = funcblue[0][0], funcblue[0][1]

    blue, red, bag = int(f[0](float(totals[-1]))), int(f[1](float(totals[-1]))), totals[-1]

    return blue, red, bag

print(p100(1e12))

def p100_2(target):
    blue=15
    total=21
    blue_next=85
    total_next=120
    while  total_next < target:
        blue, total, blue_next, total_next = blue_next, total_next, total_next * 4 + blue - 2, blue_next * 8 + total - 4

    return blue_next

def p100_3(target):
    # OEIS A046090
    # a(n)    = 7*a(n-1) - 7*a(n-2) + a(n-3) - Harvey P. Dale, Apr 13 2012
    blues = [1, 3, 15, 85]
    while blues[-1] < target: blues += [7 * blues[-1] - 7 * blues[-2] + blues[-3]]
    return(blues[-2])

print(p100_3(1e12))

from sympy.ntheory.continued_fraction import *
from sympy.ntheory.primetest import is_square
from sympy import sqrt

def p100_4():

    it = continued_fraction_convergents(continued_fraction_iterator(sqrt(2)))

    while 1:
        f = next(it) # Next continued fraction
        # print(f)
        y, x = f.p, f.q
        # print(y, x)
        if 2*x**2 == 1+y**2 and y%2 == 1:
            t = (1+y)//2
            print(t)
            if t > 10**12:
                print("Answer is", (1+int(sqrt(1+2*t*(t-1))))//2)
                break

p100_4()
# OEIS
    # blue, red, bag = 0, 0, 0
    # total = start
    # Found = False
    # while not Found:
    #     for f in funcblue:
    #         b1, r1 = f[0](total), f[1](total)
    #         if isinteger(b1) and isinteger(r1):
    #             bag, blue, red = total, b1, r1
    #             # print(total, blue, red, total * 4 + blue - 2)
    #             Found = ishalf(blue, total) and total > 10 ** 5
    #
    #     total += 1
