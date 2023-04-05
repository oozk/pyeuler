#!/usr/bin/env python3

from sympy import isprime, divisors, primefactors
from functools import lru_cache

def p829(N, DEPTH):

    def double_factorial(n):
        r = 1
        while n > 1:
            r *= n
            n -= 2
        return r

    @lru_cache(maxsize=None)
    def ab(n):
        if isprime(n): return (n, 1)
        a = [d for d in divisors(n) if d <= n**.5][-1]
        return (a, n//a)

    @lru_cache(maxsize=None)
    def T(n):
        a, b = ab(n)
        R    = [(a, b)]
        if not isprime(a):
            R   += T(a)
        if b > 1 and not isprime(b):
            R   += T(b)
        return R

    @lru_cache(maxsize=None)
    def S(n):
        # Signature of T(n)
        a, b = ab(n)
        R    = 'P' if isprime(a) else 'C'
        R   += 'P' if isprime(b) else 'C' if b > 1 else '_'
        if R[0] == 'C':
            R   += S(a)
        if R[1] == 'C':
            R   += S(b)
        return R

    def precalc(N, K):
        TG, NL = {}, {}
        for n in range(2, K+1):
            # if any(p > N for p in primefactors(n)): continue
            k = S(n)
            NL[n] = k
            try:
                TG[k] += [n]
            except:
                TG[k]  = [n]
        for k in TG.keys():
            TG[k] = sorted(TG[k])
            # print(k, TG[k])
        return TG, NL

    def M(n, K, TG, NL):

        @lru_cache(maxsize=None)
        def M_helper(n):
            MH = []
            a, b = ab(n)
            if b == 1:
                return 2
            k    = S(n)
            for a_ in TG[NL[a]]:
                if a_ > a: break
                for b_ in TG[NL[b]]:
                    if a_ > b_: continue
                    if b_ > b : break
                    m = a_ * b_
                    if S(m) == k:
                        MH += [m]
            return sorted(MH)

        nff     = double_factorial(n)

        if nff <= K:
            return min(TG[NL[nff]])

        a, b    = ab(nff)
        if b <= K:
            answer = [M_helper(nff)[0]]
        else:
            k      = S(nff)
            answer = [nff]
            for a_ in M_helper(a):
                if a_ > a: break
                for b_ in M_helper(b):
                    if a_ > b_: continue
                    if b_ > b : break
                    m = a_ * b_
                    if S(m) == k:
                        answer += [m]
                        print(m)
                        if len(answer) >= DEPTH: # search depth
                            return min(answer)
        return min(answer)

    K = max(b for (a, b) in T(double_factorial(N))[1:])
    sign_T, sign_n = precalc(N, K) # Signatures of T(n) and n
    for n in range(32, N+1):
        m = M(n, K, sign_T, sign_n)
        print('$M(' + str(n) + ') = ' + str(m) + '$')
    # return sum(M(n, K, sign_T, sign_n) for n in range(2, N+1))

print(p829(33, 12))
