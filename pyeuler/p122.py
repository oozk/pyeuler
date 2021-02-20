#!/usr/bin/env python3

from sympy import isprime, factorint

def p122(n):
    m = [0, 1, 1, 2]
    for i in range(4, n+1):
        if isprime(i):
            m.append(min(m[j] + m[i-j] for j in range(1, i)))
        else:
            f = factorint(i)
            m.append(min(sum(m[k] * f[k] for k in f), \
                         min(m[j] + (m[i-j] if j != i - j else 1) \
                         for j in range(1, i))))
    for i in range(1, n+1):
        print(m[i])
    return sum(m[i] for i in range(1, n+1))


print(p122(200))


def p122_2(n):
    tree =
    while

    3_branch = [[1, 2, 3]]
    4_branch = [[1, 2, 4]]

# euler122=0
# for k in range(1, 101):
#     pwrs=[[1]]
#     totals=[1]
#     while not(k in totals):
#         pwrsnew=[]
#         for p in pwrs:
#             pwrsnew+=[p+[p[-1]+pwr] for pwr in p if p[-1]+pwr<=k]
#         pwrs=pwrsnew
#         totals=[i[-1] for i in pwrs]
#     euler122+=len(pwrs[0])-1
#     print(pwrs[-1])
#     print(totals[-1])
#     print(k,len(pwrs[0])-1)
# print(euler122)
