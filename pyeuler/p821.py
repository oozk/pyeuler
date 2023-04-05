#!/usr/bin/env pypy3

from math import log, floor, gcd
from itertools import combinations

def p821_0(N):
    R1 = set(x for x in range(1, N+1))
    m = lambda S, k: set(k*x for x in S)
    Sol = set()
    mmax = 0
    for r in range(1, len(R1)):
        for S in combinations(R1, r):
            S1 = set(S)
            S2 = m(S1, 2)
            S3 = m(S1, 3)
            if len(S1 & S2) + len(S1 & S3) + len(S2 & S3) == 0:
                b = len((S1 | S2 | S3) & R1)
                if mmax < b:
                    mmax = b
                    Sol = S1
    return Sol

print(p821_0(15))
quit()


def p821(N):

    def f_sieve(N, M):
        K = sorted([2**i * 3**j for i in range(0, int(log(N, 2))+1)
                                for j in range(0, int(log(N, 3))+1)
                                if i+j != 1 and 2**i * 3**j <= N])
        S = {k:True for k in K}
        for m in M:
            S[m] = False
        for k in K:
            # if 1 < k < M:
            #     S[k] = False
            # if k >= M and S[k]:
            if S[k]:
                if k*2 in K: S[k*2] = False
                if k*3 in K: S[k*3] = False
                if k%2==0 and k*3//2 in K: S[k*3//2] = False
                # if k%3==0 and k*2//3 in K: S[k*2//3] = False

        return [k for k, v in sorted(S.items(), key=lambda x: x[0]) if v]
    
    print(f_sieve(100, [4]))
    quit()

    def k_inter(N, F4, F6):
        L    = []
        h    = lambda n: n if n%6 in [1, 5] else n-1 if n%6==0 else n-n%6+1
        for i in range(len(F4)):
            if i < len(F6):
                f4, f6 = h(floor(N/F4[i])), h(floor(N/F6[i]))
                if f4 < 1: f4 = 0
                if f6 < 1: f6 = 0
                if f4 != f6:
                    L += [((f4, f6), 1)] if f4 < f6 else [((f6, f4), -1)]
        return L

    def count(k, A):
        return len([k*x for x in A if k*x <= N]) + len([k*x for x in A if 2*k*x <= N]) + len([k*x for x in A if 3*k*x <= N])

    def advance(n):
        if n%6 == 0:
            return n+1
        if n%6 == 1:
            return n+4
        if n%6 == 5:
            return n+2

    def k_group(I):
        K    = set(x[0] for x in I)
        I    = [(k, sum(x[1] for x in I if x[0] == k)) for k in K]
        while sum(1 for x in range(1, len(I)) if I[x][0][0] < I[x-1][0][1]) > 0:
            for i in range(1, len(I)):
                if I[i][0][0] < I[i-1][0][1] and I[i-1][0][0] < I[i][0][0] and I[i-1][0][1] < I[i][0][1]:
                    I     += [((I[i-1][0][1], I[i][0][1]), I[i][1])]
                    I     += [((I[i][0][0], I[i-1][0][1]), I[i-1][1])]
                    I[i], I[i-1] = ((I[i][0][0], I[i-1][0][1]), I[i][1]), ((I[i-1][0][0], I[i][0][0]), I[i-1][1])
                    I      = sorted(I)
                    K      = set(x[0] for x in I)
                    I      = [(k, sum(x[1] for x in I if x[0] == k)) for k in K]
                    break
                elif I[i][0][0] < I[i-1][0][1] and I[i-1][0][0] < I[i][0][0]:
                    I     += [((I[i][0][0], I[i-1][0][1]), I[i-1][1])]
                    I[i-1] = ((I[i-1][0][0], I[i][0][0]), I[i-1][1])
                    I      = sorted(I)
                    K      = set(x[0] for x in I)
                    I      = [(k, sum(x[1] for x in I if x[0] == k)) for k in K]
                    break
                elif I[i][0][0] < I[i-1][0][1] and I[i-1][0][0] == I[i][0][0]:
                    I     += [((I[i-1][0][1], I[i][0][1]), I[i][1])]
                    I[i]   = ((I[i][0][0], I[i-1][0][1]), I[i][1])
                    I      = sorted(I)
                    K      = set(x[0] for x in I)
                    I      = [(k, sum(x[1] for x in I if x[0] == k)) for k in K]
                    break

        I = [x for x in I if x[1] == 1]
        for i in range(len(I)):
            while count(I[i][0][0], F4) >= count(I[i][0][0], F6):
                if advance(I[i][0][0]) <= N:
                    I[i] = ((advance(I[i][0][0]), I[i][0][1]), I[i][1])
                else:
                    break
        while sum(1 for x in range(1, len(I)) if I[x][0][0] == I[x-1][0][1]) > 0:
            for i in range(1, len(I)):
                if I[i][0][0] == I[i-1][0][1]:
                    I  += [((I[i-1][0][0], I[i][0][1]), I[i][1])]
                    I[i], I[i-1] = ((0, 0), 0), ((0, 0), 0)
                    I   = sorted([x for x in I if x != ((0, 0), 0)])
                    break
        return I

    F4     = f_sieve(N, [4, 32])
    F6     = f_sieve(N, [])
    print(sorted(F4))
    print(sorted(F6))
    I      = k_group(sorted(k_inter(N, F4, F6) + k_inter(N//2, F4, F6) + k_inter(N//3, F4, F6)))

    answer = 0
    for x in I:
        answer += 1 + floor((x[0][1]-x[0][0])/6)
        chk     = 1 + floor((x[0][1]-x[0][0])/6)
        x_0     = x[0][0]+4 if x[0][0] % 6 == 1 else x[0][0]+2
        if x[0][1] - x_0 >= 0:
            answer += 1 + floor((x[0][1]-x_0)/6)
            chk    += 1 + floor((x[0][1]-x_0)/6)

    for m in F4:
        for k in range(1, 4):
            for l in [1, 5]:
                n = floor((N-k*l*m)/(6*k*m)) + 1 if k*l*m <= N else 0
                if n > 0:
                    answer += n

    # def coprimes_of_6(n):
    #     R = []
    #     for i in range(1, n+1):
    #         if gcd(6, i) == 1:
    #             R += [i]
    #     return R
    # print(I)
    # K = coprimes_of_6(N)
    # L = []
    # M = [7, 23, 25, 29, 31, 35, 37, 41 ]
    # for f in F4:
    #     for k in K:
    #         if k not in M and f*k <= N:
    #
    #             L += [f*k]
    # for f in F6:
    #     for k in M:
    #         if f*k <= N:
    #             L += [f*k]
    #
    # R = set(range(1, N+1))
    # m = lambda S, k: set(k*x for x in S)
    # S1 = set(L)
    # S2 = m(S1, 2)
    # S3 = m(S1, 3)
    # print(len(S1 & S2) + len(S1 & S3) + len(S2 & S3))
    # print(S1 & S2, S1 & S3, S2 & S3)
    # print(len(((S1 | S2) | S3) & R))

    return answer

print(p821(1e2)) #16))
# for i in range(1, 100):
#     print(i, p821(i)) #1e16))


def p821_2(N):

    from itertools import combinations

    def no_gcd_6(n):
        R = []
        for i in range(1, n+1):
            if gcd(6, i) == 1:
                R += [i]
        return R

    R  = set(sorted([2**i * 3**j for i in range(0, int(log(N, 2))+1)
                                for j in range(0, int(log(N, 3))+1)
                                if i+j != 1 and 2**i * 3**j <= N]))

    R1 = set(x for x in range(1, N+1))
    m = lambda S, k: set(k*x for x in S)
    c = 0
    T = set()
    Z = {k:0 for k in no_gcd_6(N)}
    D = {}

    for k in Z.keys():
        R2 = [x for x in R if x*k <= N]
        for r in range(1, len(R2)):
            for S in combinations(R2, r):
                S1 = set()
                for s in S:
                    if s*k <= N: S1 |= {s*k}
                if Z[k] > 0 and len(S1) < 2:
                    break
                S2 = m(S1, 2)
                S3 = m(S1, 3)

                if len(S1 & S2) + len(S1 & S3) + len(S2 & S3) == 0:
                    b = len((S1 | S2 | S3) & R1)
                    if Z[k] < b:
                        Z[k] = b
                        D[k]  = [s for s in S if s*k <= N]

    S1 = set()
    for k in D.keys():
        # print(k,  D[k])
        for f in D[k]:
            if k*f <= N:
                S1 |= {k*f}
    print(sorted(S1))
    S2 = m(S1, 2)
    print(sorted(S2))
    S3 = m(S1, 3)
    print(sorted(S3))
    print(len(S1 & S2) + len(S1 & S3) + len(S2 & S3))
    return len((S1 | S2 | S3) & R1), sorted((S1 | S2 | S3) & R1)

# print(p821(300))
print(p821_2(100))

# for n in range(1, 120):
#     print(n, max(p821(n), p821_2(n)))




def p821_3(N, L, LL):
    def f_sieve(N, M):
        K = sorted([2**i * 3**j for i in range(0, int(log(N, 2))+1)
                                for j in range(0, int(log(N, 3))+1)
                                if i+j != 1 and 2**i * 3**j <= N])
        S = {k:True for k in K}
        for m in M:
            S[m] = False
        for k in K:
            # if 1 < k < M:
            #     S[k] = False
            # if k >= M and S[k]:
            if S[k]:
                if k*2 in K: S[k*2] = False
                if k*3 in K: S[k*3] = False
                if k%2==0 and k*3//2 in K: S[k*3//2] = False
                # if k%3==0 and k*2//3 in K: S[k*2//3] = False

        return [k for k, v in sorted(S.items(), key=lambda x: x[0]) if v]


    def factors(B, N):
        B = B - B%6
        S = []
        for k in range(B, N+1, 6):
            if k+1 <= N: S += [k+1]
            if k+5 <= N: S += [k+5]
        return sorted(S)

    A = f_sieve(N, [4, 32])
    B = f_sieve(N, [])
    print(A)
    print(B)
    K = factors(int(1e16/L), int(1e16/L)+LL)

    result = 0
    count  = {'A':0, 'B':0}

    for k in K:
        a1, a2, a3 = len([k*x for x in A if k*x <= N]), len([k*x for x in A if 2*k*x <= N]), len([k*x for x in A if 3*k*x <= N])
        b1, b2, b3 = len([k*x for x in B if k*x <= N]), len([k*x for x in B if 2*k*x <= N]), len([k*x for x in B if 3*k*x <= N])

        if a1+a2+a3 < b1+b2+b3:
            result += b1+b2+b3
            count['B'] += 1
        else:
            result += a1+a2+a3
            count['A'] += 1
        # print(k, a1+a2+a3 < b1+b2+b3, a1+a2+a3, b1+b2+b3, a1, a2, a3, b1, b2, b3)
    return sum(v for k, v in count.items()), count['B'] > count['A'], count['B'], count['A']

# for L in range(100, 0, -1):
#     print(L, p821_3(int(1e16), L, 10000))

# 9192815500685875
# 9219661511328178