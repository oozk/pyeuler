#!/usr/bin/env python3

def p618(N, m):
    m  = int(m)

    F  = [0, 1, 1]
    while len(F) <= N+1: F += [F[-1] + F[-2]]

    sieve = [False, False] + [True] * (int(F[N]) + 1)
    for i in range(2, int(F[N] ** .5) + 1):
        if sieve[i]:
            for j in range(2*i, int(F[N]) + 1, i): sieve[j] = False
    primes, sieve = [i for i, b in enumerate(sieve) if b], []

    S = [1] + [0] * (F[N+1] + 1)
    for p in primes:
        for i in range(F[N+1]-p):
            S[p+i] = (S[p+i] + S[i] * p) % m

    return sum(S[f] for f in F[2:N+1]) % m

print(p618(24, 1e9))
