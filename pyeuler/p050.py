#!/usr/bin/env python3

###
# Problem 50
# https://projecteuler.net/problem=50
###

def p050(n):
    primes, sieve = prime_sieve(n)
    max = 0
    lim = len(primes)
    result = 0
    for i in range(0, lim):
        sum = primes[i]
        count = 1
        for j in range(i + 1, lim):
            sum += primes[j]
            count += 1
            if sum < n:
                if sieve[sum]:
                    if max < count:
                        max = count
                        result = sum
            else:
                break
    return result

def prime_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, len(sieve), i):
                sieve[j] = False
    for i, p in enumerate(sieve):
        if p: primes += (i, )
    return primes, sieve

print(p050(1000000))
