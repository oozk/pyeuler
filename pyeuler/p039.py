#!/usr/bin/env python3

def p039(n):
    return max(range(1, n+1), key=solutions)

def solutions(p):
    count = 0
    for a in range(1, p + 1):
        for b in range(a, (p - a) // 2 + 1):
            c = p - a - b
            if a ** 2 + b ** 2 == c ** 2:
                count += 1
    return count

print(p039(1000))
