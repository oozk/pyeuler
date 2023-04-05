#!/usr/bin/env python3

# from heapq import heapify, heappop, heappush
from math import ceil

def p793(N):

    S =[290797]
    for k in range(N-1):
        S += [S[-1]**2 % 50515093]
    S = sorted(S)
    n = (N-1) // 2 - 6
    L = ceil(N * (N-1) / 4)
    M = S[n-1] * S[n]
    c = n * (n-1) // 2

    F = {i:n if i <= n else i+1 for i in range(N-1)}
    while True:
        M1 = float('inf')
        for i in range(3*N//5):
            j = F[i]
            if j >= N-1: continue
            k  = sum(1 for s in S[j:] if s <= M / S[i])
            j  = j + k
            c += k
            print(c, L, M)
            if c == L-1:
                return M

            F[i] = j
            if j <= N-1 and M1 > S[i]*S[j]:
                M1 = S[i]*S[j]
        M = M1


print(p793(1000003))

# 497520726689832
# 492700616748525

    # while c < ceil(len(S) * (len(S)-1) / 4):
    #     a, i, j = F[0]
    #     print(a)
    #     c += 1
    #     heappop(F)
    #     if j+1 < len(S):
    #         heappush(F, (S[i]*S[j+1], i, j+1))
