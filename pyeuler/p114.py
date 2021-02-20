#!/usr/bin/env python3

def p114(N):
	W = [0, 1, 1, 2]
	while len(W) <= N:
		W += [W[-1] + sum(W[:-3]) + 2]
	return W[N]

print(p114(50))
