#!/usr/bin/env python3

def base3(n):
    r = ''
    while n > 0:
        r   = str(n % 3) + r
        n //= 3
    return ('0'*4 + r)[-4:]

for i in range(81):
    print(i, base3(i))
