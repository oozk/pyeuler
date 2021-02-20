#!/usr/bin/env python3

def p347_1(N):

    sieve = {i:[] for i in range(0, (int(N) + 1))}
    for i in range(2, int(N) + 1):
        if sieve[i] == []:
            for j in range(2*i, int(N) + 1, i): sieve[j] += [str(i)]

    sieve = {k:'-'.join(v) for (k, v) in sieve.items() if len(v) == 2}
    M     = {i:0 for i in sieve.values()}
    for k, v in sieve.items(): M[v] = k

    return sum(v for (k, v) in M.items())

print(p347_1(1e7))

from math import log

def p347_2(N):

    sieve  = [False, False] + [True] * (int(N)-1)
    for i in range(2, int(N ** .5) + 1):
        if sieve[i]:
            for j in range(2*i, int(N) + 1, i): sieve[j] = False
    primes, sieve = [i for i, b in enumerate(sieve) if b], []

    l      = lambda p, q, N: range(0, int(log(N/p/q) / log(p))+1) \
                                   if int(log(N/p/q) / log(p)) > 0 \
                                   else range(0, 1)
    M      = lambda p, q, N: max(p*q*(p**i)*(q**j) for i in l(p, q, N) \
                                                   for j in l(q, p, N) \
                                                   if p*q*(p**i)*(q**j) <= N)

    return sum(M(p, q, N) for i, p in enumerate(primes[:-1]) for q in primes[i+1:])

# print(p347_2(1e7))
