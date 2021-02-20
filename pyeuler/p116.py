#!/usr/bin/env python3

def p116(n):
    result = 0
    for i in [2, 3, 4]:
        tiles  = [1] + [0] * n
        for j in range(1, n + 1):
            tiles[j] += tiles[j-1]
            if j >= i:
                tiles[j] += tiles[j-i]
        result += tiles[-1] - 1
    return result

print(p116(50))

 100808458960497
