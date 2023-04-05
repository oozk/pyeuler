#!/usr/bin/env python3

from math import log

def p832(n, MOD):
    k  = int(log(3*n+1, 4))
    M  = 3*sum(int(5*pow(2, 4*i-5) - pow(2, 2*i-3)) for i in range(1, k+1))
    M %= MOD

    a  = 4**k
    n -= (a-1)//3
    M += 6*a*n + 3*n**2 - 3*n
    M %= MOD

    H  = hex(n)[2:][::-1]
    Q  = [4*a+b for a in [0, 0, 1, 2] for b in [0, 0, 1, 2]]
    S  = Q.copy()
    for p, q in enumerate(H):
        if p > 0:
            Q  = [(x*16) % MOD for x in Q]
            S  = [(x*pow(16, p, MOD) + sum(S)) % MOD for x in Q]
            M -= 6*Q[int(q, 16)] * int(H[:p][::-1], 16)
        M -= 6*sum(S[:int(q, 16)])
        M %= MOD

    return M

print(p832(int(1e18), 1000000007))

def p832_2(n, MOD):
    k  = int(log(3*n-1, 4))
    M  = int('1'*k, 16) + (4**(2*k-1)-5*4**(k-1)+1)//15 + 4**k * (n-(4**k-1)//3)

    H  = hex(n-(4**k-1)//3)[2:][::-1]
    Q  = [4*a+b for a in [0, 1, 1, 1] for b in [0, 1, 1, 1]]
    S  = Q.copy()
    for p, q in enumerate(H):
        if p > 0:
            Q  = [(x*16) for x in Q]
            S  = [(x*pow(16, p) + sum(S)) for x in Q]
            M += Q[int(q, 16)] * int(H[:p][::-1], 16)
        M += sum(S[:int(q, 16)])

    return 6*M % MOD

print(p832_2(int(1e18), 1000000007))

from math import floor, log
from decimal import Decimal

def p832_3(n, MOD):
    def S_sum(n):
        S = 0
        for i in range(int(log(n, 4)+1)):
            p, q = 4**i, 4**(i+1)
            b    = [floor(Decimal(n)/Decimal(q))*p] * 4
            r    = n-sum(b)
            m    = floor(Decimal(r)/Decimal(p))
            for j in range(4):
                if j < m:
                    b[j] += p
                elif j == m:
                    b[j] += r-m*p
            S += p*sum(b[1:])
        return S

    k  = int(log(3*n-1, 4))
    r  = n-(4**k-1)//3
    return 6*(int('1'*k, 16) + sum(S_sum(4**i) for i in range(k)) \
              + r*4**k + S_sum(r)) % MOD

print(p832_3(int(1e18), 1000000007))


def S(n, D):
    r, k = 0, 0
    while n>0: r+=D[n%4]*4**k; n//=4; k+=1
    return r

def T(n):
    k     = int(log(3*n-1, 4))
    i     = (3*n-4**k-2)//3
    a     = 4**k+i
    b     = 2*a - S(i, [0, 0, 1, 5])
    a_o_b = 3*a - S(i, [0, 0, 5, 7])
    return (a, b, a_o_b)

# print(T(int(1e18)))

def T2(n):
    k     = int(log(3*n-1, 4))
    i     = (3*n-4**k-2)//3
    a     = 4**k + i
    b     = 2*4**k + S(i, [0, 2, 3, 1])
    a_o_b = 3*4**k + S(i, [0, 3, 1, 2])
    return (a, b, a_o_b)

str_input = """
9
1
2
3
4
5
6
7
8
9
"""
def CF_C(str_input):
    def ceil_div(a, b):
        return b and a//b + bool(a%b)

    def S(n, D):
        r, k = 0, 0
        while n>0: r+=D[n%4]*4**k; n//=4; k+=1
        return r

    def T(n):
        k     = int(log(3*n-1, 4))
        i     = (3*n-4**k-2)//3
        a     = 4**k + i
        b     = 2*4**k + S(i, [0, 2, 3, 1])
        a_o_b = 3*4**k + S(i, [0, 3, 1, 2])
        return (a, b, a_o_b)

    I = [int(x) for x in str_input.splitlines() if len(x) > 0]
    t = I[0]
    for n in I[1:]:
        print(T(ceil_div(n, 3))[(n-1) % 3])

CF_C(str_input)
# print(T2(int(1e18)))

def S_sum(n, D):
    S = 0
    for i in range(int(log(n, 4)+1)):
        p, q = 4**i, 4**(i+1)
        b    = [floor(Decimal(n)/Decimal(q))*p] * 4
        r    = n-sum(b)
        m    = floor(Decimal(r)/Decimal(p))
        for j in range(4):
            if j < m:
                b[j] += p
            elif j == m:
                b[j] += r-m*p
        S += p*sum(D[0]*b[0], D[1]*b[1], D[2]*b[2], D[3]*b[3])
    return S

#A006015 PROG
def a(n, D=[0, 2, 3, 1]):
    r, k = 0, 0
    while n>0: r+=D[n%4]*4**k; n//=4; k+=1
    return r

# for n in range(100):
#     print(n, a(n))

#A004468 PROG
def A004468(n, D=[0, 3, 1, 2]):
    r, k = 0, 0
    while n>0: r+=D[n%4]*4**k; n//=4; k+=1
    return r

def A004480(n, D=[0, 15, 5, 10]):
    r, k = 0, 0
    while n>0: r+=D[n%4]*4**k; n//=4; k+=1
    return r

for n in range(100):
    print(n, A004480(n))

#(Onur Ozkan, Mar 7 2023)


def R1(n):
    a = 0
    for i in range(n+1):
        a += R(i)
    return a

def S1(n):
    a = 0
    for i in range(n+1):
        a += S(i)
    return a

def p832_0(n, K):
    round = 0
    M     = []
    while round < n:
        for a in range(1, K):
            if a in M: continue
            M += [a]
            break
        for b in range(1, K):
            if b in M: continue
            if b^a in M: continue
            M += [b]
            M += [b^a]
            print(a, a*2 - b, a*3 - (b^a))
            break

        round += 1

    print(sorted(M), len(M))
    return sum(M)

# print(p832_0(2000, 100000000))

def A004480(n):
    return n
