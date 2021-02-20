#!/usr/bin/env python3

def p072(lim):

    tots  = totient_sieve(int(lim))
    pool  = [t for i, t in enumerate(tots[2:])]
    return sum(pool)


def totient_sieve(n):
	totients = list(range(n + 1))
	for i in range(2, len(totients)):
		if totients[i] == i:
			for j in range(i, len(totients), i):
				totients[j] -= totients[j] // i
	return totients

print(p072(1e6))
