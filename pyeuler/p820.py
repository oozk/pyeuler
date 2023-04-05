#!/usr/bin/env python3

# from numba import prange, jit
#
# @jit(nopython=True, parallel=True)
from tqdm import tqdm
from sympy import multiplicity, n_order
from math import floor

def p820(N):

    result = 0
    for k in range(1, N+1):
        result += floor(pow(10, N, 10*k) / k)
    return result

print(p820(10000000))


#     def A051626(n):
#         return 0 if (m:=(n>>(~n & n-1).bit_length())//5**multiplicity(5, n)) == 1 else n_order(10, m)
#
#     def A051628(n):
#         return max(multiplicity(2, n), multiplicity(5, n))
#
#     def d(x, i):
#         n    = 1
#         c    = 1
#         while c < i:
#             n  = n * 10 % x
#             c += 1
#         return (n*10)//x
#
#     result = 0
#     for n in tqdm(range(1, N+1)):
#         l = A051626(n)
#         if l > 0:
#             s = A051628(n)
#             p = (N-s) % l
#             i = 1 if l == 1 else l if p == 0 else p
#             result += d(n, s+i)
#
#     return result
#
# print(p820(10000000))
