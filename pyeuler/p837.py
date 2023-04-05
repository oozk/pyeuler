#!/usr/bin/env python3

from math import comb
L = [87, 93, 117, 171, 174, 186, 213, 234, 279, 285, 309, 327, 333, 339, 342, 345, 348, 357, 369, 372, 405, 426, 453, 465, 468, 555, 558, 570, 597, 618, 651, 654, 666, 675, 678, 681, 684, 690, 696, 714, 738, 744, 789, 810, 837, 849, 852, 906, 930, 936]

for n in L:
    print(n, "'" + ('000000000'+ bin(n)[2:])[-10:])

def p837(m, n, MOD):
    k = m + n
    l = (n - 3)//2
    ans = 0
    for i in range(l+1):
        ans += comb()

from itertools import permutations

def p837(K):

    def f(Q, S):
        ans = 0
        R = []
        L = set(p for p in permutations(S))
        for p in L:
            P = Q
            for r in p:
                if r == '0':
                    P = P[:2][::-1] + P[-1]
                else:
                    P = P[0] + P[1:][::-1]
            if P == Q:
                ans += 1
                R   += [int(''.join(p), 2)]
        # for r in sorted(R):
        #     print(r)
        return sorted(R)

    
    for k in range(1, K+1):
        L = []
        for m in range(K+1):
            for n in range(K+1):
                if m + n == k:
                    S = ['0'] * m + ['1'] * n
                    print(k, m, n, f('ABC', S))
                    L += f('ABC', S)
        # for r in sorted(L):
        #     print(k, r)        

# p837(10)

