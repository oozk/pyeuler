#!/usr/bin/env python3

from functools import lru_cache
from math import log
from sympy import divisors, factorint, isprime, primefactors

def p827(K, M, latex):

    # Build look up lists for 4k+1 and 4k+3 primes and log values
    P4k1  = [p for p in range(200) if isprime(p) and p%4==1]
    P4k3  = [p for p in range(200) if isprime(p) and p%4==3]
    L4k1  = [log(p) for p in P4k1]
    L4k3  = [log(p) for p in P4k3]
    L1, L2, L3 = L4k1[0], log(2), L4k3[0]

    @lru_cache(maxsize=None)
    def E4k1(n, sort_flag):
        # decompose exponents for 4k+1 primes
        SF = lambda x: sum(L4k1[i] * l for i, l in enumerate(x))
        S  = set()
        D  = divisors(n+1)
        for d in D:
            r, x = (d-1), ((n+1)//d - 1) // 2
            if r == 0:
                S |= {(x, )}
            elif r < 8:
                S |= {tuple(sorted([x, r//2])[::-1])}
            elif r >= 8 and r != n:
                S |= {tuple(sorted([x]+list(s))[::-1]) for s in E4k1(r, False)}
        S  = {tuple(x for x in s if x != 0) for s in S}
        return sorted(S, key=lambda x: SF(x))[0] if sort_flag else S

    @lru_cache(maxsize=None)
    def E4k3(n, sort_flag):
        # decompose exponents for 4k+3 primes
        SF = lambda x: sum(L4k3[i] * l for i, l in enumerate(x))
        S  = set()
        D  = divisors(2*n+1)
        for d in D[:len(D)//2 + 1]:
            r, x = (n-(d-1)//2) //d, (d-1)//2
            S |= {tuple(sorted([x, r])[::-1])}
            if r > 3 and r != n:
                S |= {tuple(sorted([x]+list(s))[::-1]) for s in E4k3(r, False)}
            if x > 3 and x != n:
                S |= {tuple(sorted([r]+list(s))[::-1]) for s in E4k3(x, False)}
        S  = {tuple(x for x in s if x != 0) for s in S}
        return sorted(S, key=lambda x: SF(x))[0] if sort_flag else S

    def H(P1, P2, P3):
        # Returns log value of prime powers 4k+1, 2, 4k+3
        lsum = lambda L, P: sum(L[i] * n for i, n in enumerate(sorted(P)[::-1]))
        return lsum(L4k1, P1) + L2*P2 + lsum(L4k3, P3)

    def F(P1, P2, P3):
        # Returns number based on prime powers 4k+1, 2, 4k+3
        result = pow(2, P2, M) if M > 1 else pow(2, P2)
        for i, n in enumerate(sorted(P1)[::-1]):
            result *= pow(P4k1[i], n, M)  if M > 1 else pow(P4k1[i], n)
        for i, n in enumerate(sorted(P3)[::-1]):
            result *= pow(P4k3[i], n, M) if M > 1 else pow(P4k3[i], n)
        return (result % M) if M > 1 else result

    def Q(n):
        # Solution to PE 827
        SF     = lambda p1, p2, p3: L1*p1 + L2*p2 + L3*p3
        Sol    = set()          # Feasible solution set for Q(n)
        D1     = divisors(n+1)
        for x in D1:
            x1 = x-1
            r  = 2 * (n - x1) // (x1+1) + 1
            D2 = divisors(r)
            for d in D2[:len(D2)//2]:
                k, a     = (r//d + d)//2, (r//d - d)//2
                for x3 in [(-2*(a+1) + 2*k)//4, (-2*(a+1) - 2*k)//4,
                           (-2*(-a+1)+ 2*k)//4, (-2*(-a+1)- 2*k)//4]:
                    if x3 < 0: continue
                    x2   = (n-(x1+(x1+1)*x3))//(2*(x1+1)*x3+x1+1)+1
                    Sol |= {(x1, x2, x3)} # exponents for 4k+1, 2, 4k+3

        S      = ((0,), 0, (0,))
        qmin   = 0
        Sol    = sorted(Sol, key=lambda x: SF(*x)) # Approx sort in ascending order
        for (l1, x2, l3) in Sol:
            x1 = E4k1(l1, True)  # pick the lowest value exponent set for 4k+1
            x3 = E4k3(l3, True)  # pick the lowest value exponent set for 4k+3
            v  = H(x1, x2, x3)   # evaluate log value
            if qmin == 0:
                qmin = v
                S    = (x1, x2, x3)
            if qmin  > v:
                qmin = v
                S    = (x1, x2, x3)
        return F(*S), S          # return smallest Q(n) number

    def R(q):
        # R(Q(n)) == n using OEIS A024363
        def A(n):
            if n % 4 == 2 or n < 2:
                return 0
            else:
                F = primefactors(n)
                return pow(2, len(F)-1) if any(p%4!=1 for p in F) else pow(2, len(F))

        return sum(A(d) for d in divisors(q))

    def D(n):
        # Decomposes number to 4k+1, 2 and 4k+3 prime powers
        F  = factorint(n)
        P1 = tuple(F[p] for p in sorted(F.keys()) if p%4==1)
        P2 = F[2]
        P3 = tuple(F[p] for p in sorted(F.keys()) if p%4==3)
        return P1, P2, P3

    def W(P1, P2, P3):
        # Returns written form of Q(n)
        if latex:
            result  = '2^{'+ str(P2) + '} \cdot{} '
            S       = [(P4k1[i], n) for i, n in enumerate(sorted(P1)[::-1])]
            S      += [(P4k3[i], n) for i, n in enumerate(sorted(P3)[::-1])]
            result += ' \cdot{} '.join(str(p) + ('^{' + str(n) + '}' if n > 1 else '') for (p, n) in sorted(S))
        else:
            result  = '2^'+ str(P2) + ' • '
            S       = [(P4k1[i], n) for i, n in enumerate(sorted(P1)[::-1])]
            S      += [(P4k3[i], n) for i, n in enumerate(sorted(P3)[::-1])]
            result += ' • '.join(str(p) + ('^' + str(n) if n > 1 else '') for (p, n) in sorted(S))
        return result

    answer = 0
    for k in range(1, K+1):
        q, s    = Q(10**k)
        answer += q
        if M > 1:
            answer %= M
        if latex:
            print('$Q(10^{' + str(k) + '}) = ' + W(*s) + '$')
        else:
            print('Q(10^' + str(k) + ') = ' + W(*s))

    return (answer) % M if M > 1 else answer

print(p827(18, 409120391, False))
