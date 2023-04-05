#!/usr/bin/env python3

from sympy import primerange, factorint

def p823(N, M, MOD):
    def min_factor(n, P):
        if n == 1:
            return 1

        for p in P:
            if n % p == 0:
                return p

    def rotate(R, P, M):
        for i in range(M):
            l  = 1
            T  = []
            for j in range(len(R)):
                x    = min_factor(R[j], P)
                n    = R[j] // x
                if n > 1: T += [n]
                l   *= x
            T += [l]
            R  = T
        return R

    #Initialize
    R = list(range(2, N+1))
    P = list(primerange(N))
    L = int((2*sum(sum(factorint(n).values()) for n in R))**.5)+1
    R = rotate(R, P, L*L)

    #Enumerate & Group Primes
    D   = {}  # ID Primes
    T   = {}  # (Start Position, Max Rotations)
    A   = {}  # (Initial Row, Initial Column)
    id  = 1
    for i in range(len(R)-1, -1, -1):
        c  = len(R)-i-1
        r  = 0
        while R[i] > 1:
            p     = min_factor(R[i], P)
            R[i]  = R[i] // p
            D[id] = p
            A[id] = (r, c)
            T[id] = (L*L, r+c+1)
            id   += 1
            r    += 1

    #Rotate M times
    for i in T.keys():
        p, r = T[i]
        m    = (int(M) - p) % r
        A[i] = ((A[i][0] - m) % r, (A[i][1] + m) % r)

    #Compute Answer
    answer = 0
    A      = {v:k for k, v in A.items()}
    for c in range(L):
        n = 1
        for r in range(L):
            if (r, c) in A.keys():
                n *= D[A[(r, c)]]
                n %= MOD
        if n > 1: answer += n
        answer %= MOD

    return answer % MOD

print(p823(10000, 1e16, 1234567891))

from sympy import isprime
from numpy import zeros, int64, vstack, r_, c_, sort

def p823_0(N, k, M):
    R = [x for x in range(2, N+1)]
    P = [p for p in R if isprime(p)]
    c = 1
    L = [[] for x in R]
    D = {}
    for p in P:
        f = True
        while f:
            f = False
            for i in range(len(R)):
                if R[i]%p == 0:
                    f      = True
                    R[i]   = R[i] // p
                    L[i]  += [c]
                    D[c]   = p
                    c     += 1

    S = zeros((N-1, N-1), dtype=int64)

    for i in range(len(L)):
        A = L[i]
        for j in range(len(A)):
            S[j][i] = A[j]

    for i in range(1, M+1 if M > 0 else sum(range(k+1))+2):
        print('Step: ' + str(i))
        X = vstack(([x for x in sort(S[0]) if x > 0] + [0]*(N-1))[:N-1])
        S = c_[r_[S[1:, 1:], zeros((1, N-2), dtype=int64)], X]
        print(S[:k,-k:])

    A = zeros((N-1, N-1), dtype=int64)

    for i in range(len(S)):
        for j in range(len(S)):
            if S[i][j] > 0:
                A[i][j] = D[S[i][j]]
    print(A)

# p823_0(10000, 5, 0)

def p823_old(N, M, MOD):
    R = [x for x in range(2, N+1)]

    # Enumerate Primes
    P = [p for p in R if isprime(p)]
    c = 1
    D = {}
    for p in P:
        f = True
        while f:
            f = False
            for i in range(len(R)):
                if R[i]%p == 0:
                    f      = True
                    R[i]   = R[i] // p
                    D[c]   = p
                    c     += 1

    #Enumerate & Group Primes by (In Position, Rotations), (Initial Row, Initial Column)
    T = {1:(1, 1), 2:(2, 2), 3:(4, 2)}
    A = {1:(0, 0), 2:(0, 1), 3:(1, 0)}
    s, p, c = 4, 3, 2
    for i in range(4, len(D)+1):
        if i < s+p:
            T[i] = (s+p, p)
            A[i] = (i-s, c)
            c   -= 1
        if i == s+p-1:
            s += p
            p += 1
            c  = p-1

    # Rotations
    for i in T.keys():
        p, r = T[i]
        m    = (int(M) - p) % r
        A[i] = ((A[i][0] - m) % r, (A[i][1] + m) % r)
    A = {v:k for k, v in A.items()}
    l = max(k[1] for k in A.keys())+1
    answer = 0
    count  = 0
    for c in range(l):
        n = 1
        for r in range(l):
            if (r, c) in A.keys():
                print(r, c, D[A[(r, c)]])
                n *= D[A[(r, c)]]
                count += 1
        print(c, n)
        answer += n
        # answer %= MOD
    print(count)
    return answer #% MOD
