#!/usr/bin/env python3

def F(m, n):
    W = [0] + [1] * (m-1) + [2]
    while len(W) <= n:
        W += [W[-1] + sum(W[:-m]) + 2]
    return W[n]

def p115(m, L):
    W = [0] + [1] * (m-1) + [2]
    while W[-1] < L:
        W += [W[-1] + sum(W[:-m]) + 2]
    return len(W) - 1

print(p115(50, 1e6))
