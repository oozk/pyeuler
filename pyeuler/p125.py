#!/usr/bin/env python3

def p125(N):

    bounds      = int(N ** .5 + 1)
    palindromic = lambda n: str(n) == str(n)[::-1]

    result = 0
    seen   = set()
    for i in range(1, bounds):
        n = i ** 2
        for j in range(i+1, bounds):
            n += j ** 2
            if n < N and palindromic(n) and n not in seen:
                result += n
                seen |= {n}
            if n > N:
                break

    return result


print(p125(1e8))
